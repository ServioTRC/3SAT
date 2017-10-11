def sat_creator(variables, clause_type):
    global dummy_number 
    if clause_type == 1:
        #Beginning clause
        print(variables[0], variables[1], dummy_number)
        dummy_number *= -1
        for i in range(2, len(variables)):
            print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            print(dummy_number) 
            dummy_number *= -1           

    elif clause_type == 2:
        for i in range(len(variables)):
            print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            print(dummy_number)
            dummy_number *= -1

    elif clause_type == 3:
        #Final clause
        for i in range(len(variables)-2):
            print(dummy_number, variables[i], end=' ')
            dummy_number *= -1
            dummy_number += 1
            print(dummy_number)
            dummy_number *= -1
        print(dummy_number, variables[-2], variables[-1])      

dummy_number = 0

def main():
    global dummy_number
    try:
        #file read
        file = open("simple_v3_c2.cnf")
        content = file.read()
        file.close()
        lines = content.split("\n")

        header = True
        counter = 1
        num_line = 0
        total_lines = len(lines)
        #while True:
        while num_line<total_lines:
            #line = input()
            line = lines[num_line]
            #print("line", num_line, line)
            if line[0] == "c":
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
    except EOFError:
        pass


main()