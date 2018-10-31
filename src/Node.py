import copy


class Node:
    def __init__(self, old_unassigned, old_assigned, var_chosen=None, val_chosen=None, clauses=None):
        # If first node
        if var_chosen is None:
            self.unassigned = old_unassigned
            self.assigned = old_assigned
        else:
            # Create new unassigned dictionary
            self.unassigned = copy.deepcopy(old_unassigned)
            del self.unassigned[var_chosen]

            # Create new assigned dictionary
            self.assigned = copy.deepcopy(old_assigned)
            self.assigned[var_chosen] = val_chosen

            # Set other fields
            self.var_chosen = var_chosen
            self.val_chosen = val_chosen

            print(self.unassigned, len(self.unassigned))
            print(self.assigned, len(self.assigned))
            print()

            # Forward-Check remaining variables
            self.forward_check(clauses)

    def forward_check(self, clauses):
        for clause in clauses:
            # If newly assigned var is not in the clause, can't remove potential value
            if int(self.var_chosen) not in clause and -int(self.var_chosen) not in clause:
                continue

            # Check each clause new var is in
            clause_size = len(clause)
            vars_assigned = 0
            for var in iter(self.assigned):
                if int(var) in clause:
                    # print('\n', int(var), ' is in ', clause, ' ?\n')
                    vars_assigned += 1
                if -int(var) in clause:
                    # print('\n', -int(var), ' is in ', clause, ' ?\n')
                    vars_assigned += 1

            # If every val in clause assigned but one
            unassigned_var = None
            any_already_true = False
            if clause_size - vars_assigned == 1:
                for clause_var in clause:
                    if str(abs(clause_var)) not in self.assigned:
                        unassigned_var = clause_var
                    elif self.assigned[str(abs(clause_var))] == 0 and clause_var < 0:
                        any_already_true = True
                    elif self.assigned[str(abs(clause_var))] == 1 and clause_var > 0:
                        any_already_true = True

                # If we get to this point and any_already_true is False, we can remove value
                if not any_already_true:
                    if unassigned_var < 0 and 1 in self.unassigned[str(abs(unassigned_var))]:
                        self.unassigned[str(abs(unassigned_var))].remove(1)
                        if len(self.unassigned[str(abs(unassigned_var))]) == 0:
                            return
                    elif unassigned_var > 0 and 0 in self.unassigned[str(abs(unassigned_var))]:
                        self.unassigned[str(abs(unassigned_var))].remove(0)
                        if len(self.unassigned[str(abs(unassigned_var))]) == 0:
                            return
