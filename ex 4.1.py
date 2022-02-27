import json

hashtags = {}
with open("tweets.txt", "r") as f:
    lines = f.readlines()

    for l in lines:
        try:
            dict = json.loads(l)
            h = dict['text']
            full_list = h.split()
            for word in full_list:
                if word[0] == '#':
                    if word not in hashtags.keys():
                            hashtags[word] = 1
                    else:
                            hashtags[word] += 1
        except:
            pass
sort_order = sorted(hashtags.items(), key=lambda x:x[1], reverse=True)
# print(sort_order)

result = []
for i in sort_order:
    a = str(i[0]) + " = " + str(i[1])
    result.append(a)
for i in range(10):
    print(result[i])

# def space(hashtags):
#     hasht_list = []
#     arr = []
#     for i in hashtags.keys():
#         hasht_list.append(i)
#     for i in hasht_list:
#         arr.append(len(i))
#     longest_h = max(arr)
#     return longest_h
#
#
# for i in sort_order:
#     space_we_need = " " * (space(hashtags) - len(i[0]))
#     print(f"{i[0]}{space_we_need} =  {i[1]}")







'''first version'''
# with open("tweets.txt", "r", encoding="UTF-8") as f:
#     lines = f.readlines()
# a = []
# for i in lines:
#     for j in i.split():
#         if(j[0] == "#"):
#             a.append(j)
# # print(a)
#
# unique = set(a)
# c = {}
# # print(unique)
# for i in unique:
#     c[i] = a.count(i)
# # print(c)
#
# sort_order = sorted(c.items(), key=lambda x:x[1], reverse=True)
# # print(sort_order)
#
# result = []
# for i in sort_order:
#     a = str(i[0]) + " = " + str(i[1])
#     result.append(a)
#
# for i in range(10):
#     print(result[i])


