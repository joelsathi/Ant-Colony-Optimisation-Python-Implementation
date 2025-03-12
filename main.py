import sys
from utils import print_matrix, print_iteration
from pheromone_calculator import update_pheromone_matrix
from probability_calculator import predict_next_move
from distance_calculator import calc_distance
from input_reader import get_input
import numpy as np

ITERATION_COUNT = 200
EVAPORATION_RATE = 0.2

sys.stdout = open("output.txt", 'w')

# Get the input
n, distance_matrix, ant_count, initial_guess = get_input(file_name="input.txt")

pheromone_matrix = [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: 
            pheromone_matrix[i][j] = 0

initial_dist = [calc_distance(distance_matrix, path) for path in initial_guess]

print_matrix(distance_matrix, n)
print()
print_iteration(pheromone_matrix, initial_guess, initial_dist, 0)
next_guesses = initial_guess

for iter in range(1, ITERATION_COUNT):

    # Breaking condition: If all the ants are following the same path break
    first_guess = next_guesses[0]
    flag = False
    for guess in next_guesses:
        if guess != first_guess:
            flag = True
            break
    if not flag:
        break

    pheromone_matrix = update_pheromone_matrix(pheromone_matrix, distance_matrix, next_guesses, EVAPORATION_RATE)

    next_guesses = []
    distance_arr = []
    for i in range(ant_count):
        # Every ant is starting from the same node (Here it is 1)
        # This will predict the path for each ant
        cur_path = [initial_guess[0][0]]

        ant_prob_arr = np.random.rand(n-1)
        for j in range(n-1):
            # Each time step a random number is generated to identify the range
            ant_prob_rand = ant_prob_arr[j]
            next_move = predict_next_move(pheromone_matrix, cur_path, ant_prob_rand)
            cur_path.append(next_move)
        
        next_guesses.append(cur_path)

        dist = calc_distance(distance_matrix, cur_path)
        distance_arr.append(dist)

    print_iteration(pheromone_matrix, next_guesses, distance_arr, iter)

