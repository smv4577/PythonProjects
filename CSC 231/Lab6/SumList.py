# __author__ = 'guinnc'
#
#
# # # # def sumN(n):
# # # #     if n == 0:
# # # #         return 0
# # # #     if n == 1:
# # # #         return 1
# # # #     return sumN(n -1) + n
# # # #
# # # # n = int(input("Give me an integer: "))
# # # # print("The sum of 0 to", n, "is", sumN(n))
# # #
# # # def sumList(list):
# # #     if len(list) == 0:
# # #         return 0
# # #     else:
# # #         return list[0] + sumList(list[1:])
# # #
# # #
# # # def searchList(list, target):
# # #     if list == []:
# # #         return False
# # #     if list[0] == target:
# # #         return True
# # #     return searchList(list[1:], target)
# # #
# # # # print(sumList([1, 2, 3, 4]))
# # #
# # # done = False
# # # list = []
# # # while not done:
# # #     text = input("Enter a number:")
# # #     if text[0] == "q":
# # #         break
# # #
# # # target = int(input("Enter a number: "))
# # #
# # # if searchList(list, target):
# # #     print("Yes, it is in the list")
# # # else:
# # #     print("No, it is not in the list")
# # #
# # def count(s, ch):
# #     if len(s) == 0:
# #         return 0
# #     if s[0] == ch:
# #         return 1 + count(s[1:], ch)
# #     else:
# #         return 0 + count(s[1:], ch)
# #
# # while True:
# #     theString = input("Give me a string: ")
# #     theChar = input("Give me a character: ")
# #     print(theChar, "occurs", count(theString, theChar), "times inside of", theString)
# #
# def isPalindrome(s):
#     if len(s) == 0:
#         return True
#     if len(s) == 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return isPalindrome(s[1:-1])
#
#
# while True:
#     text = input("Enter a string: ")
#     if isPalindrome(text.lower()):
#         print("Yes,", text, "is a palindrome")
#     else:
#         print("No,", text, "is not a palindrome")
#


def giveMeANumber():
    text = input("Give me a positive integer: ")
    try:
        num = int(text)
        if num > 0:
            return num
        else:
            print("That's a negative number")
            return giveMeANumber()
    except:
        print("That's not a number")
        return giveMeANumber()

number = giveMeANumber()

print(number)
