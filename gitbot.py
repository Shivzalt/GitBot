import os
from random import randint, random
import datetime

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 6, 30)

for i in range(int((end_date - start_date).days)):
    date = start_date + datetime.timedelta(days=i)
    num_commits = randint(1, 10)
    for j in range(num_commits):
        d = date.strftime("%A, %B %d, %Y")
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        commit_message = f"Added {d} to file.txt"
        os.system(f'git commit --date="{d}" -m "{commit_message}"')
    os.system('git push origin main')