# The idea here is to read the file line by line and and split it. When we splitt if the the seconde 
# elments unit is Kbps then we devide by 1000 if its Mbps we just appendt it directly to the list 
# We can put some more condition for sure if we wanted 
filename="task4.txt"
file=open(filename,"r").readlines()
List=[]
for i in file:# We open a for loop which goes through every element in the file
    a=i.split()
    if(a[1]=="Kbps"):# if the seconde elmens is Kbps then we deivded it by 1000 and then append it
        x=int(a[0])/1000 # We shouldnt forget that we we read the elemets from the lists if itrepratet as string
        # thats why we should change it to Integer. 
        List.append(x)
    else :
        List.append(int(a[0]))

#The rest of the code is used from task 2 and 3  
def jainstall(tp_values):
    nummerator = sum(tp_values) ** 2
    denominator=2*sum([x**2 for x in tp_values])
    JFI=nummerator/denominator
    return JFI 
print(jainstall(List))