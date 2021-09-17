# ROCK PAPER SCISSOR
import random

def RPS(bot,you):    #To set the main logic behind the game.
    # If both value are eqaul declare a tie!
    if(bot==you):
        return None

    # all possiblities if bot choose R
    elif(bot=='R'):
        if(you=='P'):
            return True
        elif(you=='S'):
            return False

     # all possiblities if bot choose R
    elif(bot=='S'):
        if(you=='P'):
            return False
        elif(you=='R'):
            return True
     # all possiblities if bot choose R
        
    elif(bot=='P'):
        if(you=='S'):
            return True
        elif(you=='R'):
            return False


#user will play against the bot 
print("Bot's turn : R(Rock) or P(Paper) or S(Scissor) ")
bot=random.randint(1,3) #with this bot will choose random value from 1,2 and 3.

if(bot==1):
    bot='R'
elif(bot==2):
    bot='P'
elif(bot==3):
    bot='S' 

you=input('''Enter your choice:
 R(Rock) 
 P(Paper) 
 S(Scissor) :\n ''')

res=RPS(bot,you)

if(res==None):
    print("Its a tie because bot had also choose",bot)
elif(res==True):
    print("You won because bot had choose",bot)
else:
    print("You loose because bot had choose",bot)    
