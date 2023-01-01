import os
from random import randint
import datetime

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

for i in range(int((end_date - start_date).days)):
    date = start_date + datetime.timedelta(days=i)
    for j in range(10):
        d = date.strftime("%A, %B %d, %Y")
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        commit_message = f"Added {d} to file.txt"
        os.system(f'git commit --date="{d}" -m "{commit_message}"')
    os.system('git push origin main')