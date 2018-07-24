import shelve

set = shelve.open('./init/load')
windows = {}
windows['h'] = 360
windows['w'] = 540
windows['caption'] = "Card-Warrior"
windows['background'] = "./resource/background.bmp"
set['windows'] = windows
print(set)
print(windows)
set.close()
