
def print_inupper(filename):
    with open (filename,"r") as file:
        for line in file:
            print(line.strip().upper())
            
print_inupper("names.txt")
