# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))
for subject in subjects:
    print(subject)
# Challenge:

#print out each subject but stop when you reach "History"
for subject in subjects:
    if subject == "History":
        break
    else:
        print(subject)
#Skip science and print out the rest
for subject in subjects:
    if subject == "Science":
        continue
    print(subject)
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for index in range(len(subjects)):
    print("Subject"+ str( index)+ ": "+subjects[index])

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.

total= 0
for number in numbers:
    total += number
print("Total: " ,total)
#Adds the total and the number each time ex:0+5 then 5+10, etc
new_numbers = list(range(1,600001))
#This creates a list of numbers from 1 to 600001
#Challenge sum up all the numbers from 1 to 600001 and print the total 
new_total = 0
for x in new_numbers:
    new_total += x
print("Total: ",new_total)

new_list =list(range(5,26))
total_new = 0
for x in new_list:
    total_new += x
print("Total: ", total_new)
