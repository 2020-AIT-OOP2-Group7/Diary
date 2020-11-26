from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "日記なんて久しぶりに書いた""

    def get_author(self):
        return "KAME"