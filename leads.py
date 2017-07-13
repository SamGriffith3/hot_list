# Imports
import csv
import OS
import tkinter as tk

root = tk.Tk()
app = Application(master=root)
app.mainloop()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

top = Toplevel()
    def create_new_user(self):
        self.new_user = tk.Button(self)
        self.new_user["text"] = "Add New User"
        self.new_user["command"] = self.add_user
        self.new_user.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def add_user(self):
        print("New Hot List Lead")
        self.username = Entry(add_user)
        self.username.pack()
        add_vehicle_interest():
        
    def add_vehicle_interest(self):
        print("New Vehicle Interest")
        self.vehicle_type = Listbox(add_user)
        self.vehicle_type.pack()
        self.vehicle_type.insert(END, "Vehicle Type")
        for item in ["Sedan", "Coupe", "Truck", "Hatchback"]:
            self.vehicle_type.insert(END, item)
        


create_new_user()









