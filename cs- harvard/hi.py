def main():
    x  = input("Enter a number: ")
    if is_even(int(x)):
        print("Even")
    else:
        print("ODD")


def is_even(ex):
    return True if ex % 2 == 0 else False
    



main()
