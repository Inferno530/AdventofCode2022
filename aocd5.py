with open('day5.txt') as f:
    data = [i for i in f.readlines()]

with open('day5nobox.txt') as j:
    order = [i for i in j.readlines()]

#going to make some stacks quickly

initpos = [[],[],[],[],[],[],[],[],[]]
columns = []

'''
    [D] 
[N] [C] position 2 and 6 are letters
[Z] [M] [P] position 2, 6, and 10 are letters
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In the actual file, there are 9 positions, so 2, 6, 10, 14, 18, 22, 26, 30, and 34 contain letters
Which is technically 1, 5, 9, 13, 17, 21, 25, 29, 33 in a list
'''

#data parser
for i in range(8):
    for index, letter in enumerate(data[i]):
        if letter.isspace() == False and letter != '[' and letter != ']':
            if index == 1:
                initpos[0].append(letter)
            if index == 5:
                initpos[1].append(letter)
            if index == 9:
                initpos[2].append(letter)
            if index == 13:
                initpos[3].append(letter)
            if index == 17:
                initpos[4].append(letter)
            if index == 21:
                initpos[5].append(letter)
            if index == 25:
                initpos[6].append(letter)
            if index == 29:
                initpos[7].append(letter)
            if index == 33  :
                initpos[8].append(letter)

#data reordering
for thing in initpos:
    thing.reverse()

#NOW WE CAN START READING

#note that commands start from line 11 and end on 512

for line in order:
   command = []
   for number in line.split():
        try:
            command.append(int(number))
        except ValueError:
            pass    
   for i in range(command[0]):
        crate = initpos[command[1]-1].pop()
        initpos[command[2]-1].append(crate)


for items in initpos:
    print(items[-1])
