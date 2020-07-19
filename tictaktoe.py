shutdef printbox():
    for i in range(3):
        print("\t")
        for j in range(3):
            print(i + 1, j + 1, ':', number[i][j], '\t', end='\t')
        print()

def staircase(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")

        k = k - 2
        for j in range(0, i + 1):
            print(" #", end="")

        print("\r")
staircase(6)
i=0
j=0
number=[[1,2,3],[4,5,6],[7,8,9]]
print("this is the allocation of cross and zeros")
for i in range(3):
    print("\t")
    for j in range(3):
        print(i + 1, j + 1, ':',' ', '\t', end='\t')
    print()

print("X goes first")
while number[i][j]!='X' or number[i][j]!='O':
    print("where do u want to place your X")
    print("enter the coordinates of the placement as shown in the allocation box ")
    ix=int(input("enter the i coordinate "))
    jx=int(input("enter the j coordinate "))
    number[ix-1][jx-1]='X'
    if number[i][j]=='X' or number[i][j]=='O':
        print("all filled . DRAW")
        printbox()
        break
    printbox()
    if (number[0][0] == 'X' and number[0][1] == 'X' and number[0][2] == 'X') or (
            number[1][0] == 'X' and number[1][1] == 'X' and number[1][2] == 'X') or (
            number[2][0] == 'X' and number[2][1] == 'X' and number[2][2] == 'X') or (
            number[0][0] == 'X' and number[1][0] == 'X' and number[2][0] == 'X') or (
            number[0][1] == 'X' and number[1][1] == 'X' and number[2][1] == 'X') or (
            number[0][2] == 'X' and number[1][2] == 'X' and number[2][2] == 'X') or (
            number[0][2] == 'X' and number[1][1] == 'X' and number[2][0] == 'X') or (
            number[0][0] == 'X' and number[1][1] == 'X' and number[2][2] == 'X'):
        print(" X WINs")

        break
    if (number[0][0] == 'O' and number[0][1] == 'O' and number[0][2] == 'O') or (
            number[1][0] == 'O' and number[1][1] == 'O' and number[1][2] == 'O') or (
            number[2][0] == 'O' and number[2][1] == 'O' and number[2][2] == 'O') or (
            number[0][0] == 'O' and number[1][0] == 'O' and number[2][0] == 'O') or (
            number[0][1] == 'O' and number[1][1] == 'O' and number[2][1] == 'O') or (
            number[0][2] == 'O' and number[1][2] == 'O' and number[2][2] == 'O') or (
            number[0][2] == 'O' and number[1][1] == 'O' and number[2][0] == 'O') or (
            number[0][0] == 'O' and number[1][1] == 'O' and number[2][2] == 'O'):
        print(" O WINs")

        break

    print(" where do u want to place your O")
    print("enter the coordinates of the placement as shown in the allocation box ")
    io = int(input("enter the i coordinate "))
    jo = int(input("enter the j coordinate "))
    number[io-1][jo-1] = 'O'
    printbox()
