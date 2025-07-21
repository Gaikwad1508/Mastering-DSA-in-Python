def getChar(num):
    if num<1 and num>26:
        return ''
    return chr(ord('a') + num - 1)

def printAllCodes(input, takenSoFar):
    if input == '':
        print(takenSoFar)
        return
    
    firstSingleDigit = int(input[0:1])
    char1 = getChar(firstSingleDigit)

    firstDoubleDigit = int(input[0:2])
    char2 = getChar(firstDoubleDigit)

    if firstSingleDigit > 0 and firstSingleDigit < 10:
        printAllCodes(input[1:], takenSoFar + char1)

    if firstDoubleDigit > 9 and firstDoubleDigit < 27:
        printAllCodes(input[2:], takenSoFar + char2)

    return


input = '1123'
printAllCodes(input, '')

input2 = '123629'
printAllCodes(input2, '')