def sat_creator(variables, clause_type):
    global dummy_number
    if clause_type == 1:
        #Beginning clause
    elif clause_type == 2:
        #Middle clause
    elif clause_type == 3:
        #Final clause

dummy_number = 0

def main():
    try:
        header = True
        counter = 0
        while True:
            line = input()
            if line[0] == "c":
                continue
            else:
                values = line.split(" ")
                if header:
                    variables = int(values[2])
                    clauses = int(values[3])
                    print(variables, clauses)
                    header = False
                else:
                    if counter == 0:
                        #Beginning clause
                        clause_type = 1
                    elif counter == (clauses - 1):
                        #Final clause
                        clause_type = 3
                    else:
                        #Middle clause
                        clause_type = 2
                    
                    #Removes last cero
                    values.pop()

                    sat_creator(values, clause_type)

                    counter += 1
    except EOFError:
        pass


main()