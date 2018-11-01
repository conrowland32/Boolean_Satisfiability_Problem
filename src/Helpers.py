from Node import Node
import json

start_clauses = None
total_runs = 1
output_file = None


def set_clauses(clauses):
    global start_clauses
    start_clauses = clauses


def set_output(output):
    global output_file
    output_file = open("../results/example" + output + "_output.txt", "w")


def close_output():
    global output_file
    output_file.close()


def backtracking_search(node):
    global start_clauses
    global total_runs

    # Reached terminal assignment
    if len(node.unassigned) == 0:
        return node
    next_var = get_next_selection(node)
    if total_runs <= 250:
        output_file.write(str(node.assigned))
        if next_var is None:
            output_file.write("\nNone    total runs: " +
                              str(total_runs) + "\n\n")
        else:
            output_file.write("\n" + next_var + "    total runs: " +
                              str(total_runs) + "\n\n")
    print(total_runs)

    # No valid selection remaining
    if next_var is None:
        return None

    for val in node.unassigned[next_var]:
        total_runs += 1
        new_node = Node(node.unassigned, node.assigned,
                        next_var, val, start_clauses)
        result = backtracking_search(new_node)
        if result is not None:
            return result
    return None


def get_next_selection(node):
    current_var = None
    current_rem_vals = 3
    current_degree = 0

    # Minimum Remaining Values
    for var in node.unassigned:
        if len(node.unassigned[var]) == 0:
            return None
        if len(node.unassigned[var]) < current_rem_vals and len(node.unassigned[var]) > 0:
            current_var = var
            current_rem_vals = len(node.unassigned[var])
            current_degree = get_degree(var)
        # Degree tiebreaker
        elif len(node.unassigned[var]) == current_rem_vals:
            comp_degree = get_degree(var)
            if comp_degree > current_degree:
                current_var = var
                current_rem_vals = len(node.unassigned[var])
                current_degree = comp_degree
    return current_var


def get_degree(var):
    global start_clauses
    degree = 0
    for clause in start_clauses:
        degree += (clause.count(int(var)) + clause.count(-int(var)))
    return degree
