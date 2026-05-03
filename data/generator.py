
import pandas as pd
import random
from datetime import datetime, timedelta
import argparse

def generate(n_users=300, seed=42):
    random.seed(seed)
    channels = ["blog","instagram","newsletter","affiliate"]
    interactions = ["view","click"]
    rows = []
    for u in range(n_users):
        user = f"user_{u}"
        steps = random.randint(3,10)
        start = datetime(2025,1,1) + timedelta(days=random.randint(0,200))
        for s in range(steps):
            rows.append([
                user,
                random.choice(channels),
                random.choice(interactions),
                start + timedelta(days=s),
                "campaign_1",
                False,
                0.0
            ])
        rows.append([
            user,
            "affiliate",
            "conversion",
            start + timedelta(days=steps+1),
            "campaign_1",
            True,
            float(random.randint(200,2000))
        ])
    df = pd.DataFrame(rows, columns=["user_id","channel","interaction_type","timestamp","campaign_id","conversion","revenue"])
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/campaign.csv")
    args = parser.parse_args()
    df = generate()
    df.to_csv(args.out, index=False)
    print(f"Wrote {args.out}")
