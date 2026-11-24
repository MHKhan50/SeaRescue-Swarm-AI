import argparse,json
from .environment import RescueGrid
from .coordination import sweep_target
from .metrics import summarize
def run(seed=7,steps=250,communication=.75):
    e=RescueGrid(seed=seed)
    for t in range(steps):
        for a in e.agents:
            connected=e.rng.random()<communication
            target=sweep_target(a,t if connected else t//2,e.width,e.height)
            e.move(a,target)
    return summarize(len(e.found),len(e.victims),steps,[a.energy for a in e.agents])
def main():
    p=argparse.ArgumentParser(); p.add_argument("--seed",type=int,default=7); p.add_argument("--steps",type=int,default=250); p.add_argument("--communication",type=float,default=.75); a=p.parse_args()
    print(json.dumps(run(a.seed,a.steps,a.communication),indent=2))
if __name__=="__main__":main()
