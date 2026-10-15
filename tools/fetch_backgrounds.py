"""Download any background listed in backgrounds/index.json that has a
downloadUrl and is not in the repo yet. Run by the fetch-backgrounds GitHub
Action (GitHub's runners can reach Unsplash/Pexels; Claude's workspace can't).
Only licensed, people-free photos go in index.json - see backgrounds/holiday/README.md."""
import json, os, sys, urllib.request

idx = json.load(open("backgrounds/index.json"))
got = 0
for it in idx["items"]:
    url, path = it.get("downloadUrl"), it["file"]
    if not url or os.path.exists(path):
        continue
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "urbook-social-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
        f.write(r.read())
    print("fetched", path, os.path.getsize(path))
    got += 1
print("done,", got, "new file(s)")
