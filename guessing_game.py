secret_phrase = "ww2"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_phrase and not out_of_guess:
     if guess_count < guess_limit :
        guess= input("Guess the word: ")
        guess_count += 1
     else:
        out_of_guess = True
if out_of_guess:
    print("Out of guesses , You failed ! ")
else:
    print("You won ;)")

