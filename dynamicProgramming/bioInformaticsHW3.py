import sys
import math
with open(sys.argv[1],'r') as f:
    file1 = f.read()

lines = file1.splitlines()

atom_ca1 = []
for line in lines:
    if line[0:4] == 'ATOM' and line[13:15] == 'CA':
        atom_ca1.append(line)

coordinates = []

for line in atom_ca1:
    line = line.split()
    coordinates.append(line[6:9])

dist = []
temp = []
t = 0 
print coordinates
for i in range(0,len(coordinates)):
    for j in range(0,len(coordinates)):
        for k in range(0,3):
            t = t + (float(coordinates[j][k]) - float(coordinates[i][k]))*(float(coordinates[j][k]) - float(coordinates[i][k]))
        temp.append(math.sqrt(t))
        t = 0
    dist.append(temp)
    temp = []


with open(sys.argv[2],'r') as f2:
    file2 = f2.read()

lines2 = file2.splitlines()

atom_ca2 = []
for line2 in lines2:
    if line2[0:4] == 'ATOM' and line2[13:15] == 'CA':
        atom_ca2.append(line2)

coordinates2 = []

for line2 in atom_ca2:
    line2 = line2.split()
    coordinates2.append(line2[6:9])

dist2 = []
temp2 = []
t2 = 0 
for i in range(0,len(coordinates2)):
    for j in range(0,len(coordinates2)):
        for k in range(0,3):
            t2 = t2 + (float(coordinates2[j][k]) - float(coordinates2[i][k]))* (float(coordinates2[j][k]) - float(coordinates2[i][k]))
        temp2.append(math.sqrt(t2))
        t2 = 0
    dist2.append(temp2)
    temp2 = []

tot = 0
ind1 = 0
ind2 = 0
smallest = 1000000000

for i in range(0,len(dist)-20):
    for j in range(0,len(dist2)-20):
        tot = 0
        for k in range(0,20):
            for l in range(0,20):
                tot = tot + abs(dist2[j+k][j+l] - dist[i+k][i+l])
        if tot < smallest:
            smallest = tot
            ind1 = i
            ind2 = j

print "Seed Alignment found at :"
print "========================="
print "Prot1: " + sys.argv[1] + " " + str(ind1)
print "Prot2: " + sys.argv[2] + " " + str(ind2)
