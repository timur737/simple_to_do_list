from tkinter import *

root = Tk()
root.title("To Do List")


class Todo:
    tasks = []

    def __init__(self,main):

        self.win = Label(text="Enter tasks", fg="blue")
        self.win2 = Listbox(root)
        self.fram = Frame(main, bg = "white")
        self.ent = Entry()
        self.btn1 = Button(text="Add", command=self.add, fg="red")
        self.done = Button(text="Done", command=self.del_one, fg="green")
        root.geometry("300x400")
        self.win.pack()
        self.fram.pack()
        self.ent.pack()
        self.btn1.pack()
        self.done.pack()
        self.win2.pack()


    def updated(self):
        self.deleted()
        for i in self.tasks:
            self.win2.insert("end", i)

    def add(self):
        task = self.ent.get()
        if task != "":
            self.tasks.append(task)
            self.updated()
        else:
            self.win["text"] = "No enter task"
        self.ent.delete(0, "end")

    def deleted(self):
        self.win2.delete(0, "end")

    def del_one(self):
        task = self.win2.get("active")
        if task in self.tasks:
            self.tasks.remove(task)
        self.updated()
        



q = Todo(root)
root.mainloop()
