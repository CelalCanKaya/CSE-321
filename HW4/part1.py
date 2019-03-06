def optimalSeq(A):
    cost = []
    hotels = []
    for i in range(0, len(A)):	#For every hotel
        cost.append((200-A[i])**2)	#Calculate the cost from beginning to this hotel and add to cost array
        hotels.append(0)	
        for j in range(0, i):		#Loop for calculate the optimal cost
            if cost[i] > (cost[j] + ((200-(A[i]-A[j]))**2)):	#If the current cost is worse than the calculated one
                cost[i]=cost[j]+((200-(A[i]-A[j]))**2)	#CurrentCost=NewCost
                hotels[i]=j+1	#Add to hotels array for printing the path
    print("Optimal Sequence Of Hotels: ", set(hotels), "\nTotal Penalty: ", cost[len(cost)-1])	#Display results - I wrote set(hotels) because i dont want to display a hotel more than once
   

optimalSeq([190, 220, 410, 580, 640, 770, 950, 1100, 1350])
