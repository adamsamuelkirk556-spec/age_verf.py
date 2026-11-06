import sys
while True:
    try:
        y = str(input("Enter your full name: "))
        x = int(input("Enter age please: "))
        break
    except ValueError:
        print ("please enter a valid age\n")
def a(x):
    if x >= 50:
        return "to old"
    elif x >= 20:
        print ("you have met the age requirements")
        return "approved"
    else:
        return "just a lil guy."

def ap():
    full = a(x)
    if full == "approved":
        return "approved_age"
    else:
        print (y, "you've been denied because you're,", full)
        return"denied"
status = ap()
if status == "approved_age":
    job = str(input("Please enter your occupation: "))
    hobby = str(input("Please enter your hobby: "))
    other = str(input("Please enter your other: "))

def admin_op(file_object):
    if status == "approved_age":
        print ("=============================================", file=file_object)
        print ("             application", file=file_object)
        print ("=============================================", file=file_object)
        print ("name:", y, file=file_object)
        print ("age: ", x, file=file_object)
        print ("job:", job, file=file_object)
        print ("hobby:", hobby, file=file_object)
        print ("other:", other, file=file_object)
        print("==============================================", file=file_object)
        print ("")
    else:
        print("==============================================", file=file_object)
        print ("             rejection notice", file=file_object)
        print ("name: ", y, file=file_object)
        print ("was denied for being:", a(x), file=file_object)
        print("age: ", x, file=file_object)
        print("==============================================", file=file_object)
while True:

        print ("1 -- existing file")
        print ("2 -- new file")
        print ("3 -- output to console")
        print ("")
        try:
            option = int(input("please choose save option: "))
        except ValueError:
            print ("")
            print ("please enter valid option\n")
            continue

        if option == 1:
            try:
                save_loc = str(input("Please enter your save location: "))
                with open(save_loc, "a") as f:
                    admin_op(f)
                break
            except FileNotFoundError:
                print ("please enter a valid save location\n")
            except IsADirectoryError:
                print ("this is a directory, please enter valid file name\n")

        elif option == 2:
            try:
                save_loc = str(input("Please enter your save location: "))
                with open(save_loc, "x") as f:
                    admin_op(f)
                break
            except FileExistsError:
                print ("file already exists\n")
            except IsADirectoryError:
                print ("this is a directory, please enter valid file name\n")
        elif option == 3:
            admin_op(sys.stdout)
            break
        else:
            print ("please enter valid option\n")
