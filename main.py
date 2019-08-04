import random

def show_state(secret_word, guessed):
    for x in secret_word:
        if x in guessed:
            print(x, end=' ')
        else:
            print('_', end=' ')
            
def make_guess(available_guesses, guessed):
    global guesses_left
    
    print('')
    print('')
    print('make a guess from {}'.format(available_guesses))
    print('{} guesses_left'.format(guesses_left))

    user_guess = input().upper()

    available_guesses = available_guesses.replace(user_guess, '')
    guessed = guessed + user_guess
    
    guesses_left = guesses_left - 1 
    
    return available_guesses, guessed


words = ['LANFRANC', 'WINTERBOURNE', 'HERTFORDSHIRE', 'BRUNEL', 'CITY']
available_guesses = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
guessed = ''
guesses_left = 10

secret_word = random.choice(words)

while guesses_left !=0:
    show_state(secret_word, guessed)
    available_guesses, guessed = make_guess(available_guesses, guessed)
