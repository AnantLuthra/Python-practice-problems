"""
Input:
N=5
S="RGRGR"
Output:
2
Explanation:
We need to change only the 2nd and 
4th(1-index based) characters to 'R', 
so that the whole string becomes 
the same colour.
"""

def process():
    ...

def RedOrGreen(self,N,S):
       x=S.count('R')
       y=S.count('G')
       if x>y:
           return y
       elif x<y:
           return x
       elif all(elem=='R' for elem in S)==True or all(elem=='G' for elem in S)==True:
           return 0
       elif x==y:
           return x

