
#一些调试的草稿
from matplotlib.font_manager import fontManager
unique_fonts=set()

for font in fontManager.ttflist:
    if font.name:
        unique_fonts.add(font.name)
for font_name in sorted(unique_fonts):
    print(font_name)