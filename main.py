
from diaries.DiarySample import DiarySample

from diaries.Ohashi import Ohashi
from diaries.FukumotoDiaryNew import FukumotoDiaryNew
from diaries.AminoDiary import AminoDiary
from diaries.KatokitiDiary import KatokitiDiary

diaries = [DiarySample(), Ohashi(),FukumotoDiaryNew(), AminoDiary(), Katokiti()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()