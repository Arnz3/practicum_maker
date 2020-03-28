from docx import *
from tkinter import *
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

root = Tk()
root.title("Practicum Maker")


def add_titel(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.style = doc.styles["Titel"]
    p.alignment = 1
    run = p.add_run(text)
    run.bold = True
    run.underline = True


def add_spec(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.style = doc.styles["specs"]
    p.alignment = 1
    run = p.add_run(text)
    run.bold = True
    run.underline = True


def add_kop(text):
    global nr
    nr += 1
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.style = doc.styles["specs"]
    p.alignment = 0
    run = p.add_run(str(nr) + "." + text)
    run.bold = True
    run.underline = True


def add_foto(names, oneperson=False):
    if oneperson:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        names = names.lower()
        p.add_run().add_picture(f"pictures/{names}.jpg", width=Cm(3), height=Cm(4))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        name = doc.add_paragraph(names)
        name.alignment = 1
        name.paragraph_format.space_after = Pt(0)

    else:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        for name in names:
            name = name.lower()
            p.add_run().add_picture(f"pictures/{name}.jpg", width=Cm(3), height=Cm(4))
            p.add_run(" " * 7)
            last_paragraph = doc.paragraphs[-1]
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2 = doc.add_paragraph()
        p2.alignment = 1
        p2.paragraph_format.space_after = Pt(0)
        for i in range(len(names)):
            p2.add_run(names[i])
            p2.add_run(" " * 7)
            i += 1


def add_info(vraag, info):
    p = doc.add_paragraph()
    p.add_run(vraag).bold = True
    p.add_run(info)


def add_lid():
    global leden_aantl
    leden_aantl += 1
    if leden_aantl == 2:
        global lid2_e
        lid2_e = Entry(root, width=50)
        lid2_e.insert(0, "Naam + Voornaam")
        lid2_e.grid(row=5, column=1, columnspan=2)
    elif leden_aantl == 3:
        global lid3_e
        lid3_e = Entry(root, width=50)
        lid3_e.insert(0, "Naam + Voornaam")
        lid3_e.grid(row=6, column=1, columnspan=2)
    elif leden_aantl == 4:
        global lid4_e
        lid4_e = Entry(root, width=50)
        lid4_e.insert(0, "Naam + Voornaam")
        lid4_e.grid(row=7, column=1, columnspan=2)
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


def create_doc():
    global doc
    doc = Document()
    global leden_aantl
    leden_aantl = 1
    global nr
    nr = 0

    # --------   styles   --------
    # create style "Titel"
    Titel = doc.styles.add_style("Titel", WD_STYLE_TYPE.PARAGRAPH)
    font = Titel.font
    font.name = "Verdana"
    font.size = Pt(20)

    # create style "Normal"
    Normal = doc.styles["Normal"]
    font1 = Normal.font
    font1.name = "Verdana"
    font1.size = Pt(12)

    # create style "specs"
    specs = doc.styles.add_style("specs", WD_STYLE_TYPE.PARAGRAPH)
    font2 = specs.font
    font2.name = "Verdana"
    font2.size = Pt(14)

    vak = vak_e.get()
    pracNr = str(pracNr_e.get()) + " "
    pracTitel = pracTitel_e.get()
    datum = datum_e.get()
    klas = klas_e.get()
    jaar = jaar_e.get()
    filename = filename_e.get() + ".docx"

    naam = naam_e.get()
    if leden_aantl == 1:
        namen = (naam, lid1_e.get())
    elif leden_aantl == 2:
        namen = (naam, lid1_e.get(), lid2_e.get())
    elif leden_aantl == 3:
        namen = (naam, lid1_e.get(), lid2_e.get(), lid3_e.get())
    elif leden_aantl == 4:
        namen = (naam, lid1_e.get(), lid2_e.get(), lid3_e.get(), lid4_e.get())

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run().add_picture("pictures/logo_vti.jpg", width=Cm(5.66), height=Cm(3.59))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_titel("practicum " + str(pracNr) + vak)
    add_titel(pracTitel)
    add_spec("Het verslag van:")
    add_foto(namen[0], True)
    add_spec("De groepsleden:")
    add_foto(namen)
    add_info("Datum van het practicum: ", datum)
    add_info("Klas: ", klas)
    add_info("Vak: ", vak)
    add_info("Schooljaar: ", jaar)
    add_info("Leerkracht: ", "Ing. B. Aernoudt")
    doc.add_page_break()
    add_kop("Doel van de proef")
    add_kop("Benodigdheden")
    add_kop("H- en P- zinnen en gevarensymbolen")
    add_kop("Beschrijving, voorstelling en waarnemingen van de proef")
    add_kop("Vragen")
    add_kop("Berekeningen")
    add_kop("Besluit")
    doc.save(filename)


# --------- GUI ---------

vak_l = Label(root, text="Vak:")
vak_l.grid(row=0, column=0)
vak_e = Entry(root, width=50)
vak_e.grid(row=0, column=1, columnspan=2)
vak_e.insert(0, "Vak")

pracNr_l = Label(root, text="Practicum Nummer:")
pracNr_l.grid(row=1, column=0)
pracNr_e = Entry(root, width=50)
pracNr_e.grid(row=1, column=1, columnspan=2)
pracNr_e.insert(0, "Practicum Nummer")

pracTitel_l = Label(root, text="Practicum Titel:")
pracTitel_l.grid(row=2, column=0)
pracTitel_e = Entry(root, width=50)
pracTitel_e.grid(row=2, column=1, columnspan=2)
pracTitel_e.insert(0, "Practicum Titel")

naam_l = Label(root, text="Eigen naam:")
naam_l.grid(row=3, column=0)
naam_e = Entry(root, width=50)
naam_e.grid(row=3, column=1, columnspan=2)
naam_e.insert(0, "Naam + Voornaam")

leden_l = Label(root, text="Groepsleden:")
leden_l.grid(row=4, column=0)
lid1_e = Entry(root, width=50)
lid1_e.grid(row=4, column=1, columnspan=2)
lid1_e.insert(0, "Naam + Voornaam")

add_lid = Button(root, text="+", command=add_lid)
del_lid = Button(root, text="-", command=del_lid)
add_lid.grid(row=8, column=1)
del_lid.grid(row=8, column=2)

datum_l = Label(root, text="Practicum Datum:")
datum_l.grid(row=9, column=0)
datum_e = Entry(root, width=50)
datum_e.grid(row=9, column=1, columnspan=2)
datum_e.insert(0, "Datum van het practicum")

klas_l = Label(root, text="Klas:")
klas_l.grid(row=10, column=0)
klas_e = Entry(root, width=50)
klas_e.grid(row=10, column=1, columnspan=2)
klas_e.insert(0, "Klas")

jaar_l = Label(root, text="Schooljaar:")
jaar_l.grid(row=11, column=0)
jaar_e = Entry(root, width=50)
jaar_e.grid(row=11, column=1, columnspan=2)
jaar_e.insert(0, "2019 - 2020")

filename_l = Label(root, text="bestandsnaam:")
filename_l.grid(row=12, column=0)
filename_e = Entry(root, width=50)
filename_e.grid(row=12, column=1, columnspan=2)
filename_e.insert(0, "bestandsnaam")

create = Button(root, text="Maak document!", command=create_doc)
create.grid(row=13, column=1)

root.mainloop()
