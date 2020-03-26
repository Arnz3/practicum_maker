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


def add_foto(names, oneperson=False):
    if oneperson:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
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
        i = 0
        for i in range(len(names)):
            p2.add_run(names[i])
            p2.add_run(" " * 7)
            i += 1


def add_info(vraag, info):
    p = doc.add_paragraph()
    p.add_run(vraag).bold = True
    p.add_run(info)


def create_doc():
    doc = Document()
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
    # -------------------------------
    logo = doc.add_picture("pictures\\logo_vti.jpg", width=Cm(5.66), height=Cm(3.59))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    namen = ("Arno", "senne", "matthias")
    add_titel("practicum 1")
    add_titel("Proefondervinderlijk blal bla a boem de la kaka")
    add_spec("Het verslag van:")
    add_foto(namen[0], True)
    add_spec("De groepsleden:")
    add_foto(namen)
    add_info("Datum van het practicum: ", "07/01/2020")
    add_info("Klas: ", "4IW")
    add_info("Vak: ", "Chemie")
    add_info("Schooljaar: ", "2019 - 2020")
    add_info("Leerkracht: ", "Ing. B. Aernoudt")
    doc.save(fileName)


info = Label(root, text="Welkom bij Practicum Maker, Vul de gegevens in en druk dan op ...").pack()

vak_e = Entry(root, width=50)
vak_e.pack()
vak_e.insert(0, "Vak")

pracNr_e = Entry(root, width=50)
pracNr_e.pack()
pracNr_e.insert(0, "Practicum Nummer")

pracTitel_e = Entry(root, width=100)
pracTitel_e.pack()
pracTitel_e.insert(0, "Practicum Titel")

naam_e = Entry(root, width=50)
naam_e.pack()
naam_e.insert(0, "Naam + Voornaam")

leden_e = Entry(root, width=100)
leden_e.pack()
leden_e.insert(0, "Groepsleden")

datum_e = Entry(root, width=50)
datum_e.pack()
datum_e.insert(0, "Datum van het practicum")

klas_e = Entry(root, width=50)
klas_e.pack()
klas_e.insert(0, "Klas")

jaar_e = Entry(root, width=50)
jaar_e.pack()
jaar_e.insert(0, "Schooljaar")
