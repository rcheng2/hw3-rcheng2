import math
import os
from csv import reader

#Task 1
def con_vs_vow(string):
    print("Task 1: ",end =" ")
    string = string.lower()

    vow = set("aeiou")

    count_vow = 0
    count_con = 0

    for letter in string:
        if letter in vow : 
            count_vow += 1
        else:
            count_con += 1

    
    if count_vow > count_con:
        return print("True")
    elif count_con > count_vow:
        return print("False")
    else :
        return print("None")

con_vs_vow("iiiwwww")


#Task 2
print("\nTask 2: ",end =" ")
def vol(r, h):
    return print(math.pi*h*r*r)

vol(5,5)


#Task 3
print("\nTask 3: ",end =" ")
def single_string(inputs):
    
    strings = ",".join(inputs)
    print(strings)

single_string(["123123ds","asdf","casdf"])


#Task 4
print("\nTask 4: ",end =" ")
def multiple_strings(inputs):
    filename = "output.csv"
    strings = [",".join(element) for element in inputs]
    #print(strings)
    output = open(filename, "w")
    for element in strings:
        output.write(element + "\n")
    output.close()
    print(os.path.abspath(filename))
    return os.path.abspath(filename)

multiple_strings([["123123ds","asdf","casdf"], ["a","b","c"],["ka","df","asd"]])


#Task 5
print("\nTask 5: ",end =" ")
def reverse(file):
    with open(file,'r') as element:
        rows = reader(element)
        list_from_rows = list(rows)
        print(list_from_rows)

reverse(multiple_strings([["123123ds","asdf","casdf"], ["a","b","c"],["ka","df","asd"]]))


#Task 6
print("\nTask 6: ",end =" ")
def error_handling(x,y):
    try:
        print("%s divided by %s is equal to: %s" %(x,y,x//y))
    except ZeroDivisionError:
        print("You are trying to divide by 0. Try another set of numbers.")

error_handling(2,0)

#Task 7
print("\nTask 7: ",end =" ")
def no_dupes(numlist):
    nodupes=[]
    for i in numlist:
        if i not in nodupes:
            nodupes.append(i)
    return print("The array with no dupes: ", nodupes)

no_dupes([1,1,1,1,1,1,1,1,1,1])


#Task 8
print("\nTask 8: ",end =" ")
def create_folder():
   
    os.mkdir("hw3-folder")
    print("My directory's files: ", os.listdir('.'))

create_folder()