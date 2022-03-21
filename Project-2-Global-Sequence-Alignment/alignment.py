# alignment.py: Reads from standard input, the output produced by
# edit_distance.py, i.e., input strings x and y, and the opt matrix. The
# program then recovers an optimal alignment from opt, and writes to
# standard output the edit distance between x and y and the alignment itself.

import stdarray
import stdio

g = 0
h = 0

# Read x, y, and opt from standard input.
x = stdio.readLine()
y = stdio.readLine()
opt= stdarray.create2D(stdio.readInt(), stdio.readInt(), 0)
for i in range(len(opt)):
    for j in range(len(opt[i])):
        opt[i][j]=stdio.readInt()

# Compute M and N.
M = len(x)
N = len(y)

# Write edit distance between x and y.
stdio.writeln('Edit distance = ' + str(opt[0][0]))

# Recover and write an optimal alignment.

diagnol=None
down=None
right=None

while g<M and h<N:
    right=opt[g][h] - opt[g][h+1]
    down=opt[g][h]-opt[g+1][h]
    diagnol=opt[g][h] - opt[g+1][h+1]
    k=0<=diagnol<=1
    l=(diagnol==0 and x[g]==y[h] or diagnol==1 and x[g] !=y[h])

    if down==2:
        stdio.writeln(x[g]+" - "+ str(down))
        g+=1

    elif right==2:
        stdio.writeln("-"+ y[h]+ " " + str(right))
        h+=1
    elif k and l:
        stdio.writeln(x[g]+" " +  y[h]+ " " + str(diagnol))
        g+=1
        h+=1
if g<M:
    stdio.writeln(x[g]+" - " + str(2))
elif h<N:
    stdio.writeln("- "+ y[h]+" " +str(2))

