fo = open('unicode.txt', 'r')

line = fo.read()

list1 = ['0000', '0001', '0010','0011','0100','0101','0110','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
list2 = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


print(list1[list2.index('1')], end = ' ')

inp = 'U+0x41'
line = line.replace('U+0x', ' ')

list1[1]
for i in line:
    if i == ' ':
        print()
        
    elif i == 'U' or i == '+' or i == 'x':
        continue
    
    else:
        print(list1[list2.index(i.upper())], end = ' ')
        
        
fo2 = open('binary.txt', 'r')

line = fo2.read()
