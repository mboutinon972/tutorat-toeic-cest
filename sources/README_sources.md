# Sources de génération

Ces fichiers servent à régénérer les documents du dossier `Niveaux`.

- `levels/<niveau>.txt` : exercices, textes, scripts audio et questions (format maison).
- `audio_src/<niveau>.txt` : scripts audio d'origine (réponse correcte en premier).
- `lex/<niveau>.lex` : lexiques (mot | nature | traduction).
- `gram/<niveau>.md` : fiches de grammaire et conjugaison.
- `build.py` : exercices, corrigés et audio. `python3 build.py A1 --audio`
- `lexbuild.py`, `schbuild.py`, `sch_*.py` : lexiques et schémas.
- `guide.md` : guide du tuteur.

Prérequis : pandoc, python-docx, matplotlib, wordfreq (facultatif), et pour l'audio kokoro-onnx avec le modèle dans `~/tts`.
