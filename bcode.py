def square_area(s):
    return s ** 2


def circle_area(r):
    return 3.14159 * r ** 2


def main():
    s, r = 5.0, 3.0
    print(f"Square area: {square_area(s)}")
    print(f"Circle area: {circle_area(r)}")


if __name__ == "__main__":
    main()
