import pandas as pd

data = pd.read_csv("search.csv")
lines = []
# data['magic number'] = 

with open("reference.txt") as file:
    lines = [line.rstrip() for line in file]

outfile = open("out.txt", "w")

output_funcs = []
output_names = []

i = 0
for row in data['BFMv2 Signal Name']:
    row_func = data['iMX8 Function'][i]
    row_func = row_func.replace(".", "_")
    i += 1

    found = False
    for line in lines:
        if row_func in line:
            found = True
            row_func = row_func.split(' ')
            outfile.write("<" + row_func[0] + " 0x104>, //" + row + "\n")
            break

    if not found:
        print("Could not find " + row_func)
        continue

outfile.close()