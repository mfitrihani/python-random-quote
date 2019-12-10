import random


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    line1, line2 = random.sample(quotes, 2)
    print(line1.rstrip())
    print(line2.rstrip())


if __name__ == "__main__":
    primary()
