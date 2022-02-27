import json

emotionD = {}

with open("AFINN-111.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        to_list = l.strip().split()
        emotionD[''.join(to_list[:-1])] = int(to_list[-1])

tweetall = {}

with open("tweets.txt") as tweets:
    lines = tweets.readlines()
    for l in lines:
        value = 0
        try:
            dict = json.loads(l)
            message = dict['text']
            for m in message.split():
                if m in emotionD.keys():
                    value += emotionD[m]

            tweetall[message] = value
        except:
            pass

sort_order = sorted(tweetall.items(), key=lambda x:x[1], reverse=True)

print("\n-----------------------------------------Most positive tweets------------------------------------------\n")
result = []
for i in sort_order:
    a = str(i[0]) + " = " + str(i[1])
    result.append(a)

for i in range(10):
    print(f"{i + 1}) {result[i]}")
print("\n-----------------------------------------Most negative tweets------------------------------------------\n")

last_ten = result[-10:][::-1]  #[::-1] to reverse
for i in range(10):
    print(f"{i + 1}) {last_ten[i]}")
