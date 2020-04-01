from tkinter import *

HEIGHT = 600
WIDTH = 700


def add_lid():
    global leden_aantl
    leden_aantl += 1
    if leden_aantl == 2:
        lid2_e = Entry(groep_frame)
        lid2_e.place(relx=0.25, rely=0.4, relwidth=0.7)
    elif leden_aantl == 3:
        lid3_e = Entry(groep_frame)
        lid3_e.place(relx=0.25, rely=0.6, relwidth=0.7)
    elif leden_aantl == 4:
        lid4_e = Entry(groep_frame)
        lid4_e.place(relx=0.25, rely=0.8, relwidth=0.7)
    elif leden_aantl > 4:
        leden_aantl = 4


def del_lid():
    global leden_aantl
    leden_aantl -= 1
    if leden_aantl == 3:
        lid4_e.destroy()
    elif leden_aantl == 2:
        lid3_e.destroy()
    elif leden_aantl == 1:
        lid2_e.destroy()
    elif leden_aantl < 1:
        leden_aantl = 1


root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

welcome_frame = Frame(root, bd=5)
welcome_frame.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.1)

welcome = Label(welcome_frame, text="Welkom bij Practicum Maker. Vul de gegevens in om een practicum te maken")
welcome.place(relwidth=0.75, relheight=1)

helper = Button(welcome_frame, text="Help")
helper.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.8)

# ----------   PRAC INFO   ----------

info_frame = LabelFrame(root, text="Practicum Info", bd=5)
info_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

vak_l = Label(info_frame, text="Vak:")
vak_l.place(relx=0.02, rely=0, relwidth=0.2)
vak_e = Entry(info_frame)
vak_e.place(relx=0.25, rely=0, relwidth=0.7)

prac_nr_l = Label(info_frame, text="Practicum Nummer:")
prac_nr_l.place(relx=0.02, rely=0.14, relwidth=0.2)
prac_nr_e = Entry(info_frame)
prac_nr_e.place(relx=0.25, rely=0.14, relwidth=0.7)

prac_titel_l = Label(info_frame, text="Practicum Titel:")
prac_titel_l.place(relx=0.02, rely=0.28, relwidth=0.2)
prac_titel_e = Entry(info_frame)
prac_titel_e.place(relx=0.25, rely=0.28, relwidth=0.7)

datum_l = Label(info_frame, text="Datum:")
datum_l.place(relx=0.02, rely=0.42, relwidth=0.2)
datum_e = Entry(info_frame)
datum_e.place(relx=0.25, rely=0.42, relwidth=0.7)

klas_l = Label(info_frame, text="Klas:")
klas_l.place(relx=0.02, rely=0.56, relwidth=0.2)
klas_e = Entry(info_frame)
klas_e.place(relx=0.25, rely=0.56, relwidth=0.7)

jaar_l = Label(info_frame, text="Schooljaar:")
jaar_l.place(relx=0.02, rely=0.70, relwidth=0.2)
jaar_e = Entry(info_frame)
jaar_e.place(relx=0.25, rely=0.70, relwidth=0.7)

ber = Checkbutton(info_frame, text="Berekeningen")
ber.place(relx=0.25, rely=0.84)

# ----------   GROEP   ----------
leden_aantl = 1

groep_frame = LabelFrame(root, text="Groep", bd=5)
groep_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.3, )

naam_l = Label(groep_frame, text="Eigen naam:")
naam_l.place(relx=0.02, rely=0, relwidth=0.2)
naam_e = Entry(groep_frame)
naam_e.place(relx=0.25, rely=0, relwidth=0.7)

leden_l = Label(groep_frame, text="Groepsleden:")
leden_l.place(relx=0.02, rely=0.2, relwidth=0.2)
lid1_e = Entry(groep_frame)
lid1_e.place(relx=0.25, rely=0.2, relwidth=0.7)

add = Button(groep_frame, text="+", command=add_lid)
add.place(relx=0.02, rely=0.8, relwidth=0.1)
sub = Button(groep_frame, text="-", command=del_lid)
sub.place(relx=0.13, rely=0.8, relwidth=0.1)

# ----------   BESTAND   ---------

file_frame = LabelFrame(root, text="Bestand", bd=5)
file_frame.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.1)

bestand_l = Label(file_frame, text="Bestandsnaam:")
bestand_l.place(relx=0.02, rely=0, relwidth=0.2)
bestand_e = Entry(file_frame)
bestand_e.place(relx=0.25, rely=0, relwidth=0.45)

create_file = Button(file_frame, text="Maak Practicum", command="")
create_file.place(relx=0.75, rely=0, relwidth=0.2)

# ----------   ERRORS   ----------

errors = LabelFrame(root, text="ERRORS", bd=5)
errors.place(relx=0.1, rely=0.8, relwidth=0.8)

root.mainloop()
