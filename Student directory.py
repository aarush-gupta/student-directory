from tkinter import *

f = open("student-data.txt", "r")
# 1) Store following information'
# a) Name  - String
# b) Age  - Integer
# c) Grade - Integer
# d) Gender - single letter - M/F
# e) Hobbies  - String

# 2) Store some examples in a comma separated list in a file

# 3) Get a name from user

# 4) Match the name with what's in the file and if name matches, print all data. If not, tell username not found and if they would like to add this record

# Bugs:

# search should look up any case(Fixed)
# search should return partial results.
# Get password in a loop until a match is found(Fixed)
# run program in a loop until match is found
# Password must be entered before you can search.(Fixed)


# Checking Password


def check_password():
    # Printing PW
    password_right = password_value.get("1.0", "end-1c")
    print(password_right)
    # Checking if PW is correct
    if password_right == "PW:":
        Output.insert(END, 'PW Accepted.Enter your name in the search box below. Then click the search button')
        instruction2.pack()
        student_name_value.pack()
        student_name_value.focus()
        get_student_info_button.pack()
    else:
        Output.insert(END, ' Wrong PW. Try again.')

    """
    else:
        Output.insert(END, "Password invalid. IN YOUR FACE IF YOU ARE A HACKER! Going to auto-quit this program...")
        time.sleep(3)
        quit()
        """


# Looking for name
def get_student_info():
    # Variables
    student_name = student_name_value.get("1.0", "end-1c")

    times = int(0)
    records = f.readlines()
    # Checking for name
    for record in records:
        print(record.split(",")[0])
        print(student_name)

        for e in range(5):
            if record.split(",")[0].upper() == student_name.upper():
                Output.insert(END, "Username detected")
                times = times + 1

        if times == 0:
            Output.insert(END, "Match not Found. would you like to add the record for " + str(student_name_value) + "?")

# Getting ready...


name = "abc"
# Draw box
root = Tk()
root.geometry("300x300")
root.title(" Search ")

# Draw controls
# Labels and text
instruction = Label(text="Enter PW: ")
password_value = Text(root, height=3,
                      width=45,
                      bg="pink")
instruction2 = Label(text="Enter Name: ")
student_name_value = Text(root, height=3,
                          width=45,
                          bg="Yellow")
# Output box
Output = Text(root, height=6,
              width=45,
              bg="cyan")
# Submit button
check_password_button = Button(root, height=1,
                               width=20,
                               text="Check PW",
                               command=lambda: check_password())
get_student_info_button = Button(root, height=1,
                                 width=20,
                                 text="Search",
                                 command=lambda: get_student_info())
# Running everything
instruction.pack()
password_value.pack()
password_value.focus()

check_password_button.pack()


Output.pack()

mainloop()
