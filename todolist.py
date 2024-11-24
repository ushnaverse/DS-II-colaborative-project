import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from PairingHeap import PairingHeap
from TaskManager import Task
from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk 


class TodolistApp:
    def __init__(self, master):
        self.master = master
        master.title("Todolist")
        master.geometry("333x500")

        # Load the image file
        self.background_image = tk.PhotoImage(file="bg2.png")

        # Create a canvas and display the image on it
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.master.after(4000, self.master.destroy)


if __name__ == '__main__':
    root = tk.Tk()
    app = TodolistApp(root)
    personal = {}
    root.mainloop()
    

pref = {"Good" : 2, "Average" : 4, "Bad" : 6}

class TodoListApp:
    def __init__(self, master):
        self.P = PairingHeap()
        self.master = master
        master.title("Todo List App")
        master.geometry("333x500")
        master.configure(bg="maroon")

        self.todo_list = []
        
        self.weightage_label = tk.Label(master, text="Subject", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.subject = tk.Entry(master, bg="white", fg="black")
        self.subject.pack()

        self.weightage_label = tk.Label(master, text="Assignment", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.todo_entry = tk.Entry(master, bg="white", fg="black")
        self.todo_entry.pack()

        self.weightage_label = tk.Label(master, text="Weightage", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.weightage_entry = tk.Entry(master, bg="white", fg="black")
        self.weightage_entry.pack()
        
        
        self.label_priority = tk.Label(master, text ="Preference:", bg="maroon", fg="white")
        self.label_priority.pack()
        
        
        # create a list of items for the dropdown menu
        options = ["Good", "Average", "Bad"]

        # create a variable to store the selected item
        self.selected_option = tk.StringVar()

        # set the default value for the variable
        self.selected_option.set(options[0])
        print(self.selected_option.get())
        # create the dropdown menu
        self.dropdown = tk.OptionMenu(root, self.selected_option, *options)
        self.dropdown.pack()

        # self.priority_entry = tk.Entry(master, bg="white", fg= "black")
        # self.priority_entry.pack()

        self.deadline_label = tk.Label(master, text="Deadline", bg="maroon", fg="white")
        self.deadline_label.pack()

        self.deadline_entry = DateEntry(master, bg="white", date_pattern="yyyy-mm-dd")
        self.deadline_entry.pack()
        
        self.add_button = tk.Button(master, text="Add", command=self.add_todo, bg="white")
        self.add_button.pack()

        
        self.next_button = tk.Button(master, text="Next", command=self.go_next, bg="white")
        self.next_button.pack()
        
        self.todo_frame = tk.Frame(master, bg="white")
        self.todo_frame.pack()
        
    def go_next(self):
        self.master.destroy()
    def add_todo(self):
        todo = self.todo_entry.get()
        subject = self.subject.get()
        weightage = self.weightage_entry.get()
        deadline = self.deadline_entry.get()
        # preference = self.priority_entry.get()
        deadline = deadline.split("-")
        task1= Task(subject, int(weightage), (deadline), pref[self.selected_option.get()], todo)
        self.P.Insert(task1)
        self.todo_entry.delete(0, tk.END)
        self.weightage_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.subject.delete(0,tk.END)
        
        self.todo_list.append((todo, weightage, deadline))

        todo_label = tk.Label(self.todo_frame, text=f"{todo}, weightage: {weightage}, deadline: {deadline}", bg="white", fg="black")
        todo_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

    window = tk.Tk()
    window.title('My Learning Track')
    window.geometry('333x500')
    window['bg'] = 'maroon'
    missed_tasks =[]

    app.P.traverse(app.P.root)
    tasks = app.P.tasks
    # [
    #     {'priority': 3, 'course name': 'LA', 'deadline': '2023-04-23', 'Assignment': 'Final'},
    #     {'priority': 2, 'course name': 'CA', 'deadline': '2023-05-05', 'Assignment': 'HW'},
    #     {'priority': 1, 'course name': 'DSII', 'deadline': '2023-05-01', 'Assignment': 'HW'},
    #     {'priority': 5, 'course name': 'Hikma', 'deadline': '2023-05-01', 'Assignment': 'HW'},
    #     {'priority': 4, 'course name': 'IPnS', 'deadline': '2023-05-05', 'Assignment': 'HW'}
    # ]

    # Sort tasks by priority
    # tasks.sort(key=lambda x: x['priority']) #pairing heap

    # Create a label widget to display the top priority task with deadline date
    label = tk.Label(window, text=f"Top priority task: {app.P.Top().task}, Deadline: {app.P.Top().date}", background='#f7d7c4')
    label.pack()

    # Define a function to remove the top priority task and update the label and table
    def remove_top_task():
        # if tasks:
        #     if datetime.strptime(tasks[0]['deadline'], '%Y-%m-%d').date() < datetime.now().date() :
        #         missed_tasks.append(tasks[0]['course name'])
        #     tasks.pop(0)
            
        if tasks:
            label.config(text=f"Top priority task: {app.P.Top().task}, Deadline: {app.P.Top().date}")
            checkbox_text.set(app.P.Top().task)
            tasks.pop(0)
            app.P.Delete()
            if app.P.root !=None:
                checkbox_text.set(app.P.Top().task)
                label.config(text=f"Top priority task: {app.P.Top().task}, Deadline: {app.P.Top().date}")
            else:
                label.config(text="Well Done, No tasks left!!!")
                tree.delete(*tree.get_children()) #deletes all the items from a tkinter treeview widget
                #tree.get_children() returns a tuple of all the items in treeview and * unpacks the tuple in individual arguments
                window.destroy()
                window1 = tk.Tk()
                window1.title('My Learning Track')
                window1.geometry('333x500')

                background_image = tk.PhotoImage(file="congo.png")
                # Load the image file
                canvas = tk.Canvas(width=333, height=500)
                canvas.pack()
                canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

                window1.mainloop()
            checkbox.deselect()
            update_table()
        # else:
        #     label.config(text="Congratulations, No tasks left!!!")
        #     tree.delete(*tree.get_children())
            
        # Print missed tasks
        # print(f"Missed tasks: {missed_tasks}")

    # txt_output = Text(window, height=5, width=10)
    # txt_output.pack(pady=10)

    # for item in missed_tasks:
    #     txt_output.insert(END, item + "\n")


    # Create a Checkbutton widget for the top priority task
    checkbox_text = tk.StringVar()
    checkbox_text.set(app.P.Top().task)
    checkbox = tk.Checkbutton(window, textvariable=checkbox_text, command=remove_top_task, background= "#f7d7c4")
    checkbox.pack()

    def update_table():
        # Clear existing items from tree
        tree.delete(*tree.get_children())
        
        # Populate tree with all tasks
        for i, task in enumerate(tasks):
            tree.insert("", "end", iid=i, values=(i+1, task.course_name, task.date, task.task))
            
        # Set column widths
        tree.column("#", width=20, minwidth=20, stretch=False)
        tree.column("Course Name", width=100, minwidth=100, stretch=False)
        tree.column("Deadline", width=100, minwidth=100, stretch=False)
        tree.column("Assignment", width=80, minwidth=80, stretch=False)

    # Create a table view with tasks, deadlines and assignments
    tree = ttk.Treeview(window, columns=("#", "Course Name", "Deadline", "Assignment"), show="headings")
    tree.heading("#", text="#")
    tree.heading("Course Name", text="Course Name")
    tree.heading("Deadline", text="Deadline")
    tree.heading("Assignment", text="Assignment")

    # Set column widths for the treeview
    tree.column("#", width=50)
    tree.column("Course Name", width=100)
    tree.column("Deadline", width=100)
    tree.column("Assignment", width=100)

    # Customize the color and dimensions of the Treeview widget
    style = ttk.Style(window)
    style.configure("Treeview", background="#f7d7c4", foreground="black", rowheight=20, fieldbackground="#f7d7c4", font=("Calibri", 11))
    style.map('Treeview', background=[('selected', '#f7d7c4')])

    tree.pack(pady=20)

    # Call update_table() function to populate the Treeview widget with tasks
    update_table()

    # Create a button to go back to the previous screen

    window.mainloop()

