import DeveloperCredits
import string
import random
import os


#CHARACTERS VARIABLES
def characters():

    #LETTERS, DIGITS AND SPECIAL-CHARACTERS
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    lettersLower = ""
    lettersUpper = ""

    #SEPARETE UPPER AND LOWER LETTERS
    for caracter in letters:
        if caracter.islower():
            lettersLower += caracter
        else:
            lettersUpper += caracter

    #RETURN ARRAY-CHARACTERS
    arrayCharacters = lettersUpper, lettersLower, digits, special
    print(arrayCharacters)
    return arrayCharacters

#INPUT CHECKTRUE TARGET VARIABLE
def inputTrueUser():

    #PERSONAL RECOMENDATION ABOUT SAFE PASSWORD
    print("I personally recommend to user, generate long passwords approx (12 or more characters)...\n"
          "with a combination of numbers, letters and symbols to make a strong secure password.\n")

    #INPUTS AND CHECKS TRUE OR FALSE
    Upper = input("LetterUpper? (Y/N) ---> ").lower() == "y"
    Lower = input("LetterLower? (Y/N) ---> ").lower() == "y"
    Digits = input("Numbers? (Y/N) ---> ").lower() == "y"
    Special = input("SpecialCharacters? (Y/N) ---> ").lower() == "y"

    #RETURN ARRAY-BOOLEAN-CHARACTERS
    ArrayBoolean =[Upper, Lower, Digits, Special]
    return ArrayBoolean

#GENERATE CHARACTERS VARIABLES
def characterChecks(arrayCharacters, ArrayBoolean):

    charactersPassword = ""

    lettersUpper = arrayCharacters[0]
    lettersLower = arrayCharacters[1]
    digits = arrayCharacters[2]
    special = arrayCharacters[3]

    #CHECK BOOLEANS
    if ArrayBoolean[0] == True:
        charactersPassword += lettersUpper

    if ArrayBoolean[1] == True:
        charactersPassword += lettersLower

    if ArrayBoolean[2] == True:
        charactersPassword += digits

    if ArrayBoolean[3] == True:
        charactersPassword += special

    #RETURN NEW-CHARACTER STRING
    return charactersPassword

#INPUT LONGPASSWORD
def lenPasswordUser():

    # INPUT USER LEN(PASSWORD)
    LenCharacter = ""

    while LenCharacter == "":

        try:
            LenCharacter = int(input("LongPassword ---> "))

            if LenCharacter < 1:
                print("\nINGRESE UN VALOR MAYOR A 0")
                LenCharacter = ""

        except ValueError:
            print("\nINGRESE UN VALOR NUMERICO")

    print()
    return LenCharacter

#GENERATE AND PRINT RANDOM-PASSWORD
def generatepassword(charactersPassword, lenNumber):

    #CREATE A RANDOM-CHARACTERS PASSWORD
    pwd = ""
    while len(pwd)<lenNumber:

        if charactersPassword == "":
            runScript = input("\nNO SELECCIONADO NINGUN CARACTER\nDESEA VOLVER A EJECUTAR EL SCRIPT? (Y/N) ---> ").lower() == "y"

            if runScript == True:

                os.system('cls')
                main()
            else:
                quit()

        newChar = random.choice(charactersPassword)
        pwd += newChar

    return pwd

def printPassword(pwd):

    #CLEAN TERMINAL
    os.system('cls')

    #PRINT PASSWORD
    print("YOUR PASSWORD:\n"+pwd)

    #END SCRIPT
    input("\nPRESS ANY KEY TO EXIT")
    quit()

def main():

    #DEVELOPER-CREDITS
    DeveloperCredits.printCredits()

    #USER-INPUT-BOOLEAN
    ArrayBoolean = inputTrueUser()

    #CHARACTERS-ARRAY
    character = characterChecks(characters(), ArrayBoolean)

    #LEN PASSWORD USER
    lenNumber = lenPasswordUser()

    #PASSWORD-GENERATOR
    password = generatepassword(character, lenNumber)

    #PRINT PASSWORD
    printPassword(password)

"""if __name__ == '__main__':
    main()"""


