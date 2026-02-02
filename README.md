This is a python game program. the target is to find which number does the system chose, between 1 to 100, using only integers. 

Ther'es few phases of code made for this.
Before i've started the program code, i made an import order with directroy called "random' directory for later function called 'randint' for the computer to choose random number.

Afterwards we've reached to the phase of defining a function that runs the whole program.
there's two variables that im going to use, the random integer itself as a variable and a variables that declare the number of attemps.

Now we've reached to the heart of the code. The 'for' loop runs the number of times that the user can try to guess the random number.
It works in a way that ive declared a 'range' of tries, starting from 1 untill 7 using the max_attempts variable. (the reason ive putted a '+1' in the end of the argument is that the computer will stop when he will get to 7, and will stop the proccess before the user will input his 7th attemp).
   print(f"Attempt {attemp}:") ------> the 'f' order the pc to print the number of the 'for' loop comes to action. every time the loop runs the numebr of runs will be printed as a counted number and i've used it for printing the number of the user attemps as printed text.
   
                user_input = int(input()) ---> user input. that runs in every time the for loop runs.

                
        if user_input == random_number: ------> if condition. it checks if the user putted the exact number.
            print('Congrats son. You must be special')
            won = True ->>>> that switches the bool to true value
            break ---->>> stops the for loop at that point and contioue to the phase that comes after the loop skeleton.
    
        elif user_input < random_number:
            print('The number you chose is lower than the actual number' )
        else:
            print("Too high, be calm and try again")
            
    if not won: ---> printing a fina message before the program comes to end.
        print(f"\nSon, you're not ready yet. The number you were supposed to guess was {random_number}")
    
    
guess_the_number()

