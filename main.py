# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pickletools import string1


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Please Enter your first word: \n")
    anagram = input("Please enter your Second word: \n")
    for char in word:
        if char not in anagram:
            return False
    return True


i = "yes"
while i == "yes":
    print(find_anagram("word", "anagram"))
    i is not input("Do you want to continue (yes/no) : ")
    i = "no"
else:
    print("Thank you")
