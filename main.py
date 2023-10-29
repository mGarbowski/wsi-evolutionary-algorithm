from typing import Callable

import numpy as np


def find_best(population: np.ndarray, fitness: np.ndarray) -> tuple[np.ndarray, float]:
    best_idx = np.argmin(fitness)
    best_individual = population[best_idx]
    best_fitness = fitness[best_idx]

    return best_individual, best_fitness


def tournament_reproduction(population: np.ndarray, fitness: np.ndarray) -> np.ndarray:
    return population  # TODO


def mutate(population: np.ndarray, mutation_strength: float):
    pass  # TODO


def evolution(
        fitness_function: Callable[[np.ndarray], np.float64],
        population_size: int = 100,
        mutation_strength: float = 3.0,
        n_fitness_evaluations: int = 10_000,
        cube_bound: float = 100.0,
        dimensions: int = 10
) -> np.ndarray:
    """Evolutionary minimization of fitness function

    Returns the minimum of fitness_function
    """
    max_iterations = n_fitness_evaluations // population_size
    population = np.random.uniform(low=-cube_bound, high=cube_bound, size=(population_size, dimensions))
    fitness = np.apply_along_axis(fitness_function, 1, population)
    best_individual, best_fitness = find_best(population, fitness)

    for _ in range(max_iterations):
        population = tournament_reproduction(population, fitness)
        mutate(population, mutation_strength)
        fitness = np.apply_along_axis(fitness_function, 1, population)

        generation_best_individual, generation_best_fitness = find_best(population, fitness)
        if generation_best_fitness < best_fitness:
            best_individual, best_fitness = generation_best_individual, generation_best_fitness

    return best_individual


def my_fitness(vec: np.ndarray) -> float:
    return np.sum(vec)


def main():
    pop = np.random.uniform(-10, 10, (10, 3))
    print(pop)
    fit = np.apply_along_axis(my_fitness, 0, pop)
    print(pop)
    print(fit)


if __name__ == '__main__':
    main()
