# QUESTION 25.  FIBONACCI SERIES:

# n=int(input())
# a=0
# b=1
# i=1
# while (i<=n):
#     print(a , end=" ")
#     x=a+b
#     a=b
#     b=x
#     i+=1




# QUESTION 26.  REVERSE A NUMBER:

# n=int(input())
# r=0
# while(n>0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# print(r)




# QUESTION 27.      GCD(GREATEST COMMON DIVISOR) OR HCF(HIGHEST COMMON FACTOR):

# a=int(input())
# b=int(input())
# n1=a
# n2=b
# while (n2>0):
#     t=n2
#     n2=n1%n2
#     n1=t
# HCF = n1
# LCM = (a*b)// HCF
# print("HCF: ", HCF )
# print("LCM: ", LCM)
    



# QUESTION 29.      BINARY TO DECIMAL:

# n=int(input())
# c=0
# sum=0
# while(n>0):
#     r=n%10
#     sum=sum+r*2**c
#     c+=1
#     n=n//10
# print(sum)




# QUESTION 30.      DECIMAL TO BINARY:
# ####### WRONG#########
# n= int(input())
# binary_sum=0
# while n>0:
#     binary_sum+= n%2
#     n=n//2

# print("sum of binry digit:" ,binary_sum)



# QUESTION 31.    PRIME?

# n=int(input())
# i=0
# count=0
# i=1
# while(i<=n):
#     if (n%i==0):
#         count+=1
#     i+=1
# if (count == 2):
#     print("Yes")
# else:
#     print("No")




# QUESTION 32.      PERFECT NUMBER?

# n=int(input())
# i=1
# sum=0
# while(i<n):
#     if n % i==0:
#         sum=sum+i
#     i+=1
# if (sum==n):
#     print("Yes")
# else:
#     print("No")




# QUESTION 33.      ARMSTRONG NUMBER?

# n=int(input("Enter the number: "))
# count=0
# sum=0
# m=n
# while(n>0):
#     n=n//10
#     count+=1

# n=m
# while(n>0):
#     r=n%10
#     sum=sum+r**count
#     n=n//10
# if sum==m:
#     print("Yes , it is a armstrong number")
# else:
#     print("Not armstrong number")




# QUESTION 34.      STAR PATTERN 1:

# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print("*", end=" ")
#         j+=1
#     print()
#     i+=1
    



# QUESTION 35.    STAR PATTERN 2:

# n= int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n-i):
#         print(" ", end=" ")
#         j+=1
#     k=1
#     while(k<=i):
#         print("*",end=" ")
#         k+=1
#     print()
#     i+=1  




# QUESTION 36.      STAR PATTERN 3:
# n=int(input())
# i=1
# while(i<=n):
#     print(" "*(i-1) + "*",end=" ")
#     i+=1
#     print()




# QUESTION 37.        STAR PATTERN 4:
# n=int(input())
# i=1
# while(i<=n):
#     j=1
#     while(j<=n-i):
#         print(" ",end=" ")
#         j+=1
#     k=1
#     while (k<=(2*i-1)):
#         print("*", end=" ")
#         k+=1
#     i+=1
#     print()




# QUESTION 38.      FIRSST N PRIME NUMBERS:

# n=int(input())
# i=2
# count=0
# while(count<n):
#     flag=True
#     j=2
#     while(j <= i //2):
#         if (i%j==0):
#             flag=False
#         j+=1
#     if flag:
#         print(i, end=" ")
#         count+=1
#     i+=1
        