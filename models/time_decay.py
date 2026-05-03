
import pandas as pd, sys, json
df = pd.read_csv(sys.argv[1])
df["timestamp"] = pd.to_datetime(df["timestamp"])
res = {}
for user, g in df.groupby("user_id"):
    conv = g[g["conversion"]==True]
    if conv.empty: continue
    rev = conv["revenue"].iloc[0]
    ct = conv["timestamp"].iloc[0]
    g["w"] = 1/((ct - g["timestamp"]).dt.days + 1)
    total = g["w"].sum()
    for _, r in g.iterrows():
        res[r["channel"]] = res.get(r["channel"], 0) + (r["w"]/total)*rev
print(json.dumps(res))
