"""

- Two values are given first is odd and second is product of it with 3.
- We've to make following pattern 
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""

from rich.console import Console

console = Console()
value = input().split()
n = int(value[0])
m = int(value[1])
check1 = 3
check2 = 1

for i in range(1, n+1):
    if i <= (n-1)/2:
        for _ in range(int(((m-1)/2))-check2):
            console.print("-", end="", style="blue")

        for _ in range(1, check1+1, 3):
            console.print(".|.", end="", style="yellow")
        
        for _ in range(int(((m-1)/2))-check2):
            console.print("-", end="", style="blue")
        
        if i != ((n-1)/2):
            check1 += 3*2
            check2 += 3
        print() 

    elif i == ((n-1)/2) + 1:
        for _ in range(int((m-7)/2)):
            console.print("-", end="", style="blue")
        for letter in "WELCOME":
            console.print(letter, end="", style="red")
        for _ in range(int((m-7)/2)):
            console.print("-", end="", style="blue")

        print()
    
    else:
        for _ in range(int(((m-1)/2))-check2):
            console.print("-", end="", style="blue")

        for _ in range(1, check1+1, 3):
            console.print(".|.", end="", style="yellow")
        
        for _ in range(int(((m-1)/2))-check2):
            console.print("-", end="", style="blue")
        check1 -= 3*2
        check2 -= 3
        print()
    
