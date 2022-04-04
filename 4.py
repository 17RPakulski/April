# i dunno
fo = open('unicode.txt', 'r')

line = fo.readline()

for i in line:
    if i == 'U' or i == '+' or i == '0' or i == 'x':
        pass
    else:
        print(ord(i))
        
        