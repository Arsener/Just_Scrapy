import re

s = '/sadfad \ fsadfa \n fadsadewf : * asdfa|d fad'
t = re.sub('/|\\\|:|\*|\?|"|<|>|\||\\n', '', s)
print(t)