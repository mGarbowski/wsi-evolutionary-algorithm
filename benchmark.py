from dataclasses import dataclass
from typing import Callable

import numpy as np

from evolution import evolution, Solution
from cec2017.functions import f2, f13


@dataclass
class Result:
    func_name: str
    n_samples: int
    mutation_strength: float
    population_size: int
    avg_value: float
    std_value: float
    min_value: float
    max_value: float


@dataclass
class Experiment:
    function: Callable
    population_size: int
    mutation_strength: float
    n_samples: int = 25
    n_fitness_evaluations: int = 10_000


def make_experiment(experiment: Experiment):
    solutions = [
        evolution(
            fitness_function=experiment.function,
            population_size=experiment.population_size,
            mutation_strength=experiment.mutation_strength,
            n_fitness_evaluations=experiment.n_fitness_evaluations
        ) for _ in range(experiment.n_samples)
    ]

    opt_values = [solution[1] for solution in solutions]

    return Result(
        experiment.function.__name__,
        experiment.n_samples,
        experiment.mutation_strength,
        experiment.population_size,
        np.average(opt_values),
        np.std(opt_values),
        np.min(opt_values),
        np.max(opt_values)
    )


def print_results(results: list[Result]):
    print("| Function | Samples | Sigma | Mu    | Avg         | Std         | Min         | Max         |")
    print("|----------|---------|-------|-------|-------------|-------------|-------------|-------------|")
    for r in results:
        print(
            f"| {r.func_name:>8} | {r.n_samples:>7} | {r.mutation_strength:>5} | {r.population_size:>5} | {r.avg_value:>11.2f} | {r.std_value:>11.2f} | {r.min_value:>11.2f} | {r.max_value:>11.2f} |")


def main():
    # f2 experiments
    # experiments = [Experiment(f2, 2**power, 3.0) for power in range(2, 7)]
    # experiments = [Experiment(f2, 16, mut) for mut in (0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0)]
    # experiments = [Experiment(f2, 16, mut, n_fitness_evaluations=50_000) for mut in (0.5, 1.0)]

    # f13 experiments
    # experiments = [Experiment(f13, 2**power, 3.0) for power in range(2, 7)]
    # experiments = [Experiment(f13, pop, mut) for pop in (8, 16) for mut in (0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0)]
    experiments = [
        Experiment(f13, 8, 1.0, n_fitness_evaluations=50_000),
        Experiment(f13, 16, 0.5, n_fitness_evaluations=50_000),
    ]

    results = [make_experiment(e) for e in experiments]
    print_results(results)


if __name__ == '__main__':
    main()
