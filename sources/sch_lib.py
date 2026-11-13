import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, FancyArrowPatch, Ellipse
plt.rcParams["font.family"] = "DejaVu Sans"

NAVY = "#1F3864"; BLUE = "#2E75B6"; LBLUE = "#DDEBF7"; GREEN = "#E2F0D9"; DGREEN = "#548235"
ORANGE = "#FCE4D6"; DORANGE = "#C55A11"; YELLOW = "#FFF2CC"; GREY = "#EDEDED"; RED = "#F8D7DA"; DRED = "#C00000"
PURPLE = "#E4DFEC"


def canvas(title, sub=None, w=10, h=6.0):
    fig = plt.figure(figsize=(w, h), dpi=170)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 60 * h / 6.0)
    ax.axis("off")
    top = 60 * h / 6.0
    ax.add_patch(FancyBboxPatch((1.5, top - 7.2), 97, 5.6, boxstyle="round,pad=0.2,rounding_size=1", fc=NAVY, ec=NAVY))
    ax.text(50, top - 4.4, title, ha="center", va="center", color="white", fontsize=15, fontweight="bold")
    if sub:
        ax.text(50, top - 10.2, sub, ha="center", va="center", color="#444444", fontsize=10.5, style="italic")
    return fig, ax


def box(ax, cx, cy, w, h, text, fc=LBLUE, ec=BLUE, fs=10, bold=False, color="#111111", ha="center", lw=1.4, style="round,pad=0.25,rounding_size=1.2"):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw))
    ax.text(cx if ha == "center" else cx - w / 2 + 1.2, cy, text, ha=ha, va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", color=color, linespacing=1.35)


def arr(ax, x1, y1, x2, y2, text=None, color=NAVY, fs=9, lw=1.8, rad=0.0, tdx=0, tdy=1.6):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=15, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))
    if text:
        ax.text((x1 + x2) / 2 + tdx, (y1 + y2) / 2 + tdy, text, ha="center", va="center", fontsize=fs, color=color,
                bbox=dict(fc="white", ec="none", pad=0.6))


def txt(ax, x, y, s, fs=10, color="#111111", ha="center", bold=False, style="normal", va="center"):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=color, fontweight="bold" if bold else "normal", style=style, linespacing=1.35)


def save(fig, path):
    fig.savefig(path, dpi=170, facecolor="white")
    plt.close(fig)


def timeline(ax, y, x0=5, x1=95, now=50, labels=("PASSÉ", "PRÉSENT", "FUTUR")):
    arr(ax, x0, y, x1, y, color="#555555", lw=2.5)
    ax.plot([now, now], [y - 2.2, y + 2.2], color=DRED, lw=3)
    txt(ax, now, y - 4.2, labels[1], fs=10, color=DRED, bold=True)
    txt(ax, (x0 + now) / 2, y - 4.2, labels[0], fs=10, color="#555555", bold=True)
    txt(ax, (now + x1) / 2, y - 4.2, labels[2], fs=10, color="#555555", bold=True)


def cefr(level, path):
    fig, ax = canvas("Échelle CECRL – TOEIC", "Votre niveau est en couleur vive ; les autres sont en gris")
    levels = [("A1", "120–220"), ("A2", "225–545"), ("B1", "550–780"), ("B2", "785–940"), ("C1", "945–990"), ("C2", "perfectionnement")]
    for i, (lv, sc) in enumerate(levels):
        x = 6 + i * 15.5
        h = 14 + i * 5.0
        on = lv == level
        ax.add_patch(FancyBboxPatch((x, 8), 13.2, h, boxstyle="round,pad=0.2,rounding_size=1", fc=BLUE if on else GREY, ec=NAVY if on else "#999999", lw=2 if on else 1))
        txt(ax, x + 6.6, 8 + h - 3.2, lv, fs=17, bold=True, color="white" if on else "#777777")
        txt(ax, x + 6.6, 11.5, sc, fs=8.5 if lv != "C2" else 7.6, color="white" if on else "#777777", bold=on)
    txt(ax, 50, 3.5, "Score TOEIC Listening & Reading (sur 990)", fs=10, color="#444444", style="italic")
    save(fig, path)


def toeic_structure(path):
    fig, ax = canvas("Structure du TOEIC Listening & Reading", "200 questions, 2 heures, score de 10 à 990")
    L = [("Partie 1", "Photographies", 6), ("Partie 2", "Question – réponse", 25), ("Partie 3", "Conversations", 39), ("Partie 4", "Exposés, annonces", 30)]
    R = [("Partie 5", "Phrases à compléter", 30), ("Partie 6", "Textes à compléter", 16), ("Partie 7", "Compréhension écrite", 54)]
    def row(y, parts, color, title, mins):
        txt(ax, 3, y + 13, f"{title} – 100 questions – {mins} min", fs=11, bold=True, color=NAVY, ha="left")
        x = 3
        for name, label, n in parts:
            w = 94 * n / 100
            ax.add_patch(FancyBboxPatch((x, y), w - 0.6, 9, boxstyle="round,pad=0.1,rounding_size=0.6", fc=color, ec=NAVY, lw=1.2))
            if w > 9:
                txt(ax, x + w / 2 - 0.3, y + 6.1, name, fs=9, bold=True)
                txt(ax, x + w / 2 - 0.3, y + 3.4, label if w > 14 else "", fs=8)
                txt(ax, x + w / 2 - 0.3, y + 1.3, f"{n} q.", fs=8.5, color=DRED, bold=True)
            else:
                txt(ax, x + w / 2 - 0.3, y + 6.0, "P1", fs=9, bold=True)
                txt(ax, x + w / 2 - 0.3, y + 1.3, f"{n}", fs=8.5, color=DRED, bold=True)
            x += w
        return
    row(30, L, LBLUE, "LISTENING", 45)
    row(10, R, GREEN, "READING", 75)
    txt(ax, 50, 4, "P1 = 6 photos · P2 = 25 · P3 = 39 · P4 = 30 · P5 = 30 · P6 = 16 · P7 = 54", fs=9, color="#444444", style="italic")
    save(fig, path)
