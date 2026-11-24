import argparse
import json
import statistics

from searescue.run_experiment import run


def evaluate(seeds, steps, communication):
    results = []

    for seed in seeds:
        result = run(
            seed=seed,
            steps=steps,
            communication=communication
        )
        results.append({
            "seed": seed,
            **result
        })

    rates = [item["discovery_rate"] for item in results]
    energies = [item["mean_energy_remaining"] for item in results]

    return {
        "runs": results,
        "summary": {
            "number_of_runs": len(results),
            "mean_discovery_rate": statistics.mean(rates),
            "mean_energy_remaining": statistics.mean(energies),
            "discovery_rate_std_dev": (
                statistics.stdev(rates) if len(rates) > 1 else 0.0
            )
        }
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, nargs="+",
                        default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    parser.add_argument("--steps", type=int, default=250)
    parser.add_argument("--communication", type=float, default=0.75)
    args = parser.parse_args()

    report = evaluate(args.seeds, args.steps, args.communication)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
