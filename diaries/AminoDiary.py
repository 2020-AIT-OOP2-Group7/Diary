from diaries.AbstractDiary import AbstractDiary


class AminoDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "物理の課題やらなきゃ"

    def get_author(self):
        return "Amino"