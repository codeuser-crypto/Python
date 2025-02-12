#file operations 
infile = open('class.txt', 'r') 
for line in infile: 
    print(line)

#reading file
infile = open('class.txt', 'r') 
for line in infile: 
    print(line)
infile.close()

#reading file as string
infile = open('class.txt', 'r')
filestr = infile.read()
print(filestr)

outfile = open('class.txt', 'w')
outfile.write('Hello, world!')
outfile.close()

infile = open('class.txt', 'r')
filestr = infile.readlines()
print(filestr)

y = open('class.txt', 'r')
sum = 0
for line in y:
    x = float(line)
    sum += x
print(sum)
y.close()