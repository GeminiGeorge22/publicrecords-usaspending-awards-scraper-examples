# USAspending Awards Scraper — 使用例

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeminiGeorge22/publicrecords-usaspending-awards-scraper-examples/blob/main/notebooks/quickstart.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GeminiGeorge22/publicrecords-usaspending-awards-scraper-examples/HEAD?labpath=notebooks%2Fquickstart.ipynb)

米連邦の契約・助成金の授与実績：機関、受給者、NAICS、期間。

このActorは**あなた自身の**Apifyアカウント（APIトークンまたはOAuth）で実行します。利用料はApifyの無料または有料プランであなたに課金されます。

## リンク
- [Apify Storeのページ](https://apify.com/publicrecords/usaspending-awards-scraper)
- [Apify MCPエンドポイント](https://mcp.apify.com?tools=publicrecords/usaspending-awards-scraper)
- [n8n / Make / Zapier / Pipedreamのレシピ](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates)
- [公開スナップショット（Hugging Face）](https://huggingface.co/datasets/Publicrecords/us-federal-contract-awards-top100)

## 同期実行

`APIFY_TOKEN` に自分のApifyトークンを設定してください。リポジトリにコミットしないでください。

```bash
export APIFY_TOKEN=YOUR_TOKEN
python3 examples/python/run.py
# node examples/javascript/run.js
# bash examples/curl/run.sh
```

Python・JavaScript・curlの例は `examples/` にあります。作者: Public Records。ライセンス: MIT。このリポジトリにGitHub Actionsはありません。

READMEs: [English](README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [Português](README.pt.md)
