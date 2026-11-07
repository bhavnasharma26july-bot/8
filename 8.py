totalhomework = 4
print("You have", totalhomework, "homework tasks today!")

completedcount = 0
tasknum = 1

while tasknum <= 4:

    if tasknum == 1:
        nexttask = "Math worksheet"
    elif tasknum == 2:
        nexttask = "Draw a bird"
    elif tasknum == 3:
        nexttask = "English letter writing"
    else:
        nexttask = "GK revision"

    print("Have you finished", nexttask, "?")
    answer = input("Enter yes or no: ")

    if answer == "yes":
        print("Great job!")
        completedcount = completedcount + 1
        tasknum = tasknum + 1
    else:
        print("Finish it and try again!")

    print("Homework remaining:", 4 - completedcount)

print("ALL HOMEWORK COMPLETE!")
print("Great work!")

