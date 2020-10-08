# Задание 6.

import re


lessons = {}

with open('lessons.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines:
        name, hours = l.split(':')
        hours_all = sum([int(n) for n in re.findall(r'\d+', hours)])
        lessons[name] = hours_all

print(lessons)
