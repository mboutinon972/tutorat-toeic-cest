#!/usr/bin/env python3
"""Build <L>_Lexique.docx from lex/<L>.lex and level content (examples)."""
import re, sys, pathlib
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import build

BASE = pathlib.Path(str(__import__("pathlib").Path(__file__).resolve().parent))


def sentences(level):
    txt = (BASE / "levels" / f"{level}.txt").read_text(encoding="utf-8")
    keep = []
    for line in txt.split("\n"):
        if line.startswith("Q "):
            p = line[2:].split(" | ")
            stem = p[0]
            if "-------" in stem and len(p) >= 7:
                ans = p["ABCD".index(p[5].strip()) + 1].strip()
                stem = re.sub(r"-{4,}", ans, stem)
                stem = re.sub(r"\s+([.,?!])", r"\1", stem)
            if "-------" not in stem:
                keep.append(stem)
            continue
        if re.match(r"^(EX|TEXT|AUDIO) ", line) or not line.strip():
            continue
        keep.append(re.sub(r"^(S\d?|N):\s*", "", line))
    out = []
    for k in keep:
        k = re.sub(r"^(From|To|Subject):.*$", "", k)
        for s in re.split(r"(?<=[.!?])\s+", k):
            s = s.strip()
            if 4 <= len(s.split()) <= 24:
                out.append(s)
    return out


def pattern(w):
    w = w.lower()
    if " " in w:
        return re.compile(r"\b" + re.escape(w) + r"(s|es|ed)?\b", re.I)
    forms = {w, w + "s", w + "es", w + "ed", w + "d", w + "ing", w + "ly", w + "'s"}
    if w.endswith("e"):
        forms |= {w[:-1] + "ing"}
    if w.endswith("y"):
        forms |= {w[:-1] + "ies", w[:-1] + "ied"}
    if w.endswith("ion"):
        forms |= {w[:-3] + "ions"}
    if len(w) > 3 and w[-1] not in "aeiou":
        forms |= {w + w[-1] + "ed", w + w[-1] + "ing"}
    return re.compile(r"\b(" + "|".join(re.escape(f) for f in sorted(forms, key=len, reverse=True)) + r")\b", re.I)


def esc(s):
    return s.replace("|", "/").replace("*", "\\*").replace("_", "\\_")


def make(level):
    sents = sentences(level)
    md = build.header(level, "Lexique", "Mots utilisés dans les documents du niveau")
    md += ("Chaque mot vient des exercices, des textes ou des pistes audio du niveau. "
           "L'exemple est une phrase de ces documents. **Méthode :** cachez la colonne « Traduction », "
           "devinez, puis vérifiez. Notez les mots ratés dans votre carnet.\n\n")
    n = 0
    miss = 0
    for line in (BASE / "lex" / f"{level}.lex").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            md += f"\n## {line[2:]}\n\n| Mot | Nature | Traduction | Exemple (tiré des documents) |\n| :---------------- | :--------- | :-------------------- | :------------------------------------ |\n"
            continue
        w, pos, fr = [x.strip() for x in line.split(" | ")]
        pat = pattern(w)
        cands = [s for s in sents if pat.search(s)]
        ex = ""
        if cands:
            cands.sort(key=lambda s: abs(len(s.split()) - 12))
            ex = "*" + esc(cands[0]) + "*"
        else:
            miss += 1
        md += f"| **{esc(w)}** | {pos} | {esc(fr)} | {ex} |\n"
        n += 1
    md += f"\n*{n} mots et expressions.*\n"
    d = build.OUT / level
    build.write_docx(md, d / f"{level}_Lexique.docx")
    print(level, n, "entries,", miss, "without example")


if __name__ == "__main__":
    for L in sys.argv[1:]:
        make(L)
