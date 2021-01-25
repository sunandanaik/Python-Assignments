# 1. Write a program to find the length of a given input using a for loop Ex."Iant pyhton Goa": length=15.
str: str = "Covid19 Vaccine"
print(len(str))

# 2. Write a program to print following pattern.
for x in range(1, 3):
    for y in range(1, x + 2):
        print('#', end=' ')

# 3. Write a program to print following pattern:
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")
# 4. Can you modify the multiplication table program :

num=int(input("Enter a number:"))
for i in range(10,0,-1):
    result=num * i
    print(num,"*",i, " = ",result)

#5. can you create a program so that all items of the languages list are printed except swift and c++?
Languages=["Python", "Java", "Swift", "C", "C++"]
for l in Languages:
    if l=="swift" or l=="C++":
        continue
    else:
        print(l)

#6. Print the first 100 even numbers.
for num in range(1,100):
    if num%2==0:
        print (num)
    num=num+1

#7. print even numbers up to 100.
for num in range(1,100):
    if num%2==0:
        print (num)
    num=num+1

#8. Find average of list of numbers.
def Average(lst):
 return sum(lst) / len(lst)

lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
print("Average of the list =", round(average, 2))

#9. Find largest number of list.
list1 = [10, 20, 4, 45, 99]

list1.sort()
print("Largest element is:", list1[-1])

#10. print 20 numbers of Fibonacci series.
x, y = 0, 1

while y < 20:
    print(y)
    x, y = y, x + y

#11. Print the following pattern:
for i in range(1,6):
    for j in range(1,6):
        print(j,",",i,"|")
    print("/n")
    