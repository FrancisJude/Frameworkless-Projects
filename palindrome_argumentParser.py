import argparse
from string import Template

class Palindrome():
    def isReverse(self, *arg: str) -> str:
        return ''.join(list(reversed(*arg)))

    def isPalindrome(self, word: str) -> bool:
        return True if ''.join(list(reversed(word))) == word else False

if __name__ == '__main__':
    pal = Palindrome()
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help = "Please input word", type = str)
    parser.add_argument("method", help = "Please input the function \n[1] for isReverse\n[2] for isPalindrome", type = str)
    arg = parser.parse_args()
    if arg.method == "1":
        print(f"Reversed: {pal.isReverse(arg.word)}")
        exit()
    print(f"Is Palindrome: {pal.isPalindrome(arg.word)}")

