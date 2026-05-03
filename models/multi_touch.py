
import pandas as pd, sys, json
df = pd.read_csv(sys.argv[1])
res = {}
for user, g in df.groupby("user_id"):
    conv = g[g["conversion"]==True]
    if conv.empty: continue
    rev = conv["revenue"].iloc[0]
    for _, r in g.iterrows():
        res[r["channel"]] = res.get(r["channel"], 0) + rev/len(g)
print(json.dumps(res))
