from typing import Callable

import numpy as np


def find_best(population: np.ndarray, fitness_function: Callable[[np.ndarray], np.float64]) -> tuple[np.ndarray, float]:
    best_individual = None
    best_fitness = float("inf")

    for individual in population:
        fitness = fitness_function(individual)
        if fitness < best_fitness:
            best_individual = individual
            best_fitness = fitness

    return best_individual, best_fitness


def tournament_reproduction(population: np.ndarray, fitness_function: Callable[[np.ndarray], np.float64]) -> np.ndarray:
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
    best_individual, best_fitness = find_best(population, fitness_function)

    for _ in range(max_iterations):
        population = tournament_reproduction(population, fitness_function)
        mutate(population, mutation_strength)
        generation_best_individual, generation_best_fitness = find_best(population, fitness_function)
        if generation_best_fitness < best_fitness:
            best_individual, best_fitness = generation_best_individual, generation_best_fitness

    return best_individual


def inplace_op(arr: np.ndarray):
    ones = np.random.uniform(0.0, 1.0, arr.shape)
    np.add(arr, ones, out=arr)


def main():
    my_arr = np.linspace(-5, 5, 10)
    print(my_arr)
    np.clip(my_arr, -3.0, 3.0, my_arr)
    print(my_arr)


if __name__ == '__main__':
    main()
