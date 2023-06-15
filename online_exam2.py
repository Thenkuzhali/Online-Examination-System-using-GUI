from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Label
from tkinter.font import BOLD
from tkinter.messagebox import askokcancel, WARNING
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from datetime import date

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()


def show_page(page):
    page.tkraise()


window.title('Login')

window.geometry("%dx%d" % (width, height))
window.title('Login')
window.iconbitmap('T:\\images\\login64.png')

background_image = ImageTk.PhotoImage(Image.open("T:\\images\\background.png"))
l = Label(image=background_image)
l.place(x=0, y=0)

# canvas = Canvas(window, background='light cyan')
# canvas.grid()
window.configure(background='light cyan')
# Heading

welcome = Label(window, text='WELCOME!!!', font=('Arial', 25, BOLD), bg='#091e40', fg='White')
welcome.place(x=150, y=350)

l1 = Label(window, text='ONLINE EXAMINATION-USING GUI', font=('Arial', 25, BOLD), bg='light cyan')
l1.place(x=700, y=100)

username_label = Label(window, text="Username:", font=('Arial', 16), bg='light cyan')
username_label.place(x=700, y=250)
password_label = Label(window, text="Password:", font=('Arial', 16), bg='light cyan')
password_label.place(x=700, y=350)

# Create and place form entry fields
username_entry = Entry(window, width=30, font='Arial 16')
username_entry.place(x=900, y=250)

bullet = "\u2022"
password_entry = Entry(window, width=30, font='Arial 16', show=bullet)
password_entry.place(x=900, y=350)


def register():
    global reg_password_entry
    global name_entry
    reg_window = Toplevel(window)
    # reg_window.configure(background='#E6E6FA')
    reg_window.geometry("%dx%d" % (width, height))
    reg_window.iconbitmap('T:\\images\\icon_new96.png')

    reg_window.title('Registration page')
    bg_image = ImageTk.PhotoImage(Image.open("T:\\images\\re_bg2.jpg"))
    reg_bg = Label(reg_window, image=bg_image)
    reg_bg.place(x=0, y=0)

    # Heading
    head = Label(reg_window, text='Exam Registration form', font=('Arial', 20, BOLD), bg='#abecc4')
    head.place(x=550, y=30)

    # name

    name_label = Label(reg_window, text='Name: ', font=('Arial', 14), bg='#c0f5bf')
    name_label.place(x=100, y=100)

    # name entry

    name_entry = Entry(reg_window, width=50, font='Arial 14')
    name_entry.place(x=500, y=100)

    # dob

    dob_label = Label(reg_window, text='DOB: ', font=('Arial', 14), bg='#c0f5bf')
    dob_label.place(x=100, y=150)

    # dob entry
    '''
    dob_entry = Entry(reg_window, width=50, font='Arial 14')
    dob_entry.place(x=500, y=150)
    '''

    # calendar
    cal = DateEntry(reg_window, width=15, background='darkblue', foreground='white', borderwidth=2,
                    date_pattern='dd-MM-yyyy', font='Arial 14')
    cal.set_date(date.today())
    cal.place(x=500, y=150)

    gender_var = IntVar()

    # gender
    gender_label = Label(reg_window, text='Gender: ', font=('Arial', 14), bg='#c0f5bf')
    gender_label.place(x=100, y=200)

    # Create and place radio buttons for gender selection
    male_radio = Radiobutton(reg_window, text="Male", value='1', font=('Arial', 14), bg='#abecc4', variable=gender_var)
    male_radio.place(x=500, y=200)
    female_radio = Radiobutton(reg_window, text="Female", value='2', font=('Arial', 14),
                               bg='#abecc4', variable=gender_var)
    female_radio.place(x=600, y=200)
    other_radio = Radiobutton(reg_window, text="Other", value='3', font=('Arial', 14),
                              bg='#abecc4', variable=gender_var)
    other_radio.place(x=700, y=200)

    # mobile number
    mob_num_label = Label(reg_window, text='Mobile number: ', font=('Arial', 14), bg='#d6fbd0')
    mob_num_label.place(x=100, y=250)

    # mob num entry
    mob_num_entry = Entry(reg_window, width=50, font='Arial 14')
    mob_num_entry.place(x=500, y=250)

    # email address
    email_address_label = Label(reg_window, text='Email Address: ', font=('Arial', 14), bg='#d6fbd0')
    email_address_label.place(x=100, y=300)

    # Email add entry
    email_entry = Entry(reg_window, width=50, font='Arial 14')
    email_entry.place(x=500, y=300)

    # department

    Label(reg_window, text="Department :",
          font=("Arial", 14), bg='#d6fbd0').place(x=100, y=350)

    # Combobox creation
    global n
    n = StringVar()
    department = ttk.Combobox(reg_window, font='Arial 14', width=27, textvariable=n)

    # Adding combobox drop down list
    department['values'] = (' Data Science',
                            ' Computer Science',
                            ' Computer Application',
                            ' Machine Learning',
                            ' Artificial Intelligence',
                            ' Computer Graphics',
                            ' Network Engineering',
                            ' Database Systems',
                            ' Operating Systems',
                            ' Software Engineering',
                            ' Information Technology',
                            ' Algorithms and Complexity')

    department.place(x=500, y=350)
    department.current()

    # password
    reg_pwd_label = Label(reg_window, text='Enter a password: ', font=('Arial', 14), bg='#d6fbd0')
    reg_pwd_label.place(x=100, y=400)

    # password entry
    reg_password_entry = Entry(reg_window, width=50, font='Arial 14', show=bullet)
    reg_password_entry.place(x=500, y=400)

    # re-enter password
    reg_re_pwd_label = Label(reg_window, text='Re-Enter password: ', font=('Arial', 14), bg='#d6fbd0')
    reg_re_pwd_label.place(x=100, y=450)

    # re-enter password entry
    reg_re_password_entry = Entry(reg_window, width=50, font='Arial 14', show=bullet)
    reg_re_password_entry.place(x=500, y=450)

    def redirect():
        pwd = reg_password_entry.get()
        confirm_pwd = reg_re_password_entry.get()
        if pwd == confirm_pwd:
            msg = messagebox.showinfo('confirmation', 'You have registered!')
            if msg:
                return lambda: show_page(window)
        else:
            alertLabel = Label(reg_window, text='*Passwords does not match*', fg='red', bg='#93e4ac')
            alertLabel.place(x=500, y=500)

    # submit

    login_redirect_button = Button(reg_window, text='Submit', width=10, borderwidth=5, font='Arial 16', bg="#007bff",
                                   command=redirect)
    login_redirect_button.place(x=700, y=600)

    reg_window.mainloop()


def instructions():
    # Create the main window
    instruction_window = Tk()
    instruction_window.title("Online Examination")
    instruction_window.config(background='#CBC3E3')
    instruction_window.geometry("%dx%d" % (width, height))
    instruction_window.iconbitmap('T:\\images\\icon_new96.png')

    # Create a label for the instructions
    instructions_label = Label(instruction_window, text="Please read the instructions before starting the exam:",
                               font=('Times new roman', 20), bg='#CBC3E3')
    instructions_label.place(x=450, y=50)

    # Create a text widget to display the instructions
    instructions_text = Text(instruction_window, height=25, width=150, font=('Times new roman', 14), borderwidth=5)
    instructions_text.insert(END, "\n\nA. General information:\n\n"
                                  "   1. The examination will comprise of Objective type Multiple Choice Questions"
                                  " (MCQs)\n"
                                  "   2. All questions are compulsory and each carries One mark.\n"
                                  "   3. The total number of questions, duration of examination,"
                                  " will be different based on the course, the detail is available on your screen.\n"
                                  "   4. The Subjects or topics covered in the exam will be as per the Syllabus.\n"
                                  "   5. There will be NO NEGATIVE MARKING for the wrong answers.\n\n\n"
                                  "The sequence of steps to be followed by each examinee for appearing in Examination "
                                  "using Online Examination Portal will be as follows:\n\n"
                                  "   a. The student’s details appear on the screen, "
                                  "which will be verified by the student.\n"
                                  "   b. The student will get Instructions to guide through the test.\n"
                                  "   c. The Time of the examination begins only "
                                  "when the ‘Start Exam’ button is pressed.\n"
                                  "   d. The student proceeds answering the questions one by one "
                                  "clicking on the small grey circle next to the chosen answer.\n"
                                  "   e. The examinee can move to Previous answered questions.\n"
                                  "   f. The answers can be changed at any time during the test and "
                                  "are saved automatically.\n"
                                  "   g. It is possible to Review the answered as well as the unanswered questions.\n"
                                  "   h. The Time remaining is shown in the Right Top Corner of the screen.\n"
                                  "   i. The system automatically shuts down when the time limit is over"
                                  " OR alternatively if examinee finishes the exam before time "
                                  "he can quit by pressing the ‘End Exam’ button.\n"
                                  "      Don’t click the “END EXAM” Button "
                                  "until the student want "
                                  "to quit from Examination.\n")
    instructions_text.place(x=85, y=120)
    instructions_text.config(state=DISABLED)

    def start_alert():
        from tkinter import font
        user = username_entry.get()
        dept = n.get()
        result = messagebox.askquestion("Alert:", "Are you sure to start the Exam?", icon=WARNING)
        if result == 'yes':
            window.destroy()
            instruction_window.destroy()
            top = Tk()
            top.geometry("%dx%d" % (width, height))
            top.title("Questions")
            top.iconbitmap('T:\\images\\icon_new96.png')

            listc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            listw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            font_head = font.Font(family="Helvetica", size=18, weight="bold")
            font = font.Font(family="Helvetica", size=18, weight="normal")

            frame1 = Frame(top, bg="yellow", width=1600, height=300)
            frame1.place(x=0, y=0)

            head_lab = Label(frame1, text="CANDIDATE DETAILS", font=font_head, fg="black", bg="yellow")
            head_lab.place(x=700, y=10)

            name_lab = Label(frame1, text="NAME:", font=font_head, bg="yellow")
            name_lab.place(x=100, y=100)

            entered_name = Label(frame1, text=user.upper(), font=font_head, bg="yellow")
            entered_name.place(x=200, y=100)

            dep_lab = Label(frame1, text="DEPT:", font=font_head, bg="yellow")
            dep_lab.place(x=100, y=200)

            entered_dept = Label(frame1, text=dept.upper(), font=font_head, bg="yellow")
            entered_dept.place(x=200, y=200)

            time_lab = Label(frame1, text="TIME:", font=font_head, bg="yellow")
            time_lab.place(x=1150, y=200)

            timer_label = Label(frame1, text="05:00", font=font_head, bg="yellow")
            timer_label.place(x=1225, y=200)

            def update_timer(Minutes, Seconds):
                timer_label.config(text=f"{Minutes:02d}:{Seconds:02d}")
                if Minutes == 0 and Seconds == 0:
                    clear_frame(top)
                    succ = Label(top, text="You have successfully submitted the exam!", font=font_head, fg="red",
                                 bg="yellow")
                    succ.place(x=500, y=100)
                    corr = Label(top, text="Correctly answered:", font='Helvetica 24 bold', fg="black")
                    corr.place(x=500, y=300)
                    cor_ans = Label(top, font='Helvetica 24 bold', fg="green")
                    cor_ans.place(x=850, y=300)
                    wron = Label(top, text="Wrongly answered:", font='Helvetica 24 bold', fg="black")
                    wron.place(x=500, y=400)
                    wro_ans = Label(top, font='Helvetica 24 bold', fg="red")
                    wro_ans.place(x=850, y=400)
                    c_val = sum(listc)
                    w_val = sum(listw)
                    cor_ans['text'] = c_val
                    wro_ans['text'] = w_val
                    return
                elif Seconds == 0:
                    Minutes -= 1
                    Seconds = 59
                else:
                    Seconds -= 1

                top.after(1000, update_timer, Minutes, Seconds)

            minutes = 5
            seconds = 0
            update_timer(minutes, seconds)

            frame2 = Frame(top, bg="Pink", width=500, height=500)
            frame2.place(x=0, y=300)

            head2_lab = Label(frame2, text="QUESTION PALETTE", font=font_head, fg="black", bg="pink")
            head2_lab.place(x=120, y=10)

            frame3 = Frame(top, bg="blue", width=1100, height=500)
            frame3.place(x=500, y=300)

            def end():
                answer = askokcancel(title='Confirmation', message='Are you sure to end this test?', icon=WARNING)
                if answer:
                    clear_frame(top)
                    succ = Label(top, text="You have successfully submitted the exam!", font=font_head, fg="red",
                                 bg="yellow")
                    succ.place(x=500, y=100)
                    corr = Label(top, text="Correctly answered:", font='Helvetica 24 bold', fg="black")
                    corr.place(x=500, y=300)
                    cor_ans = Label(top, font='Helvetica 24 bold', fg="green")
                    cor_ans.place(x=850, y=300)
                    wron = Label(top, text="Wrongly answered:", font='Helvetica 24 bold', fg="black")
                    wron.place(x=500, y=400)
                    wro_ans = Label(top, font='Helvetica 24 bold', fg="red")
                    wro_ans.place(x=850, y=400)
                    c_val = sum(listc)
                    w_val = sum(listw)
                    cor_ans['text'] = c_val
                    wro_ans['text'] = w_val

            def clear_frame(frame):
                for widget in frame.winfo_children():
                    widget.destroy()

            def que1():
                def correct1():
                    a = radio1.get()
                    if a == 4:
                        listc[0] = 1
                        listw[0] = 0
                    elif a == 1 or a == 2 or a == 3:
                        listc[0] = 0
                        listw[0] = 1

                def clear():
                    opt1a.deselect()
                    opt1b.deselect()
                    opt1c.deselect()
                    opt1d.deselect()

                clear_frame(frame3)
                radio1 = IntVar()
                qno1 = Label(frame3, text="QUESTION NO: 1", font=font_head, fg='black', bg="blue")
                qno1.place(x=50, y=30)
                ques1 = Label(frame3, text="In which year was the Python language developed?", font=font_head,
                              fg="black", bg="blue")
                ques1.place(x=50, y=80)
                opt1a = Radiobutton(frame3, text="1995", variable=radio1, value=1, command=correct1, font=font_head,
                                    bg="blue")
                opt1a.place(x=100, y=150)
                opt1b = Radiobutton(frame3, text="1972", variable=radio1, value=2, command=correct1, font=font_head,
                                    bg="blue")
                opt1b.place(x=100, y=200)
                opt1c = Radiobutton(frame3, text="1981", variable=radio1, value=3, command=correct1, font=font_head,
                                    bg="blue")
                opt1c.place(x=100, y=250)
                opt1d = Radiobutton(frame3, text="1989", variable=radio1, value=4, command=correct1, font=font_head,
                                    bg="blue")
                opt1d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)

                btn1.config(bg='green')

            btn1 = Button(frame2, text="1", command=que1, font='Helvetica 14')
            btn1.place(x=70, y=100, height=70, width=70)

            def que2():
                def correct2():
                    a = radio2.get()
                    if a == 2:
                        listc[1] = 1
                        listw[1] = 0
                    elif a == 1 or a == 3 or a == 4:
                        listc[1] = 0
                        listw[1] = 1

                def clear():
                    opt2a.deselect()
                    opt2b.deselect()
                    opt2c.deselect()
                    opt2d.deselect()

                clear_frame(frame3)
                radio2 = IntVar()
                qno2 = Label(frame3, text="QUESTION NO: 2", font=font_head, fg='black', bg="blue")
                qno2.place(x=50, y=30)
                ques2 = Label(frame3, text="Who developed the Python language?", font=font_head, fg="black", bg="blue")
                ques2.place(x=50, y=80)
                opt2a = Radiobutton(frame3, text="Zim Den", variable=radio2, value=1, command=correct2, font=font_head,
                                    bg="blue")
                opt2a.place(x=100, y=150)
                opt2b = Radiobutton(frame3, text="Guido van Rossum", variable=radio2, value=2, command=correct2,
                                    font=font_head, bg="blue")
                opt2b.place(x=100, y=200)
                opt2c = Radiobutton(frame3, text="Niene Stom", variable=radio2, value=3, command=correct2,
                                    font=font_head, bg="blue")
                opt2c.place(x=100, y=250)
                opt2d = Radiobutton(frame3, text="Wick van Rossum", variable=radio2, value=4, command=correct2,
                                    font=font_head, bg="blue")
                opt2d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn2.config(bg='green')

            btn2 = Button(frame2, text="2", command=que2, font='Helvetica 14')
            btn2.place(x=140, y=100, height=70, width=70)

            def que3():
                def correct3():
                    a = radio3.get()
                    if a == 4:
                        listc[2] = 1
                        listw[2] = 0
                    elif a == 1 or a == 2 or a == 3:
                        listc[2] = 0
                        listw[2] = 1

                def clear():
                    opt3a.deselect()
                    opt3b.deselect()
                    opt3c.deselect()
                    opt3d.deselect()

                clear_frame(frame3)
                radio3 = IntVar()
                qno3 = Label(frame3, text="QUESTION NO: 3", font=font_head, fg='black', bg="blue")
                qno3.place(x=50, y=30)
                ques3 = Label(frame3, text="What is the maximum possible length of an identifier in python?",
                              font=font_head, fg="black", bg="blue")
                ques3.place(x=50, y=80)
                opt3a = Radiobutton(frame3, text="16", variable=radio3, value=1, command=correct3, font=font_head,
                                    bg="blue")
                opt3a.place(x=100, y=150)
                opt3b = Radiobutton(frame3, text="32", variable=radio3, value=2, command=correct3, font=font_head,
                                    bg="blue")
                opt3b.place(x=100, y=200)
                opt3c = Radiobutton(frame3, text="64", variable=radio3, value=3, command=correct3, font=font_head,
                                    bg="blue")
                opt3c.place(x=100, y=250)
                opt3d = Radiobutton(frame3, text="None of the above", variable=radio3, value=4, command=correct3,
                                    font=font_head, bg="blue")
                opt3d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn3.config(bg='green')

            btn3 = Button(frame2, text="3", command=que3, font='Helvetica 14')
            btn3.place(x=210, y=100, height=70, width=70)

            def que4():
                def correct4():
                    a = radio4.get()
                    if a == 3:
                        listc[3] = 1
                        listw[3] = 0
                    elif a == 1 or a == 2 or a == 4:
                        listc[3] = 0
                        listw[3] = 1

                def clear():
                    opt4a.deselect()
                    opt4b.deselect()
                    opt4c.deselect()
                    opt4d.deselect()

                clear_frame(frame3)
                radio4 = IntVar()
                qno4 = Label(frame3, text="QUESTION NO: 4", font=font_head, fg="black", bg="blue")
                qno4.place(x=50, y=30)
                ques4 = Label(frame3, text="In which language is Python written?", font=font_head, fg="black",
                              bg="blue")
                ques4.place(x=50, y=80)
                opt4a = Radiobutton(frame3, text="English", variable=radio4, value=1, command=correct4, font=font_head,
                                    bg="blue")
                opt4a.place(x=100, y=150)
                opt4b = Radiobutton(frame3, text="PHP", variable=radio4, value=2, command=correct4, font=font_head,
                                    bg="blue")
                opt4b.place(x=100, y=200)
                opt4c = Radiobutton(frame3, text="C", variable=radio4, value=3, command=correct4, font=font_head,
                                    bg="blue")
                opt4c.place(x=100, y=250)
                opt4d = Radiobutton(frame3, text="All of the above", variable=radio4, value=4, command=correct4,
                                    font=font_head, bg="blue")
                opt4d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn4.config(bg='green')

            btn4 = Button(frame2, text="4", command=que4, font='Helvetica 14')
            btn4.place(x=280, y=100, height=70, width=70)

            def que5():
                def correct5():
                    a = radio5.get()
                    if a == 1:
                        listc[4] = 1
                        listw[4] = 0
                    elif a == 2 or a == 3 or a == 4:
                        listc[4] = 0
                        listw[4] = 1

                def clear():
                    opt5a.deselect()
                    opt5b.deselect()
                    opt5c.deselect()
                    opt5d.deselect()

                clear_frame(frame3)
                radio5 = IntVar()
                qno5 = Label(frame3, text="QUESTION NO: 5", font=font_head, fg='black', bg="blue")
                qno5.place(x=50, y=30)
                ques5 = Label(frame3, text="Which one of the following is the correct extension of the Python file?",
                              font=font_head, fg="black", bg="blue")
                ques5.place(x=50, y=80)
                opt5a = Radiobutton(frame3, text=".py", variable=radio5, value=1, command=correct5, font=font_head,
                                    bg="blue")
                opt5a.place(x=100, y=150)
                opt5b = Radiobutton(frame3, text=".python", variable=radio5, value=2, command=correct5, font=font_head,
                                    bg="blue")
                opt5b.place(x=100, y=200)
                opt5c = Radiobutton(frame3, text=".p", variable=radio5, value=3, command=correct5, font=font_head,
                                    bg="blue")
                opt5c.place(x=100, y=250)
                opt5d = Radiobutton(frame3, text="None of these", variable=radio5, value=4, command=correct5,
                                    font=font_head, bg="blue")
                opt5d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn5.config(bg='green')

            btn5 = Button(frame2, text="5", command=que5, font='Helvetica 14')
            btn5.place(x=350, y=100, height=70, width=70)

            def que6():
                def correct6():
                    a = radio6.get()
                    if a == 3:
                        listc[5] = 1
                        listw[5] = 0
                    elif a == 1 or a == 2 or a == 4:
                        listc[5] = 0
                        listw[5] = 1

                def clear():
                    opt6a.deselect()
                    opt6b.deselect()
                    opt6c.deselect()
                    opt6d.deselect()

                clear_frame(frame3)
                radio6 = IntVar()
                qno6 = Label(frame3, text="QUESTION NO: 6", font=font_head, fg="black", bg="blue")
                qno6.place(x=50, y=30)
                ques6 = Label(frame3, text="What do we use to define a block of code in Python language?",
                              font=font_head, fg="black", bg="blue")
                ques6.place(x=50, y=80)
                opt6a = Radiobutton(frame3, text="Key", variable=radio6, value=1, command=correct6, font=font_head,
                                    bg="blue")
                opt6a.place(x=100, y=150)
                opt6b = Radiobutton(frame3, text="Brackets", variable=radio6, value=2, command=correct6, font=font_head,
                                    bg="blue")
                opt6b.place(x=100, y=200)
                opt6c = Radiobutton(frame3, text="Indentation", variable=radio6, value=3, command=correct6,
                                    font=font_head, bg="blue")
                opt6c.place(x=100, y=250)
                opt6d = Radiobutton(frame3, text="None of these", variable=radio6, value=4, command=correct6,
                                    font=font_head, bg="blue")
                opt6d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn6.config(bg='green')

            btn6 = Button(frame2, text="6", command=que6, font='Helvetica 14')
            btn6.place(x=70, y=170, height=70, width=70)

            def que7():
                def correct7():
                    a = radio7.get()
                    if a == 3:
                        listc[6] = 1
                        listw[6] = 0
                    elif a == 1 or a == 2 or a == 4:
                        listc[6] = 0
                        listw[6] = 1

                def clear():
                    opt7a.deselect()
                    opt7b.deselect()
                    opt7c.deselect()
                    opt7d.deselect()

                clear_frame(frame3)
                radio7 = IntVar()
                qno7 = Label(frame3, text="QUESTION NO: 7", font=font_head, fg="black", bg="blue")
                qno7.place(x=50, y=30)
                ques7 = Label(frame3, text="Which character is used in Python to make a single line comment?",
                              font=font_head, fg="black", bg="blue")
                ques7.place(x=50, y=80)
                opt7a = Radiobutton(frame3, text="/", variable=radio7, value=1, command=correct7, font=font_head,
                                    bg="blue")
                opt7a.place(x=100, y=150)
                opt7b = Radiobutton(frame3, text="//", variable=radio7, value=2, command=correct7, font=font_head,
                                    bg="blue")
                opt7b.place(x=100, y=200)
                opt7c = Radiobutton(frame3, text="#", variable=radio7, value=3, command=correct7, font=font_head,
                                    bg="blue")
                opt7c.place(x=100, y=250)
                opt7d = Radiobutton(frame3, text="!", variable=radio7, value=4, command=correct7, font=font_head,
                                    bg="blue")
                opt7d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn7.config(bg='green')

            btn7 = Button(frame2, text="7", command=que7, font='Helvetica 14')
            btn7.place(x=140, y=170, height=70, width=70)

            def que8():
                def correct8():
                    a = radio8.get()
                    if a == 2:
                        listc[7] = 1
                        listw[7] = 0
                    elif a == 1 or a == 3 or a == 4:
                        listc[7] = 0
                        listw[7] = 1

                def clear():
                    opt8a.deselect()
                    opt8b.deselect()
                    opt8c.deselect()
                    opt8d.deselect()

                clear_frame(frame3)
                radio8 = IntVar()
                qno8 = Label(frame3, text="QUESTION NO: 8", font=font_head, fg="black", bg="blue")
                qno8.place(x=50, y=30)
                ques8 = Label(frame3, text="Which of the following statements is correct regarding the object-oriented",
                              font=font_head, fg="black", bg="blue")
                ques8.place(x=50, y=80)
                ques8 = Label(frame3, text="programming concept in Python?", font=font_head, fg="black", bg="blue")
                ques8.place(x=50, y=110)
                opt8a = Radiobutton(frame3, text="Classes are real-world entities while objects are not real",
                                    variable=radio8, value=1, command=correct8, font=font_head, bg="blue")
                opt8a.place(x=100, y=150)
                opt8b = Radiobutton(frame3, text="Objects are real-world entities while classes are not real",
                                    variable=radio8, value=2, command=correct8, font=font_head, bg="blue")
                opt8b.place(x=100, y=200)
                opt8c = Radiobutton(frame3, text="Both objects and classes are real-world entities", variable=radio8,
                                    value=3, command=correct8, font=font_head, bg="blue")
                opt8c.place(x=100, y=250)
                opt8d = Radiobutton(frame3, text="All of the above", variable=radio8, value=4, command=correct8,
                                    font=font_head, bg="blue")
                opt8d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn8.config(bg='green')

            btn8 = Button(frame2, text="8", command=que8, font='Helvetica 14')
            btn8.place(x=210, y=170, height=70, width=70)

            def que9():
                def correct9():
                    a = radio9.get()
                    if a == 4:
                        listc[8] = 1
                        listw[8] = 0
                    elif a == 1 or a == 2 or a == 3:
                        listc[8] = 0
                        listw[8] = 1

                def clear():
                    opt9a.deselect()
                    opt9b.deselect()
                    opt9c.deselect()
                    opt9d.deselect()

                clear_frame(frame3)
                radio9 = IntVar()
                qno9 = Label(frame3, text="QUESTION NO: 9", font=font_head, fg="black", bg="blue")
                qno9.place(x=50, y=30)
                ques9 = Label(frame3, text="What is the method inside the class in python language?", font=font_head,
                              fg="black", bg="blue")
                ques9.place(x=50, y=80)
                opt9a = Radiobutton(frame3, text="Object", variable=radio9, value=1, command=correct9, font=font_head,
                                    bg="blue")
                opt9a.place(x=100, y=150)
                opt9b = Radiobutton(frame3, text="Attribute", variable=radio9, value=2, command=correct9,
                                    font=font_head, bg="blue")
                opt9b.place(x=100, y=200)
                opt9c = Radiobutton(frame3, text="Argument", variable=radio9, value=3, command=correct9, font=font_head,
                                    bg="blue")
                opt9c.place(x=100, y=250)
                opt9d = Radiobutton(frame3, text="Function", variable=radio9, value=4, command=correct9, font=font_head,
                                    bg="blue")
                opt9d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn9.config(bg='green')

            btn9 = Button(frame2, text="9", command=que9, font='Helvetica 14')
            btn9.place(x=280, y=170, height=70, width=70)

            def que10():
                def correct10():
                    a = radio10.get()
                    if a == 1:
                        listc[9] = 1
                        listw[9] = 0
                    elif a == 2 or a == 3 or a == 4:
                        listc[9] = 0
                        listw[9] = 1

                def clear():
                    opt10a.deselect()
                    opt10b.deselect()
                    opt10c.deselect()
                    opt10d.deselect()

                clear_frame(frame3)
                radio10 = IntVar()
                qno10 = Label(frame3, text="QUESTION NO: 10", font=font_head, fg="black", bg="blue")
                qno10.place(x=50, y=30)
                ques10 = Label(frame3, text="In which year was the Python 3.0 version developed?", font=font_head,
                               fg="black", bg="blue")
                ques10.place(x=50, y=80)
                opt10a = Radiobutton(frame3, text="2008", variable=radio10, value=1, command=correct10, font=font_head,
                                     bg="blue")
                opt10a.place(x=100, y=150)
                opt10b = Radiobutton(frame3, text="2000", variable=radio10, value=2, command=correct10, font=font_head,
                                     bg="blue")
                opt10b.place(x=100, y=200)
                opt10c = Radiobutton(frame3, text="2010", variable=radio10, value=3, command=correct10, font=font_head,
                                     bg="blue")
                opt10c.place(x=100, y=250)
                opt10d = Radiobutton(frame3, text="2005", variable=radio10, value=4, command=correct10, font=font_head,
                                     bg="blue")
                opt10d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn10.config(bg='green')

            btn10 = Button(frame2, text="10", command=que10, font='Helvetica 14')
            btn10.place(x=350, y=170, height=70, width=70)

            def que11():
                def correct11():
                    a = radio11.get()
                    if a == 4:
                        listc[10] = 1
                        listw[10] = 0
                    elif a == 1 or a == 2 or a == 3:
                        listc[10] = 0
                        listw[10] = 1

                def clear():
                    opt11a.deselect()
                    opt11b.deselect()
                    opt11c.deselect()
                    opt11d.deselect()

                clear_frame(frame3)
                radio11 = IntVar()
                qno11 = Label(frame3, text="QUESTION NO: 11", font=font_head, fg="black", bg="blue")
                qno11.place(x=50, y=30)
                ques11 = Label(frame3, text="Which of the following declarations is incorrect?", font=font_head,
                               fg="black", bg="blue")
                ques11.place(x=50, y=80)
                opt11a = Radiobutton(frame3, text="_x = 2", variable=radio11, value=1, command=correct11,
                                     font=font_head, bg="blue")
                opt11a.place(x=100, y=150)
                opt11b = Radiobutton(frame3, text="__x = 3", variable=radio11, value=2, command=correct11,
                                     font=font_head, bg="blue")
                opt11b.place(x=100, y=200)
                opt11c = Radiobutton(frame3, text="__xyz__ = 5", variable=radio11, value=3, command=correct11,
                                     font=font_head, bg="blue")
                opt11c.place(x=100, y=250)
                opt11d = Radiobutton(frame3, text="None of these", variable=radio11, value=4, command=correct11,
                                     font=font_head, bg="blue")
                opt11d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn11.config(bg='green')

            btn11 = Button(frame2, text="11", command=que11, font='Helvetica 14')
            btn11.place(x=70, y=240, height=70, width=70)

            def que12():
                def correct12():
                    a = radio12.get()
                    if a == 1:
                        listc[11] = 1
                        listw[11] = 0
                    elif a == 2 or a == 3 or a == 4:
                        listc[11] = 0
                        listw[11] = 1

                def clear():
                    opt12a.deselect()
                    opt12b.deselect()
                    opt12c.deselect()
                    opt12d.deselect()

                clear_frame(frame3)
                radio12 = IntVar()
                qno12 = Label(frame3, text="QUESTION NO: 12", font=font_head, fg="black", bg="blue")
                qno12.place(x=50, y=30)
                ques12 = Label(frame3, text="Which of the following is not a keyword in Python language?",
                               font=font_head, fg="black", bg="blue")
                ques12.place(x=50, y=80)
                opt12a = Radiobutton(frame3, text="val", variable=radio12, value=1, command=correct12, font=font_head,
                                     bg="blue")
                opt12a.place(x=100, y=150)
                opt12b = Radiobutton(frame3, text="raise", variable=radio12, value=2, command=correct12, font=font_head,
                                     bg="blue")
                opt12b.place(x=100, y=200)
                opt12c = Radiobutton(frame3, text="try", variable=radio12, value=3, command=correct12, font=font_head,
                                     bg="blue")
                opt12c.place(x=100, y=250)
                opt12d = Radiobutton(frame3, text="with", variable=radio12, value=4, command=correct12, font=font_head,
                                     bg="blue")
                opt12d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn12.config(bg='green')

            btn12 = Button(frame2, text="12", command=que12, font='Helvetica 14')
            btn12.place(x=140, y=240, height=70, width=70)

            def que13():
                def correct13():
                    a = radio13.get()
                    if a == 3:
                        listc[12] = 1
                        listw[12] = 0
                    elif a == 1 or a == 2 or a == 4:
                        listc[12] = 0
                        listw[12] = 1

                def clear():
                    opt13a.deselect()
                    opt13b.deselect()
                    opt13c.deselect()
                    opt13d.deselect()

                clear_frame(frame3)
                radio13 = IntVar()
                qno13 = Label(frame3, text="QUESTION NO: 13", font=font_head, fg="black", bg="blue")
                qno13.place(x=50, y=30)
                ques13 = Label(frame3,
                               text="Why does the name of local variables start with an underscore discouraged?",
                               font=font_head, fg="black", bg="blue")
                ques13.place(x=50, y=80)
                opt13a = Radiobutton(frame3, text="To identify the variable", variable=radio13, value=1,
                                     command=correct13, font=font_head, bg="blue")
                opt13a.place(x=100, y=150)
                opt13b = Radiobutton(frame3, text="It confuses the interpreter", variable=radio13, value=2,
                                     command=correct13, font=font_head, bg="blue")
                opt13b.place(x=100, y=200)
                opt13c = Radiobutton(frame3, text="It indicates a private variable of a class", variable=radio13,
                                     value=3, command=correct13, font=font_head, bg="blue")
                opt13c.place(x=100, y=250)
                opt13d = Radiobutton(frame3, text="None of these", variable=radio13, value=4, command=correct13,
                                     font=font_head, bg="blue")
                opt13d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn13.config(bg='green')

            btn13 = Button(frame2, text="13", command=que13, font='Helvetica 14')
            btn13.place(x=210, y=240, height=70, width=70)

            def que14():
                def correct14():
                    a = radio14.get()
                    if a == 2:
                        listc[13] = 1
                        listw[13] = 0
                    elif a == 1 or a == 3 or a == 4:
                        listc[13] = 0
                        listw[13] = 1

                def clear():
                    opt14a.deselect()
                    opt14b.deselect()
                    opt14c.deselect()
                    opt14d.deselect()

                clear_frame(frame3)
                radio14 = IntVar()
                qno14 = Label(frame3, text="QUESTION NO: 14", font=font_head, fg="black", bg="blue")
                qno14.place(x=50, y=30)
                ques14 = Label(frame3,
                               text="Which of the following statements is correct for variable names in "
                                    "Python language?",
                               font=font_head, fg="black", bg="blue")
                ques14.place(x=50, y=80)
                opt14a = Radiobutton(frame3, text="All variable names must begin with an underscore.", variable=radio14,
                                     value=1, command=correct14, font=font_head, bg="blue")
                opt14a.place(x=100, y=150)
                opt14b = Radiobutton(frame3, text="Unlimited length", variable=radio14, value=2, command=correct14,
                                     font=font_head, bg="blue")
                opt14b.place(x=100, y=200)
                opt14c = Radiobutton(frame3, text="The variable name length is a maximum of 2", variable=radio14,
                                     value=3, command=correct14, font=font_head, bg="blue")
                opt14c.place(x=100, y=250)
                opt14d = Radiobutton(frame3, text="All of the above", variable=radio14, value=4, command=correct14,
                                     font=font_head, bg="blue")
                opt14d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn14.config(bg='green')

            btn14 = Button(frame2, text="14", command=que14, font='Helvetica 14')
            btn14.place(x=280, y=240, height=70, width=70)

            def que15():
                def correct15():
                    a = radio15.get()
                    if a == 2:
                        listc[14] = 1
                        listw[14] = 0
                    elif a == 1 or a == 3 or a == 4:
                        listc[14] = 0
                        listw[14] = 1

                def clear():
                    opt15a.deselect()
                    opt15b.deselect()
                    opt15c.deselect()
                    opt15d.deselect()

                clear_frame(frame3)
                radio15 = IntVar()
                qno15 = Label(frame3, text="QUESTION NO: 15", font=font_head, fg="black", bg="blue")
                qno15.place(x=50, y=30)
                ques15 = Label(frame3, text="Which of the following operators is the correct option for power(ab)?",
                               font=font_head, fg="black", bg="blue")
                ques15.place(x=50, y=80)
                opt15a = Radiobutton(frame3, text="a^b", variable=radio15, value=1, command=correct15, font=font_head,
                                     bg="blue")
                opt15a.place(x=100, y=150)
                opt15b = Radiobutton(frame3, text="a**b", variable=radio15, value=2, command=correct15, font=font_head,
                                     bg="blue")
                opt15b.place(x=100, y=200)
                opt15c = Radiobutton(frame3, text="a^^b", variable=radio15, value=3, command=correct15, font=font_head,
                                     bg="blue")
                opt15c.place(x=100, y=250)
                opt15d = Radiobutton(frame3, text="a^*b", variable=radio15, value=4, command=correct15, font=font_head,
                                     bg="blue")
                opt15d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn15.config(bg='green')

            btn15 = Button(frame2, text="15", command=que15, font='Helvetica 14')
            btn15.place(x=350, y=240, height=70, width=70)

            def que16():
                def correct16():
                    a = radio16.get()
                    if a == 1:
                        listc[15] = 1
                        listw[15] = 0
                    elif a == 2 or a == 3 or a == 4:
                        listc[15] = 0
                        listw[15] = 1

                def clear():
                    opt16a.deselect()
                    opt16b.deselect()
                    opt16c.deselect()
                    opt16d.deselect()

                clear_frame(frame3)
                radio16 = IntVar()
                qno16 = Label(frame3, text="QUESTION NO: 16", font=font_head, fg="black", bg="blue")
                qno16.place(x=50, y=30)
                ques16 = Label(frame3, text="Which of the following precedence order is correct in Python?",
                               font=font_head, fg="black", bg="blue")
                ques16.place(x=50, y=80)
                opt16a = Radiobutton(frame3,
                                     text="Parentheses, Exponential, Multiplication, Division, Addition, Subtraction",
                                     variable=radio16, value=1, command=correct16, font=font_head, bg="blue")
                opt16a.place(x=100, y=150)
                opt16b = Radiobutton(frame3,
                                     text="Multiplication, Division, Addition, Subtraction, Parentheses, Exponential",
                                     variable=radio16, value=2, command=correct16, font=font_head, bg="blue")
                opt16b.place(x=100, y=200)
                opt16c = Radiobutton(frame3,
                                     text="Division, Multiplication, Addition, Subtraction, Parentheses, Exponential",
                                     variable=radio16, value=3, command=correct16, font=font_head, bg="blue")
                opt16c.place(x=100, y=250)
                opt16d = Radiobutton(frame3,
                                     text="Exponential, Parentheses, Multiplication, Division, Addition, Subtraction",
                                     variable=radio16, value=4, command=correct16, font=font_head, bg="blue")
                opt16d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn16.config(bg='green')

            btn16 = Button(frame2, text="16", command=que16, font='Helvetica 14')
            btn16.place(x=70, y=310, height=70, width=70)

            def que17():
                def correct17():
                    a = radio17.get()
                    if a == 4:
                        listc[16] = 1
                        listw[16] = 0
                    elif a == 1 or a == 2 or a == 3:
                        listc[16] = 0
                        listw[16] = 1

                def clear():
                    opt17a.deselect()
                    opt17b.deselect()
                    opt17c.deselect()
                    opt17d.deselect()

                clear_frame(frame3)
                radio17 = IntVar()
                qno17 = Label(frame3, text="QUESTION NO: 17", font=font_head, fg="black", bg="blue")
                qno17.place(x=50, y=30)
                ques17 = Label(frame3, text="What will be the output of this function: round(4.576)?", font=font_head,
                               fg="black", bg="blue")
                ques17.place(x=50, y=80)
                opt17a = Radiobutton(frame3, text="4", variable=radio17, value=1, command=correct17, font=font_head,
                                     bg="blue")
                opt17a.place(x=100, y=150)
                opt17b = Radiobutton(frame3, text="4.5", variable=radio17, value=2, command=correct17, font=font_head,
                                     bg="blue")
                opt17b.place(x=100, y=200)
                opt17c = Radiobutton(frame3, text="576", variable=radio17, value=3, command=correct17, font=font_head,
                                     bg="blue")
                opt17c.place(x=100, y=250)
                opt17d = Radiobutton(frame3, text="5", variable=radio17, value=4, command=correct17, font=font_head,
                                     bg="blue")
                opt17d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn17.config(bg='green')

            btn17 = Button(frame2, text="17", command=que17, font='Helvetica 14')
            btn17.place(x=140, y=310, height=70, width=70)

            def que18():
                def correct18():
                    a = radio18.get()
                    if a == 3:
                        listc[17] = 1
                        listw[17] = 0
                    elif a == 1 or a == 2 or a == 4:
                        listc[17] = 0
                        listw[17] = 1

                def clear():
                    opt18a.deselect()
                    opt18b.deselect()
                    opt18c.deselect()
                    opt18d.deselect()

                clear_frame(frame3)
                radio18 = IntVar()
                qno18 = Label(frame3, text="QUESTION NO: 18", font=font_head, fg="black", bg="blue")
                qno18.place(x=50, y=30)
                ques18 = Label(frame3,
                               text="Which of the following is correctly evaluated for this function: pow(x,y,z)?",
                               font=font_head, fg="black", bg="blue")
                ques18.place(x=50, y=80)
                opt18a = Radiobutton(frame3, text="(x**y) / z", variable=radio18, value=1, command=correct18,
                                     font=font_head, bg="blue")
                opt18a.place(x=100, y=150)
                opt18b = Radiobutton(frame3, text="(x / y) * z", variable=radio18, value=2, command=correct18,
                                     font=font_head, bg="blue")
                opt18b.place(x=100, y=200)
                opt18c = Radiobutton(frame3, text="(x**y) % z", variable=radio18, value=3, command=correct18,
                                     font=font_head, bg="blue")
                opt18c.place(x=100, y=250)
                opt18d = Radiobutton(frame3, text="(x / y) / z", variable=radio18, value=4, command=correct18,
                                     font=font_head, bg="blue")
                opt18d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn18.config(bg='green')

            btn18 = Button(frame2, text="18", command=que18, font='Helvetica 14')
            btn18.place(x=210, y=310, height=70, width=70)

            def que19():
                def correct19():
                    a = radio19.get()
                    if a == 1:
                        listc[18] = 1
                        listw[18] = 0
                    elif a == 2 or a == 3 or a == 4:
                        listc[18] = 0
                        listw[18] = 1

                def clear():
                    opt19a.deselect()
                    opt19b.deselect()
                    opt19c.deselect()
                    opt19d.deselect()

                clear_frame(frame3)
                radio19 = IntVar()
                qno19 = Label(frame3, text="QUESTION NO: 19", font=font_head, fg="black", bg="blue")
                qno19.place(x=50, y=30)
                ques19 = Label(frame3, text="What will be the output of this function: all([2,4,0,6])?", font=font_head,
                               fg="black", bg="blue")
                ques19.place(x=50, y=80)
                opt19a = Radiobutton(frame3, text="False", variable=radio19, value=1, command=correct19, font=font_head,
                                     bg="blue")
                opt19a.place(x=100, y=150)
                opt19b = Radiobutton(frame3, text="True", variable=radio19, value=2, command=correct19, font=font_head,
                                     bg="blue")
                opt19b.place(x=100, y=200)
                opt19c = Radiobutton(frame3, text="0", variable=radio19, value=3, command=correct19, font=font_head,
                                     bg="blue")
                opt19c.place(x=100, y=250)
                opt19d = Radiobutton(frame3, text="Invalid code", variable=radio19, value=4, command=correct19,
                                     font=font_head, bg="blue")
                opt19d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14')
                clear_btn.place(x=500, y=380, height=50, width=150)
                btn19.config(bg='green')

            btn19 = Button(frame2, text="19", command=que19, font='Helvetica 14')
            btn19.place(x=280, y=310, height=70, width=70)

            def que20():
                def correct20():
                    a = radio20.get()
                    if a == 2:
                        listc[19] = 1
                        listw[19] = 0
                    elif a == 1 or a == 3 or a == 4:
                        listc[19] = 0
                        listw[19] = 1

                def clear():
                    opt20a.deselect()
                    opt20b.deselect()
                    opt20c.deselect()
                    opt20d.deselect()

                clear_frame(frame3)
                radio20 = IntVar()
                qno20 = Label(frame3, text="QUESTION NO: 20", font=font_head, fg="black", bg="blue")
                qno20.place(x=50, y=30)
                ques20 = Label(frame3, text="What will be the output of this statement: 'a'+'bc'?", font=font_head,
                               fg="black", bg="blue")
                ques20.place(x=50, y=80)
                opt20a = Radiobutton(frame3, text="a+bc", variable=radio20, value=1, command=correct20, font=font_head,
                                     bg="blue")
                opt20a.place(x=100, y=150)
                opt20b = Radiobutton(frame3, text="abc", variable=radio20, value=2, command=correct20, font=font_head,
                                     bg="blue")
                opt20b.place(x=100, y=200)
                opt20c = Radiobutton(frame3, text="a bc", variable=radio20, value=3, command=correct20, font=font_head,
                                     bg="blue")
                opt20c.place(x=100, y=250)
                opt20d = Radiobutton(frame3, text="a", variable=radio20, value=4, command=correct20, font=font_head,
                                     bg="blue")
                opt20d.place(x=100, y=300)
                clear_btn = Button(frame3, text="CLEAR", command=clear, font='Helvetica 14', bg='grey',
                                   borderwidth=5)
                clear_btn.place(x=500, y=380, height=50, width=150)
                end_button = Button(frame3, text="END EXAM", command=end, font='Helvetica 14', bg='#FF0000',
                                    borderwidth=5)
                end_button.place(x=750, y=380, height=50, width=150)
                btn20.config(bg='green')

            btn20 = Button(frame2, text="20", command=que20, font='Helvetica 14')
            btn20.place(x=350, y=310, height=70, width=70)

            top.mainloop()

    # Create a button to start the exam
    start_button = Button(instruction_window, text="Start Exam", command=start_alert, font='Arial 14', bg='#06C755',
                          width=10)
    start_button.place(x=700, y=700)

    # Create a button to start the exam
    start_button = Button(instruction_window, text="Start Exam", command=start_alert, font='Arial 14', bg='#008CBA',
                          width=10,  borderwidth=5)
    start_button.place(x=700, y=700)


def validate():
    entered_user = name_entry.get()
    entered_pwd = reg_password_entry.get()
    user = username_entry.get()
    pwd = password_entry.get()
    if user == entered_user and pwd == entered_pwd:
        instructions()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        username_entry.delete(0, END)
        password_entry.delete(0, END)


# Create and place the login button

login_button = Button(window, text="Login", font='Arial 14', bg='#008CBA', width=10, borderwidth=5, command=validate)
login_button.place(x=800, y=500)

# Create and place the login button
registration_button = Button(window, text="Register !", font='Arial 14 underline', bg='light cyan', fg='red',
                             relief=FLAT, command=register)
registration_button.config(bg='light cyan')
registration_button.place(x=1000, y=500)

window.mainloop()
