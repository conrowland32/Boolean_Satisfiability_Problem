import sys
from Node import Node
from Helpers import backtracking_search, set_clauses


clauses = None


def main():
    # Validate arguments
    if len(sys.argv) != 2:
        print('Incorrect arguments')
        sys.exit()
    if int(sys.argv[1]) not in [1, 2, 3, 4]:
        print('Incorrect text file number')
        sys.exit()

    # Get input from file
    input_file = open("../assignment/example" + sys.argv[1] + ".txt", "r")
    input_file.readline()

    # Build starting variable dictionary
    start_dict = dict()
    all_clauses = []
    for line in input_file:
        line_list = [int(x) for x in line.split() if x != '0']
        all_clauses.append(line_list)
        for i in line_list:
            if str(abs(i)) not in start_dict:
                start_dict[str(abs(i))] = [0, 1]

    set_clauses(all_clauses)

    # Create first search node
    start_node = Node(start_dict, dict())
    finish_node = backtracking_search(start_node)
    if finish_node is None:
        print('\n----- NO SOLUTION -----')
        sys.exit()
    print('----- FINISHING NODE FOUND -----')
    print(finish_node.assigned)
    print('-----                      -----')


if __name__ == "__main__":
    main()
