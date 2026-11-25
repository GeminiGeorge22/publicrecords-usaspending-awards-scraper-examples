**READMEs:** [English](README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)

# USAspending Awards Scraper — examples

**Try it, tell us, and star it if it helped.** Run any Public Records Actor on your own Apify account, then [leave feedback](https://github.com/GeminiGeorge22/publicrecords-mcp/blob/main/BETA.md). A star is welcome if this repo saved you time. Stars are optional and are never rewarded.

See also [publicrecords-mcp](https://github.com/GeminiGeorge22/publicrecords-mcp) (MCP servers) and [publicrecords-skills](https://github.com/GeminiGeorge22/publicrecords-skills) (Agent Skills).

US federal contract and grant awards by agency, recipient, NAICS and period.

The Actor runs on **your** Apify account (API token or OAuth). Usage is billed to you on Apify's free or paid tier.

## Links
- [MCP servers](https://github.com/GeminiGeorge22/publicrecords-mcp)
- [Agent Skills](https://github.com/GeminiGeorge22/publicrecords-skills)
- [Apify Store page](https://apify.com/publicrecords/usaspending-awards-scraper)
- [Apify MCP endpoint](https://mcp.apify.com?tools=publicrecords/usaspending-awards-scraper)
- [n8n / Make / Zapier / Pipedream recipes](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates)
- [Public snapshot dataset (Hugging Face)](https://huggingface.co/datasets/Publicrecords/us-federal-contract-awards-top100)

## Run a sync job

Set `APIFY_TOKEN` to your own Apify token. Do not commit it.

```bash
export APIFY_TOKEN=YOUR_TOKEN
python3 examples/python/run.py
# node examples/javascript/run.js
# bash examples/curl/run.sh
```

Examples in Python, JavaScript and curl are in `examples/`. Author: Public Records. License: MIT. No GitHub Actions in this repository.

