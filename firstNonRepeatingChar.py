def getFirstNonRepeatingChar(inputString):
    foundChar = ""

    for index in range(0, len(inputString)):
        currentChar = inputString[index]
        subStringToSearch = inputString[0: index] + inputString[index + 1: len(inputString) - 1]

        if (not currentChar in subStringToSearch):
            foundChar = currentChar;
            break

    return foundChar;


if __name__ == "__main__":
    
    inputString = str(raw_input("Check for first repeating characters in the following string: "))

    firstNonRepeatingChar = getFirstNonRepeatingChar(inputString)

    if (len(firstNonRepeatingChar)):
        print("This is the first non repeating char: " + firstNonRepeatingChar)
    else:
        print("No repeating char found in the string")