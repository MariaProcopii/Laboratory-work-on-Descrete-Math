frientdsDict = {}

with open("matrix.txt", "r") as f:
    line = f.readlines()

for i in range(1, len(line)):
    name_surname = line[i].split()[0] + " " + line[i].split()[1]
    nr_of_friends = 0
    for j in range(len(line[i])):
        if line[i][j] == "1":
            nr_of_friends += 1
    frientdsDict[name_surname] = nr_of_friends
# print(frientdsDict)

max_nr_of_friends = 0
name_of_person = []
allnr = []
allpeople = []
for k, v in frientdsDict.items():
    allnr.append(v)
    allpeople.append(k)
    if(v > max_nr_of_friends):
        max_nr_of_friends = v

for i in range(len(allnr)):
    if( allnr[i] == max_nr_of_friends):
        print(f"{allpeople[i]} = {max_nr_of_friends}")

f.close()

