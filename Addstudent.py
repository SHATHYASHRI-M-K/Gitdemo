from close import Logout
from manage import manage_atd
Stu_ID=["191EC111","191EC112","191EC113","191EC114","191EC115"]
Stu_name=["Abi","Akash","Ajith","Dhanush","Keerthi"]
Stu_Email=["abi111@gmail.com","akash112@gmail.com","ajith113@gmail.com","dhanush114@gmail.com","Keerthi115@gmail.com"]
Stu_leave=[1,3,0,2,0]
Stu_atdpercent=[99,97,100,98,100]
class student():
    def viewdetails(self):
        Stuid=input("Student's ID : ")
        for i in range(len(Stu_ID)):
            if(Stu_ID[i]==Stuid):
                print("Student name : ",Stu_name[i])
                print("Student Email : ",Stu_Email[i])
                print("No of leaves : ",Stu_leave[i])
                print("Attendance Percent : ",Stu_atdpercent[i])
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
                        Logout.logout(self=None)
                    else:
                        print("Enter given number")
                except ValueError:
                    print("Enter an integer")
    def addstudent(self):
        Stu_ID.append(input("Student ID : "))
        Stu_name.append(input("Student name : "))
        Stu_Email.append(input("Student Email : "))
        Leave=input("No of leaves : ")
        Stu_leave.append(Leave)
        atd=str(100-(int(Leave)))
        Stu_atdpercent.append(atd)
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
                Logout.logout(self=None)
            else:
                print("Enter given number")
        except ValueError:
            print("Enter an integer")
    
    


