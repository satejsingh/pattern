# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def numpat(n):
    # initialising starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # re assigning num
        num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")


# Driver code
n = 5
numpat(n)
