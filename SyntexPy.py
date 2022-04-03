#fibonachi

def main():
    (one, two) = (0, 1)

    limit = 1000

    while one < limit:
        print(one)
        (one, two) = (two, one+two)

if __name__ == "__main__":
    main()