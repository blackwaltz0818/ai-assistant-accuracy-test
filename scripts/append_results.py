"""Append run results (JSON objects, one per line on stdin) to results/<dir>/raw.jsonl."""
import json, sys
d = sys.argv[1]; meta = json.loads(sys.argv[2])
with open("results/%s/raw.jsonl" % d, "a", encoding="utf-8") as f:
    for line in sys.stdin:
        line = line.strip()
        if line:
            r = json.loads(line); r.update(meta); f.write(json.dumps(r, ensure_ascii=False) + "\n")
