def jainstall(tp_values):     # We are defining a new function that takes in a values
    nummerator=sum(tp_values) # We find the sum of the values for the nummereator 
    denominator=2*sum([x**2 for x in tp_values]) # Here vi find the value for the denominator
    JFI=nummerator/denominator # We find the JFI by dividing the nummrator to the denominator
    return JFI 
list=[12,2,4,5,6]          # He is an exampel
print(jainstall(list))