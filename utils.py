def print_matrix(matrix, n):
    """
    Prints a square matrix in a table format with even spacing.
    
    Args:
        matrix (list of list of int/float): The matrix to be printed.
        n (int): The dimension of the square matrix (n x n).
    """
    # Determine the maximum width needed for any element
    max_width = max(len(str(matrix[i][j])) for i in range(n) for j in range(n))
    
    for i in range(n):
        print('|', end=' ')
        for j in range(n):
            print(f"{matrix[i][j]:>{max_width}}", end=' ')
        print('|')
    print()

def print_iteration(pheromone_matrix, guess, distance_arr, iteration):
    """
    Prints the details of an iteration, including the pheromone matrix, guesses, and distances.
    
    Args:
        pheromone_matrix (list of list of float): The pheromone matrix representing trail intensities.
        guess (list of list of int): The paths chosen by the ants in the current iteration.
        distance_arr (list of float): The distances traveled by each ant.
        iteration (int): The iteration number.
    """
    print(f"\nIteration {iteration}:")
    print("Pheromone Matrix:")
    print_matrix(pheromone_matrix, len(pheromone_matrix))
    
    print("Guess:")
    for idx, g in enumerate(guess):
        print(f"Ant {idx+1}:", *g, "Distance:", distance_arr[idx])
    print()
