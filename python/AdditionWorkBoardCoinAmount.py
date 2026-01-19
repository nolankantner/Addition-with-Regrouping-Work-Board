#This is a script to help find how many coins are needed for 1 work board set

coins = [0,0,0,0,0,0,0,0,0,0] #index counts as coin number
for x in range(0,1000): #change 1000 in lines 2 and 3 for higher digit boards (100 for tens place, 10000 for thousands place, etc.)
    for y in range(0,1000):
        for i in range(0,10):
            if str(x).count(str(i)) + str(y).count(str(i)) + str(x+y).count(str(i)) > coins[i]:
                coins[i] = str(x).count(str(i)) + str(y).count(str(i)) + str(x+y).count(str(i))
coins[1] += 2 #adds 2 extra 1 coins for the 2 sliders
for i in range(0,10):
    print("Coin",str(i),"  Amount",coins[i])

