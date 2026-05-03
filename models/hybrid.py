
import pandas as pd, sys, json
df = pd.read_csv(sys.argv[1])
df["timestamp"] = pd.to_datetime(df["timestamp"])
channel_w = {"blog":1.3,"newsletter":1.2,"instagram":1.0,"affiliate":1.5}
inter_w = {"view":0.5,"click":1.0,"conversion":2.0}
res = {}
for user, g in df.groupby("user_id"):
    conv = g[g["conversion"]==True]
    if conv.empty: continue
    rev = conv["revenue"].iloc[0]
    ct = conv["timestamp"].iloc[0]
    g["decay"] = 1/((ct - g["timestamp"]).dt.days + 1)
    g["weight"] = g["decay"] * g["channel"].map(channel_w) * g["interaction_type"].map(inter_w)
    total = g["weight"].sum()
    for _, r in g.iterrows():
        res[r["channel"]] = res.get(r["channel"], 0) + (r["weight"]/total)*rev
print(json.dumps(res))
