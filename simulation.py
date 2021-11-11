import random
n=100000
w=0
for _ in range(n):
    list_of_doors=['a','b','c']

    #'this is where the car is
    truth=random.choice(list_of_doors)

    # first we pick a random door
    my_answer=random.choice(list_of_doors)

    doors_I_didnt_pick = [x for x in list_of_doors if x != my_answer]
    while True:
        #the host picks a door from the list of doors we didn't pick
        change=random.choice(doors_I_didnt_pick)

        #we want that door to be the door that doesn't have the car behind.
        if change!=truth:
            break
    #the host opens the door 'change' ,shows us that it didn't have the car behind it. Asks us again if we want to stay or switch
    doors_I_didnt_pick.remove(change)

    #so the only item left in the list is the door we are switching to. It is supposed to increase our chance of winning the car.
    if doors_I_didnt_pick[0]==truth:
        w=w+1

print(w/n)
