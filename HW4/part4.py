def party(people, pairs):
    dict = {}   #Dictionary for which person know which of the others
    for person in people:   #Initialize the dictionary
        dict[person]=0
    for i in pairs:     #For every pair increase their dictionary value 1
        dict[i[0]] += 1
        dict[i[1]] += 1
    while(not(all(i>=5 for i in dict.values()))):   #Loop until find the guests
        temp = []
        for i in dict:  
            if dict[i]<5 or len(dict)-1-dict[i]<5:  #If someone know less than 5 people or didnt know less than 5 people
                for x in pairs:
                    if x[0] in dict.keys() and x[1] in dict.keys(): #Decrease the other people values who knows him/her  
                        if x[0] == i:
                            dict[x[1]] -= 1
                        elif x[1] == i:
                            dict[x[0]] -= 1
                temp.append(i)  #Add him to temp array for deleting from party list
        for i in temp:
            del dict[i] #Delete from party list
    return " ".join(dict.keys())

#I just took the test case from one of my classmates, because i had no time to write it

people= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'Q']
relatives = [("A", "B"), ("A", "C"), ("A", "Q"), ("A", "N"), ("A", "G"), ("A", "F"), ("A", "O"),
             ("B", "C"), ("B", "D"), ("B", "N"), ("B", "G"), ("B", "M"), ("B", "Q"),
             ("C", "D"), ("C", "Q"), ("C", "G"), ("C", "S"), ("C", "J"), ("C", "F"), ("C", "H"), ("C", "M"), ("C", "O"), ("C", "R"), ("C", "T"),
             ("D", "H"), ("D", "K"), ("D", "Q"), ("D", "N"), ("D", "T"), ("D", "O"),
             ("E", "F"), ("E", "Q"), ("E", "G"), ("E", "S"), ("E", "O"), ("E", "H"), ("E", "N"), ("E", "P"),
             ("F", "N"), ("F", "Q"), ("F", "T"), ("F", "G"),
             ("G", "H"), ("G", "J"),
             ("H", "N"), ("H", "T"), ("H", "Q"), ("H", "J"),
             ("J", "N"), ("J", "K"), ("J", "P"), ("J", "S"), ("J", "M"),
             ("K", "N"),
             ("M", "P"), ("M", "S"), ("M", "O"), ("M", "Q"), ("M", "T"),
             ("N", "P"), ("N", "Q"), ("N", "O"), ("N", "S"), ("N", "T"),
             ("O", "T"), ("O", "S"),
             ("P", "S"), ("P", "T"), ("P", "Q"),
             ("T", "Q")]

print(party(people, relatives))