# edit_distance.py: Reads strings x and y from standard input and computes
# the edit-distance matrix opt. The program outputs x, y, the dimensions
# (number of rows and columns) of opt, and opt itself.

import stdarray
import stdio

# Read x and y.
x = stdio.readString()
y = stdio.readString()

# Create (M + 1) x (N + 1) matrix opt with elements initialized to 0, where
# M and N are lengths of x and y respectively.
M = len(x)
N = len(y)
opt = stdarray.create2D(M + 1, N +1, 0)

# Initialize opt[M][j] (j < N) and opt[i][N] (i < M) to appropriate values.
for j in range(0, N):
    opt[M][j] = 2 * (N - j)

for i in range(0, M):
    opt[i][N] = 2 * (M - i)

# Compute the rest of opt.
for i in range(M -1, -1, -1):
    for j in range(N - 1, -1, -1):
        opt[i][j] = min(opt[i + 1][j + 1] + (0 if x[i] == y[j] else 1),
                        opt[i + 1][j] + 2, opt[i][j + 1] + 2)

# Write x, y, dimensions of opt, and opt.
stdio.writeln(x)
stdio.writeln(y)
stdio.writef('%d %d\n', M + 1, N + 1)
for i in range(M + 1):
    for j in range(N + 1):
        if j == N:
            stdio.writef('%3d\n' , opt[i][j])
        else:
            stdio.writef('%3d ', opt[i][j])
