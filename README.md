# Holistic Evaluation of Travel Blogger Campaign ROI and Attribution Models

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![DOI](https://zenodo.org/badge/1226993436.svg)](https://doi.org/10.5281/zenodo.20032513)

A system-level, reproducible framework for evaluating ROI and attribution across multi-channel travel marketing campaigns.

## Overview

Travel marketing operates across distributed channels (blogs, social, newsletters, affiliates). Traditional attribution (especially last-click) compresses multi-stage journeys into single events, leading to misallocation of value.

This repository provides:

- A Signal-level research paper (paper/paper.md)
- A production-grade dataset generator (data/generator.py)
- Attribution models: last-click, linear multi-touch, time-decay, hybrid (models/)
- A reproducible experiment pipeline (experiments/)
- Comparable outputs (results/*.json, results/comparison.csv)
- Publication-ready visuals (results/figures/)
- Citation + DOI-ready metadata

## Core Idea

Attribution is a system, not a report. The goal is to represent how influence is distributed across time, channels, and interactions.

The hybrid model combines:
- Time decay (recency)
- Channel weights (context)
- Interaction weights (intent)

## Structure

```
.
├── paper/
├── data/
├── models/
├── experiments/
├── results/
│   └── figures/
├── methodology/
├── CITATION.cff
├── .zenodo.json
└── README.md
```

## Quick Start

```bash
pip install pandas matplotlib numpy
python data/generator.py --out data/campaign.csv
python experiments/run_all.py --input data/campaign.csv
python experiments/make_charts.py
```

Open the notebook:

```bash
jupyter notebook experiments/analysis.ipynb
```

## Outputs

```
results/
  last_click.json
  multi_touch.json
  time_decay.json
  hybrid.json
  comparison.csv
  figures/
    last_click.png
    multi_touch.png
    time_decay.png
    hybrid.png
    comparison.png
```

## Example Comparison

| Channel     | last_click | multi_touch | hybrid | delta |
|------------|------------|-------------|--------|-------|
| blog        | 2000       | 5500        | 7000   | 5000  |
| instagram   | 1000       | 5200        | 4000   | 3000  |
| newsletter  | 1500       | 5300        | 6000   | 4500  |
| affiliate   | 18000      | 6000        | 9000   | -9000 |

## Reproducibility

- Dataset is generated programmatically
- Models are deterministic given a seed
- Full pipeline can be rerun end-to-end

## Citation

See CITATION.cff

## License

MIT
