#!/usr/bin/env python3
"""Build exercise docs, corrigés and audio from levels/*.txt.
Usage: build.py <level> [--audio]
"""
import sys, re, os, subprocess, pathlib

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "out"
TTS = pathlib.Path.home() / "tts"

BANDS = {
    "A1": "TOEIC 120 à 220 points, minimum 60 en Listening et 60 en Reading",
    "A2": "TOEIC 225 à 545 points, minimum 110 en Listening et 115 en Reading",
    "B1": "TOEIC 550 à 780 points, minimum 275 en Listening et 275 en Reading",
    "B2": "TOEIC 785 à 940 points, minimum 400 en Listening et 385 en Reading",
    "C1": "TOEIC 945 à 990 points, minimum 490 en Listening et 455 en Reading",
    "C2": "perfectionnement : le TOEIC ne distingue pas C2 de C1 (945 à 990 points)",
}
L = "ABCDEFG"


def slug(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:40]


def parse(level):
    lines = (BASE / "levels" / f"{level}.txt").read_text(encoding="utf-8").splitlines()
    blocks = []  # each: dict(kind,title,extra,body,audio,questions)
    cur = None
    for raw in lines:
        line = raw.rstrip()
        if not line.strip() or line.startswith("#"):
            continue
        m = re.match(r"^(EX|TEXT|AUDIO)\s+(.*)$", line)
        if m:
            kind, rest = m.group(1), m.group(2)
            parts = [p.strip() for p in rest.split("|")]
            cur = dict(kind=kind, title=parts[0], extra=parts[1:], body=[], audio=[], qs=[])
            blocks.append(cur)
            continue
        if line.startswith("Q "):
            p = [x.strip() for x in line[2:].split("|")]
            stem, opts, ans, expl = p[0], p[1:-2], p[-2], p[-1]
            cur["qs"].append(dict(stem=stem, opts=opts, ans=ans, expl=expl))
            continue
        if cur["kind"] == "AUDIO":
            sp, txt = line.split(":", 1)
            cur["audio"].append((sp.strip(), txt.strip()))
        else:
            cur["body"].append(line)
    return blocks


def qmd(qs, start=1):
    out = []
    for i, q in enumerate(qs, start):
        out.append(f"{i}. {q['stem']}")
        out.append("")
        lines = [f"**{L[k]}.** {o}" for k, o in enumerate(q["opts"])]
        out.append("    " + "\\\n    ".join(lines))
        out.append("")
    return "\n".join(out)


def header(level, title, sub):
    return (f"# {title}\n\n*Niveau {level} – {BANDS[level]} – {sub}*\n\n"
            f"Nom : ______________________  Date : ____________  Score : ____ / ___\n\n")


def write_docx(md, path):
    tmp = path.with_suffix(".md")
    tmp.write_text(md, encoding="utf-8")
    subprocess.run(["pandoc", "-f", "markdown-smart", str(tmp), "-o", str(path)], check=True)
    tmp.unlink()
    add_borders(path)


def add_borders(path):
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    d = Document(str(path))
    for t in d.tables:
        tblPr = t._tbl.tblPr
        b = OxmlElement("w:tblBorders")
        for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
            x = OxmlElement(f"w:{e}")
            x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "4"); x.set(qn("w:color"), "999999")
            b.append(x)
        tblPr.append(b)
    d.save(str(path))


def build(level, audio):
    blocks = parse(level)
    d = OUT / level
    d.mkdir(parents=True, exist_ok=True)
    exs = [b for b in blocks if b["kind"] == "EX"]
    txts = [b for b in blocks if b["kind"] == "TEXT"]
    auds = [b for b in blocks if b["kind"] == "AUDIO"]
    corr = [f"# Corrigés – Niveau {level}\n\n*{BANDS[level]}*\n"]

    for n, b in enumerate(exs, 1):
        instr = b["extra"][0] if b["extra"] else ""
        md = header(level, f"Exercice {n} : {b['title']}", "Tutorat d'anglais") + f"**Consigne :** {instr}\n\n" + qmd(b["qs"])
        write_docx(md, d / f"{level}_Exercice_{n}_{slug(b['title'])}.docx")
        corr.append(f"\n## Exercice {n} : {b['title']}\n")
        corr.append("| N° | Réponse | Explication |\n| :-- | :--- | :------------------------------------ |")
        for i, q in enumerate(b["qs"], 1):
            corr.append(f"| {i} | {q['ans']} | {q['expl']} |")

    md = header(level, "Compréhension écrite", "3 textes") + "Lisez chaque texte, puis répondez aux questions. Temps conseillé : 1 minute par question.\n\n"
    for n, b in enumerate(txts, 1):
        md += f"## Texte {n} : {b['title']}\n\n" + "\n\n".join(b["body"]) + "\n\n" + qmd(b["qs"]) + "\n"
        corr.append(f"\n## Compréhension écrite, texte {n} : {b['title']}\n")
        corr.append("| N° | Réponse | Explication |\n| :-- | :--- | :------------------------------------ |")
        for i, q in enumerate(b["qs"], 1):
            corr.append(f"| {i} | {q['ans']} | {q['expl']} |")
    write_docx(md, d / f"{level}_Comprehension_ecrite.docx")

    md = header(level, "Compréhension orale", "2 pistes audio") + (
        "Écoutez chaque piste (fichiers MP3 joints), deux fois si besoin, puis répondez. "
        "Lisez les questions **avant** d'écouter.\n\n")
    for n, b in enumerate(auds, 1):
        md += f"## Piste {n} : {b['title']}\n\n*Fichier : {level}_Piste_{n}.mp3*\n\n" + qmd(b["qs"]) + "\n"
        corr.append(f"\n## Compréhension orale, piste {n} : {b['title']}\n")
        corr.append("| N° | Réponse | Explication |\n| :-- | :--- | :------------------------------------ |")
        for i, q in enumerate(b["qs"], 1):
            corr.append(f"| {i} | {q['ans']} | {q['expl']} |")
        corr.append(f"\n**Transcription, piste {n}**\n")
        for sp, txt in b["audio"]:
            corr.append(f"- {txt}" if sp == "N" else f"- **{sp}** : {txt}")
    write_docx(md, d / f"{level}_Comprehension_orale.docx")
    write_docx("\n".join(corr) + "\n", d / f"{level}_Corrige.docx")

    if audio:
        make_audio(level, auds, d)
    nq = sum(len(b["qs"]) for b in blocks)
    print(level, "blocks:", len(exs), "ex,", len(txts), "texts,", len(auds), "audio;", nq, "questions")


def make_audio(level, auds, d):
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(str(TTS / "kokoro-v1.0.onnx"), str(TTS / "voices-v1.0.bin"))
    for n, b in enumerate(auds, 1):
        vmap = {}
        for kv in b["extra"][0].split(","):
            a, v = kv.split("=")
            vmap[a.strip()] = v.strip()
        speed = float(b["extra"][1]) if len(b["extra"]) > 1 else 1.0
        chunks, sr = [], 24000
        for sp, txt in b["audio"]:
            v = vmap[sp]
            lang = "en-gb" if v.startswith("b") else "en-us"
            samples, sr = k.create(txt, voice=v, speed=speed, lang=lang)
            chunks.append(samples)
            chunks.append(np.zeros(int(sr * 0.9), dtype=np.float32))
        wav = d / f"{level}_Piste_{n}.wav"
        sf.write(str(wav), np.concatenate(chunks), sr)
        mp3 = d / f"{level}_Piste_{n}.mp3"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-b:a", "96k", str(mp3)], check=True)
        wav.unlink()


if __name__ == "__main__":
    build(sys.argv[1], "--audio" in sys.argv)
