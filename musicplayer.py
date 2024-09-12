#installed pygame on mac terminal with 'pip3 install pygame'
from pygame import mixer

mixer.init()
#Must input full path to file :]
song = input("Enter .mp3 file you want to play: ")
mixer.music.load(song)
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Press 'p' to pause\nPress 'r' to resume\nPress 'v' to set volume\nPress 'e' to exit\n")
    choice = input()

    if choice == "p":
        mixer.music.pause()
    elif choice == "r":
        mixer.music.unpause()
    elif choice == "v":
        nVol = float(input("Enter new volume, 0-1:"))#doesn't really change the volume!
    elif choice == "e":
        mixer.music.stop()
        break
