from PIL import Image

SIZE = 16
LEFT = 10
TOP = 37
SPACEX = 18
SPACEY = 9
COLUMNS = 15
ROWS = 17
TOTAL = 251

img = Image.open(r'mons.png')

x = LEFT
y = TOP
for i in range(1, TOTAL+1):
    new = img.crop((x, y, x+SIZE, y+SIZE))
    new.save(f'{i:03}.ico')
    # print(x,y)
    x += SIZE + SPACEX
    if i % COLUMNS == 0:
        y += SIZE + SPACEY
        x = LEFT
