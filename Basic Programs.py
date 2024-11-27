#Basic Programs
#1.program to convert lowercase to uppercase.
'''
s1=input("Enter the string: \n")
print(s1.upper())
'''
#2.program to convert uppercase to lowercase.
'''
s2=input("Enter the string: \n")
print(s2.lower())
'''
#3.program to convert uppercase to lowercase and lowercase to uppercase without using method
'''
s3=input("Enter the string:\n")
print(s3.swapcase())
'''
'''
s3=input("Enter a string:\n")
converted_string= ""
for char in s3:
    if 'A' <= char <= 'Z':
        converted_string += chr(ord(char)+32)
    elif 'a' <= char <='z':
        converted_string += chr(ord(char)-32)
    else:
        converted_string += char
print("Original:", s3)
print("converted:",converted_string)
'''
#4.print the indexes and characters of a string
'''
str_=input("enter a string:")
index_=0
str_1=[]
while index_ < len(str_):
    str_1.append((index_, str_[index_]))
    index_+=1
print(str_1)
'''
#5.program to convert uppercase to lowercase and lowercase to uppercase without using inbuilt method for more than one character
'''
#program to convert lower to upper and viceversa for one character
s3=input("Enter a string:\n")
converted_string= ""
for char in s3:
    if 'A' <= char <= 'Z':
        converted_string += chr(ord(char)+32)
    elif 'a' <= char <='z':
        converted_string += chr(ord(char)-32)
    else:
        converted_string += char
print("Original:", s3)
print("converted:",converted_string)

#another method
n=input("Enter:")
if 'a'<=n<='z':
    print(chr(ord(n)-32))
elif 'A'<=n<='Z':
    print(chr(ord(n)+32))
'''
'''
#program to convert lower to upper and viceversa for multiple characters
string_=input("Enter:")
index_=0
new_str=''
while index_<len(string_):
    if 'a'<=string_[index_]<='z':
        new_str+=chr(ord(string_[index_])-32)
    elif 'A'<=string_[index_]<='Z':
        new_str+=chr(ord(string_[index_])+32)
    else:
        new_str+=string_[index_]
    index_+=1
print(new_str)
'''     
#6.program to get the string in reverse order
'''
str1=input("Enter the string:\n")
print(str1[::-1])
'''
#another method(without slicing)
'''
inp_=input("enter a string:")
i=0
n_s=''
while i<len(inp_):
    n_s=inp_[i]+n_s
    i+=1
print(n_s)
'''
#7.program to get the length of strings in a list
#names=['eve','james','bill','steve','mill','amul']
'''
names=['eve','james','bill','steve','mill','amul']
i=0
l_=[]
while i< len(names):
    l_+=[[names[i],len(names[i])]]
    i += 1
print(l_)#[['eve', 3], ['james', 5], ['bill', 4], ['steve', 5], ['mill', 4], ['amul', 4]]
'''
#8.program to get the 1st character of each string in list
#names=['eve','james','bill','steve','mill','amul']
'''
names=['eve','james','bill','steve','mill','amul']
first_chars=[string[0] for string in names]
print("first characters:")
for char in first_chars:
    print(char)
'''
#9.program to get the end character of each string in list
#names=['eve','james','bill','steve','mill','amul']
'''
names=['eve','james','bill','steve','mill','amul']
end_chars=[string[-1] for string in names]
print("end characters:")
for char in end_chars:
    print(char)
'''

#10.create a dictionary with starting character and word in the list
#names=['eve','james','bill','steve','mill','amul']
'''
names=['eve','james','bill','steve','mill','amul']
dic={}
i=0
while i<len(names):
    dic[names[i][0]]=names[i]
    i+=1
print(dic)
'''
#11.create a dictionary with word and length word in the list.
'''
names=['eve','james','bill','steve','mill','amul']
dic={}
i=0
while i<len(names):
    dic[names[i]]=len(names[i])
    i+=1
print(dic)
'''
#12.program to print only the words starting with vowel.
#names=['eve','james','bill','steve','mill','amul']
'''
words=['eve','james','bill','steve','mill','amul']
vowels=['a','e','i','o','u','A','E','I','O','U']
for word in words:
    if word[0] in vowels:
        print(word)
'''


#13.program to get the numbers which is of even
#l=[2,3,4,45,43,89,12,90,77,65]
'''
l=[2,3,4,45,43,89,12,90,77,65]
for num in l:
    if num%2==0:
        print(num)
        
#another method
n=[2,3,4,45,43,29,12,90,77,65]
i=0
while i<len(n):
    if int(str(n[i])[0])%2==0:
        print(n[i])
    i+=1

'''
#14.program to get the numbers starting with even number
#l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
'''
l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
for num in l:
    num_str = str(num)
    if num_str[0] in ['0','2','4','6','8']:
        print(num)

l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
n=0
while n<len(l):
    if int(str(n[i])[0])%2==0:
        print(
    
    
'''
#15.program to get the numbers ending with odd number
#l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
'''
l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
for num in l:
    num_str = str(num)
    if num_str[0] in ['1','3','5','7','9']:
        print(num)
'''
#16.program to get 1 to 10
'''
i=1
while i<=10:
    print(i)
    i=i+1
'''
#17.program to get -1 to -10
'''
num=-1
while num>=-10:
    print(num)
    num-=1
'''
#18.program to get 10 to 1
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''
#19.program to get 1 to user input
'''
num=int(input("Enter a number: "))
i=1
while i <= num:
    print(i)
    i += 1
'''
#20.program to get -20 to -10
'''
num=-20
while num<=-10:
    print(num)
    num+=1
'''
#21.program to get 1 to -10
'''
num=1
while num>=-10:
    print(num)
    num -= 1#1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10(line by line)
'''
#22.program to get -1 to 20
'''
num=-1
while num<=20:
    print(num)
    num += 1
'''
#23.program to get -10 to -1
'''
num=-10
while num<=-1:
    print(num)
    num+=1
'''


#24.program to find the area of rectangle using user input
'''
length=float(input("Enter the length of Rectangle:"))
width=float(input("Enter the width of Rectangle:"))
area= length * width
print(area)
'''
#25.program to square a number using user input
'''
num=int(input("Enter a number:"))
square= num ** 2
print(square)
'''
#26.program to add a integer and a float
'''
int_value=int(input("Enter an integer:"))
float_value=float(input("Enter a float:"))
result=int_value + float_value
print(result)
'''
#27.program to find the square root
'''
import math
num=int(input("Enter a number:"))
square_root=math.sqrt(num)
print(square_root)
'''
#28.program to add two numbers
'''
a=10
b=20
print(a+b)
'''
#29.program to print a string 10 times
'''
string=input("enter a string: \n")
print(string* 10)
'''
#30.program to combine two integer
'''
a='10'
b='20'
print(a+b)
'''
#31.program to calculate area of triangle
'''
base=float(input("Enter the base of Triangle:"))
height=float(input("Enter the height of Triangle:"))
area = 0.5 * base * height
print(area)
'''
#32.program to convert kilometer to miles
'''
kilometers=float(input("Enter distance in kilometers:"))
conversion_factor=0.621371
miles=kilometers * conversion_factor
print(miles)
'''
#33.program to convert any negative number to positive number
'''
num=float(input("Enter a number:"))
if num < 0:
    num = -num
    print(num)
'''
#34.program to convert integer to float
'''
int_value=int(input("Enter an integer:"))
float_value=float(int_value)
print(float_value)
'''
#35.program to find the reminder and quotient
'''
dividend=int(input("Enter the dividend:"))
divisor=int(input("Enter the divisor:"))
quotient=dividend // divisor
remainder=dividend % divisor
print(quotient)
print(remainder)
'''
#36.program to round a number
'''
num=float(input("Enter a number:"))
rounded_number=round(num)
print(rounded_number)
'''
#37.program to find the simple interest
'''
principal=int(input("Enter the principal amount:"))
rate=int(input("Enter the annual interest rate(in %):"))
time=int(input("Enter the time period in years: "))
simple_interest=(principal * rate * time)/100
print(simple_interest)
'''
#38.program to find the compound interest
'''
principal=int(input("Enter the principal amount:"))
rate=int(input("Enter the annual interest rate(in %):"))
n=int(input("Enter the number of times that interest is compounded per year:"))
time=int(input("Enter the time period in years: "))
rate_decimal = rate / 100
amount=principal * (1 + rate_decimal/n)(n*time)
compound_interest=amount-principal
print(compound_interest)
'''
#39.program to get factorial of a number
'''
n=int(input("Enter a num:"))
i=1
fact=1
while n>=i:
    fact=fact*i
    i=i+1
print(fact)
''' 





