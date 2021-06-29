# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pypart(n):
    myList = []
    for i in range(1, n + 1):
        myList.append("*" * i)
    print("\n".join(myList))


# Driver Code
n = 5
pypart(n)
