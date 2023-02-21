import re
from Addstudent import student
from manage import manage_atd
from close import Logout
Userlist=["Anushri"]
Emaillist=["anushri12@gmail.com"]
Pswdlist=["Anu123@#"]
class Register():
    @classmethod
    def signup(self):
        print("\t\t\t\t\t\tSignup\t\t\t\t\t\t")
        Username = input("Enter Username : ")
        Email = input("Enter Email : ")
        if re.match(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[@.])",Email):
            #print("Valid Email")
            pswd=input("Enter password: ")
            if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[*@#$!%^&{}])(?=.*[0-9])",pswd):
                #print("Strong password")
                Reenter_pswd=input("Reenter Password : ")
                if(Reenter_pswd == pswd):
                    print("\t\t\t\t\tRegistration is successful\t\t\t\t\t")
                    Userlist.append(Username)
                    Emaillist.append(Email)
                    Pswdlist.append(pswd)
                    Register.login(self)
                else:
                    print("Not matched")
            else:
                print("Weak password")
        else:
            print("Invalid Email")
    def login(self):
        print("\t\t\t\t\t\tLogin\t\t\t\t\t\t")
        User_name = input("Enter Username : ")
        E_mail = input("Enter Email : ")
        password = input("Enter Password : ")
        if User_name in Userlist:
            if E_mail in Emaillist:
                if password in Pswdlist:
                    print("\t\t\t\t\tLogin successful\t\t\t\t\t")
                    print("\t\t\t\tStudents individual dashboard\t\t\t\t")
                    print("1 - Addstudent  2 - view Students details,3 - Students leave apply,4 - Logout : ")
                    try:
                        number=int(input())
                        if(number==1):
                            student.addstudent(self)
                        elif(number==2):
                            student.viewdetails(self)
                        elif(number==3):
                            manage_atd.manage(self)
                        elif(number==4):
                            Logout.logout(self)
                        else:
                            print("Enter given number")
                    except ValueError:
                        print("Enter an integer")
                else:
                    print(" Invalid Username or password")
            else:
                print("Invalid Username or password")
        else:
            print("Invalid Username or password")
    