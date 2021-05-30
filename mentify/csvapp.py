import pandas as pd


def addNewMentor():
    m_name = input("Enter Mentor's Name: ")
    m_password = input("Enter Mentor's Password:")
    m_gender = input("Enter Mentor's Gender: ")
    m_age = input("Enter Mentor's Age: ")
    m_category = input()
    mbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Hackathon\mentor.csv")
    cnt = mbf["m_name"].count()
    mbf.at[cnt] = [m_name, m_password, m_gender, m_age, m_category]
    mbf.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentor.csv")
    mntrc = pd.read_csv(r"C:\Users\Leepa\Desktop\Hackathon\mentor.csv")
    mntrc.at[cnt] = [m_age, m_category]
    mntrc.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentorlog.csv")
    print("Mentor added successfully")
    print(mbf)


def addNewMentee():
    mn_name = input("Enter Mentee's Name: ")
    mn_password = input("Enter Mentee's Password:")
    mn_gender = input("Enter Mentee's Gender: ")
    mn_age = input("Enter Mentee's Age: ")
    mn_relationship = input()
    mn_peer = input()
    mn_career = input()
    dbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Hackathon\mentee.csv")
    cnt = dbf["mn_name"].count()
    dbf.at[cnt] = [mn_name, mn_gender, mn_age, mn_relationship, mn_peer, mn_career]
    dbf.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentee.csv")
    dntrc = pd.read_csv(r"C:\Users\Leepa\Desktop\Hackathon\mentor.csv")
    dntrc.at[cnt] = [mn_age, mn_category]
    dntrc.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentorlog.csv")
    print("Mentee added successfully")
    print(dbf)


def deleteMentee():
    mn_name = float(input("Enter the Mentor name: "))
    dbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\mentee.csv")
    dbf = dbf.drop(dbf[dbf["mn_name"] == mn_name].index)
    dbf.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentee.csv")
    print("Mentee Deleted Successfully")
    print(dbf)


def deleteMentor():
    m_name = float(input("Enter the Mentor name: "))
    mbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\mentor.csv")
    mbf = mbf.drop(mbf[mbf["m_name"] == m_name].index)
    mbf.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentor.csv")
    print("Mentor Deleted Successfully")
    print(mbf)


def showMentee():
    dbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\Mentee.csv")
    print(dbf)


def showMentor():
    mbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\Mentor.csv")
    print(mbf)


def searchMentee():
    mn_name = input("Enter the mentee name: ")
    dbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\mentee.csv")
    df = dbf.loc[dbf["mn_name"] == mn_name]
    if df.empty:
        print("No mentee found with given name")
    else:
        print("Mentee Details are: ")
        print(df)


def searchMentor():
    m_name = input("Enter the mentor name: ")
    mbf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\mentor.csv")
    mf = mbf.loc[mbf["m_name"] == m_name]
    if mf.empty:
        print("No mentor found with given name")
    else:
        print("Mentor Details are: ")
        print(mf)


def loginMentee():
    msname = input("Enter Name: ")
    if msname:
        print("Welcome ", msname)
        return True
    else:
        print("No Name Provided")


def loginMentor():
    mnsname = input("Enter Name: ")
    mnspwd = input("Enter Password: ")
    mf = pd.read_csv(r"C:\Users\Leepa\Desktop\Info Project\mentor.csv")
    mf = mf.loc[mf["mn_name"] == mnsname]
    if mf.empty:
        print("Invalid Name Provided")
        return False
    else:
        mf = mf.loc[mf["m_password"] == mnspwd]
        if mf.empty:
            print("Invalid Password provided")
            return False
        else:
            print("Name and Password verified successfully")
            return True


def MentorRate():
    m_times == 0
    m_totalrate == 0
    m_rate = int(input(
        "Please rate the mentor from a scale of 1-5, 1 being very rude/uncomfortable to 5 being very pleasant/joyful"))
    m_totalrate += m_rate
    m_times += 1
    m_finalrate = m_totalrate/m_times
    print("The average rating of this Mentor is: ", m_finalrate)
    dntrc = pd.read_csv(r"C:\Users\Leepa\Desktop\Hackathon\mentorlog.csv")
    cnt = dntrc["mn_age"].count()
    dntrc.at[cnt] = [mn_name, mn_age, mn_category, m_finalrate]
    dntrc.to_csv(r"C:\Users\Leepa\Desktop\Info Project\mentorlog.csv")


def choicemenu():
    choice = int(input("Enter your Choice: "))
    return choice


if loginMentee():
    while True:
        choice = choicemenu()
        if choice == 1:
            addNewMentor()
        elif choice == 2:
            addNewMentee()
        elif choice == 3:
            deleteMentor()
        elif choice == 4:
            deleteMentee()
        elif choice == 5:
            showMentor()
        elif choice == 6:
            showMentee()
        elif choice == 7:
            MentorRate()
        elif choice == 8:
            break
        else:
            print("Invalid Option Selected...")
print("Thank you for using the admin base of Mentify")
