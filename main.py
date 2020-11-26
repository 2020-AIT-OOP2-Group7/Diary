from diaries.DiarySample import DiarySample
from diaries.FukumotoDiaryNew import FukumotoDiaryNew

diaries = [DiarySample(),
            FukumotoDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()