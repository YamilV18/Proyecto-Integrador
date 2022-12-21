from fpdf import FPDF
class Generarpdf(FPDF):
    pass
    def texto(self,nombre):
        with open(nombre, 'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,30.0)
        self.set_font('Courier', '', 13)
        self.multi_cell(0,10,txt)
    def titulo(self, title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', "B", 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align="C",txt=title,border=0)
pdf = Generarpdf()
pdf.add_page()
pdf.texto('facturaresultante.txt')
pdf.titulo("FACTURA ELECTRÓNICA")
pdf.set_author("Los 3 reyes vagos")
pdf.output('Factura resultante.pdf','F')
