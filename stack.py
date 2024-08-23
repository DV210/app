a=[]
def push(x):
    a.append(x)

def delete(x):
    if x==')' and a[-1]=='(':
        a.pop()
    elif x=='}' and a[-1]=='{':
        a.pop()
    elif x==']' and a[-1]=='[':
        a.pop()
    else:
        return

s=input()
for x in s:
    if x in '([{':
        push(x)
    elif x in ')]}':
        delete(x)
if len(a)==0:
    print("Balanced")
else:
    print("Unbalanced")
    
