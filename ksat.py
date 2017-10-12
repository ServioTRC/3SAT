def sat_creator(variables, clause_type):
    global dummy_number, results
    if clause_type == 1:
        #Beginning clause
        #print(variables[0], variables[1], dummy_number)
        results.append([variables[0], variables[1], dummy_number])
        dummy_number *= -1
        for i in range(2, len(variables)):
            temp = dummy_number
            #print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            #print(temp, variables[i], dummy_number)
            results.append([temp, variables[i], dummy_number])                        
            dummy_number *= -1           

    elif clause_type == 2:
        for i in range(len(variables)):
            temp = dummy_number
            #print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            #print(dummy_number)
            results.append([temp, variables[i], dummy_number])    
            dummy_number *= -1

    elif clause_type == 3:
        #Final clause
        for i in range(len(variables)-2):
            temp = dummy_number
            #print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            #print(dummy_number)
            results.append([temp, variables[i], dummy_number])
            dummy_number *= -1
        #print(dummy_number, variables[-2], variables[-1])      
        results.append([dummy_number, variables[-2], variables[-1]])

def save_results():
    global results, file2
    file2 = open("instance_3SAT_result.txt", "w")
    file2.write("c A 3-SAT instance for the given clauses\n")
    file2.write("p cnf "+str(-results[-1][0])+" "+str(len(results))+"\n")
    for clause in results:
        file2.write(str(clause[0])+" "+str(clause[1]) +" "+str(clause[2])+"\n")
    file2.close()

dummy_number = 0
results = []

def main():
    global dummy_number
    try:
        #file read
        file = open("instance_3SAT_example.txt")
        content = file.read()
        file.close()
        lines = content.split("\n")

        header = True
        counter = 1
        num_line = 0
        total_lines = len(lines)
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
                    #print(variables, clauses, dummy_number)
                    header = False
                else:
                    if counter == 1:
                        #Beginning clause
                        clause_type = 1
                    elif counter == clauses:
                        #Final clause
                        clause_type = 3
                    else:
                        #Middle clause
                        clause_type = 2
                    #Removes last cero
                    values.pop()

                    sat_creator(values, clause_type)

                    counter += 1
            num_line += 1
        save_results()
    except EOFError:
        pass


main()