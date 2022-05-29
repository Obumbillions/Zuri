# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    # [assignment] Add your code here

    if len(word1) == len(word2) and sorted(word1.lower()) == sorted(word2.lower()):
        return True

    else:
        return False

word1 = input('word1: ')
word2 = input('word2: ')
print("--->", find_anagram(word1, word2))