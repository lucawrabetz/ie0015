import random


def main():
    x: int = 1
    y: float = 2.5
    s: str = "luca"
    n: int = 100

    for i in range(n):
        a = random.choice((x, y, s))

        if isinstance(a, int):
            print("a is x")
            print("a: ", a)
            print("x: ", x)

        elif isinstance(a, float):
            print("a is y")
            print("a: ", a)
            print("y: ", y)

        elif isinstance(a, str):
            print("a is s")
            print("a: ", a)
            print("s: ", s)


if __name__ == "__main__":
    main()
