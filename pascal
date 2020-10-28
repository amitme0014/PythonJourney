
##########################################Factorial Program##############################
def fact(n):
    factorial=1
    
    if n<0:
        print("Sorry factorial cant't be done")
    elif n==0:
        return 1
    else:
        for i in range(2,n+1):
            factorial=factorial*i
        return factorial

######################################To find the combination############################
def comb(i,j):
    comb_result=fact(i)//(fact(i-j)*fact(j))
    return comb_result
#########################################################################################
for i in range(0,int(input())):
    for j in range(0,i+1):
        print(comb(i,j)," ",end=" ")
    print()
    
