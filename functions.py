
def modifyString(input):
    input += " that has been modified"

def modifyStringReturn(input):
    input += " that has been modified"
    return input

testString = "This is a test string"
modifyString(testString)
print(testString)
testString = modifyStringReturn(testString)
print(testString)
