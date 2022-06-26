#!/usr/bin/env python
# coding: utf-8

# # Python program to find the largest among 3 numbers
# 

# In[ ]:


a=int(input('Enter the first age '))
b=int(input('Enter the second age '))
c=int(input('Enter the third age '))

max=a
if max < b:
    max=b
if max < c:
    max=c
print(max)


# # Python program to convert temperature from celsius to farhenheit

# In[ ]:


temp=float(input('Enter temperature in celsius'))
farhenheit=(temp*1.8)+32
print(farhenheit)


# # Swap 2 variable in python using another variable

# In[ ]:


a=int(input('Enter your first number'))
b=int(input('Enter your second number'))
temp=a
a=b
b=temp
print("value of a:",a)
print("value of b:",b)


# ## Python code to add 3 digits of the number entered by the user.

# In[ ]:


num=int(input('Enter your number'))
a=num%10 #(345: 345%10=5)
num=num//10 #(// is used for integer division )
b=num%10
c=num//10

rev=a+b+c
print(rev)


# In[ ]:


#adding 4 digit numbers
num=int(input('Enter your number'))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
d=num//10

rev=a+b+c+d
print(rev)


# # Reverse digits in python

# In[ ]:


user_input=int(input('Enter your number'))
num=user_input
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
d=num//10

rev=1000*a + 100*b + 10*c +d
print('Original number :', user_input)
print('reverse number:', rev)
if user_input==rev:
    print('True')
else:
    print('False')



# # Python program to determine whether the number is even or odd

# In[ ]:


num=int(input('Enter your number'))
if num%2==0:
    print('This is an even number')
else:
    print('This is an odd number')


# # Leap year program

# In[ ]:


year=int(input('Enter your year'))
if year%4==0:
    print('Leap year')
else:
    print('not a leap year')


# # Python program to find an euclidean distance

# In[ ]:


x1=int(input('Enter x1 of x_cordinate'))
y1=int(input('Enter y1 of y_cordinate'))
x2=int(input('Enter x2 of x_cordinate'))
y2=int(input('Enter y2 of y_cordinate'))

d=((x2-x1)**2-(y2-y1)**2)**0.5
print(d)


# # Python program to check if the given 3 angles can form a triangle or not.
# 

# In[ ]:


a=int(input('Enter your first angle'))
b=int(input('Enter your second angle'))
c=int(input('Enter your third angle'))

if a+b+c==180 and a!=0 and b!=0 and c!=0:
    print('Possible')
else:
    print('Not Possible')


# # Python program | To calculate Profit or Loss for given selling and cost price.
# 

# In[ ]:


cp=int(input('Enter the cost price'))
sp=int(input('Enter the selling price'))
if cp>sp:
    amount=cp-sp
    print('Loss of :', amount)
elif sp>cp:
    amount=sp-cp
    print('profit of:', amount)
else:
    print('No profit no loss', amount-amount)


# # Python program to calculate Simple Interest.
# 

# In[ ]:


p=float(input('Enter your principal amount that you want to lend'))
r=float(input('Enter the interest you want to take'))
t=float(input('Enter the time in years you wish to lend the money'))

si=(p*r*t)/100
print('The simple interest on the loan will be:', si)
a=p+si
print('The amount you should recive:', a)


# # Calculate Volume of Cylinder. Also find out the cost of milk if the milk is being sold at Rs 40 per litre.

# In[ ]:


r=float(input('Enter the radius:'))
h=float(input('Enter the height:'))
v=3.14*(r**2)*h
print('The volume of the container is:', v)
cost=v/1000*40
print('The cost of the milk will be:',"Rs",cost)


# # Python program to check if a given number is divisible by both 3 & 6.
# 

# In[ ]:


num=int(input('Enter the number'))
if num%3==0 and num%6==0:
    print(num,"is divisible by 3 and 6 both")
elif num%3==0 and num%6!=0:
    print(num,"is divisible by 3 but not by 6")
elif num%3!=0 and num%6==0:
    print(num,"is divisible by 6 but not by 3")
else:
    print(num,"is not divisible by 3 and 6 both")
    


# # Determine Weather type

# In[ ]:


#if temp>=30 and humidity>=90 weather is hot and humid
#if temp>=30 and humidity<90 weather is hot
#if temp<30 and humidity >=90 weather is cold and humid
#if temp<30 and humidity <90 weather is cold

temp=float(input('Enter temperature in celsius'))
humidity=float(input('Enter humidity percentage'))

if temp>=30 and humidity>=90:
    print('weather is hot and humid')
elif temp>=30 and humidity<90:
    print('weather is hot')
elif temp<30 and humidity >=90:
    print(weather is cold and humid)
else:
    print('weather is cold')



# # Python program to find the sum of the square of a given number

# In[ ]:


num=int(input('Enter your number'))
a=num%10
num=num//10
b=num%10
c=num//10

add=(a**2)+(b**2)+(c**2)
print('the required sum is:', add)


# # Python program to check if a given number is Armstrong number or not.

# In[ ]:


user_input=int(input('Enter your number'))
num=user_input
print(num)
a=num%10
num=num//10
b=num%10
c=num//10

add=(a**3)+(b**3)+(c**3)
if add==user_input:
    print('Number is an armstrong number')
else:
    print('Number is not an armstrong number')
    


# # Narcissictic number

# In[ ]:


user_input=int(input('Enter your number'))
num=user_input
print(num)
a=num%10
num=num//10
b=num%10
c=num//10

add=(a**3)+(b**3)+(c**3)
if add==user_input:
    print('Number is a Narcissictic number')
else:
    print('Number is not a Narcissictic number')
    


# # Calculate Inhand salary 

# In[ ]:


user_input=float(input('Enter the annual salary'))

if user_input >500000 and user_input<=1000000:
    tax=(10/100)*user_input
    temp_salary=user_input-tax
elif user_input >1000000 and user_input<=2000000:
    tax=(20/100)*user_input
    temp_salary=user_input-tax
else:
    tax=(30/100)*user_input
    temp_salary=user_input-tax 
print('Salary after deduction of taxes are:', temp_salary)

hra=(10/100)*temp_salary
da=(5/100)*temp_salary
pf=(3/100)*temp_salary

in_handsalary=temp_salary+hra+da+pf
print('The inhand salary will be:', in_handsalary)

if in_handsalary <= 999:
    print(in_handsalary)
elif in_handsalary >=1000 and in_handsalary <9999:
    print(in_handsalary/1000,'k')
elif in_handsalary >=100000 and in_handsalary<=9999999:
    print(in_handsalary/100000,'l')
else:
    print(in_handsalary/10000000,'cr')
    


# # How to write a menu driven program in Python.
# 

# In[ ]:


user_input=input('''
Enter how would you like to proceed?
1. Convert cm to inches.
2. Convert km to miles.
3. Convert usd in inr.
4. Exit

''')

if user_input=='1':
    cm=float(input('Enter your value in cm'))
    inches=cm*0.394
    print('Your value in inch is:', inches)
elif user_input=='2':
    km=float(input('Enter your value in km'))
    miles=km*0.621
    print('Your value in miles will be:', miles)
elif user_input=='3':
    usd=float(input('Enter your value in USD'))
    inr=usd*77.69
    print('The value in rs will be:', inr)
else:
    print('Bye')


# # How to Swap two numbers in Python?
# 

# In[ ]:


a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
a=a+b
b=a-b
a=a-b

print('After swapping the value of a is:', a,"and the value of b is:",b)


# # Python program to print the sum of first n numbers.
# 

# In[ ]:


n=int(input('Enter your number:'))
s=n* (n+1)/2
print(s)


# # Python program to multiply two numbers without using the '*' operator.

# In[ ]:


first_num=int(input('Enter your first number'))
second_num=int(input('Enter your second number'))

sum=0
for i in range(0,first_num):
    sum=sum+second_num
print('Your sum is:', sum)


# # Python program to find the Factorial of a given number.

# In[ ]:


#with recursion
def factorial(n):
    if n==1:
        return n
    else:
        fact=n*factorial(n-1)
        return fact


# In[ ]:


factorial(5)


# In[ ]:


#without recursion

num=int(input('Enter your number'))
i=1
if i>0:
    while num>=1:
        i=i*num
        num=num-1
    print(i)
    


# # Python program to print first 25 Odd numbers.
# 

# In[ ]:


flag=0
i=1
while True:
    if i%2!=0:
        print(i)
        flag=flag+1
    if flag==25:
        break
    i=i+1
        
    
    


# # Python program to check a number is Prime or not.
# 

# In[ ]:


num=int(input('Enter your number'))
if num==2:
    print('Prime number')
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,'is Not a prime number')
            break
        else:
            print(num,'is a prime number')
            break
else:
    print(num,'is Not a prime number')    
            


# # Python program to print Armstrong number in the range 100 to 1000.
# 

# In[ ]:


for num in range(100,1000):
    i=num
    a=num%10
    num=num//10
    b=num%10
    c=num//10
    
    add=(a**3)+(b**3)+(c**3)
    if add==i:
        print(i)


# # Python program to print the all possible combinations from the Digits.
# 

# In[ ]:


for i in range(1,5):
    for j in range(1,5):
        if i!=j:
            print(i,j)


# # Python program to calculate HCF of two numbers

# In[ ]:


a=int(input('Enter first number'))
b=int(input('Enter second number'))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print(rem)


# # Python program to calculate LCM of two numbers

# In[ ]:


a=int(input('Enter first number'))
num1=a
b=int(input('Enter second number'))
num2=b

while num1%num2!=0:
    rem=num1%num2
    num1=num2
    num2=rem
hcf=num2
lcm=(a*b)/hcf
print(lcm)


# # Python program to print first 25 prime numbers.

# In[ ]:


flag=0
num=2
while flag<=25:
    for i in range(2,num):
        if num%i==0:
            break
    else:
            print (num)
            flag=flag+1
    num=num+1
        


# # Python program to print the first 20 Fibonacci series.
# 

# In[ ]:


count=0
a=0
b=1
print(a)
print(b)
while True:
    c=a+b
    a=b
    b=c
    print(c)
    count=count+1
    if count==18:
        break


# # Python program for Compound Interest
# 

# In[ ]:


p=float(input('Enter the principal amount'))
r=float(input('Enter the rate of interset'))
t=int(input('Enter the time elapsed'))
a=p*(1+r/100)**t
print(a)
ci=a-p
print(ci)


# # Python program to print the sum of (n + nn + nnn).

# In[ ]:


n=input('Enter the number')
print(n)
nn=n+n
print(nn)
nnn=n+n+n
print(nnn)
sum=int(n)+int(nn)+int(nnn)
print(sum)


# # Python program to count the total number of digits in a given number
# 

# In[ ]:


num=int(input('Enter your number'))
count=0
while num>0:
    num=num//10
    count=count+1
print('the length of the digit will be',count)


# # Python code to find the factors of a given number.
# 

# In[ ]:


num=int(input('Enter your number'))
for i in range(1, num+1):
    if num%i==0:
        print(i)


# # Python program to reverse a given number.
# 

# In[ ]:


num=int(input('Enter your number'))
rev=0
while num>0:
    rem=num%10
    num=num//10
    rev=(rev*10)+rem
print(rev)


# In[ ]:


num=int(input('Enter your number'))
rev=0
while num>0:
    rem=num%10
    num=num//10
    rev=(rev*10)+rem
print(rev)


# # Python program to print pyramid

# In[ ]:


row=int(input('Enter the number of rows'))
for i in range(0,row
              ):
    for j in range(0,row-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    print()
    


# # How to print different patterns in Python using Nested Loop.

# In[ ]:


row=int(input('Enter the number of rows'))
for i in range(1,row+1):
    for j in range(0,i):
        print("*",end=" ")
    print()


# In[ ]:


row=int(input('Enter the number of rows'))
for i in range(1,row+1):
    for j in range(0,i):
        print("*", end=" ")
    print()
    
for k in range(row,0,-1):
    for l in range(0,k-1):
        print('*',end=" ")
    print()


# In[ ]:


rows=int(input('Enter the number of rows'))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print (j, end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    print()


# In[ ]:


rows=int(input('Enter the number of rows'))
num=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()


# In[ ]:


rows=int(input('Enter the number of rows'))
num=1
for i in range(0, rows):
    for j in range(0,rows-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print()


# # Python program to print the sum of a given series.

# In[ ]:


num=int(input('Enter the number'))
result=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    result=result + (i/fact)
    
print(result)


# # Python program to calculate the sum of the given series.
# series====1+x**2/2+x**3/3-----------+x**n/n

# In[ ]:


x=int(input('Enter the number'))
n=int(input('Entet nth value'))
sum=1

for i in range(2,n+1):
    sum=sum+(x**i)/i
print(sum)


# series=(x-1/x)+1/2(x-1/x)**2+1/2(x-1/x)**3-------1/2(x-1/x)**7
# 

# In[ ]:


x=int(input('Enter the number'))
n=7
sum=((x-1)/x)

for i in range(2,n+1):
    sum=sum+1/2*((x-1)/x)**i
print(sum)


# # Python program to print the sum and average of the numbers entered by the user.
# 

# In[ ]:


num=int(input('Enter your number'))
add=0
avg=0
count=0
while True:
    if num!=0:
        add=add+num
        count=count+1
        avg=add/count
        num=int(input('Enter another number'))
    else:
        print('Thank you')
        break

print('Sum of the number is:', add)
print('Average of the number is', avg)
    
    


# # Python code to find the length of a given string without using the len() function. 
# 

# In[ ]:


str=input('Enter your string')
count=0

for i in str:
    count=count+1
print('The length of the string is:', count)


# # Python program to extract username from the given email.
# 

# In[ ]:


email=input('Enter your email')
username,mail=email.split('@')
print(username)


# # Python program to find the index position of a character in another string.
# 
# 

# In[ ]:


a=input('Enter your string')
b=input('Enter your character')
print(a.index(b))


# # Python program to count number of vowels used in a given string.
# 

# In[ ]:


a=input('Enter your string')
vowels='aeiou'
count=0

for i in a:
    if i in vowels:
        count=count+1
        
print(count)


# # Python program to remove a particular character from a given string.
# 

# In[ ]:


a=input('Enter your string')
b=int(input('Enter the value of the string you wish to remove'))
c=a[0:b-1]
d=a[b:]
print(c+d)


# # Python program to check whether a given string is palindrom or not.
# 

# In[ ]:


a=input('Enter your string')
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
print(rev)
if rev==a:
    print('Palindrome')
else:
    print('Not a palindrome')


# # Python code to remove duplicate elements from a List.
# 

# In[ ]:


l1=[1,2,2,3,4,4,5,6,6,7,7]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)


# # Python program to convert a string to title case without using title() function.
# 

# In[ ]:


a=input('Enter your string')
y=a.split()
print (y)

r=''

for i in y:
    r=r+i[0].upper()+i[1:].lower()+" "
print(r)


# # Python program to print the maximum value of a given list without using the max() function.

# In[ ]:


L=[2,3,4,5,6,7,8,9]
max=L[0]
for i in L:
    if i>max:
        max=i
        
print(max)


# # Python program to reverse a given list.
# 

# In[ ]:


L=[2,3,4,5,6,7,8,9]
rev=[]

for i in range(len(L)-1,-1,-1):
      rev.append(L[i])
print(rev)


# # Python program to search a number in a given list.
# 

# In[ ]:


L=[1,2,3,4,5,6,7,8,9]
num=int(input('Enter your number'))
for i in L:
    if i==num:
        print('True')
        break
else:
    print('False')
        


# # Python code to turn every item of a list into it's square.
# 

# In[ ]:


L1=[1,2,3,4,5,6,7,8,9]
L2=[]
for i in L1:
    L2.append(i**2)
print(L2)


# # How to reverse words in a string.
# 

# In[ ]:


a=input('Enter your string')
x=a.split()
rev=[]
for i in range(len(x)-1,-1,-1):
    rev.append(x[i])
y=' '.join(rev)
print(y)


# # Python program to find number of words in a string.
# 

# In[ ]:


a=input('Enter your string ')
count=0

for i in a:
    if i==' ':
        count=count+1
num=count+1
print(num)
    


# # Python program to check whether the list is sorted or not without using sort() function.
# 

# In[ ]:


L=[1,2,3,4,5,6]
flag=0
for i in range(0,len(L)-1):
    if L[i]>=L[i+1]:
        flag=1
        break
if flag==0:
    print('Sorted')
else:
    print('Not sorted')


# # Put Even and Odd Elements of a list in two different List using Python.
# 

# In[ ]:


L=[1,2,3,4,5,6,7,8,9]
L_even=[]
L_odd=[]
for i in L:
    if i%2==0:
        L_even.append(i)
    else:
        L_odd.append(i)
        
print(L_even)
print(L_odd)


# # How to combine two list in Python without using the '+' operator.
# 

# In[ ]:


L1=[1,2,3,4,5]
L2=[6,7,8,9]
L=[]
for i in L1:
    L.append(i)
for j in L2:
    L.append(j)
    
print(L)


# # List in Python | Change item values | Replace item
# 

# In[ ]:


L=[1,2,3,4]
find=int(input('Enter the number you want to replace'))
replace=int(input('Enter the number you want to replace with'))
for i in range(0,len(L)):
    if find==L[i]:
        L[i]=replace
        print(L)
        break
else:
    print('Not found')


# # How to flatten a 2D list in Python
# 

# In[6]:


L=[1,2,3,4,[5,6,7,8]]
rev=[]
for i in L:
    if type(i)==list:
        rev.extend(i)
    else:
        rev.append(i)
        
print(rev)


# # Python program to find union and intersection of two lists.
# 

# In[9]:


L1=[1,2,3,4,5]
L2=[3,4,5,6,7,8]
union=[]
intersection=[]

#Union
for i in L1:
    if i not in union:
        union.append(i)
for j in L2:
    if j not in union:
        union.append(j)
        
#Intersection
for i in L1:
    if i in L2:
        intersection.append(i)

print(union)
print(intersection)


# # Convert Integer to String without using str()
# 

# In[12]:


def convert(number):
    digits='0123456789'
    result=''
    while number!=0:
        current_number=number%10
        result=result+digits[current_number]
        number=number//10
    return result
print(type(convert(23)))


# # Python code to print the maximum item of each row of a matrix
# 

# In[16]:


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]

for i in matrix:
    max=i[0]
    for j in i:
        if j>max:
            max=j
    print(max)


# # Python code to print the shape of the matrix. 

# In[17]:


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]
row=0
for i in matrix:
    row=row+1
    
print(row,"*", len(i))


# # Python program to check whether multiplication is possible between two given matrices.

# In[21]:


matrix_1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]
row_1=0
for i in matrix_1:
    row_1=row_1+1
    column_1=len(i)
    print('Matrix 1 is:', i)
print('Row 1 is:', row_1)
print('Column 1 is:', column_1)

matrix_2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]

row_2=0
for j in matrix_2:
    row_2=row_2+1
    column_2=len(j)
    print('Matrix 2 is:', j)
print('Row 2 is:', row_2)
print('Column 2 is:', column_2)

if column_1==row_2:
    print('Multiplication possible')
else:
    print('Not possible')


# # Python program to sort an unsorted list in Python without using Sort() function.
# 

# In[23]:


L=[4,6,8,3,7,20,10]
for i in range(len(L)):
    for k in range(0,len(L)-1):
        
        if L[k]>L[k+1]:
            temp=L[k]
            L[k]=L[k+1]
            L[k+1]=temp
            
print(L)


# 

# In[ ]:





# In[ ]:




