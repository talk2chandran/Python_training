

'''
Space Analysis
recursion:
      5*fact(4)
         4*fact(3)
            3*fact(2)
               2*fact(1)

Time complexity    iter: O(n)    recursion: O(n)
Space complexity   iter: O(1)    recursion: O(n)

'''

#recursive
def fact(num):
    #base condition
    if num==0 or num==1 :
        return 1
    #recursive condition
    else:
        return num * fact(num-1)

n=5
f=fact(n)
print(f)




'''

#iterative
f=1
n=5

if n==0 or n==1 :
    f=1
elif n<0:
    f=0


#f=1#n=5

while (n>1):
    f = f*n  
    n = n-1  

print(f)
'''

