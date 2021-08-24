import re

filename = input("Please Enter FileName: ")
key_value = input("Please Enter Your KeyWord: ")
file1 = open(filename, 'r')
Lines = file1.readlines()

pist = []

for line in Lines:
    pist.append(line)

config_index = []

for i in range(0, len(pist)):
    if not re.match(r'\s', pist[i]):
        config_index.append(i)

config_index_2d = []

for a in range(0, int((len(config_index)) / 2)):
    config_index_2d.append([config_index[a * 2], config_index[(a * 2) + 1]])

config_index_2d_contain = []

for b in range(0, len(config_index_2d)):
    for c in range(config_index_2d[b][0], config_index_2d[b][1] + 1):
        if pist[c].__contains__("SSL-VPN-FW-LAN"):
            config_index_2d_contain.append([config_index_2d[b][0], config_index_2d[b][1]])
            break

sub_config = []
sub_config_2d = []

for d in range(0, len(config_index_2d_contain)):
    for e in range(config_index_2d_contain[d][0], config_index_2d_contain[d][1] + 1):
        if re.match(r'^ {4}[^ ]', pist[e]):
            sub_config.append(e)

for g in range(0, int((len(sub_config)) / 2)):
    sub_config_2d.append([sub_config[g * 2], sub_config[(g * 2) + 1]])

sub_config_2d_contain = []

for h in range(0, len(sub_config_2d)):
    for j in range(sub_config_2d[h][0], sub_config_2d[h][1] + 1):
        if pist[j].__contains__("SSL-VPN-FW-LAN"):
            sub_config_2d_contain.append([sub_config_2d[h][0], sub_config_2d[h][1]])
            break

f = open("res.txt", "w")

for k in range(0, len(config_index_2d_contain)):
    f.write(pist[config_index_2d_contain[k][0]])
    for l in range(0, len(sub_config_2d_contain)):
        if config_index_2d_contain[k][0] < sub_config_2d_contain[l][0] and config_index_2d_contain[k][1] > \
                sub_config_2d_contain[l][1]:
            for m in range(sub_config_2d_contain[l][0], sub_config_2d_contain[l][1] + 1):
                f.write(pist[m])
    f.write(pist[config_index_2d_contain[k][1]])

f.close()
