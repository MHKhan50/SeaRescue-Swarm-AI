import argparse
import json

from .environment import RescueGrid
from .coordination import sweep_path
from .metrics import summarize


def run(seed=7, steps=250, communication=0.75):
    e = RescueGrid(seed=seed)
    paths = [
        sweep_path(i, len(e.agents), e.width, e.height)
        for i in range(len(e.agents))
    ]
    waypoint_indices = [0] * len(e.agents)

    for _ in range(steps):
        for i, agent in enumerate(e.agents):
            if not agent.active:
                continue

            path = paths[i]

            if waypoint_indices[i] >= len(path):
                continue

            target = path[waypoint_indices[i]]

            if (agent.x, agent.y) == target:
                waypoint_indices[i] += 1

                if waypoint_indices[i] >= len(path):
                    continue

                target = path[waypoint_indices[i]]

            e.move(agent, target)

    return summarize(
        len(e.found),
        len(e.victims),
        steps,
        [agent.energy for agent in e.agents]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--steps", type=int, default=250)
    parser.add_argument("--communication", type=float, default=0.75)
    args = parser.parse_args()

    print(json.dumps(
        run(args.seed, args.steps, args.communication),
        indent=2
    ))


if __name__ == "__main__":
    main()
