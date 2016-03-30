import re
import os

def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]','',sentence).lower()
    if len(sentence) != 0 and sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    elif len(sentence) == 0:
        return True
    else:
        return False

def its_is_palindrome(sentence):
    while sentence != " ":
        sentence = re.sub(r'[^A-Za-z]','',sentence).lower()
        if len(sentence) >= 1 and sentence[0] == sentence[-1]:
            sentence = sentence[1:-1]
            continue
        elif len(sentence) == 0:
            return True
        else:
            return False
def main():
    sentence = input("Test letters for palindrome -ness, SPACE to exit: ")
    if is_palindrome(sentence) and its_is_palindrome(sentence):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("This is a palindrome")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("This is NOT a palindrome")

if __name__ == '__main__':
    main()
