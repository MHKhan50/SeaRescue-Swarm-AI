# SeaRescue Swarm AI
Simulation-only research starter for cooperative **civilian maritime search and rescue** using abstract aerial and surface agents in a toy 2D grid. It does not connect to or control real vehicles or vessels.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m searescue.run_experiment
```

Research question: how do intermittent communications and limited energy affect simulated search coverage and discovery rate? Compare multiple policies and random seeds before making claims.
