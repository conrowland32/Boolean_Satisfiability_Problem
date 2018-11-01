import sys
import json
import time
import matplotlib.pyplot as pyplot
from Node import Node
from Helpers import backtracking_search, set_clauses, set_output, close_output


clauses = None


def main():
    start = time.time()

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
    set_output(sys.argv[1])

    # Create first search node and run search
    start_node = Node(start_dict, dict())
    finish_node = backtracking_search(start_node)
    close_output()

    # Write output to file
    output_file = open("../results/example" + sys.argv[1] + "_output.txt", "a")
    if finish_node is None:
        output_file.write('\n----- NO SOLUTION -----')
    else:
        output_file.write('----- FINISHING NODE FOUND -----\n')
        output_file.write(str(finish_node.assigned))
        output_file.write('\n-----                      -----')

    # Write execution time
    end = time.time()
    output_file.write("\nExecution time:  " + str(end - start) + " seconds")
    output_file.close()

    # Plot solution if one was found
    if finish_node is not None:
        keys = [int(x) for x in finish_node.assigned.keys()]
        vals = [finish_node.assigned[str(y)] for y in keys]
        pyplot.figure(figsize=(6.2, 2))
        pyplot.scatter(keys, vals)
        pyplot.grid(True)
        pyplot.yticks([0, 1])
        pyplot.ylabel('Variable Assignment')
        pyplot.xlabel('Variable Identifier')
        pyplot.title('Example ' + sys.argv[1] + ' Assignments')
        pyplot.show()


if __name__ == "__main__":
    main()
