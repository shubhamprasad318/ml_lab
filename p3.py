MAX_INT = 1000
MIN_INT = -1000

def fun_alphabeta(d, node, max_player, values, alpha, beta):
    if d == 3:
        return values[node]

    if max_player:
        best_val = MIN_INT
        for i in range(2):
            value = fun_alphabeta(d + 1, node * 2 + i, False, values, alpha, beta)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val
    else:
        best_val = MAX_INT
        for i in range(2):
            value = fun_alphabeta(d + 1, node * 2 + i, True, values, alpha, beta)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val

# User input
leaf_nodes = int(input("Enter total number of leaf nodes: "))
values = [int(input(f"Enter node value {i + 1}: ")) for i in range(leaf_nodes)]
depth = int(input("Enter depth value: "))
start_node = int(input("Enter start node value: "))

# Calculate optimal value
optimal_value = fun_alphabeta(depth, start_node, True, values, MIN_INT, MAX_INT)
print("The optimal value is:", optimal_value)
