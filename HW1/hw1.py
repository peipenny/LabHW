import itertools

def evaluate_solution(solution):
    return sum(solution)

def exhaustive_search(problem_size):
    best_solution = None
    best_fitness = 0

    all_solutions = itertools.product([0, 1], repeat=problem_size)

    i = 0
    for solution in all_solutions:
        fitness = evaluate_solution(solution)
        if fitness > best_fitness:
            best_fitness = fitness
            best_solution = solution

        print(f"iteration {i+1} - sol: {solution}, fitness: {fitness}")
        i += 1

    return best_solution, best_fitness

problem_size = 100
best_solution, best_fitness = exhaustive_search(problem_size)

print("sol:", best_solution)
print("fitness:", best_fitness)