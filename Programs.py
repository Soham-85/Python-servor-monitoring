# # import math

# # a=int(input("Enter the no of students"))
# # b=int(input("Enter the no of students in second class"))
# # c=int(input("Enter the no of students in third class"))

# # desk1=math.ceil(a/2)
# # desk2=math.ceil(b/2)
# # desk3=math.ceil(c/2)

# # total=desk1+desk2+desk3
# # print(total)


# # hour=int(input("enter in hours"))
# # min=int(input("Enter in min"))
# # sec=int(input("enter in sec"))

# # angle=hour*30+min*0.5+sec*(1/120)
# # print(angle)

# x1=int(input("Enter the x cordinate of first sides"))
# y1=int(input("Enter the y cordinate of first sides"))
# x2=int(input("Enter the x cordinate of second sides"))
# y2=int(input("Enter the y cordinate of second sides"))
# x3=int(input("Enter the x cordinate of third sides"))
# y3=int(input("Enter the y cordinate of third sides"))

# if x1==x2:
#     x4=x3
# elif x1==x3:
#     x4=x2
# elif x2==x3
#     x



# n=int(input("enter the no"))
# a=0
# b=1
# count=0
# while count<n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     count+=1
a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c
# \

# n=int(input("Enter the no"))
# if n<2:
#     print("Not prime no")
# else:
#     i=2
#     while i<n:
#         if n%i==0:
#             print("Not prime no")
#             break
#         i+=1
#     else:
#             print("prime no")


# n=int(input("Enter the no"))
# i=1
# while i<=10:
#     print(f"{n} X {i} = {n*i}")
#     i+=1

n=int(input("Enter the no"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

