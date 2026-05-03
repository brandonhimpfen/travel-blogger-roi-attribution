
import pandas as pd, sys, json
df = pd.read_csv(sys.argv[1])
res = {}
for _, r in df[df["conversion"]==True].iterrows():
    res[r["channel"]] = res.get(r["channel"], 0) + r["revenue"]
print(json.dumps(res))
