with open('day5.txt') as f:
    data = [i for i in f.readlines()]

with open('day5nobox.txt') as j:
    order = [i for i in j.readlines()]

#going to make some stacks quickly

initpos = [[],[],[],[],[],[],[],[],[]]
columns = []

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


for line in order:
   command = []
   limbo = []
   for number in line.split():
        try:
            command.append(int(number))
        except ValueError:
            pass    
   for i in range(command[0]):
        crate = initpos[command[1]-1].pop()
        limbo.append(crate)
   for j in range(command[0]):
        crate2 = limbo.pop()
        initpos[command[2]-1].append(crate2)

#print out last items
for items in initpos:
    print(items[-1])