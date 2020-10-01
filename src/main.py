def sayhi(name):
    print("Hello, " + str(name) + "!")


def whoareyou():
    yourname = input("Hi! What is your name? ")
    sayhi(yourname)
    print("Welcome to the Git/GitHub tutorial!\n")


if __name__ == "__main__":
    whoareyou()

