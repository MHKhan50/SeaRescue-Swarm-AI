# SeaRescue Swarm AI

Simulation-only research code for cooperative **civilian maritime search and rescue** (SAR). Abstract aerial and surface
agents search a 2D grid for drifting persons in the water under intermittent communication and limited energy. The
code does not connect to or control real vehicles or vessels.

**Research question:** how do communication reliability and energy limits change search coverage, discovery rate and
time to discovery, and which coordination policy holds up best?

## What is in the code

| Module | Role |
|---|---|
| `searescue/environment.py` | Grid world, victim placement, agent movement and energy |
| `searescue/coordination.py` | Sweep (lawnmower) paths divided between the team members |
| `searescue/communication.py` | Message passing with delay and random packet loss; agents share the victims they have found |
| `searescue/metrics.py` | Discovery rate, energy remaining |
| `searescue/run_experiment.py` | One simulated mission |
| `searescue/evaluate.py` | Several seeds, summary statistics |

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m searescue.run_experiment                 # one mission
python -m searescue.evaluate --seeds 1 2 3 4 5 6 7 8 9 10 --communication 0.75
python -m pytest -q                               # 7 tests
```

## Current status

With the default settings (250 steps, communication reliability 0.75) the team finds all 5 victims in every one of 10
seeds (discovery rate 1.000, mean energy remaining 36.7). The default scenario is therefore too easy to separate
policies: a ceiling effect, not a result. The next step is a harder benchmark (larger grids, drift, fewer steps,
lower reliability) with a sweep over communication reliability and team size, step-to-discovery curves and
confidence intervals across seeds, as set out in `research/PAPER_OUTLINE.md`.

## How to cite

```bibtex
@software{hussain2026searescue,
  author = {Hussain, Muzammal},
  title  = {{SeaRescue Swarm AI: communication-aware multi-agent search simulation for civilian maritime rescue}},
  year   = {2026},
  url    = {https://github.com/MHKhan50/SeaRescue-Swarm-AI}
}
```

## Author

Muzammal Hussain, independent researcher, Glasgow, United Kingdom.
ORCID: [0009-0001-2570-5686](https://orcid.org/0009-0001-2570-5686)

## Licence

MIT. See `LICENSE`.

