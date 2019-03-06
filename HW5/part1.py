def algo1(arr):
    totalCost = 0
    totalTime = 0
    order = []
    rates = []
    for i in range(0, len(arr)):  #Calculate all w/t values
        rates.append(arr[i][2]/arr[i][1])
    while rates:    #Loop until all jobs are done
        index=rates.index(max(rates))   #Find the index of the maximum rated job
        totalTime = totalTime + arr[index][1]  #Calculate the totalTime
        totalCost = totalCost + totalTime*arr[index][2]   #Calculate the totalCost
        order.append(arr[index][0])  #Append the job id to order list for printing the result
        del rates[index]   #Delete the completed job
        del arr[index]     #Delete the completed job
    print("Job Order: ", order)
    print("Total Cost: ", totalCost)

algo1([[1, 1, 2], [2,3,5], [3,6,1], [4,2,7], [5, 8, 3]])