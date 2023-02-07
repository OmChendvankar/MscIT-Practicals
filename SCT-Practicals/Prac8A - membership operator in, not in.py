# Aim: write a program to find the whether there is common member in two list

# Define a function() that takes two lists
def overlapping(list1,list2):
    c = len( list1 )
    d = len( list2 )
    print( "List 1: ", list1 )
    print( "The length of List 1: ", c )
    print( "List 2: ", list2 )
    print( "The length of List 2: ", d )
    for i in range(0,c):
        for j in range(0,d):
            if(list1[i]==list2[j]):
                return 1
    return 0
#end of the function

list1=[]
list2=[]

c=int(input("Enter the number of elements that you want to insert in List 1:"))
for i in range(0,c):
    ele = int(input("Enter the element "))
    list1.append(ele)

d=int(input("Enter the number of elements that you want to insert in List 2:"))
for i in range(0,d):
    ele = int(input("Enter the element "))
    list2.append(ele)

if(overlapping(list1,list2)):
   print("The lists are overlapping")
else:
   print("The lists are not overlapping")



# Aim: Not in operator in python
list1=[]
c=int(input("Enter the number of elements that you want to insert in List 1:"))
for i in range(0,c):
    ele = int(input("Enter the element :"))
    list1.append(ele)

a = int(input("enter the number that1 you want to find in List 1:"))


if a not in list1:
    print( "The list does not contain ", a )
else:
    print( "The list contains", a )

