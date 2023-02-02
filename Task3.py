filename="task3.txt" # We read the file and name it filename
file=open(filename,"r").readlines() # We read the file line by line
List=[]    # Vi intiat an emptylist where we can put the value in it later
for i in file: # As we read the file by line, it will be interpertated as elements where there is an space
  a=i.split()  # We split it and put it in a variabel
  List.append(int(a[0])) # Then we append it into the Empty list where we first intiatet

# After the code above we use the code which werer used in the task2
def jainstall(tp_values):    
    nummerator = sum(tp_values) ** 2
    denominator=2*sum([x**2 for x in tp_values])
    JFI=nummerator/denominator
    return JFI 

print(List)
print(jainstall(List))




