t = int(input())


def prin_patt(n):

    print(f"Square Size {n}")
    if n%2 == 0:
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

    else:
        for i in range(n):
            if i == 0 or i == n - 1:
                for i in range(n):
                    print("*", end="")
                print()
            else:
                for i in range(n):
                    if i ==0 or i == n - 1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
    print()

for i in range(t):
    n = int(input())
    prin_patt(n)
