import customtkinter
from sympy import *
from tkinter import *
from sympy.plotting import plot
from PIL import Image
import threading
import time
main = customtkinter
root = customtkinter.CTk()
customtkinter.set_default_color_theme("blue")
root.title('THIVIO')
root.resizable(False, False)
window_height = 510
window_width = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

try:
    img = Image.open("12.png")
    img = img.resize((650,400))
    update = PhotoImage(light_image=img)
except:
    update = PhotoImage(file='')

stage = "Graph"
change = 0

x, y, z, a, b, c, d, e = symbols("x y z a b c d e")

switch_var = customtkinter.StringVar(value="DarkTheme")


def switch_event():
    root.set_appearance_mode(switch_var.get())


def about():
    root23 = customtkinter.CTk()
    root23.title("About/Credit")
    root23.geometry('450x50')
    label = customtkinter.CTkLabel(root23, text="This app was developed by Ansol in 2022@ETH\n"
                                                "There are many products from Ansol\n"
                                                "Ansol owner is Anania Belay. Ansol can develop any kind of app for you.")
    label.pack()
    root23.mainloop()


def settings():
    root2 = customtkinter.CTk()
    root2.title("Settings")
    root2.geometry('400x200')
    switch_1 = customtkinter.CTkSwitch(root2, text="Theme Dark", command=switch_event,
                                       variable=switch_var, onvalue="dark", offvalue="light")
    switch_1.pack(padx=20, pady=10)

    butt = customtkinter.CTkButton(root2, text="Check For Update")
    butt2 = customtkinter.CTkButton(root2, text="More Product from AnSol")
    butt.pack(padx=20, pady=10)
    butt2.pack(padx=20, pady=10)

    butt3 = customtkinter.CTkButton(root2, text="Credits", command=about)
    butt3.pack(padx=20, pady=10)
    root2.mainloop()


def graph_create(function):
    def create_plot():
        try:
            parsed_function = sympify(function)
            p1 = plot(parsed_function, show=True, size=(6, 4))
            p1.save('12.png')
            update.configure(file="12.png")
            label.configure(text='', image='12.png')
        except Exception as e:
            print(f"Error: {e}") 

    threading.Thread(target=create_plot).start() 


def simplfier(function):
    return simplify(function)


def eve(function, value):
    num = f"{function}-{value}"
    return solve(num)


def decompose(function):
    return apart(function)


# Frame for input field and buttons
frame = customtkinter.CTkFrame(master=root, width=600, height=75, corner_radius=10)

# Function input field
entry = customtkinter.CTkEntry(frame, height=45, width=230, text_color='white', placeholder_text="Write function")
entry.grid(row=0, column=0, padx=10, pady=10)

# Combobox for selecting action (Graph, Decompose, etc.)
combobox = customtkinter.CTkComboBox(master=frame, values=["Graph", "Decompose", "Simplify", "Evaluate"])
combobox.grid(row=0, column=1, padx=10, pady=10)
combobox.set("Graph")


# Adjusted layout to place "Run" button and cog icon nicely
# Cog icon (Settings button)
sets = PhotoImage(file='setting.png')
bu = customtkinter.CTkButton(frame, text="", image=sets, width=35, height=35, command=settings)
bu.grid(row=0, column=2, padx=10, pady=10)

button2 = customtkinter.CTkButton(frame, text="Run", command=lambda: evaluate())
button2.grid(row=0, column=3, padx=10, pady=10)

frame.pack(padx=20, pady=10)


def evaluate():
    if combobox.get() == "Graph":
        graph_create(entry.get())
        print(entry.get())
    elif combobox.get() == "Simplify":
        value = simplfier(entry.get())
        label.configure(text=value, image='')
    elif combobox.get() == "Evaluate":
        starter = entry.get()
        splitted = starter.split('=')
        comed = eve(splitted[0], splitted[1])
        label.configure(text=comed, image='')
    elif combobox.get() == 'Decompose':
        valve = decompose(entry.get())
        label.configure(text=valve, image='')


# Frame for output (Graph, result, etc.)
frame2 = customtkinter.CTkFrame(master=root, width=600, height=400, corner_radius=10)

label = customtkinter.CTkLabel(master=frame2, text="", height=400, width=600)
label.place(relx=.5, rely=.5, anchor=CENTER)

frame2.pack(padx=20, pady=5)

root.mainloop()
