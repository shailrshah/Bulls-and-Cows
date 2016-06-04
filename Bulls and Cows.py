import random
import linecache

DIGITS = 3


def unique_values(n):
    s = [0]*10
    while n:
        s[n % 10] += 1
        if s[n % 10] > 1:
            return False
        n //= 10
    return True


def get_counts(x, ans):
    bulls = 0
    cows = 0
    for i in range(0, len(str(x))):
        user_digit = x // 10 ** i % 10
        for j in range(0, len(str(ans))):
            ans_digit = ans // 10 ** j % 10
            if ans_digit == user_digit:
                if i != j:
                    cows += 1
                if i == j:
                    bulls += 1
    return [bulls, cows]


def no_of_lines(n):
    # Number of different 4 digit integers with no digit repeated = 9*9*8*7 = 4536
    mul = 1
    for i in range(1, n+1):
        if i == 1:
            mul *= 9
        else:
            mul *= (9-i+2)
    return mul


print("Welcome to Shail's Bulls and Cows game!")
print("\nThe goal is to guess an "+str(DIGITS)+"-digit secret number, in which all digits are different.")
print("If your digits are in the right place, then they are bulls.")
print("If your digits are there in the secret number but not in the right place, they are cows.")
print("\nFor example, If secret word is 4871 and your guess is 1834, then there is 1 bull(8) and 2 cows(1 and 4).")


play_again = True
while play_again is True:
    print("\n-------------Begin!-------------")
    ans = int(linecache.getline('random_numbers'+str(DIGITS)+'.txt', random.randrange(0, no_of_lines(DIGITS))))
    print("Cheat: " + str(ans))
    end = False
    prev_no = []
    bulls = []
    cows = []
    history = [prev_no, bulls, cows]

    count = 0
    while end is not True:

        x = int(input("\nGuess the "+str(DIGITS)+" digit number: "))
        if unique_values(x) is False or len(str(x)) is not DIGITS:
            print("The number should have "+str(DIGITS)+" unique digits.")
            continue

        prev_no.append(x)
        [b, c] = get_counts(x, ans)
        bulls.append(b)
        cows.append(c)

        if bulls[count] is DIGITS:
            end = True
            print("Success! The answer was indeed "+str(ans)+"! You did it in "+str(count+1)+" steps.")
            resp = input("Do you want to play again? (Y/N): ")
            if resp == "N":
                play_again = False
                print("\nThanks for playing Shail's Bulls and Cows!")
        else:
            count += 1
            for i in range(0, count):
                print("n = "+str(prev_no[i])+"\tbulls = "+str(bulls[i])+"\tcows = "+str(cows[i]))
            print("Try again! (Guess Count: " + str(count)+")")
            if ans > x:
                print("Hint: The secret number is larger than your guess!")
            else:
                print("Hint: The secret number is smaller than your guess!")
