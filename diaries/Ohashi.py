from diaries.AbstractDiary import AbstractDiary


class Ohashi(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "宿題が多かった"

    def get_author(self):
        return "Ohashi"