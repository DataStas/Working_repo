from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, title_header_name):
        super().__init__()
        self.title_header = title_header_name
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
    
    def header(self):
        # Arial bold 15
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        # Calculate width of title and position
        w = self.get_string_width(self.title_header) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, self.title_header, 1, 1, 'С', 1)
        # Line break
        self.ln(10)

    def footer(self):
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Страница ' + str(self.page_no()), 0, 0, 'L')

    def chapter_title(self, num, label):
        # Arial 12
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 15, 'Часть %d : %s' % (num, label), 0, 1, 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name, image_names):
        # Read text file
        name = "./txts/" + name 
        try:
            with open(name, 'rb') as fh:
                txt = fh.read().decode('utf-8')
        except FileNotFoundError:
            print('Файл с текстом не найден')
        self.write(1, txt)
        self.ln(50)
        try:
            for ind, image in enumerate(image_names):
                if ind % 2 == 0:
                    self.add_page()
                    y = 40
                if image[:3] == 'pie':
                    h = 120
                    w = 120
                else:
                    h = 120
                    w = 160
                image = './pngs/' + image
                self.image(name=image, x=20, y=y, h=h, w=w)
                y += 123

        except FileNotFoundError:
            print("Файл с картинкой не найден")

    def print_chapter(self, num, title, name, image_names):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name, image_names)