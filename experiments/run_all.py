
import subprocess, json, argparse, os

def run(cmd):
    out = subprocess.check_output(cmd, shell=True)
    return json.loads(out.decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/campaign.csv")
    args = parser.parse_args()

    os.makedirs("results", exist_ok=True)

    lc = run(f"python models/last_click.py {args.input}")
    mt = run(f"python models/multi_touch.py {args.input}")
    td = run(f"python models/time_decay.py {args.input}")
    hy = run(f"python models/hybrid.py {args.input}")

    json.dump(lc, open("results/last_click.json","w"))
    json.dump(mt, open("results/multi_touch.json","w"))
    json.dump(td, open("results/time_decay.json","w"))
    json.dump(hy, open("results/hybrid.json","w"))

    # comparison csv
    channels = set(lc) | set(mt) | set(td) | set(hy)
    rows = []
    for c in channels:
        rows.append({
            "channel": c,
            "last_click": lc.get(c,0),
            "multi_touch": mt.get(c,0),
            "time_decay": td.get(c,0),
            "hybrid": hy.get(c,0),
            "delta": hy.get(c,0) - lc.get(c,0)
        })
    import pandas as pd
    df = pd.DataFrame(rows).sort_values("channel")
    df.to_csv("results/comparison.csv", index=False)
    print("Wrote results/*.json and results/comparison.csv")
