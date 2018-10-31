start_clauses = None
from Node import Node


def set_clauses(clauses):
    global start_clauses
    start_clauses = clauses


def backtracking_search(node):
    global start_clauses

    # Reached terminal assignment
    if len(node.unassigned) == 0:
        return node
    next_var = get_next_selection(node)

    # No valid selection remaining
    if next_var is None:
        return None

    for val in node.unassigned[next_var]:
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
        else:
            return None
    return current_var


def get_degree(var):
    global start_clauses
    degree = 0
    for clause in start_clauses:
        degree += (clause.count(int(var)) + clause.count(-int(var)))
    return degree
