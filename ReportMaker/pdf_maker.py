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

    def print_text_from_txt(self, name):
        try:
            with open(name, 'rb') as fh:
                txt = fh.read().decode('utf-8')
        except FileNotFoundError:
            print('Файл с текстом не найден')
        self.write(10, txt)
        self.add_page()

    def print_images(self, image_names):
        avg_names = [avg_name for avg_name in image_names if avg_name[:3] == 'avg'] 
        image_names = [name for name in image_names if name[:3] != 'avg']

        try:
            for image in image_names:
                image = './pngs/' + image
                if image[:3] == 'pie':
                    h = 120
                    w = 120
                    self.image(name=image, x=20, y=20, h=h, w=w)
                elif image[:3] == 'avg':
                    pass
                else:
                    h = 120
                    w = 160
                    self.image(name=image, x=20, y=20, h=h, w=w)
                self.add_page()
        except FileNotFoundError:
            print("Файл с картинкой {image} не найден")
        h = 100
        w = 140
        ind = 0
        if len(avg_names) > 0:
            while ind <= len(avg_names):
                try:
                    image = './pngs/' + avg_names[ind]
                except IndexError:
                    image = './pngs/' + avg_names[ind-1]
                    image_2 = image
                else:
                    try:
                        image_2 = './pngs/' + avg_names[ind+1]
                    except IndexError:
                        image_2 = image
                try:
                    self.image(name=image, x=10, y=30, h=h, w=w)
                    self.image(name=image_2, x=10, y=130, h=h, w=w)
                except FileNotFoundError:
                    print("Файлы по усреднителю не найдены")
                self.add_page()
                ind += 2
        else:
            print("По усреднителю нет файлов!")
                

    
    
    def chapter_body(self, name, image_names):
        # Read text file
        name = "./txts/" + name
        self.print_text_from_txt(name)
        self.print_images(image_names)
                



    def print_chapter(self, num, title, name, image_names):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name, image_names)