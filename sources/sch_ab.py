from sch_lib import *
import math


# ---------------- A1 ----------------
def a1_present(path):
    fig, ax = canvas("Le présent simple : 3 formes", "Habitudes et vérités générales")
    cols = [(17, "AFFIRMATIF", GREEN, DGREEN, "sujet + verbe\n(+ s à he / she / it)", "She works in Paris.\nWe work in Paris."),
            (50, "NÉGATIF", RED, DRED, "sujet + do / does + not\n+ verbe de base", "She does not work.\nThey do not work."),
            (83, "QUESTION", YELLOW, DORANGE, "Do / Does + sujet\n+ verbe de base ?", "Does she work here?\nDo you work here?")]
    for x, t, fc, ec, rule, ex in cols:
        box(ax, x, 41, 30, 7, t, fc=ec, ec=ec, fs=13, bold=True, color="white")
        box(ax, x, 29, 30, 11, rule, fc=fc, ec=ec, fs=10.5)
        box(ax, x, 15, 30, 11, ex, fc="white", ec=ec, fs=10.5, color="#222222")
        arr(ax, x, 36, x, 34.8, color=ec, lw=1.4)
        arr(ax, x, 23, x, 21, color=ec, lw=1.4)
    box(ax, 50, 3.6, 94, 4.6, "Attention : après do / does, le verbe n'a JAMAIS de -s (Does she work ?  et non  Does she works ?)", fc=YELLOW, ec=DORANGE, fs=10, bold=True)
    save(fig, path)


def a1_inonat(path):
    fig, ax = canvas("in / on / at : du plus large au plus précis", "Les prépositions de temps (et de lieu) fonctionnent comme un entonnoir")
    tiers = [(8, 92, 12, 44, 54, "IN", "siècle, année, saison, mois,\nparties du jour", "in 2026 · in August · in winter\nin the morning", LBLUE, BLUE),
             (14, 86, 22, 34, 44, "ON", "jours, dates", "on Monday · on May 1st\non the second floor", GREEN, DGREEN),
             (22, 78, 32, 24, 34, "AT", "heures précises, moments", "at 9 o'clock · at noon · at night\nat the desk · at the door", ORANGE, DORANGE)]
    # trapezoids
    ys = [(46, 31), (31, 17), (17, 5)]
    xs = [(8, 92, 22, 78), (22, 78, 34, 66), (34, 66, 40, 60)]
    cols = [(LBLUE, BLUE, "IN", "année, saison, mois, partie du jour", "in 2026 · in August · in winter · in the morning", "lieu : un espace (in the office, in Lyon)"),
            (GREEN, DGREEN, "ON", "jour, date", "on Monday · on May 1st", "lieu : une surface (on the table, on the 2nd floor)"),
            (ORANGE, DORANGE, "AT", "heure précise, moment", "at 9 o'clock · at noon · at night", "lieu : un point (at the desk, at the door)")]
    for (ytop, ybot), (xa, xb, xc, xd), (fc, ec, w, l1, l2, l3) in zip(ys, xs, cols):
        ax.add_patch(Polygon([(xa, ytop), (xb, ytop), (xd, ybot), (xc, ybot)], fc=fc, ec=ec, lw=1.8))
    txt(ax, 50, 43, "IN", fs=16, bold=True, color=BLUE)
    txt(ax, 50, 38.7, "année · saison · mois · partie du jour", fs=9.5)
    txt(ax, 50, 35.6, "in 2026 · in August · in winter · in the morning", fs=9.5, style="italic")
    txt(ax, 50, 28, "ON", fs=16, bold=True, color=DGREEN)
    txt(ax, 50, 24.3, "jour · date", fs=9.5)
    txt(ax, 50, 21.2, "on Monday · on May 1st", fs=9.5, style="italic")
    txt(ax, 50, 14, "AT", fs=16, bold=True, color=DORANGE)
    txt(ax, 50, 10.3, "heure précise", fs=9.5)
    txt(ax, 50, 7.2, "at 9 · at noon · at night", fs=9, style="italic")
    txt(ax, 4, 38, "lieu :\nun espace\n(in the office)", fs=8.5, ha="left", color=BLUE)
    txt(ax, 4, 24, "lieu :\nune surface\n(on the table)", fs=8.5, ha="left", color=DGREEN)
    txt(ax, 4, 10, "lieu :\nun point\n(at the desk)", fs=8.5, ha="left", color=DORANGE)
    save(fig, path)


def a1_questions(path):
    fig, ax = canvas("Les mots interrogatifs", "Choisir le mot selon la réponse attendue")
    box(ax, 50, 26, 16, 8, "QUESTION ?", fc=NAVY, ec=NAVY, fs=12, bold=True, color="white")
    items = [("Who ?", "une personne", "Who is late ?  – Anna."), ("What ?", "une chose", "What is this ?  – A file."),
             ("Where ?", "un lieu", "Where is the room ?  – On the 3rd floor."), ("When ?", "un moment", "When do you leave ?  – At six."),
             ("Why ?", "une raison (because)", "Why are you happy ?  – Because ..."), ("How ?", "une manière", "How do you go ?  – By bus."),
             ("How much ?", "un prix, indénombrable", "How much is it ?  – $20."), ("How many ?", "un nombre (dénombrable)", "How many chairs ?  – Ten.")]
    pos = [(16, 39), (50, 40), (84, 39), (88, 26), (84, 13), (50, 12), (16, 13), (12, 26)]
    for (w, sens, ex), (x, y) in zip(items, pos):
        box(ax, x, y, 29 if x not in (88, 12) else 22, 10.5 if x not in (88, 12) else 9.5, f"{w}\n{sens}\n{ex}", fc=LBLUE, ec=BLUE, fs=8.4)
    for (w_, h_), (x, y) in zip([(29, 10.5) if p[0] not in (88, 12) else (22, 9.5) for p in pos], pos):
        dx, dy = 50 - x, 26 - y
        t1 = min((w_ / 2 + 1) / abs(dx) if dx else 9e9, (h_ / 2 + 1) / abs(dy) if dy else 9e9)
        t2 = min(9.5 / abs(dx) if dx else 9e9, 5.5 / abs(dy) if dy else 9e9)
        arr(ax, x + dx * t1, y + dy * t1, 50 - dx * t2, 26 - dy * t2, color="#7F7F7F", lw=1.2)
    save(fig, path)


def a1_clock(path):
    fig, ax = canvas("Dire l'heure en anglais", "Heure pile, et quart, et demie, moins le quart", h=6.0)
    ax.set_aspect("auto")
    items = [(15, "3:00", "three o'clock", 0), (38, "3:15", "a quarter past three", 15), (62, "3:30", "half past three", 30), (85, "3:45", "a quarter to four", 45)]
    for cx, dig, words, mn in items:
        cy = 29
        r = 9.3
        e = Ellipse((cx, cy), 2 * r * 0.6, 2 * r, fc="white", ec=NAVY, lw=2.5)
        ax.add_patch(e)
        for k in range(12):
            a = math.radians(90 - k * 30)
            ax.plot([cx + 0.6 * r * 0.86 * math.cos(a), cx + 0.6 * r * 0.95 * math.cos(a)], [cy + r * 0.86 * math.sin(a), cy + r * 0.95 * math.sin(a)], color=NAVY, lw=1.2)
        # hands
        am = math.radians(90 - mn * 6)
        hrs = 3 + mn / 60
        ah = math.radians(90 - hrs * 30)
        ax.plot([cx, cx + 0.6 * r * 0.8 * math.cos(am)], [cy, cy + r * 0.8 * math.sin(am)], color=BLUE, lw=2.2)
        ax.plot([cx, cx + 0.6 * r * 0.5 * math.cos(ah)], [cy, cy + r * 0.5 * math.sin(ah)], color=DRED, lw=3.2)
        txt(ax, cx, 14.5, dig, fs=15, bold=True, color=NAVY)
        txt(ax, cx, 10, words, fs=9.5, style="italic")
    txt(ax, 50, 3.6, "12:00 = noon (midi) · 00:00 = midnight (minuit) · 9:45 = a quarter to ten", fs=9.5, color="#444444")
    save(fig, path)


# ---------------- A2 ----------------
def a2_tenses(path):
    fig, ax = canvas("Passé, présent, futur : les formes de base", "Quel temps pour quelle idée ?")
    timeline(ax, 30, now=50)
    box(ax, 19, 42, 30, 11, "PRÉTÉRIT SIMPLE\nI worked yesterday.\nWe went to Paris in 2024.", fc=ORANGE, ec=DORANGE, fs=9.5)
    box(ax, 50, 42, 24, 11, "PRÉSENT CONTINU\nI am working now.\n(en ce moment)", fc=YELLOW, ec=DORANGE, fs=9.5)
    box(ax, 81, 42, 32, 11, "FUTUR\nwill : décision, promesse\ngoing to : projet décidé", fc=GREEN, ec=DGREEN, fs=9.5)
    box(ax, 19, 15, 30, 10, "marqueurs : yesterday, last week,\nthree days ago, in 2024", fc="white", ec=DORANGE, fs=9)
    box(ax, 50, 15, 26, 10, "now, at the moment,\ntoday", fc="white", ec=DORANGE, fs=9)
    box(ax, 81, 15, 32, 10, "tomorrow, next week,\nsoon, in two days", fc="white", ec=DGREEN, fs=9)
    save(fig, path)


def a2_past(path):
    fig, ax = canvas("Le prétérit : affirmatif, négatif, question", "Après did / didn't, le verbe revient à la forme de base")
    rows = [(41, "AFFIRMATIF", GREEN, DGREEN, "sujet + verbe au prétérit", "We booked a room.   He went home."),
            (26, "NÉGATIF", RED, DRED, "sujet + did not (didn't) + verbe de base", "We didn't book a room.   He didn't go home."),
            (11, "QUESTION", YELLOW, DORANGE, "Did + sujet + verbe de base ?", "Did you book a room ?   Did he go home ?")]
    for y, t, fc, ec, rule, ex in rows:
        box(ax, 12, y, 20, 10, t, fc=ec, ec=ec, fs=10.5, bold=True, color="white")
        box(ax, 43, y, 38, 10, rule, fc=fc, ec=ec, fs=10)
        box(ax, 82, y, 33, 10, ex.replace("   ", "\n"), fc="white", ec=ec, fs=9.2)
        arr(ax, 22, y, 24, y, color=ec)
        arr(ax, 62.5, y, 65, y, color=ec)
    save(fig, path)


def a2_compare(path):
    fig, ax = canvas("Comparatifs et superlatifs", "Trois familles d'adjectifs")
    heads = ["Adjectif", "Comparatif", "Superlatif"]
    xs = [27, 55, 83]
    for x, h in zip(xs, heads):
        box(ax, x, 44.5, 25, 5.5, h, fc=NAVY, ec=NAVY, fs=11, bold=True, color="white")
    fam = [(33, "COURT (1 syllabe)", "fast", "fast + er + than\nfaster than", "the fast + est\nthe fastest", LBLUE, BLUE),
           (19.5, "LONG (2+ syllabes)", "expensive", "more + adjectif + than\nmore expensive than", "the most + adjectif\nthe most expensive", GREEN, DGREEN),
           (6.5, "IRRÉGULIER", "good / bad", "better / worse", "the best / the worst", ORANGE, DORANGE)]
    for y, name, ex, comp, sup, fc, ec in fam:
        txt(ax, 14.5, y + 6.2, name, fs=8.8, bold=True, color=ec, ha="left")
        box(ax, 27, y, 25, 9, ex, fc=fc, ec=ec, fs=10.5, bold=True)
        box(ax, 55, y, 25, 9, comp, fc=fc, ec=ec, fs=9.2)
        box(ax, 83, y, 25, 9, sup, fc=fc, ec=ec, fs=9.2)
        arr(ax, 39.8, y, 42.2, y, color=ec)
        arr(ax, 67.8, y, 70.2, y, color=ec)
    save(fig, path)


def a2_modals(path):
    fig, ax = canvas("Les verbes modaux : de l'obligation à la liberté", "Pas de -s à la 3e personne, toujours suivis de la base verbale")
    ax.add_patch(Polygon([(6, 33), (94, 25), (94, 41), (6, 41)], fc="none", ec="none"))
    # gradient bar
    n = 40
    import matplotlib.colors as mc
    c1, c2 = mc.to_rgb("#C55A11"), mc.to_rgb("#548235")
    for i in range(n):
        t = i / (n - 1)
        col = tuple(c1[k] * (1 - t) + c2[k] * t for k in range(3))
        ax.add_patch(plt.Rectangle((6 + i * 88 / n, 31), 88 / n + 0.1, 5, fc=col, ec="none"))
    txt(ax, 6, 39.5, "OBLIGATION", fs=10, bold=True, color=DORANGE, ha="left")
    txt(ax, 94, 39.5, "LIBERTÉ", fs=10, bold=True, color=DGREEN, ha="right")
    items = [(14, "must\nhave to", "obligation forte"), (36, "should", "conseil"), (58, "could / can", "permission,\nrequête polie"), (80, "may / might", "possibilité")]
    for x, w, d in items:
        arr(ax, x, 30.5, x, 26.5, color=NAVY, lw=1.4)
        box(ax, x, 21.2, 19, 9, f"{w}", fc=LBLUE, ec=BLUE, fs=10.5, bold=True)
        txt(ax, x, 12, d, fs=9)
    box(ax, 26, 5, 42, 6.2, "mustn't = INTERDIT  (You mustn't smoke.)", fc=RED, ec=DRED, fs=9.5, bold=True)
    box(ax, 74, 5, 44, 6.2, "don't have to = PAS OBLIGATOIRE", fc=GREEN, ec=DGREEN, fs=9.5, bold=True)
    save(fig, path)


# ---------------- B1 ----------------
def b1_perfect(path):
    fig, ax = canvas("Present perfect ou prétérit ?", "Le present perfect relie le passé au présent")
    # two timelines
    txt(ax, 4, 46, "PRÉTÉRIT SIMPLE : fini, daté", fs=10.5, bold=True, color=DORANGE, ha="left")
    arr(ax, 6, 38, 94, 38, color="#555555", lw=2.2)
    ax.plot([70, 70], [35.8, 40.2], color=DRED, lw=3); txt(ax, 70, 33, "maintenant", fs=9, color=DRED)
    ax.plot([30], [38], marker="X", color=DORANGE, ms=11)
    txt(ax, 30, 44, "I sent it yesterday.", fs=9.5, style="italic")
    txt(ax, 30, 33, "hier (date précise)", fs=9, color="#555555")
    txt(ax, 4, 27, "PRESENT PERFECT : relié au présent", fs=10.5, bold=True, color=BLUE, ha="left")
    arr(ax, 6, 17.5, 94, 17.5, color="#555555", lw=2.2)
    ax.plot([70, 70], [15.3, 19.7], color=DRED, lw=3); txt(ax, 70, 12.5, "maintenant", fs=9, color=DRED)
    ax.add_patch(FancyArrowPatch((22, 17.5), (70, 17.5), arrowstyle="-|>", mutation_scale=18, color=BLUE, lw=6, alpha=0.55))
    txt(ax, 46, 22.5, "I have worked here since 2023.", fs=9.8, style="italic")
    txt(ax, 22, 12.5, "début", fs=9, color="#555555")
    box(ax, 30, 5, 56, 5.5, "have / has + participe passé · for + durée · since + point de départ", fc=YELLOW, ec=DORANGE, fs=9)
    box(ax, 80, 5, 30, 5.5, "ever · never · already · yet", fc=GREEN, ec=DGREEN, fs=9)
    save(fig, path)


def b1_cond(path):
    fig, ax = canvas("Les conditionnels 0, 1 et 2", "Plus la probabilité baisse, plus le temps recule")
    rows = [(40, "TYPE 0", "toujours vrai", "If + présent, présent", "If you heat ice, it melts.", GREEN, DGREEN, 100),
            (26, "TYPE 1", "possible dans le futur", "If + présent, will + base", "If I finish early, I will call you.", YELLOW, DORANGE, 65),
            (12, "TYPE 2", "irréel ou improbable", "If + prétérit, would + base", "If I had more time, I would study.", ORANGE, DRED, 25)]
    for y, t, sens, rule, ex, fc, ec, p in rows:
        box(ax, 11, y, 16, 10, f"{t}", fc=ec, ec=ec, fs=12, bold=True, color="white")
        box(ax, 38, y, 33, 10, f"{rule}\n{sens}", fc=fc, ec=ec, fs=9.5)
        box(ax, 73.5, y, 28, 10, ex, fc="white", ec=ec, fs=8.6)
        ax.add_patch(plt.Rectangle((90.3, y - 5), 2.6, 10, fc="white", ec=ec, lw=1))
        ax.add_patch(plt.Rectangle((90.3, y - 5), 2.6, 10 * p / 100, fc=ec, ec=ec))
        arr(ax, 19.5, y, 20.2, y, color=ec)
    txt(ax, 91.6, 4.5, "probabilité", fs=7, color="#555555")
    save(fig, path)


def b1_passive(path):
    fig, ax = canvas("Du actif au passif", "L'objet devient sujet ; le verbe devient be + participe passé")
    txt(ax, 4, 49, "ACTIF", fs=11, bold=True, color=DORANGE, ha="left")
    box(ax, 22, 42, 28, 8, "The company", fc=LBLUE, ec=BLUE, fs=11)
    box(ax, 52, 42, 22, 8, "sent", fc=ORANGE, ec=DORANGE, fs=11)
    box(ax, 80, 42, 28, 8, "the invoice", fc=GREEN, ec=DGREEN, fs=11)
    txt(ax, 22, 36.5, "sujet", fs=8.5, color="#555555"); txt(ax, 52, 36.5, "verbe", fs=8.5, color="#555555"); txt(ax, 80, 36.5, "objet", fs=8.5, color="#555555")
    txt(ax, 4, 26, "PASSIF", fs=11, bold=True, color=BLUE, ha="left")
    box(ax, 22, 18, 28, 8, "The invoice", fc=GREEN, ec=DGREEN, fs=11)
    box(ax, 52, 18, 22, 8, "was sent", fc=ORANGE, ec=DORANGE, fs=11)
    box(ax, 80, 18, 28, 8, "by the company", fc=LBLUE, ec=BLUE, fs=11)
    arr(ax, 80, 37.5, 25, 22.5, color=DGREEN, lw=2, rad=0.0)
    arr(ax, 22, 37.5, 78, 22.5, color=BLUE, lw=2, rad=0.0)
    box(ax, 52, 6, 92, 6.5, "Temps : présent = is / are + pp · prétérit = was / were + pp · perfect = has / have been + pp · futur = will be + pp", fc=YELLOW, ec=DORANGE, fs=8.8)
    save(fig, path)


def b1_wordform(path):
    fig, ax = canvas("Formation des mots : quelle nature de mot manque ?", "Partie 5 du TOEIC : repérer la position dans la phrase")
    data = [(18, 36, "NOM", "après un article ou\nun possessif", "The ____ of the plan\n(decision)", LBLUE, BLUE),
            (50, 36, "VERBE", "après un sujet\nou un modal", "We will ____ the file\n(update)", GREEN, DGREEN),
            (82, 36, "ADJECTIF", "avant un nom ou\naprès be", "a ____ manager\n(reliable)", YELLOW, DORANGE),
            (34, 12, "ADVERBE", "modifie un verbe,\nun adjectif, une phrase", "She replied ____\n(quickly)", ORANGE, DRED),
            (66, 12, "SUFFIXES", "-tion -ment -ness : nom\n-ize -ify -en : verbe\n-ful -able -ive -al : adj.\n-ly : adverbe", "", PURPLE, "#7030A0")]
    for x, y, t, rule, ex, fc, ec in data:
        w = 28 if t != "SUFFIXES" else 34
        h = 20 if t != "SUFFIXES" else 21
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2 + (0 if t != 'SUFFIXES' else 0)), w, h, boxstyle="round,pad=0.25,rounding_size=1.2", fc=fc, ec=ec, lw=1.6))
        txt(ax, x, y + h / 2 - 3, t, fs=11.5, bold=True, color=ec)
        txt(ax, x, y + (1.5 if ex else -1.5), rule, fs=8.6)
        if ex:
            txt(ax, x, y - 6, ex, fs=8.6, style="italic", color="#333333")
    save(fig, path)


def b1_connectors(path):
    fig, ax = canvas("Les connecteurs essentiels", "Choisir selon la relation logique")
    groups = [(14, "OPPOSITION", "but · however\nalthough · even though\nwhereas · despite", LBLUE, BLUE),
              (38, "CAUSE", "because · since · as\nbecause of · due to", GREEN, DGREEN),
              (62, "CONSÉQUENCE", "so · therefore\nas a result", YELLOW, DORANGE),
              (86, "BUT", "to · in order to\nso that", ORANGE, DRED)]
    for x, t, w, fc, ec in groups:
        box(ax, x, 44, 21, 7, t, fc=ec, ec=ec, fs=10.5, bold=True, color="white")
        box(ax, x, 27, 21, 21, w, fc=fc, ec=ec, fs=9.8)
        arr(ax, x, 40, x, 37.8, color=ec, lw=1.4)
    box(ax, 50, 6, 92, 7.5, "although + proposition  ·  despite / in spite of + nom ou -ing  ·  because + proposition  ·  because of / due to + nom", fc=GREY, ec="#7F7F7F", fs=9, bold=True)
    save(fig, path)
