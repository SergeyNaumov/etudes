import jinja2
import pdfkit

def get_html():
  templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
  templateEnv = jinja2.Environment(loader=templateLoader)
  TEMPLATE_FILE = "template1.html"
  template = templateEnv.get_template(TEMPLATE_FILE)
  return template.render(
    name='Mark'
  )



pdfkit.from_string(get_html(), 'out.pdf')
