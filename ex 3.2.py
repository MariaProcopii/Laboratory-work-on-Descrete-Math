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
names = []
nrFriends = []

for k, v in frientdsDict.items():
    names.append(k)
    nrFriends.append(v)


arr = []
for i in names:
    arr.append(len(i))
longest_name = max(arr)


for i in range(len(nrFriends)): #sorting nr
    swap = False
    for j in range(len(nrFriends) - 1):
        if(nrFriends[j] > nrFriends[j + 1]):
            x = nrFriends[j]
            nrFriends[j] = nrFriends[j + 1]
            nrFriends[j + 1] = x
            swap = True
    if( swap == False):
        break
unique_nr = list(set(nrFriends))[::-1]  #reversed unique list of nr

for i in unique_nr:
    for k, v in frientdsDict.items():
        if(i == v):
            space_we_need = " "*(longest_name - len(k))
            print(f"{k}{space_we_need} =  {v}")

f.close()