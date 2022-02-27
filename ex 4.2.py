import json

emotionD = {}

with open("AFINN-111.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        to_list = l.strip().split()
        emotionD[''.join(to_list[:-1])] = int(to_list[-1])

with open("result.txt", "w") as result, open("tweets.txt") as tweets:
    lines = tweets.readlines()
    for l in lines:
        value = 0
        try:
            dict = json.loads(l)
            id = dict['id']
            message = dict['text']
            for m in message.split():
                if m in emotionD.keys():
                    value += emotionD[m]

            result.write(f"{id} = {value}\n")
        except:
            pass





# import json
#
# emotionD = {}
#
# with open("AFINN-111.txt", "r") as f:
#     lines = f.readlines()
#     for l in lines:
#         arr = l.strip().split()
#         emotionD[arr[0]] = arr[1]
#
# with open("result.txt", "w") as result_f, open("tweets.txt") as tweets_f:
#     lines = tweets_f.readlines()
#     for l in lines:
#         value = 0
#         try:
#             dict = json.loads(l)
#             id = dict['id']
#             message = dict['text']
#             for m in message.split():
#                 if m in emotionD.keys():
#                     value += emotionD[m]
#
#             result_f.write(f"{id} = {value}\n")
#         except:
#             pass