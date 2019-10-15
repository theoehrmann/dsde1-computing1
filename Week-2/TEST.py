from random import randint

number = 0 #reset variables
randomnumber = randint(0,5)

def game():
    number = int(input("Type in a number 1-5  "))
    print (number)
    print (randomnumber) 
    if randomnumber == 2:
        print("bingo")
    while randomnumber <= 3:
        print ("not ok")
        random number +=1