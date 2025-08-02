""" Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string."""


word=input("enter the string:")
n=int(input("enter the number of character you want to remove from the string starting from 0:"))
if(n<len(word)):
    print("original word is:"+ word)
    print(f"the word after removing {n} characetrs is :",word[n:len(word)])
else:
    print("the number is more than the length of the string")

    