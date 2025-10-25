import statistics
def show():
    with open("grades.txt","r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            line = line.split(",")
            print(line[0]+": "+ line[1])

def search():
    ask_name = input("Insert Name: ").strip()
    found = False
    with open("grades.txt", "r", encoding="utf-8") as g:
        for line in g:
            name, grade = line.strip().split(",")
            if name.lower() == ask_name.lower():
                print(f"{name}, Grade(%):{grade}")
                found = True
                break  # stop once we find the match
    if not found:
        print("Student not found.")

def add():
    add_amnt = int(input("How many students are you adding?"))
    for i in range(add_amnt):
        add_name = input("Insert Name: ").strip()
        add_grade = input("Insert Grade(%): ").strip()
        with open("grades.txt", "a", encoding="utf-8") as h:
            h.write(f"\n{add_name},{add_grade}")

def remove():
    target = input("Who would you like to remove: ").strip()
    with open("grades.txt", "r", encoding="utf-8") as j:
        lines = j.readlines()

    new_lines = []
    found = False
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        if name.lower() != target.lower(): #.lower makes all cahracters lowercase thus reduces the need to write perfectly
            new_lines.append(line + "\n")
        else:
            found = True
    with open("grades.txt", "w", encoding="utf-8") as k:
        k.writelines(new_lines)
    if found:
        print("")
        print(f"{target} has been removed.")
        print("")
    else:
        print(f"{target} was not found.")

def average():
    with open("grades.txt", "r", encoding="utf-8") as l:
        list = []
        for line in l:
            name, grade = line.strip().split(",")
            list.append(int(grade))

        x =statistics.mean(list)
        with open("summary.txt", "a", encoding="utf-8") as m:
            m.write(f"\nClass average: {x}")
            #still need to do time stamp but not sure on how it works
def menu():
    print("----------------------")
    print("GRADEBOOK MANAGER")
    while True:
        print("What would you like to do: ")
        choice = int(input("Display(1),Search(2),Add(3),Remove(4),Avg Grade(5): "))
        if choice == 1:
            show()
        elif choice == 2:
            search()
        elif choice == 3:
            add()
        elif choice == 4:
            remove()
        elif choice == 5:
            average()
        else:
            print("Invalid Choice")

menu()

"""
Each file mode is important as it allows for the text file to be changed differently,
 a will be used when appending to the file thus useful for adding on to it without removing what was there previously used in my add function.  
r will be used to read files and is important to look over them and look for certain characteristics in the text file used in my show or search fucntion.
w will be used to write new all while removing the text that was there previously thus making useful for modifying or deleting text thus used in my remove function.

Using context managers context managers (with open(...)) allows us to access files much more quicky and leaves less room for error.
The reason being that when open() is used if file.close() is forgotten the program will crash and make clutter unecessarily. 
Essentailly context managers automatically handle the closing of files thus facilitating us as programers.

"""