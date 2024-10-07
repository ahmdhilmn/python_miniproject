import random

user_win = 0
computer_win = 0
options = ['rock', 'paper', 'scissor']

playing = input('Do you want to play Rock/Paper/Scissor? If not type Q to quit : ')

if playing.lower() == 'yes':
    print('Okay lets play the game!!\n')

elif playing.lower() == 'q':
    print('\nIts okay nevermind\n')
    quit()

while True:
    user_input = input('Type Rock/Paper/Scissor to start the game: ').lower()
    if user_input == options:
        break

    if user_input not in options:
        continue

random_number = random.randint(1,3)
# rock = 1, paper = 2, scissor = 3

computer_pick = options[random_number]
print('Computer pick', computer_pick + '.')

if user_input == 'rock' and computer_pick ==


        