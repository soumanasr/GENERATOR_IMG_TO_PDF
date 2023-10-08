from fpdf import FPDF
import os

pdf=FPDF()
pdf.set_auto_page_break(0)
img_list=[x for x in os.listdir("feb")]
for img in img_list:
    pdf.add_page()
    image="feb\\"+img
    pdf.image(image,w=200,h=260)
pdf.output("palsfa.pdf")
print("completed...........")
