import random
num = random.randrange(1000, 9999)
while num < 1000 or num > 9999:
    num = random.randrange(1000, 9999)
done = False
digits = []
for i in range(4):
    digits.append(num % 10)
    num = int(num/10)
while not done:
    cows = 0
    bulls = 0
    user_num = input("Enter a 4-digit number, or QQQ to quit")
    user_num = user_num.strip()
    if user_num == "QQQ" or user_num == "qqq":
        out = ""
        for i in digits:
            out += str(i)
        print("The number was {0}".format(out))
        sys.exit("Game over")
    try:
        user_num = int(user_num)
    except:
        print("That's not a number. Try again.")
        continue
    if user_num < 1000 or user_num > 9999:
        print("Number is not 4 digits long. Try again.")
        continue

    user_digits = []
    for i in range(4):
        digit = user_num % 10
        user_digits.append(digit)
        user_num = int(user_num/10)
    user_digits.reverse()
    for i in range(4):
        if user_digits[i] == digits[i]:
            cows += 1
        elif user_digits[i] in digits:
            bulls += 1
    print("Cows: {0}, Bulls: {1}".format(cows, bulls))
    if cows == 4:
        done = True
        out = ""
        for i in digits:
            out += str(i)
        print("Congratulations! You guessed the number: " + str(out))
