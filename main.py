
from diaries.DiarySample import DiarySample

from diaries.Ohashi import Ohashi
from diaries.FukumotoDiaryNew import FukumotoDiaryNew
from diaries.AminoDiary import AminoDiary

diaries = [DiarySample(), Ohashi(),FukumotoDiaryNew(), AminoDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()