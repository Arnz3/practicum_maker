from docx import *
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

fileName = "practicum.docx"
doc = Document()

logo = doc.add_picture("pictures\\logo_vti.jpg", width=Cm(5.66), height=Cm(3.59))
last_paragraph = doc.paragraphs[-1]
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

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
        doc.add_picture(f"pictures/{names}.jpg", width=Cm(3), height=Cm(4))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        name = doc.add_paragraph(names)
        name.alignment = 1

    else:
        p = doc.add_paragraph()
        for name in names:
            name = name.lower()
            p.add_run().add_picture(f"pictures/{name}.jpg", width=Cm(3), height=Cm(4))
            p.add_run(" " * 7)
            last_paragraph = doc.paragraphs[-1]
            last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2 = doc.add_paragraph()
        p2.alignment = 1
        i = 0
        for i in range(len(names)):
            p2.add_run(names[i])
            p2.add_run(" " * 7)
            i += 1


namen = ("Arno", "senne", "matthias")
add_titel("practicum 1")
add_titel(" ")
add_titel("Proefondervinderlijk blal bla a boem de la kaka")
add_spec("Het verslag van:")
add_foto(namen[0], True)
add_spec("De groepsleden:")
add_foto(namen)




doc.save(fileName)
