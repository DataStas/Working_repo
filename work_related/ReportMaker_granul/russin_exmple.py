from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

text = u"""
English: Hello World
Greek: Γειά σου κόσμος
Polish: Witaj świecie
Portuguese: Olá mundo
Russian: Здравствуй, Мир
Vietnamese: Xin chào thế giới
Arabic: مرحبا العالم
Hebrew: שלום עולם
"""
with open('exp_info.txt', 'rb') as fh:
    txt = fh.read().decode('utf-8')
# for txt in text.split('\n'):
    pdf.write(1, txt)
    pdf.ln(8)


pdf.output("unicode.pdf", 'F')