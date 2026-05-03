
import json, os
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("results/figures", exist_ok=True)

def plot_json(path, title):
    with open(path) as f:
        data = json.load(f)
    plt.figure()
    plt.bar(list(data.keys()), list(data.values()))
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    out = f"results/figures/{title}.png"
    plt.savefig(out)
    plt.close()

if __name__ == "__main__":
    plot_json("results/last_click.json", "last_click")
    plot_json("results/multi_touch.json", "multi_touch")
    plot_json("results/time_decay.json", "time_decay")
    plot_json("results/hybrid.json", "hybrid")

    df = pd.read_csv("results/comparison.csv")
    df.set_index("channel")[["last_click","multi_touch","time_decay","hybrid"]].plot(kind="bar")
    plt.title("Comparison by Channel")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/figures/comparison.png")
    plt.close()
