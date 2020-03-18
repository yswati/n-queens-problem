print("hello")
lis=[[0 for i in range(0,4)] for j in range(0,4)]
for i in range(0,4):
    for j in range(0,4):
        if j==0:
            lis[i][j]="q"
        else:
            lis[i][j]=0
print(lis)

violation=0
def conflict(num1,num2):
    for i in range(0,4):
        for j in range(0,4):
            if lis[i][j]=="q":
                for k in range(0,4):
                    if lis[i][k]=="q":
                        violation+=1
                    if lis[k][j]=="q":
                        violation+=1
                u=i+1,v=j+1
                while u<4 and v<4:
                    if lis[u][v]=="q":
                            violation+=1
                            
                        if lis[i+1][j-1]=="q":
                            violation+=1
                        if lis[i-1][j+1]=="q":
                            violation+=1
                        if lis[i-1][j-1]=="q":
                            violation+=1




