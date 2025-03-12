def predict_next_move(pheromone_matrix, visited_path, ant_prob_rand):
    """
    Predicts the next move for an ant based on the pheromone matrix.
    
    The probability of moving to node i is given by:
    
        Probability(node i) = pheromone_matrix[current_node][i] / sum(pheromone_matrix[current_node][j])
    
    where j represents the set of unvisited nodes.
    
    Args:
        pheromone_matrix (list of list of float): The pheromone levels between nodes.
        visited_path (list of int): The path taken by the ant so far.
        ant_random_prob (float): A random probability value for decision-making.
    
    Returns:
        int: The next node to visit.
    
    Raises:
        ValueError: If the denominator is zero (i.e., no pheromone trail exists to an unvisited node).
    """

    n = len(pheromone_matrix)
    cur_node = visited_path[-1] - 1

    # Identify the unvisited nodes
    unvisited_nodes = [i for i in range(n) if i+1 not in visited_path]

    # Calculate the denominator for probability normalization
    denominator = 0
    for node in unvisited_nodes:
        denominator += pheromone_matrix[cur_node][node]

    if denominator == 0:
        raise ValueError("Denominator is zero. Please check the pheromone matrix.")

    # Compute probability distribution
    probability_row = [pheromone_matrix[cur_node][node]/denominator for node in unvisited_nodes]

    # Compute cumulative probability
    cumulative_prob = [probability_row[0]]
    for i in range(1, len(probability_row)):
        cumulative_prob.append(cumulative_prob[i-1] + probability_row[i])

    # Select the next node based on the random probability
    for i in range(len(cumulative_prob)):
        if ant_prob_rand <= cumulative_prob[i]:
            return unvisited_nodes[i]+1