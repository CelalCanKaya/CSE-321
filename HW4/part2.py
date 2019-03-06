dictionary = ["it", "was", "the", "best", "of", "times", "and", "all"]    

def dict(w):    #Function for check the given word is in dictionary or not
    if w in dictionary:
        return True
    else:
        return False
    
def algo2(string):
    boolArr = [];       #Boolean Array for check the previous words are valid
    for i in range(0,len(string)+1):    #Fill the array with False and created with +1 length cause of first word
        boolArr.append(False)
    boolArr[0] = True       #Mark first index as true  
    for i in range(1,len(string)+1):    #Nested loops for traverse the string
        for j in range(0,i+1):
            if (boolArr[j] and dict(string[j:i])):  #If previousWords are valid and the word from j to i th index is in dictionary or not
                boolArr[i] = True  #Mark as True
                break
    result=""   #result Word for reconstruct the word
    for i in range(0,len(string)):  #Loop for reconstruct the string
        result=result + string[i]       
        if boolArr[i+1]==True:  #If there is a space add it
            result=result + " "
    print("Reconstructed Document: ", result)   #Display the reconstructed sequence
    return boolArr[len(boolArr)-1]


print(algo2("itwasthebestoftimes"))
