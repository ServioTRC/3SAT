def sat_creator(variables, clause_type):
    global dummy_number, results_clauses
    if clause_type == 1:
        #Beginning clause
        #print(variables[0], variables[1], dummy_number)
        results_clauses.append([variables[0], variables[1], dummy_number])
        dummy_number *= -1
        # for i in range(2, len(variables)):
        #     temp = dummy_number
        #     #print(dummy_number, variables[i], end=' ')
        #     dummy_number *= -1
        #     dummy_number += 1
        #     #print(temp, variables[i], dummy_number)
        #     results.append([temp, variables[i], dummy_number])
        #     dummy_number *= -1

    elif clause_type == 2:
        for i in range(len(variables)):
            temp = dummy_number
            #print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            #print(dummy_number)
            results_clauses.append([temp, variables[i], dummy_number])
            dummy_number *= -1

    elif clause_type == 3:
        #Final clause
        for i in range(len(variables)-2):
            temp = dummy_number
            #print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            #print(dummy_number)
            results_clauses.append([temp, variables[i], dummy_number])
            dummy_number *= -1
        #print(dummy_number, variables[-2], variables[-1])      
        results_clauses.append([dummy_number, variables[-2], variables[-1]])

def save_results():
    global results, file2
    file2 = open("instance_3SAT_result.txt", "w")
    file2.write("c A 3-SAT instance for the given clauses\n")
    #file2.write("p cnf " + str(-results[-1][0]) + " " + str(len(results)) + "\n")
    for problem in results:
        for clause in problem:
            #print(clause)
            file2.write(str(clause[0])+" "+str(clause[1]) +" "+str(clause[2])+"\n")
    file2.close()

dummy_number = 0
results = []
results_clauses = []

def main():
    global dummy_number, results_clause, results_clauses
    try:
        #file read
        file = open("instance_3SAT_example.txt")
        content = file.read()
        file.close()
        lines = content.split("\n")

        header = True
        #counter = 1
        num_line = 0
        total_lines = len(lines)-1
        #Reviews enters at end of file
        limit = total_lines -1 
        for _ in range(limit, 0, -1):
            if lines[num_line] == "":
                total_lines -= 1
            else:
                break

        #while True:

        while num_line<total_lines:
            #line = input()
            line = lines[num_line]
            #print("line", num_line, line)
            if line != "" and line[0] == "c":
                num_line += 1
                continue
            else:
                values = line.split(" ")
                if header:
                    variables = int(values[2])
                    clauses = int(values[3])
                    dummy_number = variables + 1
                    header = False
                else:
                    values.pop()
                    total_variables = len(values)
                    #Case 3 variables
                    if total_variables == 3:
                        results_clauses.append([values[0], values[1], values[2]])
                    else:
                        dummy_number = variables + 1
                        #Case 1 variable
                        if total_variables == 1:
                            results_clauses.append([values[0], dummy_number, dummy_number+1])
                        #Case 2 variables
                        elif total_variables == 2:
                            results_clauses.append([values[0], values[1], dummy_number+1])
                        #Case more than 3 variable
                        else:
                            first_clause = values[:2]
                            sat_creator(first_clause, 1)

                            middle_clauses = values[2:len(values)-2]
                            sat_creator(middle_clauses, 2)

                            last_clause = values[len(values)-2:]
                            sat_creator(last_clause, 3)

                    # if counter == 1:
                    #     #Beginning clause
                    #     clause_type = 1
                    # elif counter == clauses:
                    #     #Final clause
                    #     clause_type = 3
                    # else:
                    #     #Middle clause
                    #     clause_type = 2
                    # #Removes last cero
                    # values.pop()
                    #
                    # sat_creator(values, clause_type)

                    print("Clausulas linea", num_line - 1, results_clauses)
                    results.append(results_clauses)
                    results_clauses = []
            num_line += 1
        #print("*****************************************+")
        #print(results)
        save_results()
    except EOFError:
        pass


main()