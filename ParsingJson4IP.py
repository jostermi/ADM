import json
import sys
import socket

output = ('cheating')

f2 = open('Output.txt','w')
json_file = open('RTP-IP.json')
data = json.load(json_file)
for index in range(len(data['clusters'])):
    output = data['clusters'][index]['nodes'][0]['ip']
    print output
    f2.write(output + '\n')
json_file.close()
f2.close()
