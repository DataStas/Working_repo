from datetime import datetime

def get_broadcast_data(self):
    """Возвращает дату начало центральной трансляции"""
    month_dict = {"января": 1,
                "февраля": 2,
                    "марта": 3,
                    "апреля": 4,
                    "мая": 5,
                    "июня": 6,
                    "июля": 7,
                    "августа": 8,
                    "сентября": 9,
                    "октября": 10,
                    "ноября": 11,
                    "декабря": 12,}

    data = self.elements_is_visibility(locator=SportLocators.BROADCAST_DATE)[1].text
    data_day, data_month, data_time = data.replace("в", "").split()
    data_str = f"{data_day}-{month_dict[data_month]}-{datetime.datetime.now().year} {data_time}"
    return datetime.datetime.strptime(data_str, "%d-%m-%Y %H:%M")

if __name__ == "__main__":
