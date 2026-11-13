from sch_lib import *
import matplotlib.colors as mc


def gradient(ax, x0, x1, y, h, c1, c2, n=40):
    a, b = mc.to_rgb(c1), mc.to_rgb(c2)
    for i in range(n):
        t = i / (n - 1)
        col = tuple(a[k] * (1 - t) + b[k] * t for k in range(3))
        ax.add_patch(plt.Rectangle((x0 + i * (x1 - x0) / n, y), (x1 - x0) / n + 0.1, h, fc=col, ec="none"))


# ---------------- B2 ----------------
def b2_reported(path):
    fig, ax = canvas("Discours rapporté : on recule d'un temps", "She said (that) ...  — verbe introducteur au passé")
    box(ax, 27, 45, 38, 5.5, "DISCOURS DIRECT", fc=NAVY, ec=NAVY, fs=10.5, bold=True, color="white")
    box(ax, 73, 45, 38, 5.5, "DISCOURS RAPPORTÉ", fc=NAVY, ec=NAVY, fs=10.5, bold=True, color="white")
    rows = [("présent simple : \"I work\"", "prétérit : she worked"), ("présent continu : \"I am working\"", "past continuous : she was working"),
            ("prétérit : \"I sent it\"", "past perfect : she had sent it"), ("present perfect : \"I have finished\"", "past perfect : she had finished"),
            ("will : \"I will call\"", "would : she would call"), ("can : \"I can help\"", "could : she could help"),
            ("must : \"You must wait\"", "had to : I had to wait")]
    for i, (a, b) in enumerate(rows):
        y = 38 - i * 5.2
        box(ax, 27, y, 38, 4.3, a, fc=LBLUE, ec=BLUE, fs=8.8)
        box(ax, 73, y, 38, 4.3, b, fc=GREEN, ec=DGREEN, fs=8.8)
        arr(ax, 46.5, y, 53.5, y, color=NAVY, lw=1.8)
    txt(ax, 50, 1.8, "now → then · today → that day · tomorrow → the next day · yesterday → the day before · here → there", fs=8.6, color="#444444", style="italic")
    save(fig, path)


def b2_cond3(path):
    fig, ax = canvas("Conditionnel 3 et conditionnel mixte", "Deux façons de parler d'un passé qui n'a pas eu lieu")
    arr(ax, 5, 22, 95, 22, color="#555555", lw=2.4)
    ax.plot([68, 68], [19.8, 24.2], color=DRED, lw=3)
    txt(ax, 68, 17.2, "maintenant", fs=9, color=DRED, bold=True)
    txt(ax, 24, 17.2, "PASSÉ", fs=9.5, color="#555555", bold=True)
    txt(ax, 88, 17.2, "futur", fs=9, color="#555555")
    ax.plot([24], [22], marker="o", color=DORANGE, ms=11)
    box(ax, 24, 33, 38, 8, "If + past perfect\nIf I had studied (je n'ai pas étudié)", fc=ORANGE, ec=DORANGE, fs=9)
    arr(ax, 24, 29, 24, 23.8, color=DORANGE, lw=1.6)
    box(ax, 24, 44, 40, 6.5, "TYPE 3 : ... I would have passed.", fc=YELLOW, ec=DORANGE, fs=9.5, bold=True)
    box(ax, 74, 44, 44, 6.5, "MIXTE : ... I would have a better job now.", fc=GREEN, ec=DGREEN, fs=9, bold=True)
    arr(ax, 24, 37.2, 24, 40.6, color=DORANGE, lw=1.8)
    arr(ax, 44, 35, 60, 41, color=DGREEN, lw=1.8, rad=-0.1)
    box(ax, 27, 8.5, 48, 11, "Type 3 : If + had + participe,\nwould have + participe\n(passé → passé)", fc=ORANGE, ec=DORANGE, fs=9)
    box(ax, 76, 8.5, 40, 11, "Mixte : If + had + participe,\nwould + base\n(passé → présent)", fc=GREEN, ec=DGREEN, fs=9)
    save(fig, path)


def b2_gerund(path):
    fig, ax = canvas("Verbe + -ing ou verbe + to ?", "Un verbe en suit un autre : quelle forme ?")
    box(ax, 50, 42, 24, 6.5, "VERBE + VERBE", fc=NAVY, ec=NAVY, fs=11, bold=True, color="white")
    cols = [(14, "+ -ing", "enjoy · avoid · finish\nsuggest · mind\nconsider · keep", LBLUE, BLUE),
            (38, "+ to + base", "want · hope · decide\nplan · agree · refuse\nmanage · afford", GREEN, DGREEN),
            (62, "les deux,\nmême sens", "like · love · hate\nstart · begin\nprefer", YELLOW, DORANGE),
            (86, "les deux,\nsens différent", "remember · forget\nstop · try · regret", ORANGE, DRED)]
    for x, t, w, fc, ec in cols:
        arr(ax, 50, 38.7, x, 32.5, color=ec, lw=1.8)
        box(ax, x, 29.5, 21, 6.5, t, fc=ec, ec=ec, fs=9.5, bold=True, color="white")
        box(ax, x, 15, 21, 16, w, fc=fc, ec=ec, fs=9.2)
    box(ax, 86, 3.6, 25, 4.8, "stop smoking ≠ stop to smoke", fc="white", ec=DRED, fs=7.8)
    box(ax, 35, 3.6, 64, 4.8, "Après une préposition : toujours -ing (interested in learning, look forward to meeting)", fc=GREY, ec="#7F7F7F", fs=8.4)
    save(fig, path)


def b2_linkers(path):
    fig, ax = canvas("Les connecteurs logiques par fonction", "Partie 6 du TOEIC : choisir le lien qui convient")
    groups = [("ADDITION", "moreover · furthermore\nin addition · besides", LBLUE, BLUE),
              ("OPPOSITION", "however · nevertheless\non the other hand\nwhereas · in contrast", ORANGE, DORANGE),
              ("CAUSE", "owing to · due to\nsince · as · because of", YELLOW, "#BF9000"),
              ("CONSÉQUENCE", "therefore · consequently\nas a result · thus · hence", GREEN, DGREEN),
              ("EXEMPLE", "for instance · for example\nsuch as · namely", PURPLE, "#7030A0"),
              ("CONCLUSION", "in conclusion · overall\nto sum up · all in all", GREY, "#595959")]
    for i, (t, w, fc, ec) in enumerate(groups):
        x = 18 + (i % 3) * 32
        y = 36 if i < 3 else 14
        box(ax, x, y + 7, 28, 5.5, t, fc=ec, ec=ec, fs=10, bold=True, color="white")
        box(ax, x, y - 2, 28, 11.5, w, fc=fc, ec=ec, fs=9)
    save(fig, path)


def b2_future(path):
    fig, ax = canvas("Les futurs : simple, continu, accompli", "Où se place l'action par rapport à un repère futur ?")
    arr(ax, 5, 28, 95, 28, color="#555555", lw=2.4)
    ax.plot([20, 20], [25.8, 30.2], color=DRED, lw=3); txt(ax, 20, 23, "maintenant", fs=9, color=DRED, bold=True)
    ax.plot([72, 72], [25.8, 30.2], color=NAVY, lw=3); txt(ax, 72, 23, "repère futur\n(June, 5 p.m.)", fs=9, color=NAVY, bold=True)
    ax.add_patch(FancyArrowPatch((22, 33), (70, 33), arrowstyle="-|>", mutation_scale=16, color=DGREEN, lw=5, alpha=0.6))
    box(ax, 33, 44, 44, 7.5, "FUTURE PERFECT : will have + participe\nBy June, we will have hired ten people.", fc=GREEN, ec=DGREEN, fs=9.3)
    ax.add_patch(FancyArrowPatch((66, 36.5), (84, 36.5), arrowstyle="-|>", mutation_scale=16, color=BLUE, lw=5, alpha=0.6))
    box(ax, 79, 44, 36, 7.5, "FUTURE CONTINUOUS : will be + -ing\nAt 5 p.m., I will be flying.", fc=LBLUE, ec=BLUE, fs=9)
    box(ax, 28, 10, 40, 11, "be due to : prévu officiellement\nThe shipment is due to arrive Friday.", fc=YELLOW, ec=DORANGE, fs=9)
    box(ax, 74, 10, 40, 11, "be about to : imminent\nThe meeting is about to begin.", fc=ORANGE, ec=DORANGE, fs=9)
    save(fig, path)


# ---------------- C1 ----------------
def c1_inversion(path):
    fig, ax = canvas("L'inversion pour l'emphase", "Adverbe négatif ou restrictif + auxiliaire + sujet")
    rows = [("I have never seen such a result.", "Never have I seen such a result."),
            ("We had hardly started when the alarm rang.", "Hardly had we started when the alarm rang."),
            ("She had no sooner left than he arrived.", "No sooner had she left than he arrived."),
            ("They not only refused, but also complained.", "Not only did they refuse, but they also complained."),
            ("We saw the error only after the audit.", "Only after the audit did we see the error."),
            ("You should not share this under any circumstances.", "Under no circumstances should you share this.")]
    box(ax, 27, 46, 40, 4.5, "FORME NORMALE", fc=GREY, ec="#7F7F7F", fs=10, bold=True)
    box(ax, 74, 46, 44, 4.5, "FORME INVERSÉE (soutenue)", fc=NAVY, ec=NAVY, fs=10, bold=True, color="white")
    for i, (a, b) in enumerate(rows):
        y = 39 - i * 6.0
        box(ax, 27, y, 44, 4.8, a, fc="white", ec="#7F7F7F", fs=7.9)
        box(ax, 76, y, 44, 4.8, b, fc=LBLUE, ec=BLUE, fs=7.9, bold=True)
        arr(ax, 49.5, y, 53.5, y, color=NAVY, lw=1.6)
    txt(ax, 50, 2.4, "Inversion conditionnelle : Should you need help ... · Were it not for ... · Had we known ...", fs=8.8, style="italic", color="#444444")
    save(fig, path)


def c1_deduction(path):
    fig, ax = canvas("Modaux du passé : degré de certitude", "must / might / can't + have + participe")
    gradient(ax, 6, 94, 28, 7, "#C00000", "#548235")
    txt(ax, 6, 38.5, "0 %", fs=10, bold=True, color=DRED, ha="left")
    txt(ax, 94, 38.5, "100 %", fs=10, bold=True, color=DGREEN, ha="right")
    marks = [(14, "can't / couldn't\nhave + pp", "impossible\nShe can't have sent it.", RED, DRED),
             (50, "may / might / could\nhave + pp", "possible\nThey might have changed it.", YELLOW, DORANGE),
             (86, "must have + pp", "quasi certain\nHe must have missed the train.", GREEN, DGREEN)]
    for x, w, d, fc, ec in marks:
        ax.plot([x, x], [28, 35], color="white", lw=3)
        arr(ax, x, 26.5, x, 23.5, color=ec, lw=1.8)
        box(ax, x, 17.5, 27, 11, f"{w}\n\n{d}", fc=fc, ec=ec, fs=8.4)
    box(ax, 28, 4.3, 50, 5, "should have + pp : reproche, regret (You should have called.)", fc=LBLUE, ec=BLUE, fs=8.5)
    box(ax, 77, 4.3, 38, 5, "needn't have + pp : geste inutile", fc=GREY, ec="#7F7F7F", fs=8.5)
    save(fig, path)


def c1_cleft(path):
    fig, ax = canvas("Mettre en relief : les phrases clivées", "Même information, trois mises en valeur différentes")
    box(ax, 50, 41, 72, 8, "The delay caused the loss.", fc=GREY, ec="#7F7F7F", fs=12, bold=True)
    items = [(17, "IT-CLEFT", "It was the delay\nthat caused the loss.", "souligne le sujet", LBLUE, BLUE),
             (50, "WH-CLEFT", "What caused the loss\nwas the delay.", "souligne l'information", GREEN, DGREEN),
             (83, "ALL-CLEFT", "All we need is\nmore time.", "souligne l'unique chose", ORANGE, DORANGE)]
    for x, t, ex, d, fc, ec in items:
        arr(ax, 50 + (x - 50) * 0.2, 36.5, x, 28.5, color=ec, lw=2)
        box(ax, x, 24.5, 27, 6, t, fc=ec, ec=ec, fs=10.5, bold=True, color="white")
        box(ax, x, 12, 27, 13, ex, fc=fc, ec=ec, fs=10)
        txt(ax, x, 3.5, d, fs=8.8, style="italic", color="#444444")
    save(fig, path)


def c1_register(path):
    fig, ax = canvas("Du registre familier au registre soutenu", "Le TOEIC attend le registre professionnel (colonne centrale à droite)")
    gradient(ax, 6, 94, 44, 2.5, "#F4B183", "#1F3864")
    txt(ax, 6, 48.3, "INFORMEL", fs=10, bold=True, color=DORANGE, ha="left")
    txt(ax, 94, 48.3, "FORMEL", fs=10, bold=True, color=NAVY, ha="right")
    rows = [("get", "receive", "obtain"), ("buy", "purchase", "acquire"), ("ask for", "request", "enquire"),
            ("start", "begin", "commence"), ("end", "finish", "terminate"), ("help", "support", "assist"),
            ("need", "have to", "require")]
    for j, h in enumerate(["informel", "neutre / professionnel", "soutenu"]):
        xs = [17, 50, 83][j]
        box(ax, xs, 39.5, 26, 4.2, h, fc=[ORANGE, LBLUE, "#D9D2E9"][j], ec=[DORANGE, BLUE, NAVY][j], fs=8.8, bold=True)
    for i, r in enumerate(rows):
        y = 33 - i * 4.3
        for j, w in enumerate(r):
            xs = [17, 50, 83][j]
            box(ax, xs, y, 26, 3.4, w, fc="white", ec="#BFBFBF", fs=9)
        arr(ax, 31, y, 36.5, y, color="#7F7F7F", lw=1.2, tdy=0)
        arr(ax, 64, y, 69.5, y, color="#7F7F7F", lw=1.2, tdy=0)
    save(fig, path)


def c1_hedging(path):
    fig, ax = canvas("Atténuer une affirmation (hedging)", "Du ton catégorique au ton nuancé, plus courtois et plus professionnel")
    box(ax, 22, 44, 36, 5.5, "TROP CATÉGORIQUE", fc=RED, ec=DRED, fs=10, bold=True)
    box(ax, 74, 44, 44, 5.5, "NUANCÉ (professionnel)", fc=GREEN, ec=DGREEN, fs=10, bold=True)
    rows = [("This is wrong.", "This seems to be incorrect."), ("It will fail.", "It is likely to / could well fail."),
            ("We disagree.", "I'm not entirely convinced that ..."), ("You must change this.", "It might be worth changing this."),
            ("The data prove it.", "The data suggest / indicate that ..."), ("That's impossible.", "That seems unlikely.")]
    for i, (a, b) in enumerate(rows):
        y = 37 - i * 5.8
        box(ax, 22, y, 36, 4.5, a, fc="white", ec=DRED, fs=9)
        box(ax, 74, y, 44, 4.5, b, fc="white", ec=DGREEN, fs=9)
        arr(ax, 40.7, y, 51.3, y, color=NAVY, lw=1.6)
    txt(ax, 50, 2.2, "Outils : seem · appear · tend to · might · could · it is possible that · somewhat · to some extent", fs=8.6, style="italic", color="#444444")
    save(fig, path)


# ---------------- C2 ----------------
def c2_argument(path):
    fig, ax = canvas("Construire un argument nuancé", "Structure d'un paragraphe de niveau C2")
    steps = [("1", "THÈSE", "claim", "It is widely held that ...", LBLUE, BLUE),
             ("2", "PREUVE", "evidence", "For instance, in particular ...", GREEN, DGREEN),
             ("3", "CONCESSION", "concede", "Admittedly, granted ...", YELLOW, DORANGE),
             ("4", "RÉFUTATION", "rebut", "Nevertheless, however ...", ORANGE, DRED),
             ("5", "CONCLUSION", "conclude", "On balance, ultimately ...", PURPLE, "#7030A0")]
    for i, (n, t, e, f, fc, ec) in enumerate(steps):
        x = 11 + i * 19.5
        box(ax, x, 33, 17, 18, "", fc=fc, ec=ec)
        txt(ax, x, 39.5, n, fs=16, bold=True, color=ec)
        txt(ax, x, 33.8, t, fs=9.3, bold=True, color=ec)
        txt(ax, x, 30.3, f"({e})", fs=8, style="italic")
        txt(ax, x, 25.5, f, fs=7.7)
        if i < 4:
            arr(ax, x + 9, 33, x + 10.5, 33, color=NAVY, lw=2)
    box(ax, 50, 9, 88, 8, "Exemple : It is widely held that remote work boosts output. Studies in several sectors, for instance, report gains. Admittedly,\nthe evidence is mixed; nevertheless, on balance, the benefits appear to outweigh the drawbacks.", fc=GREY, ec="#7F7F7F", fs=8)
    save(fig, path)


def c2_modality(path):
    fig, ax = canvas("L'échelle de la probabilité", "Choisir le bon degré, du certain à l'improbable")
    gradient(ax, 6, 94, 32, 6, "#548235", "#C00000")
    txt(ax, 6, 41.5, "CERTAIN", fs=10, bold=True, color=DGREEN, ha="left")
    txt(ax, 94, 41.5, "IMPROBABLE", fs=10, bold=True, color=DRED, ha="right")
    items = [(12, "will\nis bound to\nis sure to", GREEN, DGREEN), (31, "is likely to\nis set to\nshould (attendu)", LBLUE, BLUE),
             (50, "may well\nis liable to\nstands to", YELLOW, DORANGE), (69, "might\ncould conceivably", ORANGE, DORANGE),
             (88, "is unlikely to\nis hardly likely to\nis most improbable", RED, DRED)]
    for x, w, fc, ec in items:
        ax.plot([x, x], [32, 38], color="white", lw=3)
        arr(ax, x, 30.5, x, 27, color=ec, lw=1.6)
        box(ax, x, 17.5, 17, 17, w, fc=fc, ec=ec, fs=8.4)
    box(ax, 50, 4.2, 88, 5, "Verbes d'atténuation : seem · appear · tend to · is said to · is thought to (prise de distance)", fc=GREY, ec="#7F7F7F", fs=8.5)
    save(fig, path)


def c2_paraphrase(path):
    fig, ax = canvas("Six stratégies de paraphrase", "Reformuler sans répéter les mots d'origine")
    box(ax, 50, 25.5, 20, 9, "PARAPHRASE", fc=NAVY, ec=NAVY, fs=11.5, bold=True, color="white")
    items = [(16, 38, "SYNONYME", "begin → commence", LBLUE, BLUE, (30, 35), (40, 29)),
             (50, 40, "CLASSE DE MOT", "decided quickly →\ntheir decision was quick", GREEN, DGREEN, (50, 34.4), (50, 30.2)),
             (84, 38, "ACTIF ↔ PASSIF", "The board approved it →\nIt was approved", YELLOW, DORANGE, (70, 35), (60, 29)),
             (16, 13, "NÉGATION", "cheap → not expensive", ORANGE, DRED, (30, 16), (40, 22)),
             (50, 10, "STRUCTURE", "Although tired → Despite\nbeing tired", PURPLE, "#7030A0", (50, 15.6), (50, 21)),
             (84, 13, "NOMINALISATION", "because prices rose →\nowing to the rise in prices", GREY, "#595959", (70, 16), (60, 22))]
    for x, y, t, e, fc, ec, p0, p1 in items:
        box(ax, x, y, 28, 10.5, f"{t}\n{e}", fc=fc, ec=ec, fs=8.6)
        arr(ax, p0[0], p0[1], p1[0], p1[1], color="#7F7F7F", lw=1.4)
    save(fig, path)


def c2_tone(path):
    fig, ax = canvas("Registre et ton", "Adapter le niveau de langue au destinataire")
    gradient(ax, 6, 94, 36, 5, "#F4B183", "#1F3864")
    items = [(14, "FAMILIER", "I reckon we should\nwrap this up.", ORANGE, DORANGE), (38, "NEUTRE", "I think we should\nfinish this.", LBLUE, BLUE),
             (62, "PROFESSIONNEL", "I would suggest that\nwe conclude this.", GREEN, DGREEN), (86, "TRÈS FORMEL", "It is my considered view\nthat we ought to conclude.", "#D9D2E9", NAVY)]
    for x, t, e, fc, ec in items:
        ax.plot([x, x], [36, 41], color="white", lw=3)
        arr(ax, x, 34.5, x, 31.5, color=ec, lw=1.6)
        box(ax, x, 22, 21, 17, f"{t}\n\n{e}", fc=fc, ec=ec, fs=8.2)
    txt(ax, 50, 7, "Ton :  tactful (diplomate)  ·  blunt (franc, direct)  ·  curt (sec)  ·  deferential (déférent)  ·  dismissive (méprisant)", fs=8.8, color="#444444", style="italic")
    save(fig, path)


def c2_time(path):
    fig, ax = canvas("Gérer son temps au TOEIC (repères indicatifs)", "2 heures : l'audio impose le rythme ; la lecture se gère soi-même")
    rows = [("Listening (P1–P4)", 45, "audio imposé", LBLUE, BLUE), ("Partie 5 : 30 phrases", 10, "≈ 20 s par question", GREEN, DGREEN),
            ("Partie 6 : 16 questions", 8, "≈ 30 s par question", YELLOW, DORANGE), ("Partie 7 : 54 questions", 57, "≈ 1 min par question", ORANGE, DRED)]
    tot = 120
    x = 6
    for lab, m, note, fc, ec in rows:
        w = 88 * m / tot
        ax.add_patch(FancyBboxPatch((x, 28), w - 0.4, 9, boxstyle="round,pad=0.1,rounding_size=0.6", fc=fc, ec=ec, lw=1.5))
        txt(ax, x + w / 2 - 0.2, 32.5, f"{m} min", fs=11 if m > 15 else 8.6, bold=True, color=ec)
        x += w
    legend_y = 20
    for i, (lab, m, note, fc, ec) in enumerate(rows):
        box(ax, 25 + (i % 2) * 50, legend_y - (i // 2) * 8.5, 43, 6.5, f"{lab} : {m} min  ({note})", fc=fc, ec=ec, fs=8.4)
    txt(ax, 50, 2.8, "Conseil : ne restez jamais bloqué. Répondez, marquez la question et revenez-y s'il reste du temps.", fs=9, style="italic", color="#444444")
    save(fig, path)
