y = str(input("Enter your full name"))
x = int(input("Enter age please: "))
def a(x):
    if x >= 50:
        return "to old"
    elif x >= 20:
        print "you've met the age requirements"
        return "approved"
    else:
        return "just a lil guy."

def ap():
    full = a(x)
    if full == "approved":
        return "approved_age"
    else:
        print y, "you've been denied becauce you're,", full
        return"denied" 

if ap() == "approved_age":
    job = str(input("Please enter your occupation"))
    hobby = str(input("Please tell us what your hobbies are"))
    other = str(input("Please inform us of any other hobbies"))
    print "congraulations,", y, ", your application has been submitted!"

def admin_op():
    if ap() == "approved_age":
        print "name:", y
        print "age:", x
        print "job:", job
        print "hobby:", hobby
        print "other:", other
    else:
        print "name:", y
        print "was denied for being:", a(x)

admin_op()
