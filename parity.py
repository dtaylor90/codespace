def main():
    x = int(input( "what's x? "))
    if is_even(x):
    print( "EVEN")
else:
    print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()