def algo2(n, M, sequenceNY, sequenceSF):
    arr1 = [0]
    arr2 = [0]
    plan = []
    for i in range(0, n):
        arr1.append(sequenceNY[i] + min(arr1[i], M+arr2[i]))   #Calculate the totalCost of current optimal plan + current NY cost
        arr2.append(sequenceSF[i] + min(arr2[i], M+arr1[i]))   #Calculate the totalCost current optimal plan + current SF cost
    for cost in range(n, 0, -1):   #Loop for print the optimal plan
        if arr1[cost]<arr2[cost]:
            plan.insert(0, "NY")
        elif arr2[cost]<arr1[cost]:
            plan.insert(0, "SF")
        elif cost<4:
            plan.insert(0, plan[0])
        else:
            plan = ["NY"] * n
            break   
    print("Optimal Plan: ", plan)
    return min(arr1[n], arr2[n])  #Return the optimal paths cost        

print(algo2(4, 10, [1, 3, 20,30], [50,20,2,4]))
print(algo2(4, 10, [1, 3, 21,34], [1,3,20,35])) 