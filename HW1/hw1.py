import itertools
import time

def evaluate_solution(solution):
    return sum(solution)

def exhaustive_search(problem_size, max_runtime):
    best_solution = None
    best_fitness = 0

    all_solutions = itertools.product([0, 1], repeat=problem_size)

    start_time = time.time()
    i = 0
    for solution in all_solutions:
        fitness = evaluate_solution(solution)
        if fitness > best_fitness:
            best_fitness = fitness
            best_solution = solution

        print(f"iteration {i+1} - sol: {solution}, fitness: {fitness}")
        i += 1

        current_time = time.time()
        runtime = current_time - start_time
        if runtime >= max_runtime:
            break

    return best_solution, best_fitness

problem_size = 100
max_runtime = 30 * 60  # 30 minutes

best_solution, best_fitness = exhaustive_search(problem_size, max_runtime)

print("sol:", best_solution)
print("fitness:", best_fitness)