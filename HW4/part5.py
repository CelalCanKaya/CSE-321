def algo5(variables, constraints):
    for x in constraints:   #For every constraints
        if "!=" in x:   #If there is inequality
            temp=x.split("!=")  #Split the string and find index
            if variables[int(temp[0][1:])]==variables[int(temp[1][1:])]:
                return False    #No need to check more
        else:   #If there is inequality
            temp=x.split("=") #Split the string and find index
            if variables[int(temp[0][1:])]!=variables[int(temp[1][1:])]:
                return False #No need to check more
    return True

print(algo5([5,2,5,7], [("x0=x2"), ("x1!=x3")]))
print(algo5([5,2,5,7], [("x0=x2"), ("x0=x3")]))
