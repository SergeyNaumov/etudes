# simple_table_html.py
import os.path
from fpdf import FPDF, HTMLMixin
 
class HTML2PDF(FPDF, HTMLMixin):
    pass

def read_template(file):
  handle=open(file)
  data=handle.read()
  handle.close()
  return data

def simple_demo():
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  pdf.add_page()
  pdf.add_font('FreeSans', '', './fonts/FreeSans.ttf', uni=True)
  pdf.set_font("FreeSans")
  pdf.cell(200, 10, txt="Привет", ln=1, align="C")
  pdf.output("simple_demo.pdf")

def html2pdf(html):
  pdf = HTML2PDF()
  dir = os.path.dirname('./fonts')
  font = os.path.join(dir, 'font', 'DejaVuSansCondensed.ttf')
  #print('font:',font)
  pdf.add_font('FreeSans', '', font, uni=True) # 
  #pdf.add_font('FreeSans', '', './fonts/FreeSans.ttf', uni=True) # 
  #pdf.set_font('FreeSans', '', 14)
  pdf.add_page()

  pdf.write_html(u"hello!")
  fn = 'html2pdf.pdf'
  pdf.output(fn,'F')
  #pdf.output('html2pdf.pdf')


 
if __name__ == '__main__':
  html=read_template('./templates/template1.html')
  html2pdf(html)

