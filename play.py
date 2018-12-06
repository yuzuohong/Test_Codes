from pygame import mixer

path = input('Enter the full path to your music \n (e.g d:\music\\taylor swift\\blank space.mp3): ')

'''
mixer.init()
mixer.music.load(path)
mixer.music.play()
'''

sound = mixer.Sound(path)

sound.set_volume(0.5)
