# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def alphapat(n):
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65

    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # explicitely converting to char
            ch = chr(num)

            # printing char value
            print(ch, end=" ")

        # incrementing number
        num = num + 1

        # ending line after each row
        print("\r")


# Driver Code
n = 5
alphapat(n)
