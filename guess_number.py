#guess the number game
import random
print("hey whats ur name?")
name = input()
print('hey '+name +' i am thinking a number between 1-20,can u guess it?')


while True:
    num=random.randint(1,20)
    print('say,what  am i guessing?')
    for guess in range(1,7):
            no=int(input())
            if(num>no):
                print('think something bigger')
            elif(num<no):
                print('think something smaller')
            else:
                break
    if(no==num):
        print('congrats , '+ name +',u have guessed it in '+str(guess) +' try')
        print('wanna try again?say ok/no')
        response=input()
        if(response=='no'):
            break
    else:
        print('u idiot,let me say this.The no is: '+str(num)+'.Go and fuck ur brain')
        print('wanna try again?say ok/no')
        response=input()
        if(response=='no'):
            break
