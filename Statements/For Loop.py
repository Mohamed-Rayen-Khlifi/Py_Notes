for character in "text":
    print(character, end=' ')

for number in [1,2,3]:
    print(number, end=' ')

for name in ("rayen", "emna", "hasna", "kais"):
    print(name, end=' ')

for name, age in {'rayen': 24, 'emna': 19}.items():
    print(name, age)

for counter in range(0,10,1): #0 start, 9 end, 1 step
    print(counter, end=' ')
