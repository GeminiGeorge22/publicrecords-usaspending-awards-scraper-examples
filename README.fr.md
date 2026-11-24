# USAspending Awards Scraper — exemples

[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeminiGeorge22/publicrecords-usaspending-awards-scraper-examples/blob/main/notebooks/quickstart.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GeminiGeorge22/publicrecords-usaspending-awards-scraper-examples/HEAD?labpath=notebooks%2Fquickstart.ipynb)

Attributions fédérales US (marchés et subventions) par agence, bénéficiaire, NAICS et période.

L'Actor s'exécute sur **votre** compte Apify (jeton API ou OAuth). L'usage vous est facturé, sur l'offre gratuite ou payante d'Apify.

## Liens
- [Fiche Apify Store](https://apify.com/publicrecords/usaspending-awards-scraper)
- [Point d'accès MCP Apify](https://mcp.apify.com?tools=publicrecords/usaspending-awards-scraper)
- [Recettes n8n / Make / Zapier / Pipedream](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates)
- [Jeu de données public (Hugging Face)](https://huggingface.co/datasets/Publicrecords/us-federal-contract-awards-top100)

## Lancer un appel synchrone

Définissez `APIFY_TOKEN` avec votre propre jeton Apify. Ne le commitez pas.

```bash
export APIFY_TOKEN=YOUR_TOKEN
python3 examples/python/run.py
# node examples/javascript/run.js
# bash examples/curl/run.sh
```

Des exemples Python, JavaScript et curl sont dans `examples/`. Auteur : Public Records. Licence : MIT. Pas de GitHub Actions dans ce dépôt.

READMEs: [English](README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [Português](README.pt.md)
