import sys, os, pathlib
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import build, sch_lib, sch_ab, sch_cd
PLAN = {
 "A1": [("toeic", "Le test : 7 parties, 200 questions. Repérez où vous perdez des points."),
        ("a1_present", "Présent simple : après do / does, le verbe n'a jamais de -s."),
        ("a1_inonat", "in, on, at : du plus large (in) au plus précis (at)."),
        ("a1_questions", "Le mot interrogatif se choisit d'après la réponse attendue."),
        ("a1_clock", "Pour l'heure : o'clock, a quarter past, half past, a quarter to.")],
 "A2": [("toeic", "Le test : 7 parties, 200 questions. Repérez où vous perdez des points."),
        ("a2_tenses", "Trois repères : prétérit (fini), présent continu (en cours), futur (will / going to)."),
        ("a2_past", "Prétérit : did / didn't + base ; le verbe ne se met au prétérit que dans l'affirmatif."),
        ("a2_compare", "Court : -er / -est. Long : more / most. Irréguliers : better / best, worse / worst."),
        ("a2_modals", "Modaux : mustn't = interdit, don't have to = pas obligatoire.")],
 "B1": [("b1_perfect", "Date précise = prétérit ; lien avec le présent (for, since, already, yet) = present perfect."),
        ("b1_cond", "Type 0, 1, 2 : plus la situation est irréelle, plus le temps recule."),
        ("b1_passive", "Passif : l'objet passe en sujet, le verbe devient be + participe passé."),
        ("b1_wordform", "Partie 5 : regardez d'abord la position du mot dans la phrase."),
        ("b1_connectors", "Connecteurs : opposition, cause, conséquence, but.")],
 "B2": [("b2_reported", "Discours rapporté : on recule d'un temps et on change les repères."),
        ("b2_cond3", "Type 3 (passé → passé) ou mixte (passé → présent)."),
        ("b2_gerund", "Verbe + verbe : retenez les listes et les verbes à double sens."),
        ("b2_linkers", "Partie 6 : trouvez la relation logique avant de choisir le connecteur."),
        ("b2_future", "Future perfect (accompli avant un repère) et future continuous (en cours à un repère).")],
 "C1": [("c1_inversion", "Après un adverbe négatif ou restrictif, l'auxiliaire passe avant le sujet."),
        ("c1_deduction", "Modaux du passé : de l'impossible (can't have) au quasi certain (must have)."),
        ("c1_cleft", "Phrases clivées : it-cleft, wh-cleft, all-cleft."),
        ("c1_register", "Au TOEIC, privilégiez la colonne neutre ou professionnelle."),
        ("c1_hedging", "Nuancer une affirmation rend le ton plus professionnel.")],
 "C2": [("c2_argument", "Un paragraphe nuancé suit cinq étapes : thèse, preuve, concession, réfutation, conclusion."),
        ("c2_modality", "Du certain à l'improbable : choisissez le degré exact."),
        ("c2_paraphrase", "Six stratégies pour reformuler sans répéter."),
        ("c2_tone", "Le ton doit rester cohérent avec le destinataire."),
        ("c2_time", "Repères de temps par partie du test (à adapter à votre rythme).")],
}
def make(L):
    d = pathlib.Path(__file__).resolve().parent / "sch" / L; d.mkdir(exist_ok=True, parents=True)
    sch_lib.cefr(L, str(d / "cefr.png"))
    items = [("cefr", "Où se situe ce niveau sur l'échelle CECRL et en points TOEIC ?")] + PLAN[L]
    md = build.header(L, "Schémas", "Tutorat d'anglais") + "Chaque schéma résume un point clé de la fiche de grammaire. Regardez-le, cachez la légende, puis expliquez-le avec vos mots.\n\n"
    for n, (k, cap) in enumerate(items, 1):
        p = d / f"{k}.png"
        if k == "toeic": sch_lib.toeic_structure(str(p))
        elif k != "cefr":
            fn = getattr(sch_ab, k, None) or getattr(sch_cd, k)
            fn(str(p))
        md += f"![Schéma {n} : {cap}]({p}){{width=16.5cm}}\n\n"
    tmp = build.OUT / L / f"{L}_Schemas.docx"
    build.write_docx(md, tmp)
    print(L, len(items), "schemas")
for L in sys.argv[1:]: make(L)
