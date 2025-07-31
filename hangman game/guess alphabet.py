import random 
l=["amit","aman","kartik","suraj","kiran","ksjdgjfu"]
k=random.choice(l)
i=1
w=len(k)
print("total words in predefine string is:",w)

while ( i<=6 or i<=w):
       b=[]
       a=input("enter the 1 alphabet at a time:_")
              
       if ( a in k):
              b.append(a)
              i=i+1
              print("correct guess")
       
       if ( a not in k):
              b.append(a)
              b.pop()
              i=i+1
              print("incorrect guess")
       '''else:
              print("ERROR")
              break'''
              
print("guess word is ",k)
