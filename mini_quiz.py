print('Welcome to my Quiz Game!')

playing = input('This Quiz Game consist of 12 questions regarding general knowledge. Type Yes to start the quiz: ')

if playing.lower() == 'yes':
    print('Okay lets start the game!\n')
    score = 0

else:
    print('\nIts okay nevermind :)\n')
    quit()

#ask the player questions and the player answer it.
answer = input('1) What is the most biggest ocean in the world? : ')
if answer.lower() == 'pacific ocean':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('2) How many continents are there in the world? : ')
if answer.lower() == '7':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('3) What is the capital city of France? : ')
if answer.lower() == 'paris':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('4) What temperature does the water boil at? (celcius) : ')
if answer.lower() == '100':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('5) What does 3.142 represent in mathematical concept? : ')
if answer.lower() == 'pi':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('6) Which country has the biggest land mass in the world : ')
if answer.lower() == 'russia':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('7) What is the scientific name for human? : ')
if answer.lower() == 'homo sapien':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('8) What is the capital city of Canada : ')
if answer.lower() == 'ottawa':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('9) What is the name of our galaxy : ')
if answer.lower() == 'milky way':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('10) H20 is the chemical symbol of what?: ')
if answer.lower() == 'water':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('11) In which country does the PETRONAS Twin Tower located at? : ')
if answer.lower() == 'malaysia':
    print('CORRECT!!')
    score += 1
    print('Next Question\n')

else:
    print('INCORRECT!!\n')

answer = input('12) What is the Metric unit for height? : ')
if answer.lower() == 'meter':
    print('CORRECT!!\n')
    score += 1

else:
    print('INCORRECT!!\n')


#calculate and display the total mark of the quiz.
print('Your have got ' + str(score) + ' correct answers!')
percent_score = (score/12) * 100
formatted_score = format(percent_score, '.2f')
print('Your score is ' + formatted_score + '% for this quiz!')
print('Thank you for playing!!')