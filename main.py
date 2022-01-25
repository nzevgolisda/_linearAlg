

class Board:
    def __init__(self, L, b):
        self.A = L
        self.b = b
        
    def addRow(self, x, y, c): #add a c - multiple of x - row to y - row
        L = self.A
        self.b[x-1] += c*self.b[y-1]
        for j in range(len(L[0])):
            L[x-1][j-1] += c*L[y-1][j-1]
        return self

    def __str__(self):
        s = ''
        L = self.A
        for i in range(len(L)):
            row = ''
            for j in range(len(L[0])):
                row += ' '+str(L[i][j])+' '
            row += '| '+str(self.b[i])
            s += row +'\n'
        return s
        
A = [[1, 2, 3, 3], 
    [4, 5, 6, 6], 
    [7, 8, 9, 9]]
b = [10, 20, 30]
matrix = Board(A, b)
print(matrix)
matrix.addRow(2, 1, -4)
print(matrix)
matrix.addRow(3, 1, -7)
print(matrix)
matrix.addRow(3, 2, -2)
print(matrix)
matrix.addRow(1, 2, 2/3)
print(matrix)

