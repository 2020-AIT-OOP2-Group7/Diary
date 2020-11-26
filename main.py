
from diaries.DiarySample import DiarySample
from diaries.AminoDiary import AminoDiary

diaries = [DiarySample(), AminoDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()