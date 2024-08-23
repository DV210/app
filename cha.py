'''def solve(s):
    n=len(s)
    buff,x,cv=s[0],1,1
    for i in range(1,n):
        if buff==s[i]:
            cv+=1
        else:
            x*=cv
            cv,buff=1,s[i]
    return x*cv
s=input()
print(solve(s))'''
'''
s=input()
lc=0
i=0
while i<len(s)-1:
    if s[i]==s[i+1]:
       j=i
       c=0
       while j<len(s)-1 and s[j]==s[j+1]:
           c+1
           j+=1
       i=j
       lc+=lc+c+1
    else:
        i+=1  
print(lc)
'''
'''s=input()
c=0
i=0
while i<len(s):
    if s.count(s[i])>2:
        c+=s.count(s[i])
        i=c
        print(c)
    else:
        i+=1
print(c)'''
s=input()
c=0
c1=0
for i in range(len(s)-1):
    if s[i]=="0" and s[i+1]=="1":
        c+=1
    elif s[i]=="1" and s[i+1]=="0":
        c1+=1
print(c,c1)
if not min(c,c1)==0:
    print(max(c,c1)+1)
else:
    print(min(c,c1))


