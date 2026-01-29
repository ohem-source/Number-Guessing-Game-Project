import random

def guess_the_number():
    
    random_number = random.randint(1, 100)
    max_attemps = 7
    won = False
    print("Welcome to 'Guess The Number', it's very important to sit down and relax before using this amazing program. Please choose an integer between 1 to 100. Be careful, you have only seven tries. Good luck son.")
    for attemp in range(1, max_attemps + 1):
        while True:
            try:
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
