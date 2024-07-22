import os
from random import randint
for i in range(1,365):
    for j in range(1,10):
        d=str(i)+" days ago"
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        commit_message = f"Added {d} to file.txt"
        os.system(f'git commit --date="{d}" -m "{commit_message}"')
os.system('git push origin main')