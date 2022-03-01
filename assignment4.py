#Question 1
print("        Question 1")

def hanoi(n, initial, final, extra):
    if n == 0:
        return
    
    hanoi(n-1, initial, extra, final)
    print(f"Move Disk {n} from {initial} to {final}")
    hanoi(n-1, extra, final, initial)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')




#Question 2
print("        \n\n\n Question 2")
n = int(input("Enter the number of rows required in in Pascal's Triangle: "))
print("\n recursions:\n")
def triangle(n, initialn=n):
    if n == 0:
        return
    
    triangle(n-1,initialn)
    print('  '*(initialn-n), end='')
    starting = 1
    for i in range(1, n+1):

        print(starting, end ='   ')

        starting = starting * (n - i) // i
    print()
triangle(n)

print("\n loops:\n")
for y in range(1, n+1):

    print('  '*(n - y), end='')

    x = 1
    for i in range(1, y+1):

        print(x, end='   ')

        x = x * (y - i) // i
    print()




#Question 3
print("     \n\n\n Question 3")
int1, int2 = map(int,input("Enter 2 numbers: ").split())

ans = divmod(int1,int2)

print(f"The quotient is {ans[0]} and reminder is {ans[1]}")

#part a
print("a. The function to analyse quotient and reminder is a callable value.")
print(callable(divmod))

#part b
if ans[0] == 0:
    print("b. The quotient is zero")
if ans[1] == 0:
    print("b. The reminder is zero")
if ans[0] != 0 and ans[1] != 0:
    print("b. All the values are non zero")

#part c
clist = ans + (4, 5, 6)

result = []
for i in range(len(clist)):
    if clist[i] < 5:
        result.append(clist[i])
print(f"c. Filtered out numbers: {result}")

#part d
setresult = set(result)
print("d. Set:",setresult)

#part e
setfrozen = frozenset(setresult)
print("e. Immutable set:",setfrozen)

#part f
print("f. Hash value of the max value from the above set:", hash(max(setfrozen)))




#Question 4
print ("     \n\n\n Question 4")

class Student:
    def __init__(me, student, sid):
        me.name = student
        me.sid = sid
    
    def __del__(self):
        print("destroyed")

student1 = Student("Karan Nanda", 21105054)
print("created")

print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

del student1




#Question 5
print("     \n\n\n Question 5")
print(" ")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b
del employee3

print(" ")




#Question6
print("     \n\n\n Question 6")
word = input("Enter the first word: ").lower()

test_word = input("Enter a new meaningful word to test your friendship: ")
 
def count_in_dictionary(word):
    count = {}
    list_1 = list(word)
    
    n = len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count

# verifying the letters of the new word
if count_in_dictionary(word) != count_in_dictionary(test_word):
    print("The letters aren't exact,so friendship is fake!")

#shopkeeper's input to verify the word's meaning
def user_input():
    ans = input("{For the Shopkeeper}\nDoes the word makes sense?(y or n)").lower()

    if ans == 'y':
        print("The friends passed the friendship test!")
    elif ans == 'n':
        print("The word doesn't have a meaning, so friendship is fake!")
    else:
        print("ERROR, try again")
        user_input()
user_input()

