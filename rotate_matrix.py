matix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

for i in range(len(matix)):
    for j in range(len(matix)):
        print(matix[i][j],"\t" ,end="")
    print("")
def rotate():
    
    rd= len(matix)//2
    for rnd in range(rd):
        que=[matix[rnd][rnd],]
        for i in range(1,len(matix[0])-rnd):
            que.append(matix[rnd][i])
            matix[rnd][i] = que.pop(0)

        right=len(matix)-rnd
        for i in range(1+rnd,right):
            que.append(matix[i][right-1])
            matix[i][right-1] = que.pop(0)

        buttom=len(matix)-rnd
        for i in range(buttom-2,rnd-1,-1):
            que.append(matix[buttom-1][i])
            matix[buttom-1][i] = que.pop(0)

        left=len(matix)-rnd
        for i in range(left-2,rnd-1,-1):
            que.append(matix[i][rnd])
            matix[i][rnd] = que.pop(0)

rotate()
print("")
for i in range(len(matix)):
    for j in range(len(matix)):
        print(matix[i][j],"\t" ,end="")
    print("")