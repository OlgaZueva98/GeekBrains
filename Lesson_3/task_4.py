# 4. Определить, какое число в массиве встречается чаще всего.

from collections import Counter
from random import randint


lst = [randint(0, 10) for i in range(100)]
c = Counter(lst)

print(f'Число {c.most_common()[0][0]} встречается чаще всего.')
      