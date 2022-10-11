array = list(map(int,input().split()))  #Input
n=len(array)

p=1
for i in array:
    if(i):  #Product of Non-Zero Entries
        p*=i
ans=[]
c=array.count(0)    #Number of Zeroes
if(c):
    ans=[0 for i in range(n)]   #All terms set to 0s
    if(c==1):   #If only 1 zero is present, there will remain one non-zero term which is the product of all non-zero terms
        ans[array.index(0)]=p

else:   
    ans=[p//i for i in array]   #Exclude the term at the current position in the product

print(ans)
