import random

def guess_the_number():
    random_number = random.randint(1, 100)
    max_attemps = 7
    won = False    
    print("Welcome to 'Guess The Number', it's very important to sit down and relax before using this amazing program. Please choose an integer between 1 to 100. Be careful, you have only seven tries. Good luck son.")
    
    for attemp in range(1, max_attemps + 1):
        print(f"Attempt {attemp}:")
        user_input = int(input())
        
        if user_input == random_number:
            won = True
            print('Congrats son. You must be special')
            break 
        elif user_input < random_number:
            print('Too low!')
        else:
            print("Too high!")
    
    
    if not won: 
            print(f"\nSon, you're not ready yet. The number you were supposed to guess was {random_number}")


guess_the_number()
