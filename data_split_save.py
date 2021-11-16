#-*- coding:utf-8 -*-
data = []
split_char = input('What is split char(ex: /, , etc)? : ')
f = open('./club_data.txt', 'w')
while 1:
    conv_data=input().replace(split_char,'\t')+'\n'
    if conv_data == '\n':
        break    
    data.append(conv_data)
for i in data:
    f.write(i)
f.close()