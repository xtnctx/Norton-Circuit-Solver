"""
Bahillo Ryan Christopher D.  (201812282)
BSCpE 2-1

Fundamentals of Electric Circuits 5th Edition >> Example 4.11 >> Figure 4.39 >> page 146

// Finished November 2019

"""

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import math
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Front_page:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1024x576+175+90")
        self.root.resizable(0,0)
        self.root.config(bd=10,relief=RIDGE)
        self.canvas = Canvas(self.root,bd=10,relief=RIDGE)
        self.load = Image.open(resource_path("Front.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas, image=self.render)
        self.img.image = self.render
        self.img.pack(anchor=W)
        self.root.title("Norton")
        self.canvas.pack(fill=BOTH, expand=1)
        title = Label(text="NORTON'S THEOREM",bd=10, relief=RIDGE, font=("Orbitron",50))
        title.place(relx=0.5,rely=0.35,anchor=CENTER)
        self.button = Button(self.canvas, text="Enter", fg="red",font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.enter)
        self.button.place(relx=0.5, rely=0.8, anchor="center")
        self.root.bind("<Return>", lambda e:self.enter())
        info = Button(self.canvas, text="What is Norton's Theorem?", fg="blue",font=("Orbitron",10), bd=5, relief=RAISED, command=self.info)
        info.place(relx=0.85, rely=0.9, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

    def info(self):
        top = Toplevel(self.root)
        Info(top)

    def enter(self):
        self.root.destroy()
        root = Tk()
        Norton(root)

class Info:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x400+300+190")
        self.root.resizable(0,0)
        self.root.config(bd=10, relief=RIDGE, bg="black")
        self.canvas_2 = Canvas(self.root)
        self.canvas_2.pack(fill=BOTH, expand=1)
        self.frame = Frame(self.canvas_2)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas_2: self.canvas_2.configure(scrollregion=self.canvas_2.bbox("all")))
        vertscroll = Scrollbar(self.canvas_2,orient="vertical", command=self.canvas_2.yview)
        self.canvas_2.configure(yscrollcommand=vertscroll.set)
        self.canvas_frame = self.canvas_2.create_window((4,4),window=self.frame, anchor="nw")
        vertscroll.pack(side=RIGHT, fill=Y)

        self.load = Image.open(resource_path("norton_info.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.frame, image=self.render, bd=5)
        self.img.image = self.render
        self.img.pack()
        ok = Button(self.frame, text="Ok", font=("Cambria",10,"bold"),width=20, bd=5, relief=RAISED, command=self.ok)
        ok.pack()
        self.root.iconbitmap(resource_path("icon.ico"))

    def ok(self):
        self.root.destroy()

class Norton:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton's Theorem")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)
        self.canvas_for_main_F = Canvas(self.canvas, bg="royalblue3", width=452, height=270, bd=10, relief=RIDGE)
        self.canvas_for_main_F.place(relx=0.26,rely=0.45,anchor=CENTER)
        self.canvas_for_entry = Canvas(self.canvas, bg="royalblue3" ,width=449, height=270, bd=10, relief=RIDGE)
        self.canvas_for_entry.place(relx=0.74, rely=0.45, anchor=CENTER)
        self.canvas_for_question = Canvas(self.canvas, bg="royalblue3" ,width=478, height=29, bd=10, relief=RIDGE)
        self.canvas_for_question.place(relx=0.258, rely=0.05)
        self.canvas_for_button = Canvas(self.canvas, bg="royalblue3" ,width=883, height=100, bd=10, relief=RIDGE)
        self.canvas_for_button.place(relx=0.0513, rely=0.738)
        
        self.label_r1 = Label(self.canvas, text="R1", bg="floral white", font=("Orbitron", 9))
        self.label_r1.place(x=180,y=205)
        entry_r1 = Label(self.canvas, text="R1", bg="royalblue3", font=("Orbitron",15))
        entry_r1.place(x=565, y=150)
        entry_sym_r1 = Label(self.canvas, text="\u2126", bg="royalblue3", font=("Orbitron",15))
        entry_sym_r1.place(x=705, y=150)

        self.label_r2 = Label(self.canvas, text="R2", bg="floral white", font=("Orbitron", 9))
        self.label_r2.place(x=246,y=176)
        entry_r2 = Label(self.canvas, text="R2", bg="royalblue3", font=("Orbitron",15))
        entry_r2.place(x=560, y=200)
        entry_sym_r2 = Label(self.canvas, text="\u2126", bg="royalblue3", font=("Orbitron",15))
        entry_sym_r2.place(x=705, y=200)

        
        self.label_r3 = Label(self.canvas, text="R3", bg="floral white", font=("Orbitron", 9))
        self.label_r3.place(x=365,y=240)
        entry_r3 = Label(self.canvas, text="R3", bg="royalblue3", font=("Orbitron",15))
        entry_r3.place(x=560, y=250)
        entry_sym_r3 = Label(self.canvas, text="\u2126", bg="royalblue3", font=("Orbitron",15))
        entry_sym_r3.place(x=705, y=250)

        self.label_r4 = Label(self.canvas, text="R4", bg="floral white", font=("Orbitron", 9))
        self.label_r4.place(x=246,y=311)
        entry_r4 = Label(self.canvas, text="R4", bg="royalblue3", font=("Orbitron",15))
        entry_r4.place(x=761, y=150)
        entry_sym_r4 = Label(self.canvas_for_entry, text="\u2126", bg="royalblue3", font=("Orbitron",15))
        entry_sym_r4.place(relx=0.87, rely=0.21, anchor="center")

        self.label_Is = Label(self.canvas, text="Is", bg="floral white", font=("Orbitron", 9))
        self.label_Is.place(x=90,y=240)
        entry_Is = Label(self.canvas, text="Is", bg="royalblue3", font=("Orbitron",15))
        entry_Is.place(x=774, y=200)
        entry_sym_I = Label(self.canvas, text="A", bg="royalblue3", font=("Orbitron",15))
        entry_sym_I.place(relx=0.916, rely=0.39, anchor="center")

        self.label_Vs = Label(self.canvas, text="Vs", bg="floral white", font=("Orbitron", 9))
        self.label_Vs.place(x=192,y=280)
        entry_Vs = Label(self.canvas, text="Vs", bg="royalblue3", font=("Orbitron",15))
        entry_Vs.place(x=757, y=250)
        entry_sym_V = Label(self.canvas_for_entry, text="V", bg="royalblue3", font=("Orbitron",15))
        entry_sym_V.place(relx=0.87, rely=0.55, anchor="center")
        
        self.load = Image.open(resource_path("main_figure.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_main_F, image=self.render, bd=5)
        self.img.image = self.render
        self.img.place(x=11,y=40)

        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)
        
        
        self.n = Label(self.canvas, font=("Orbitron",16), text="Circuit analysis using Norton's Theorem.")
        self.n.place(x=270,y=40)
#===================Resistor==========================
        self.R1 = StringVar()
        self.R2 = StringVar()
        self.R3 = StringVar()
        self.R4 = StringVar()
        
        self.r1 = Entry(self.canvas, textvariable=self.R1, bd=5, width=9, font=("Verdana",12))
        self.r2 = Entry(self.canvas, textvariable=self.R2, bd=5, width=9, font=("Verdana",12))
        self.r3 = Entry(self.canvas, textvariable=self.R3, bd=5, width=9, font=("Verdana",12))
        self.r4 = Entry(self.canvas, textvariable=self.R4, bd=5, width=9, font=("Verdana",12))
        
        self.r1.place(x=600, y=150)
        self.r2.place(x=600, y=200)
        self.r3.place(x=600, y=250)
        self.r4.place(x=800, y=150)
#======================Current =============================
        self.I = StringVar()
        self.cur = Entry(self.canvas, textvariable=self.I, bd=5, width=9, font=("Verdana",12))
        self.cur.place(x=800, y=200)
#=======================Voltage===============================
        self.V = StringVar()
        self.v = Entry(self.canvas, textvariable=self.V, bd=5, width=9, font=("Verdana",12))
        self.v.place(x=800, y=250)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
#==========================Widgets=============================        
        self.r1.focus_force()
        self.solve = Button(self.canvas, text="CALCULATE", foreground = "red", font=("Orbitron",10),state="normal", width=10, bd=5, relief=RAISED, command=self.solve)
        self.solve.place(x=700, y=325)
        list_prefix = Button(self.canvas, text="Prefixes", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.prefix_list)
        list_prefix.place(relx=0.48, y=475, anchor=E)
        clear_all_entries = Button(self.canvas, text="Clear all entries", font=("Orbitron",10), width=15, bd=5, relief=RAISED, command=self.clear_entries)
        clear_all_entries.place(relx=0.65, y=475, anchor=CENTER)
        instructions = Button(self.canvas, text="Instructions", font=("Orbitron",10), width=15, bd=5, relief=RAISED, command=self.instructions)
        instructions.place(relx=0.1, y=475, anchor=W)
        exit_program = Button(self.canvas, text="Exit", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.exit_program)
        exit_program.place(relx=0.9, y=475, anchor = E)
        self.root.bind("<Escape>",lambda e:self.exit_program())
        self.root.bind("<F1>", lambda e:self.instructions())
        self.root.bind("<F2>", lambda e:self.prefix_list())
        self.root.bind("<F3>", lambda e:self.clear_entries())

        self.r1.bind('<Return>',lambda e:self.next_entry1())
        self.r2.bind('<Return>',lambda e:self.next_entry2())
        self.r3.bind('<Return>',lambda e:self.next_entry3())
        self.r4.bind('<Return>',lambda e:self.next_entry4())
        self.cur.bind('<Return>',lambda e:self.next_entryI())
        self.v.bind('<Return>',lambda e:self.next_entryV())
        self.root.iconbitmap(resource_path("icon.ico"))
        
#-----------------------------------------------------------------------------------------
   
    def prefix_list(self):
        top = Toplevel(self.root)
        Prefix_list(top)

    def clear_entries(self):
        self.r1.delete(0,'end')
        self.r2.delete(0,'end')
        self.r3.delete(0,'end')
        self.r4.delete(0,'end')
        self.cur.delete(0,'end')
        self.v.delete(0,'end')
        self.label_r1.config(text="R1", foreground="black")
        self.label_r2.config(text="R2", foreground="black")
        self.label_r3.config(text="R3", foreground="black")
        self.label_r4.config(text="R4", foreground="black")
        self.label_Is.config(text="Is", foreground="black")
        self.label_Vs.config(text="Vs", foreground="black")
        self.r1.focus_set()
        messagebox.showinfo("Cleared!","All entries are now empty.")


    def exit_program(self):
        msg = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if msg:
            self.root.destroy()

    def instructions(self):
        top = Toplevel(self.root)
        Instructions(top)
        
    def prefix(self):
        self.omega_1 = (self.R1.get())
        self.omega_2 = (self.R2.get())
        self.omega_3 = (self.R3.get())
        self.omega_4 = (self.R4.get())
        self.ampere = (self.I.get())
        self.volt = (self.V.get())
        
        if 'T' in self.omega_1:
            new = self.omega_1.replace("T","")
            self.omega_1 = ((float(new)*1e12))
        elif 'G' in self.omega_1:
            new = self.omega_1.replace("G","")
            self.omega_1 = ((float(new)*1e9))
        elif 'M' in self.omega_1:
            new = self.omega_1.replace("M","")
            self.omega_1 = ((float(new)*1e6))
        elif 'k' in self.omega_1:
            new = self.omega_1.replace("k","")
            self.omega_1 = ((float(new)*1e3))
        elif 'm' in self.omega_1:
            new = self.omega_1.replace("m","")
            self.omega_1 = ((float(new)*1e-3))
        elif 'u' in self.omega_1:
            new = self.omega_1.replace("u","")
            self.omega_1 = ((float(new)*1e-6))
        elif 'n' in self.omega_1:
            new = self.omega_1.replace("n","")
            self.omega_1 = ((float(new)*1e-9))
        elif 'p' in self.omega_1:
            new = self.omega_1.replace("p","")
            self.omega_1 = ((float(new)*1e-12))
        elif self.omega_1 == '':
            self.omega_1 = 0
                
        if 'T' in self.omega_2:
            new = self.omega_2.replace("T","")
            self.omega_2 = ((float(new)*1e12))
        elif 'G' in self.omega_2:
            new = self.omega_2.replace("G","")
            self.omega_2 = ((float(new)*1e9))
        elif 'M' in self.omega_2:
            new = self.omega_2.replace("M","")
            self.omega_2 = ((float(new)*1e6))
        elif 'k' in self.omega_2:
            new = self.omega_2.replace("k","")
            self.omega_2 = ((float(new)*1e3))
        elif 'm' in self.omega_2:
            new = self.omega_2.replace("m","")
            self.omega_2 = ((float(new)*1e-3))
        elif 'u' in self.omega_2:
            new = self.omega_2.replace("u","")
            self.omega_2 = ((float(new)*1e-6))
        elif 'n' in self.omega_2:
            new = self.omega_2.replace("n","")
            self.omega_2 = ((float(new)*1e-9))
        elif 'p' in self.omega_2:
            new = self.omega_2.replace("p","")
            self.omega_2 = ((float(new)*1e-12))
        elif self.omega_2 == '':
            self.omega_2 = 0

        if 'T' in self.omega_3:
            new = self.omega_3.replace("T","")
            self.omega_3 = ((float(new)*1e12))
        elif 'G' in self.omega_3:
            new = self.omega_3.replace("G","")
            self.omega_3 = ((float(new)*1e9))
        elif 'M' in self.omega_3:
            new = self.omega_3.replace("M","")
            self.omega_3 = ((float(new)*1e6))
        elif 'k' in self.omega_3:
            new = self.omega_3.replace("k","")
            self.omega_3 = ((float(new)*1e3))
        elif 'm' in self.omega_3:
            new = self.omega_3.replace("m","")
            self.omega_3 = ((float(new)*1e-3))
        elif 'u' in self.omega_3:
            new = self.omega_3.replace("u","")
            self.omega_3 = ((float(new)*1e-6))
        elif 'n' in self.omega_3:
            new = self.omega_3.replace("n","")
            self.omega_3 = ((float(new)*1e-9))
        elif 'p' in self.omega_3:
            new = self.omega_3.replace("p","")
            self.omega_3 = ((float(new)*1e-12))
        elif self.omega_3 == '':
            self.omega_3 = 0

        if 'T' in self.omega_4:
            new = self.omega_4.replace("T","")
            self.omega_4 = ((float(new)*1e12))
        elif 'G' in self.omega_4:
            new = self.omega_4.replace("G","")
            self.omega_4 = ((float(new)*1e9))
        elif 'M' in self.omega_4:
            new = self.omega_4.replace("M","")
            self.omega_4 = ((float(new)*1e6))
        elif 'k' in self.omega_4:
            new = self.omega_4.replace("k","")
            self.omega_4 = ((float(new)*1e3))
        elif 'm' in self.omega_4:
            new = self.omega_4.replace("m","")
            self.omega_4 = ((float(new)*1e-3))
        elif 'u' in self.omega_4:
            new = self.omega_4.replace("u","")
            self.omega_4 = ((float(new)*1e-6))
        elif 'n' in self.omega_4:
            new = self.omega_4.replace("n","")
            self.omega_4 = ((float(new)*1e-9))
        elif 'p' in self.omega_4:
            new = self.omega_4.replace("p","")
            self.omega_4 = ((float(new)*1e-12))
        elif self.omega_4 == '':
            self.omega_4 = 0

        if 'T' in self.ampere:
            new = self.ampere.replace("T","")
            self.ampere = ((float(new)*1e12))
        elif 'G' in self.ampere:
            new = self.ampere.replace("G","")
            self.ampere = ((float(new)*1e9))
        elif 'M' in self.ampere:
            new = self.ampere.replace("M","")
            self.ampere = ((float(new)*1e6))
        elif 'k' in self.ampere:
            new = self.ampere.replace("k","")
            self.ampere = ((float(new)*1e3))
        elif 'm' in self.ampere:
            new = self.ampere.replace("m","")
            self.ampere = ((float(new)*1e-3))
        elif 'u' in self.ampere:
            new = self.ampere.replace("u","")
            self.ampere = ((float(new)*1e-6))
        elif 'n' in self.ampere:
            new = self.ampere.replace("n","")
            self.ampere = ((float(new)*1e-9))
        elif 'p' in self.ampere:
            new = self.ampere.replace("p","")
            self.ampere = ((float(new)*1e-12))
        elif self.ampere == '':
            self.ampere = 0

        if 'T' in self.volt:
            new = self.volt.replace("T","")
            self.volt = ((float(new)*1e12))
        elif 'G' in self.volt:
            new = self.volt.replace("G","")
            self.volt = ((float(new)*1e9))
        elif 'M' in self.volt:
            new = self.volt.replace("M","")
            self.volt = ((float(new)*1e6))
        elif 'k' in self.volt:
            new = self.volt.replace("k","")
            self.volt = ((float(new)*1e3))
        elif 'm' in self.volt:
            new = self.volt.replace("m","")
            self.volt = ((float(new)*1e-3))
        elif 'u' in self.volt:
            new = self.volt.replace("u","")
            self.volt = ((float(new)*1e-6))
        elif 'n' in self.volt:
            new = self.volt.replace("n","")
            self.volt = ((float(new)*1e-9))
        elif 'p' in self.volt:
            new = self.volt.replace("p","")
            self.volt = ((float(new)*1e-12))
        elif self.volt == '':
            self.volt = 0

    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'

    def next_entry1(self):
        if self.R1.get() == '0' or self.R1.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.r1.delete(0,"end")
        else:
            self.prefix()
            self.label_r1.config(text=self.convert_to_prefix(float(self.omega_1))+"\u2126",foreground="red")
            self.r2.focus_set()

    def next_entry2(self):
        if self.R2.get() == '0' or self.R2.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.r2.delete(0,"end")
        else:
            self.prefix()
            self.label_r2.config(text=self.convert_to_prefix(float(self.omega_2))+"\u2126",foreground="red")
            self.r3.focus_set()

    def next_entry3(self):
        if self.R3.get() == '0' or self.R3.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.r3.delete(0,"end")
        else:
            self.prefix()
            self.label_r3.config(text=self.convert_to_prefix(float(self.omega_3))+"\u2126",foreground="red")
            self.r4.focus_set()

    def next_entry4(self):
        if self.R4.get() == '0' or self.R4.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.r4.delete(0,"end")
        else:
            self.prefix()
            self.label_r4.config(text=self.convert_to_prefix(float(self.omega_4))+"\u2126",foreground="red")
            self.cur.focus_set()

    def next_entryI(self):
        if self.I.get() == '0' or self.I.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.cur.delete(0,"end")
        else:
            self.prefix()
            self.label_Is.config(text=self.convert_to_prefix(float(self.ampere))+"A",foreground="red")
            self.v.focus_set()

    def next_entryV(self):
        if self.V.get() == '0' or self.V.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.v.delete(0,"end")
        else:
            self.prefix()
            self.label_Vs.config(text=self.convert_to_prefix(float(self.volt))+"V",foreground="red")

    def solve(self):
        num_list = []
        r1 = self.R1.get()
        r2 = self.R2.get()
        r3 = self.R3.get()
        r4 = self.R4.get()
        i = self.I.get()
        v = self.V.get()
        num_list.append(r1)
        num_list.append(r2)
        num_list.append(r3)
        num_list.append(r4)
        num_list.append(i)
        num_list.append(v)
        for i in (num_list):
            if i == '0' or i == '':
                messagebox.showerror("Error!","Cannot be zero!")
                if r1 == '0' or r1 == '':
                    self.r1.delete(0,"end")
                if r2 == '0' or r2 == '':
                    self.r2.delete(0,"end")
                if r3 == '0' or r3 == '':
                    self.r3.delete(0,"end")
                if r4 == '0' or r4 == '':
                    self.r4.delete(0,"end")
                if i == '0' or i == '':
                    self.cur.delete(0,"end")
                if v == '0' or v == '':
                    self.v.delete(0,"end")
                return
        else:
            self.prefix()
            self.root.destroy()
            root = Tk()
            Norton_equivalent(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt)
                
class Norton_equivalent:
    def __init__(self,root,r1,r2,r3,r4,Is,Vs):
        self.root = root
        self.omega_1 = r1
        self.omega_2 = r2
        self.omega_3 = r3
        self.omega_4 = r4
        self.ampere = Is
        self.volt = Vs
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton's Theorem")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)

        self.canvas_for_figure = Canvas(self.canvas, width=500, height=350, bd=10, relief=RIDGE, bg="royalblue3")
        self.canvas_for_figure.place(relx=0.29, rely=0.5, anchor=CENTER)

        self.canvas_explain = Canvas(self.canvas, bd=10, height=500, relief=RIDGE, bg="royalblue3")
        self.canvas_explain.place(relx=0.77, rely=0.5, anchor=CENTER)

        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)
        
        self.load = Image.open(resource_path("final_figure.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_figure, image=self.render)
        self.img.image = self.render
        self.img.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
#==============================Finding Rtotal==============================================
        self.Req = ((float(self.omega_1)+float(self.omega_2)+float(self.omega_4)))
        self.RN = (1/((1/float(self.Req))+(1/float(self.omega_3))))
        label1 = Label(self.canvas_explain, bg="royalblue3", bd=5, relief=SUNKEN,
                       text="Norton Equivalent Ciruit", font=("Orbitron",15 ,"bold"))
        label1.place(relx=0.5, rely=.2, anchor="center")
        label_R = Label(self.canvas_explain, bg="royalblue3",
                        text=("Rn: {}\u2126").format(self.convert_to_prefix((self.RN))), font=("consolas",15,"bold"))
        label_R.place(relx=0.5, rely=0.5, anchor="center")
#==================================Using Mesh Analysis=====================================
        self.voltage_in_i1 = (-(float(self.omega_1)*float(self.ampere))-float(self.volt))
        self.current_in_i2 = (abs(float(self.voltage_in_i1))/float(self.Req))
        label_I = Label(self.canvas_explain, bg="royalblue3",
                        text=("In: {}A").format(self.convert_to_prefix((self.current_in_i2))), font=("consolas",15,"bold"))
        label_I.place(relx=0.5, rely=0.4, anchor="center")
        
        self.label_RN = Label(self.canvas_explain, bg="royalblue3",
                            text=(" "), font=("Orbitron",15))
        self.label_RN.place(relx=0.5, rely=0.7, anchor="center")

        self.label_RL = Label(self.canvas_explain, bg="royalblue3",
                            text=(" "), font=("Orbitron",15))
        self.label_RL.place(relx=0.5, rely=0.8, anchor="center")

        self.label_Is = Label(self.canvas, text="Is", bg="floral white", font=("Orbitron", 9))
        self.label_Is.place(x=150,y=260)
        self.label_Vs = Label(self.canvas, text="Rn", bg="floral white", font=("Orbitron", 9))
        self.label_Vs.place(x=300,y=260)
        
        self.RL = StringVar()
        self.rL = Entry(self.canvas_explain, textvariable=self.RL, bd=5, width=9, font=("Verdana",12))
        self.rL.place(relx=0.5, rely=0.6, anchor="center")
        self.rL.focus_force()
#====================Widgets===================================
        self.rL.bind('<Return>',lambda e:self.calculation_for_RL_and_RN())
        self.next_button = Button(self.canvas_explain, state="disabled", foreground="red",
                                  bd=5, relief=RAISED, text="Show Solution", font=("Orbitron",12), command=self.next)
        self.next_button.place(relx=0.5, rely=0.9, anchor="center")
        entry_r4 = Label(self.canvas_explain, bg="royalblue3", text="RL:", font=("Orbitron",15))
        entry_r4.place(x=129, rely=0.6, anchor="center")
        entry_sym_r4 = Label(self.canvas_explain, text="\u2126", bg="royalblue3", font=("Orbitron",15))
        entry_sym_r4.place(x=265, rely=0.6, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

    def calculation_for_RL_and_RN(self):
        if self.rL.get() == '0' or self.rL.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.rL.delete(0,"end")
            return
        else:
            self.rload = (self.RL.get())
            if 'T' in self.rload:
                new = self.rload.replace("T","")
                self.rload = ((float(new)*1e12))
            elif 'G' in self.rload:
                new = self.rload.replace("G","")
                self.rload = ((float(new)*1e9))
            elif 'M' in self.rload:
                new = self.rload.replace("M","")
                self.rload = ((float(new)*1e6))
            elif 'k' in self.rload:
                new = self.rload.replace("k","")
                self.rload = ((float(new)*1e3))
            elif 'm' in self.rload:
                new = self.rload.replace("m","")
                self.rload = ((float(new)*1e-3))
            elif 'u' in self.rload:
                new = self.rload.replace("u","")
                self.rload = ((float(new)*1e-6))
            elif 'n' in self.rload:
                new = self.rload.replace("n","")
                self.rload = ((float(new)*1e-9))
            elif 'p' in self.rload:
                new = self.rload.replace("p","")
                self.rload = ((float(new)*1e-12))
            elif self.rload == '':
                self.rload = 0

            if self.rload == 0:
                messagebox.showerror("Error", "Cannot be Zero!")
            else:
#===========================================Current Divider======================================
                #Current in RN
                self.cur_in_RN = ((float(self.current_in_i2)*float(self.rload))/(float(self.rload)+float(self.RN)))
                self.label_RN.config(text=("Current in Rn: {}A").format(self.convert_to_prefix((self.cur_in_RN))), font=("consolas",15,"bold"))
                
                #Current in RL
                self.cur_in_load = ((float(self.current_in_i2)*float(self.RN))/(float(self.rload)+float(self.RN)))
                self.label_RL.config(text=("Current in Rl: {}A").format(self.convert_to_prefix((self.cur_in_load))), font=("consolas",15,"bold"))
                self.next_button.config(state="normal")
        
    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'

        
    def next(self):
        if self.rL.get() == '0' or self.rL.get() == '':
            messagebox.showerror("Error!","Cannot be zero!")
            self.rL.delete(0,"end")
            return
        else:
            self.root.destroy()
            root = Tk()
            Ex_Window_1(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.rload)

        
        
class Prefix_list:
    def __init__(self, root):
        self.root = root
        self.root.title("Prefixes")
        self.root.geometry('220x220+1100+35')
        self.root.resizable(0,0)
        self.frame = Frame(self.root)
        self.frame.pack()
    
        self.box = Frame(self.frame, width=220, bd=10, bg="black", relief=RIDGE)
        self.box.grid(row=0, column=0)
        #=============================================================================================================================================================
        self.column_1 = Label(self.box, text="SYMBOL", font=('Orbitron', 10, 'bold'))
        self.column_1.grid(row=0, column=0)

        self.column_2 = Label(self.box, text="PREFIX", font=('Orbitron', 10, 'bold'))
        self.column_2.grid(row=0, column=1)

        self.column_3 = Label(self.box, text="VALUE", font=('Orbitron', 10, 'bold'))
        self.column_3.grid(row=0, column=2)

        self.T = Label(self.box, text="T", bg="black", foreground="white", font=('Orbitron', 9))
        self.T.grid(row=1, column=0)
        self.T_pref = Label(self.box, text="Terra", bg="black", foreground="white", font=('Orbitron', 9))
        self.T_pref.grid(row=1, column=1)
        self.T_val = Label(self.box, text="10^12", bg="black", foreground="white", font=('Idroid', 9))
        self.T_val.grid(row=1, column=2)

        self.G = Label(self.box, text="G", bg="black", foreground="white", font=('Orbitron', 9))
        self.G.grid(row=2, column=0)
        self.G_pref = Label(self.box, text="Giga", bg="black", foreground="white", font=('Orbitron', 9))
        self.G_pref.grid(row=2, column=1)
        self.G_val = Label(self.box, text="10^9", bg="black", foreground="white", font=('Idroid', 9))
        self.G_val.grid(row=2, column=2)

        self.M = Label(self.box, text="M", bg="black", foreground="white", font=('Orbitron', 9))
        self.M.grid(row=3, column=0)
        self.M_pref = Label(self.box, text="Mega", bg="black", foreground="white", font=('Orbitron', 9))
        self.M_pref.grid(row=3, column=1)
        self.M_val = Label(self.box, text="10^6", bg="black", foreground="white", font=('Idroid', 9))
        self.M_val.grid(row=3, column=2)

        self.k = Label(self.box, text="k", bg="black", foreground="white", font=('Orbitron', 9))
        self.k.grid(row=4, column=0)
        self.k_pref = Label(self.box, text="kilo", bg="black", foreground="white", font=('Orbitron', 9))
        self.k_pref.grid(row=4, column=1)
        self.k_val = Label(self.box, text="10^3", bg="black", foreground="white", font=('Idroid', 9))
        self.k_val.grid(row=4, column=2)

        self.m = Label(self.box, text="m", bg="black", foreground="white", font=('Orbitron', 9))
        self.m.grid(row=5, column=0)
        self.m_pref = Label(self.box, text="milli", bg="black", foreground="white", font=('Orbitron', 9))
        self.m_pref.grid(row=5, column=1)
        self.m_val = Label(self.box, text="10^-3", bg="black", foreground="white", font=('Idroid', 9))
        self.m_val.grid(row=5, column=2)

        self.u = Label(self.box, text="u", bg="black", foreground="white", font=('Orbitron', 9))
        self.u.grid(row=6, column=0)
        self.u_pref = Label(self.box, text="micro", bg="black", foreground="white", font=('Orbitron', 9))
        self.u_pref.grid(row=6, column=1)
        self.u_val = Label(self.box, text="10^-6", bg="black", foreground="white", font=('Idroid', 9))
        self.u_val.grid(row=6, column=2)

        self.n = Label(self.box, text="n", bg="black", foreground="white", font=('Orbitron', 9))
        self.n.grid(row=7, column=0)
        self.n_pref = Label(self.box, text="nano", bg="black", foreground="white", font=('Orbitron', 9))
        self.n_pref.grid(row=7, column=1)
        self.n_val = Label(self.box, text="10^-9", bg="black", foreground="white", font=('Idroid', 9))
        self.n_val.grid(row=7, column=2)

        self.p = Label(self.box, text="p", bg="black", foreground="white", font=('Orbitron', 9))
        self.p.grid(row=8, column=0)
        self.p_pref = Label(self.box, text="pico", bg="black", foreground="white", font=('Orbitron', 9))
        self.p_pref.grid(row=8, column=1)
        self.p_val = Label(self.box, text="10^-12", bg="black", foreground="white", font=('Idroid', 9))
        self.p_val.grid(row=8, column=2)
        self.root.iconbitmap(resource_path("icon.ico"))

class Instructions:
    def __init__(self, root):
        self.root = root
        self.root.title("Instructions")
        self.root.geometry('200x105+50+35')
        self.root.resizable(0,0)
        self.frame = Frame(self.root)
        self.frame.pack()
        self.box = Frame(self.frame, width=220, bd=10, bg="black", relief=RIDGE)
        self.box.grid(row=0, column=0)
        self.title = Label(self.box, text="INSTRUCTIONS:", font=('Orbitron', 10, 'bold'))
        self.title.grid(row=0, column=0)
        self.ins1 = Label(self.box, bg="black", foreground="white", text="Fill up all the entries.", font=('Orbitron', 9))
        self.ins1.grid(row=1, column=0)
        self.ins2 = Label(self.box, bg="black", foreground="white", text="DO NOT enter zero value.", font=('Orbitron', 9))
        self.ins2.grid(row=2, column=0)
        self.ins3 = Label(self.box, bg="black", foreground="white", text="Use the right prefixes.", font=('Orbitron', 9))
        self.ins3.grid(row=3, column=0)
        self.root.iconbitmap(resource_path("icon.ico"))

        
class Ex_Window_1:
    def __init__(self,root,r1,r2,r3,r4,Is,Vs,Req,RN,rload):
        self.root = root
        self.omega_1 = r1
        self.omega_2 = r2
        self.omega_3 = r3
        self.omega_4 = r4
        self.ampere = Is
        self.volt = Vs
        self.Req = Req
        self.RN = RN
        self.rload = rload
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)
        self.next_button = Button(self.canvas, text="next", command=self.next)
        self.next_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.canvas_for_figure = Canvas(self.canvas, bg="royalblue3", width=500, height=350, bd=10, relief=RIDGE)
        self.canvas_for_figure.place(relx=0.29, rely=0.5, anchor=CENTER)
        self.canvas_explain = Canvas(self.canvas, bg="royalblue3", bd=10, height=500, relief=RIDGE)
        self.canvas_explain.place(relx=0.77, rely=0.5, anchor=CENTER)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.label_r1 = Label(self.canvas, text="R1", bg="floral white", font=("Orbitron", 9))
        self.label_r1.place(x=175,y=265)
        self.label_r2 = Label(self.canvas, text="R2", bg="floral white", font=("Orbitron", 9))
        self.label_r2.place(x=246,y=190)
        self.label_r3 = Label(self.canvas, text="R3", bg="floral white", font=("Orbitron", 9))
        self.label_r3.place(x=380,y=265)
        self.label_r4 = Label(self.canvas, text="R4", bg="floral white", font=("Orbitron", 9))
        self.label_r4.place(x=246,y=350)
        
        
        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)
        
        self.label_step = Label(self.canvas_for_figure, bd=5, relief=RIDGE, text="STEP 1: Solve for the Rn", font=("Orbitron",11,"bold"))
        self.label_step.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label_r1 = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="R1 = {}\u2126".format(self.convert_to_prefix((float(self.omega_1)))))
        self.label_r1.place(relx=0.3, rely=0.25, anchor="center")
        self.label_r2 = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="R2 = {}\u2126".format(self.convert_to_prefix((float(self.omega_2)))))
        self.label_r2.place(relx=0.3, rely=0.35, anchor="center")
        self.label_r3 = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="R3 = {}\u2126".format(self.convert_to_prefix((float(self.omega_3)))))
        self.label_r3.place(relx=0.7, rely=0.25, anchor="center")
        self.label_r4 = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="R4 = {}\u2126".format(self.convert_to_prefix((float(self.omega_4)))))
        self.label_r4.place(relx=0.7, rely=0.35, anchor="center")

        self.label_sol_for_Req = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="Req = R1 + R2 + R4 = {}\u2126".format(self.convert_to_prefix((float(self.Req)))))
        self.label_sol_for_Req.place(relx=0.5, rely=0.5, anchor="center")

        self.label_sol_for_Rn = Label(self.canvas_explain, font=("Consolas",11), bg="royalblue3", text="Rn = Req || R3")
        self.label_sol_for_Rn.place(relx=0.5, rely=0.6, anchor="center")

        self.label_sol_for_Rn2 = Label(self.canvas_explain, font=("Consolas",11,"bold"), bg="royalblue3", text="Rn = {}\u2126".format(self.convert_to_prefix((float(self.RN)))))
        self.label_sol_for_Rn2.place(relx=0.5, rely=0.7, anchor="center")

        self.label_explain = Label(self.canvas_explain, bg="royalblue3", text="Set the independent sources equal to zero.Then",
                                   font=("Consolas",11,"bold"))
        self.label_explain.place(relx=0.5, rely=0.1, anchor="center")
        self.label_explain_2 = Label(self.canvas_explain, bg="royalblue3", text="solve for the total resistor of the circuit.",font=("Consolas",11,"bold"))
        self.label_explain_2.place(relx=0.035, rely=0.15, anchor="w")

        self.load = Image.open(resource_path("Rn.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_figure, image=self.render, bd=5)
        self.img.image = self.render
        self.img.place(relx=0.5, rely=0.5, anchor="center")

        next_fig = Button(self.canvas, text="Next", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.next)
        next_fig.place(relx=0.4, rely=0.9, anchor="center")

        form_b = Button(self.canvas, text="Formula", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.formula)
        form_b.place(relx=0.3, rely=0.1, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'
        
    def next(self):
        self.root.destroy()
        root = Tk()
        Ex_Window_2(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.rload)
        
    def formula(self):
        top = Toplevel()
        Formulas(top)

class Formulas:
    def __init__(self,root):
        self.root = root
        self.root.title("Formula")
        self.root.geometry('300x300+0+0')
        self.root.resizable(0,0)
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.frame = Frame(self.canvas)

        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        vertscroll = Scrollbar(self.canvas,orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vertscroll.set)
        self.canvas_frame = self.canvas.create_window((4,4),window=self.frame, anchor="nw")
        vertscroll.pack(side=RIGHT, fill=Y)
        
        self.load_2 = Image.open(resource_path("Formula.png"))
        self.render_2 = ImageTk.PhotoImage(self.load_2)
        self.img_2 = Label(self.frame, image=self.render_2, bd=5)
        self.img_2.image = self.render_2
        self.img_2.pack(anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

class Ex_Window_2:
    def __init__(self,root,r1,r2,r3,r4,Is,Vs,Req,RN,rload):
        self.root = root
        self.omega_1 = r1
        self.omega_2 = r2
        self.omega_3 = r3
        self.omega_4 = r4
        self.ampere = Is
        self.volt = Vs
        self.Req = Req
        self.RN = RN
        self.rload = rload
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)
        self.canvas_for_figure = Canvas(self.canvas, bg="royalblue3", width=500, height=350, bd=10, relief=RIDGE,)
        self.canvas_for_figure.place(relx=0.29, rely=0.5, anchor=CENTER)
        self.canvas_explain = Canvas(self.canvas, bg="royalblue3", bd=10, height=500, relief=RIDGE)
        self.canvas_explain.place(relx=0.77, rely=0.5, anchor=CENTER)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.label_step = Label(self.canvas_for_figure, bd=5, relief=RIDGE, font=("Orbitron",11,"bold"), text="STEP 2: Solve for In")
        self.label_step.place(relx=0.5, rely=0.1, anchor="center")

        self.label_r1 = Label(self.canvas, text="R1", bg="floral white", font=("Orbitron", 9))
        self.label_r1.place(x=210,y=240)
        self.label_r2 = Label(self.canvas, text="R2", bg="floral white", font=("Orbitron", 9))
        self.label_r2.place(x=246,y=205)
        self.label_r3 = Label(self.canvas, text="R3", bg="floral white", font=("Orbitron", 9))
        self.label_r3.place(x=343,y=290)
        self.label_r4 = Label(self.canvas, text="R4", bg="floral white", font=("Orbitron", 9))
        self.label_r4.place(x=246,y=330)
        self.label_Is = Label(self.canvas, text="Is", bg="floral white", font=("Orbitron", 9))
        self.label_Is.place(x=110,y=265)
        self.label_Vs = Label(self.canvas, text="Vs", bg="floral white", font=("Orbitron", 9))
        self.label_Vs.place(x=215,y=300)
        
        self.label_title = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="To find In, we short-circuit terminals a and b")
        self.label_title.place(relx=0.5, rely=0.1, anchor="center")
        self.label_title_2 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="We ignore the R3 resistor because it has been")
        self.label_title_2.place(relx=0.03, rely=0.15, anchor="w")
        self.label_title_3 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="short-circuited. Applying mesh analysis,")
        self.label_title_3.place(relx=0.03, rely=0.2, anchor="w")
        self.label_title_4 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="we obtain:")
        self.label_title_4.place(relx=0.03, rely=0.25, anchor="w")
        self.label_title_5 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="For loop (a)")
        self.label_title_5.place(relx=0.5, rely=0.35, anchor="center")

        self.Ibbb = (float(self.omega_1)+float(self.omega_2)+float(self.omega_4))
        self.Ibb = ((float(self.omega_1)*float(self.ampere))+float(self.volt))
        self.Ib = self.Ibb/self.Ibbb

        self.label_I = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11), text="Ia = {}A".format(self.convert_to_prefix(float(self.ampere))))
        self.label_I.place(relx=0.5, rely=0.4, anchor="center")

        self.label_title_6 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="For loop (b)")
        self.label_title_6.place(relx=0.5, rely=0.5, anchor="center")
        self.label_I2 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11),
                              text="{}(Ib - Ia) + {}Ib = {}".format(self.convert_to_prefix(float(self.omega_1)),
                                                                    self.convert_to_prefix(float(self.omega_2)+float(self.omega_4)),
                                                                    self.convert_to_prefix(float(self.volt))))
        self.label_I2.place(relx=0.5, rely=0.58, anchor="center")
        self.label_I2a = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11),
                             text="{}Ib - {}Ia = {}".format(self.convert_to_prefix(self.Ibbb),
                                                            self.convert_to_prefix(float(self.omega_1)),self.convert_to_prefix(float(self.volt))))
        self.label_I2a.place(relx=0.5, rely=0.63, anchor="center")

        self.label_I2b = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11), text="Substituting Ia, we obtain")
        self.label_I2b.place(relx=0.5, rely=0.68, anchor="center")
        self.label_I2c = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11),
                               text="{}Ib = {}".format(self.convert_to_prefix(float(self.Ibbb)),self.convert_to_prefix(float(self.Ibb))))
        self.label_I2c.place(relx=0.5, rely=0.72, anchor="center")

        self.label_I2d = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="Ib = {}A = In".format(self.convert_to_prefix(self.Ib)))
        self.label_I2d.place(relx=0.5, rely=0.78, anchor="center")                                            

        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)

        self.load = Image.open(resource_path("finding cur.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_figure, image=self.render, bd=5)
        self.img.image = self.render
        self.img.place(relx=0.5, rely=0.5, anchor="center")

        next_fig = Button(self.canvas, text="Next", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.next)
        next_fig.place(relx=0.4, rely=0.9, anchor="center")
        
        back_fig = Button(self.canvas, text="Back", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.back)
        back_fig.place(relx=0.2, rely=0.9, anchor="center")

        form_b = Button(self.canvas, text="Formula", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.formula)
        form_b.place(relx=0.3, rely=0.1, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'

    def back(self):
        self.root.destroy()
        root = Tk()
        Ex_Window_1(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.rload)

    def next(self):
        self.root.destroy()
        root = Tk()
        Alternative_solution(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.Ib,self.rload)

    def formula(self):
        top = Toplevel()
        Formulas(top)
        
class Alternative_solution:
    def __init__(self,root,r1,r2,r3,r4,Is,Vs,Req,RN,Ib,rload):
        self.root = root
        self.omega_1 = r1
        self.omega_2 = r2
        self.omega_3 = r3
        self.omega_4 = r4
        self.ampere = Is
        self.volt = Vs
        self.Req = Req
        self.RN = RN
        self.Ib = Ib
        self.rload = rload
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)
        self.canvas_for_figure = Canvas(self.canvas, bg="royalblue3", width=500, height=350, bd=10, relief=RIDGE)
        self.canvas_for_figure.place(relx=0.29, rely=0.5, anchor=CENTER)
        self.canvas_explain = Canvas(self.canvas, bg="royalblue3", bd=10, height=500, relief=RIDGE)
        self.canvas_explain.place(relx=0.77, rely=0.5, anchor=CENTER)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.label_r1 = Label(self.canvas, text="R1", bg="floral white", font=("Orbitron", 9))
        self.label_r1.place(x=218,y=228)
        self.label_r2 = Label(self.canvas, text="R2", bg="floral white", font=("Orbitron", 9))
        self.label_r2.place(x=270,y=190)
        self.label_r3 = Label(self.canvas, text="R3", bg="floral white", font=("Orbitron", 9))
        self.label_r3.place(x=380,y=300)
        self.label_r4 = Label(self.canvas, text="R4", bg="floral white", font=("Orbitron", 9))
        self.label_r4.place(x=270,y=345)
        self.label_Is = Label(self.canvas, text="Is", bg="floral white", font=("Orbitron", 9))
        self.label_Is.place(x=110,y=265)
        self.label_Vs = Label(self.canvas, text="Vs", bg="floral white", font=("Orbitron", 9))
        self.label_Vs.place(x=230,y=300)

        self.label_title = Label(self.canvas_for_figure, bd=5, relief=RIDGE, text="Alternative solution for In", font=("Orbitron",11))
        self.label_title.place(relx=0.5, rely=0.1, anchor="center")

        self.label1 = Label(self.canvas_explain, bg="royalblue3", text="Alternatively, we may determine In = Vth/Rth.", font=("Consolas",11))
        self.label1.place(relx=0.03, rely=0.1, anchor="w")
        self.label2 = Label(self.canvas_explain, bg="royalblue3", text="We obtain Vth as the open-circuit voltage", font=("Consolas",11))
        self.label2.place(relx=0.03, rely=0.15, anchor="w")
        self.label3 = Label(self.canvas_explain, bg="royalblue3", text="across terminals a and b.", font=("Consolas",11))
        self.label3.place(relx=0.03, rely=0.2, anchor="w")
        
        self.label4 = Label(self.canvas_explain, bg="royalblue3", text="For loop (c)", font=("Consolas",11, "bold"))
        self.label4.place(relx=0.5, rely=0.25, anchor="center")
        self.label5 = Label(self.canvas_explain, bg="royalblue3", text="Ic = {}A".format(self.convert_to_prefix(float(self.ampere))), font=("Consolas",11))
        self.label5.place(relx=0.5, rely=0.35, anchor="center")
        self.label6 = Label(self.canvas_explain, bg="royalblue3", text="For loop (d)", font=("Consolas",11, "bold"))
        self.label6.place(relx=0.5, rely=0.45, anchor="center")
        
        self.add = (float(self.omega_1)+float(self.omega_2)+float(self.omega_3)+float(self.omega_4))
        self.sub = (float(self.omega_1)*float(self.ampere))
        self.v = ((self.sub)+ float(self.volt))
        self.id = self.v/self.add
        self.vth = float(self.omega_3)*self.id
        self.label7 = Label(self.canvas_explain, bg="royalblue3", text="{}Id - {}Ic = {}".format(self.convert_to_prefix(self.add),
                                                                                self.convert_to_prefix(float(self.omega_1)),
                                                                                self.convert_to_prefix(float(self.volt))), font=("Consolas",11))
        self.label7.place(relx=0.5, rely=0.55, anchor="center")
        self.label8 = Label(self.canvas_explain, bg="royalblue3", text="Substituting Ic we get,", font=("Consolas",11,"bold"))
        self.label8.place(relx=0.5, rely=0.6, anchor="center")
        self.label9 = Label(self.canvas_explain, bg="royalblue3", text="{}Id = {}".format(self.convert_to_prefix(float(self.add)),self.convert_to_prefix(float(self.v))), font=("Consolas",11))
        self.label9.place(relx=0.5, rely=0.65, anchor="center")
        self.label10 = Label(self.canvas_explain, bg="royalblue3", text="Id = {}A".format(self.convert_to_prefix(self.id)), font=("Consolas",11))
        self.label10.place(relx=0.5, rely=0.7, anchor="center")
        self.label11 = Label(self.canvas_explain, bg="royalblue3", text="and Vth = {}Id = {}V".format(self.convert_to_prefix(float(self.omega_3)),
                                                                                     self.convert_to_prefix(float(self.vth))), font=("Consolas",11))
        self.label11.place(relx=0.5, rely=0.75, anchor="center")
        self.label12 = Label(self.canvas_explain, bg="royalblue3", text="{}Vth/{}Rth = {}A".format(self.convert_to_prefix(float(self.vth)),
                                                                                  self.convert_to_prefix(float(self.RN)),
                                                                                  self.convert_to_prefix(float(self.Ib))), font=("Consolas",11,"bold"))
        self.label12.place(relx=0.5, rely=0.8, anchor="center")

        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)

        self.load = Image.open(resource_path("alternative solution.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_figure, image=self.render, bd=5)
        self.img.image = self.render
        self.img.place(relx=0.5, rely=0.5, anchor="center") 
        
        back_fig = Button(self.canvas, text="Back", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.back)
        back_fig.place(relx=0.2, rely=0.9, anchor="center")
        
        nextfig = Button(self.canvas, text="Next", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.next)
        nextfig.place(relx=0.4, rely=0.9, anchor="center")

        form_b = Button(self.canvas, text="Formula", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.formula)
        form_b.place(relx=0.3, rely=0.1, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))


    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'


    def back(self):
        self.root.destroy()
        root = Tk()
        Ex_Window_2(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.rload)

    def formula(self):
        top = Toplevel()
        Formulas(top)

    def next(self):
        self.root.destroy()
        root = Tk()
        Ex_Window_3(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.Ib,self.rload)

        
class Ex_Window_3:
    def __init__(self,root,r1,r2,r3,r4,Is,Vs,Req,RN,Ib,rload):
        self.root = root
        self.omega_1 = r1
        self.omega_2 = r2
        self.omega_3 = r3
        self.omega_4 = r4
        self.ampere = Is
        self.volt = Vs
        self.Req = Req
        self.RN = RN
        self.Ib = Ib
        self.rload = rload
        self.root.geometry("1024x576+175+90")
        self.root.title("Norton")
        self.root.resizable(0,0)
        self.root.config(bg="black", bd=10, relief=GROOVE)
        self.canvas = Canvas(self.root, bg="white", bd=10, relief=GROOVE)
        self.canvas.pack(expand=1, fill=BOTH)
        self.canvas_for_figure = Canvas(self.canvas, bg="royalblue3", width=500, height=350, bd=10, relief=RIDGE)
        self.canvas_for_figure.place(relx=0.29, rely=0.5, anchor=CENTER)
        self.canvas_explain = Canvas(self.canvas, bg="royalblue3", bd=10, height=500, relief=RIDGE)
        self.canvas_explain.place(relx=0.77, rely=0.5, anchor=CENTER)
        self.root.bind("<Configure>", lambda event, canvas=self.canvas: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.label_Is = Label(self.canvas, text="Is", bg="floral white", font=("Orbitron", 9))
        self.label_Is.place(x=150,y=265)
        self.label_Rn = Label(self.canvas, text="Rn", bg="floral white", font=("Orbitron", 9))
        self.label_Rn.place(x=300,y=265)
        self.label_RL = Label(self.canvas, text="Rl", bg="floral white", font=("Orbitron", 9))
        self.label_RL.place(x=470,y=265)
        
        self.label_step = Label(self.canvas_for_figure, bd=5, relief=RIDGE, font=("Orbitron",11,"bold"), text="STEP 3: Find current in each resistor")
        self.label_step.place(relx=0.5, rely=0.1, anchor="center")

        self.label_title = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="We can use the current divider formula to get")
        self.label_title.place(relx=0.03, rely=0.1, anchor="w")
        self.label_title_2 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="the current in Rn and RL")
        self.label_title_2.place(relx=0.03, rely=0.15, anchor="w")
        self.label_In = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11), text="In = {}A".format(self.convert_to_prefix(float(self.Ib))))
        self.label_In.place(relx=0.5, rely=0.25, anchor="center")
        self.label_Rn = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11), text="Rn = {}\u2126".format(self.convert_to_prefix(float(self.RN))))
        self.label_Rn.place(relx=0.5, rely=0.3, anchor="center")
        self.label_Rl = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11), text="Rl = {}\u2126".format(self.convert_to_prefix(float(self.rload))))
        self.label_Rl.place(relx=0.5, rely=0.35, anchor="center")

        self.parallel = ((1/float(self.RN)) + (1/float(self.rload)))**-1
        self.cur_in_RN = ((float(self.Ib)*self.parallel)/float(self.RN))
        self.cur_in_RL = ((float(self.Ib)*self.parallel)/float(self.rload))

        self.label_asd = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="Current in RN")
        self.label_asd.place(relx=0.5, rely=0.4, anchor="center")
        self.label_Ins = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11),
                               text="({}A*{}\u2126)/{}\u2126".format(self.convert_to_prefix(float(self.Ib)),
                                                       self.convert_to_prefix(float(self.parallel)),self.convert_to_prefix(float(self.RN))))
        self.label_Ins.place(relx=0.5, rely=0.45, anchor="center")

        self.label_asd2 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="= {}A".format(self.convert_to_prefix(self.cur_in_RN)))
        self.label_asd2.place(relx=0.5, rely=0.55, anchor="center")

        self.label_fgh = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="Current in RL")
        self.label_fgh.place(relx=0.5, rely=0.65, anchor="center")
        self.label_Ins = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11),
                               text="({}A*{}\u2126)/{}\u2126".format(self.convert_to_prefix(float(self.Ib)),
                                                       self.convert_to_prefix(float(self.parallel)),self.convert_to_prefix(float(self.rload))))
        self.label_Ins.place(relx=0.5, rely=0.7, anchor="center")
        self.label_asd3 = Label(self.canvas_explain, bg="royalblue3", font=("Consolas",11,"bold"), text="= {}A".format(self.convert_to_prefix(self.cur_in_RL)))
        self.label_asd3.place(relx=0.5, rely=0.8, anchor="center")
        
        img = Image.open(resource_path("Front.png"))
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(1,1,image = self.canvas.image)

        self.load = Image.open(resource_path("rload.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.canvas_for_figure, image=self.render, bd=5)
        self.img.image = self.render
        self.img.place(relx=0.5, rely=0.5, anchor="center")

        next_fig = Button(self.canvas, text="Solve Again", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.back_to_main)
        next_fig.place(relx=0.4, rely=0.9, anchor="center")
        
        back_fig = Button(self.canvas, text="Back", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.back)
        back_fig.place(relx=0.2, rely=0.9, anchor="center")

        form_b = Button(self.canvas, text="Formula", font=("Orbitron",10), width=10, bd=5, relief=RAISED, command=self.formula)
        form_b.place(relx=0.3, rely=0.1, anchor="center")
        self.root.iconbitmap(resource_path("icon.ico"))

    def drop_4_decimal(self,num):
        return int(num*1e4)/1e4
            
    def convert_to_prefix(self,num):
        if int(num) == 0:
            if num <= 10**-9:
                return str(self.drop_4_decimal(num/10**-12)) + ' p'
            elif num > 10**-9 and num < 10**-6:
                return str(self.drop_4_decimal(num/10**-9)) + ' n'
            elif num > 10**-6 and num < 10**-3:
                return str(self.drop_4_decimal(num/10**-6)) + ' u'    
            else:
                return str(self.drop_4_decimal(num/10**-3)) + ' m'
        else:
            if num > 0 and num < 10**3:
                return str(self.drop_4_decimal(num))
            elif num >= 10**3 and num < 10**6:
                return str(self.drop_4_decimal(num/10**3)) + ' k'
            elif num >= 10**6 and num < 10**9:
                return str(self.drop_4_decimal(num/10**6)) + ' M'
            elif num >= 10**9 and num < 10**12:
                return str(self.drop_4_decimal(num/10**9)) + ' G'
            elif num >= 10**12:
                return str(self.drop_4_decimal(num/10**12)) + ' T'

    def back(self):
        self.root.destroy()
        root = Tk()
        Alternative_solution(root,self.omega_1,self.omega_2,self.omega_3,self.omega_4,self.ampere,self.volt,self.Req,self.RN,self.Ib,self.rload)

    def back_to_main(self):
        self.root.destroy()
        root = Tk()
        Norton(root)

    def formula(self):
        top = Toplevel()
        Formulas(top)


#===== Tk() =======
root = Tk()
Front_page(root)
root.mainloop()

