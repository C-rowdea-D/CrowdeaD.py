print("hey guess the number between 1 to 10 and there is only 3 guesses: ")

secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("guess ? "))
    guess_count += 1
    if guess == secret_number :
        print('You won !')
        break
else :
        print(" sorry the answer is 7 :)")
