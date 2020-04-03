from tkinter import *

HEIGHT = 600
WIDTH = 700


def add_lid():
    global leden_aantl
    leden_aantl += 1
    if leden_aantl == 2:
        lid2_e.place(relx=0.25, rely=0.4, relwidth=0.7)
    elif leden_aantl == 3:
        lid3_e.place(relx=0.25, rely=0.6, relwidth=0.7)
    elif leden_aantl == 4:
        lid4_e.place(relx=0.25, rely=0.8, relwidth=0.7)
    elif leden_aantl > 4:
        leden_aantl = 4


def del_lid():
    global leden_aantl
    leden_aantl -= 1
    if leden_aantl == 3:
        lid4_e.place_forget()
    elif leden_aantl == 2:
        lid3_e.place_forget()
    elif leden_aantl == 1:
        lid2_e.place_forget()
    elif leden_aantl < 1:
        leden_aantl = 1


def show_help():
    helper.place_forget()
    vak_e.place_forget()
    prac_nr_e.place_forget()
    prac_titel_e.place_forget()
    datum_e.place_forget()
    klas_e.place_forget()
    jaar_e.place_forget()
    ber.place_forget()

    naam_e.place_forget()
    lid1_e.place_forget()
    if leden_aantl == 2:
        lid2_e.place_forget()
    elif leden_aantl == 3:
        lid2_e.place_forget()
        lid3_e.place_forget()
    elif leden_aantl == 4:
        lid2_e.place_forget()
        lid3_e.place_forget()
        lid4_e.place_forget()

    filename_e.place_forget()
    path_b.place_forget()

    back.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.8)
    vak_i.place(relx=0.25, rely=0, relwidth=0.7)
    prac_nr_i.place(relx=0.25, rely=0.14, relwidth=0.7)
    prac_titel_i.place(relx=0.25, rely=0.28, relwidth=0.7)
    datum_i.place(relx=0.25, rely=0.42, relwidth=0.7)
    klas_i.place(relx=0.25, rely=0.56, relwidth=0.7)
    jaar_i.place(relx=0.25, rely=0.70, relwidth=0.7)
    ber_i.place(relx=0.25, rely=0.84, relwidth=0.7)

    naam_i.place(relx=0.25, rely=0, relwidth=0.7)
    leden1_i.place(relx=0.25, rely=0.3, relwidth=0.7)
    leden2_i.place(relx=0.25, rely=0.5, relwidth=0.7)

    filename_i.place(relx=0.25, rely=0, relwidth=0.7)


def go_back():
    global leden_aantl

    back.place_forget()
    vak_i.place_forget()
    prac_nr_i.place_forget()
    prac_titel_i.place_forget()
    datum_i.place_forget()
    klas_i.place_forget()
    jaar_i.place_forget()
    ber_i.place_forget()

    naam_i.place_forget()
    leden1_i.place_forget()
    leden2_i.place_forget()

    filename_i.place_forget()

    helper.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.8)
    vak_e.place(relx=0.25, rely=0, relwidth=0.7)
    prac_nr_e.place(relx=0.25, rely=0.14, relwidth=0.7)
    prac_titel_e.place(relx=0.25, rely=0.28, relwidth=0.7)
    klas_e.place(relx=0.25, rely=0.56, relwidth=0.7)
    jaar_e.place(relx=0.25, rely=0.70, relwidth=0.7)
    ber.place(relx=0.25, rely=0.84)
    naam_e.place(relx=0.25, rely=0, relwidth=0.7)
    lid1_e.place(relx=0.25, rely=0.2, relwidth=0.7)

    if leden_aantl == 2:
        lid2_e.place(relx=0.25, rely=0.4, relwidth=0.7)
    elif leden_aantl == 3:
        lid2_e.place(relx=0.25, rely=0.4, relwidth=0.7)
        lid3_e.place(relx=0.25, rely=0.6, relwidth=0.7)
    elif leden_aantl == 4:
        lid2_e.place(relx=0.25, rely=0.4, relwidth=0.7)
        lid3_e.place(relx=0.25, rely=0.6, relwidth=0.7)
        lid4_e.place(relx=0.25, rely=0.8, relwidth=0.7)

    filename_e.place(relx=0.25, rely=0, relwidth=0.45)
    path_b.place(relx=0.75, rely=0, relwidth=0.2)


# ----------   GUI   ----------

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

welcome_frame = Frame(root, bd=5)
welcome_frame.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.1)

welcome = Label(welcome_frame, text="Welkom bij Practicum Maker. Vul de gegevens in om een practicum te maken")
welcome.place(relwidth=0.75, relheight=1)

helper = Button(welcome_frame, text="Help", command=show_help)
back = Button(welcome_frame, text="back", command=go_back)
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

lid2_e = Entry(groep_frame)
lid3_e = Entry(groep_frame)
lid4_e = Entry(groep_frame)

add = Button(groep_frame, text="+", command=add_lid)
add.place(relx=0.02, rely=0.8, relwidth=0.1)
sub = Button(groep_frame, text="-", command=del_lid)
sub.place(relx=0.13, rely=0.8, relwidth=0.1)

# ----------   BESTAND   ---------

file_frame = LabelFrame(root, text="Bestand", bd=5)
file_frame.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.13)

filename_l = Label(file_frame, text="Bestandsnaam:")
filename_l.place(relx=0.02, rely=0, relwidth=0.2)
filename_e = Entry(file_frame)
filename_e.place(relx=0.25, rely=0, relwidth=0.45)

path_b = Button(file_frame, text="locatie", command='')
path_b.place(relx=0.75, rely=0, relwidth=0.2)

create_file = Button(file_frame, text="Maak Practicum", command='')
create_file.place(relx=0.4, rely=0.5, relwidth=0.2)

# ----------   ERRORS   ----------

errors = LabelFrame(root, text="ERRORS", bd=5)
errors.place(relx=0.1, rely=0.83, relwidth=0.8)

# ----------   HELP   ----------

vak_i = Label(info_frame, text="Vul hier het vak in")

prac_nr_i = Label(info_frame, text="Vul het nummer in van het practicum")

prac_titel_i = Label(info_frame, text="Vul het titel van het practicum in")

datum_i = Label(info_frame, text="Datum waarop het practicum werd uitgevoerd")

klas_i = Label(info_frame, text="Vul je klas in (zorg dat deze in het systeem zit)")

jaar_i = Label(info_frame, text="Vul het schooljaar in")

ber_i = Label(info_frame, text="Moet er een kop berekenigen in het verslag staan")

naam_i = Label(groep_frame, text="Vul je eigen naam in (Naam + Voornaam)")

leden1_i = Label(groep_frame, text="Vul de namen in van je groepsleden (Naam + Voornaam)")
leden2_i = Label(groep_frame, text="Druk op + en - om leden toe te voegen of te verwijderen")

filename_i = Label(file_frame, text="Vul de bestandsnaam in en selecteer een bestandlocatie")

root.mainloop()
