from docx import *
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

fileName = "practicum.docx"

doc = Document()

logo = doc.add_picture("pictures\\logo_vti.jpg", width=Cm(5.66), height=Cm(3.59))
last_paragraph = doc.paragraphs[-1]
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

list_styles = [s for s in doc.styles if s.type == WD_STYLE_TYPE.LIST]
Titel = doc.styles.add_style("Titel", WD_STYLE_TYPE.PARAGRAPH)
font = Titel.font
font.name = "Verdana"
font.size = Pt(20)

PracNR = doc.add_paragraph()
PracNR.style = doc.styles["Titel"]
PracNR.alignment = 1
run = PracNR.add_run("practicum1")
run.bold = True

PracTitel = doc.add_paragraph()
PracTitel.style = doc.styles["Titel"]
PracTitel.alignment = 1
run = PracTitel.add_run("proefondervindelijk meten van pH waarden van gebruiksvoorwerpen")
run.bold = True

doc.save(fileName)
