# x = input(int())
# a= x*2
# while a!=0:
#     d=a%10
#     a=a//10
# print(a)

# number = int(input('please enter your number: '))
# reverse_num = 0
# while number > 0:
#     temp = number % 10
#     reverse_num = reverse_num * 10 + temp
#     number = number // 10
# print(reverse_num)


# a = int(input())
# b = 0
# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d

# print(b)


# x =0
# i =0
# while x<=7:
#     print(i)
#     x=x+i 
#     i=x+1 
# print(x)

# def print_digits(n):
#     n = str(n)
#     for i in n:
#         print(f"{i}: {n.count(i)}")
 
# num = int(input("Enter an integer: "))
# print_digits(num)




# a =int(input())
# b = 0
# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d

# a = b
# b=0
# while a!=0:
#      d = a%10
#      a = a//10
#      b = b*10+d
#      print(d)


# n = int(input())
# i = 0
# if 1<n<7 :
#     while i < n :
#         print("salam")
#         i = i+1
# else :
#     print("")



# a = int(input())
# b = 0 
# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d
# a = b
# b=0
# while a!=0:
#     d = a%10
#     a = a//10
#     #b = b*10+d
#     print(f"{d}: ",end="")
#     i = 0
#     while i<d:
#         print(d , end="")
#         i+=1
#     print()

# n = int(input("n = "))
# if n<1:
#     print("Error: n has to be a natural number")
# else:
#     counter = 0
#     for i in range(1, int(n**0.5+1)):
#         if n%i==0:
#             counter +=1

#     if counter == 1:
#         print(n, "is a prime number")
#     else:
#         print(n, "is a composite number")
    

x = int(input())
i = 2
p = True
while i<x-1:
    if x%i == 0:
       p= False
    i=i+1   
print(p)       


