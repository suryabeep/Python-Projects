import sys

target_int = input("How many integers?")

try:
    target_int = int(target_int)
except ValueError:
    sys.exit("You must enter an integer")
print("target int is: " + str(target_int))
ints = list()
count = 0;
while count < target_int:
    new_int = input("Please enter integer {0}:".format(count + 1))
    isInt = False
    try:
        new_int = int(new_int)
        isInt = True
    except:
        print("You must enter an integer")
    if isInt:
        ints.append(new_int)
        count += 1

print("Using a for loop")
for value in ints:
    print(str(value))
