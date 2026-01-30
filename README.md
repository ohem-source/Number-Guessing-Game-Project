This is a python game program. the target is to find which number does the system chose, between 1 to 100, only integers. Iv'e chosed to add more kinds of python orders that we didn't learnd yet on the crash course,
like 'try' and 'except', and 'if not' to make the program run even if the user will input invalid value, like strings.

Ther'es few phases of code made for this.

a. first of all we need to import 'random' directory for later function called 'randint' for the computer to choose random number.

b. the second phase is about defining a function that runs the whole program, that's defining complex orders.
c. there's three variables we need to do it smoothly. 
  the random integer itself,number of attemps and a boolean var that checks if the user putted an integer and not something else.

d. the 'for' loop runs the number of times that the user can try guess the number.
  it works in a way that ive declared a 'range' of tries, starting from 1 untill 7. (the reason ive putted a '+1' in the end of the argument is that the computer will stop when he will get to 7, and will stop the proccess 
  before the user will input his 7th attemp.
e. the 'while' loop 
  
    for attemp in range(1, max_attemps + 1):
        while True:b
            try:ןמ
                print(f"Attempt {attemp}:")
                user_input = int(input())
                break
            except ValueError:
                print("Son, it's not a number, Don't waste your tries")
                continue
        if user_input == random_number:
            print('Congrats son. You must be special')
            won = True
            break
    
        elif user_input < random_number:
            print('The number you chose is lower than the actual number' )
        else:
            print("Too high, be calm and try again")
            
    if not won:
        print(f"\nSon, you're not ready yet. The number you were supposed to guess was {random_number}")
    
    
guess_the_number()

