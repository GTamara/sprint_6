import datetime


class HelperFunctions:

    @staticmethod
    def get_tomorrow_date():
        today: date = datetime.date.today()
        tomorrow_date = today + datetime.timedelta(days=1)
        return str(tomorrow_date)

    @staticmethod
    def get_text_from_raw_html(raw_html: str):
        words_list = raw_html.split()
        return ' '.join(words_list)
