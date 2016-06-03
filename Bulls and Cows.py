import random
import linecache
print("Welcome to Shail's Bulls and Cows game!")
print("\nThe objective of the game is to guess a 4-digit secret number, in which all digits are different.")
print("If your digits are in the right place, then they are bulls")
print("If your digits are there in the secret number but not in the right place, they are cows.")
print("\nFor example, If secret word is 4871 and your guess is 1834, then there is 1 bull(8) and 2 cows(1 and 4).")


play_again = True
while play_again is True:
    print("\n-------------Begin!-------------")
    ans = int(linecache.getline('random_numbers.txt', random.randrange(0, 4536)))
    # print("Cheat: " + str(ans))
    end = False
    prev_no = []
    bulls = []
    cows = []
    history = [prev_no, bulls, cows]

    count = 0
    while end is not True:

        x = int(input("\nGuess the 4 digit number: "))
        if len(str(x)) is not 4:
            print("The number should be of 4 digits.")
            continue

        prev_no.append(x)
        bulls.append(0)
        cows.append(0)
        for i in range(0, len(str(x))):
            user_digit = x // 10 ** i % 10
            for j in range(0, len(str(x))):
                ans_digit = ans // 10 ** j % 10
                if ans_digit == user_digit:
                    if i != j:
                        cows[count] += 1
                    if i == j:
                        bulls[count] += 1
        if bulls[count] is 4:
            end = True
            print("Success! The answer was indeed "+str(ans)+"! You did it in "+str(count+1)+" steps.")
            resp = input("Do you want to play again? (Y/N): ")
            if resp == "N":
                play_again = False
                print("Thanks for playing Shail's Bulls and Cows!")
        else:
            count += 1
            for i in range(0, count):
                print("n = "+str(prev_no[i])+"\tbulls = "+str(bulls[i])+"\tcows = "+str(cows[i]))
            print("Try again! (Guess Count: " + str(count)+")")