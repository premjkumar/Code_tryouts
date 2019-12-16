def solution(a):
  a=[2**int(x) for x in a] 
  #print(a) Check for the value of the elements with powers
  result=0
  int(result)
  for i in range(len(a)):
    #print(i) check for the value of the loop
    result=result+int(a[i])
  return(result)



# driver function
b=0 # setting the value to 0
int(b) #ensuring the output is integer.
c=[]
c=list(map(str ,input().split(",")))
b=solution(c)
print(b)