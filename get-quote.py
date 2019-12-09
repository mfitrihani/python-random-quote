import random


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    rnd2 = random.randint(0, last)
    print(quotes[rnd].rstrip())
    print(quotes[rnd2].rstrip())


if __name__ == "__main__":
    primary()
