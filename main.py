
from diaries.DiarySample import DiarySample
from diaries.DiaryKame import DiaryKame
from diaries.Ohashi import Ohashi
from diaries.FukumotoDiaryNew import FukumotoDiaryNew
from diaries.AminoDiary import AminoDiary
from diaries.KatokitiDiary import KatokitiDiary

<<<<<<< Updated upstream
diaries = [DiarySample(), Ohashi(),FukumotoDiaryNew(), AminoDiary(),DiaryKame(), Katokiti()]
=======
diaries = [DiarySample(), Ohashi(),FukumotoDiaryNew(), AminoDiary(), KatokitiDiary()]
>>>>>>> Stashed changes

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()