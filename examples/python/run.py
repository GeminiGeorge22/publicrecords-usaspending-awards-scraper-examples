#!/usr/bin/env python3
"""Call publicrecords/usaspending-awards-scraper on YOUR Apify account. Set APIFY_TOKEN. Do not commit the token."""
import json, os, urllib.request

TOKEN = os.environ["APIFY_TOKEN"]
URL = "https://api.apify.com/v2/acts/publicrecords~usaspending-awards-scraper/run-sync-get-dataset-items?token=" + TOKEN
payload = {
  "agency": "Department of Defense",
  "awardTypes": [
    "A",
    "B",
    "C",
    "D"
  ],
  "maxItems": 50
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=300) as resp:
    items = json.load(resp)
print(json.dumps(items[:5] if isinstance(items, list) else items, indent=2, ensure_ascii=False))
print("count", len(items) if isinstance(items, list) else "n/a")
