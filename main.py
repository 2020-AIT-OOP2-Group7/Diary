from diaries.DiarySample import DiarySample
from diaries.Ohashi import Ohashi
from diaries.FukumotoDiaryNew import FukumotoDiaryNew

diaries = [DiarySample(), Ohashi(),FukumotoDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()