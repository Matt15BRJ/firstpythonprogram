#Python:    2.7.13
#Author:    Matt Thoman
#Purpose:   Item 36 Python course. Has the user pick a color and a number to see if
#           they match up with pre-chosen ones.


def start(color="",number=0):
    color = color_choice(color)
    number = number_picker(color,number)

def color_choice(color): #conpare the user's color choice to a tuple of colors to see if they choose a good one
    colorTuple = ('green','blue','orange','red','yellow','purple','black','white','gray')
    stop = True
    while stop:
        color = raw_input('Guess a color? ').lower() #assign a string to a variable
        
        if color in colorTuple: #check to see if the user's color choice was in the tuple
            print("{} was a good choice.".format(color).capitalize())#prints user's color choice(string variable) with a comment
            color = True
            stop = False
        else:
            print("{}?? You like weird colors.".format(color).capitalize())            
            stop = False
    return color

def number_picker(color,number):
    stop = True
    while stop:
        try:
            number = input('\nPick a number 1-99: ') #assign an integer to a variable
        except NameError:#if the user enters something other than a number
            print('\nI guess you did something wrong. Try an integer this time.')
            continue
        if number == 42:
            print('\nYou must be a genius as you know the ultimate answer!!')
            stop = False
        elif number != 42:
            number +=1
            if number >= 42: #do some math to the users number to change it
                number = float((number * number)/3) #assign a float to a variable
                print("\nI didn't like your number so I changed it to {}.".format(number))
                stop = False    
            elif number < 42:
                number = (((number + 1)* 2)-1)
                print('\nI think {} is a better number.'.format(number))
                stop = False    
    winLose(color,number)   
    
def winLose(color,number):
    stop = True
    while stop:
        if number == 42 and color == True:#if both user choices were good prints this 
            print('\nYou have chosen wisely.')
            stop = False
        elif (number == 42 and color == False) or (number!= 42 and color == True):
            print('\nSo close.')#checks user's answers and prints response if at least one was good
            stop = False
        else:#if both choices were misses prints this
            print('\nYou were waayyyy off!.')
            stop = False     
    again(color,number)
    
def again(color,number):#asks user if they want to try again
    stop = True
    while stop:
        choice = raw_input('\nWould you like to try again? y/n:').lower()
        if choice == 'y':
            stop = False
            reset(color,number)
        if choice == 'n':
            print("\nFine. GO, you've stayed your hour. But first here's a bunch of randomness. HAHAHAHA!!!")
            gottaGo()
            stop = False
            
        else:
            print('\nPlease enter "y" for YES, "n" for NO...')
            stop = False

def reset(color,number):
        color = ''
        number = 0
        #reset the color and number and start all over
        start(color,number)     

def gottaGo():#if the user chose to quit then they get randomness thrown their way,
    #just because I needed to demonstrate a couple more things
    crazyList = ['bubbles','lollipops','candycorn','syrup','unicorns','Godzilla']
    crazyTup = (12,37,43,62,87,93)
    for x in crazyList:#print out everything in the crazyList
        print x
    for y in crazyTup:#itirate through the tup, divide everything by 5 and print the remainders
        print y%5
    exit()
if __name__== "__main__":
    start()                     
    
