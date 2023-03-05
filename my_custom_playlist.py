
import playsound
import os
os.chdir('newsongs')
songs = os.listdir()
songs.append('Exit')

flag=True
while flag:
    print('Select the song of your choice:')
    for x,y in enumerate(songs,1):
        print(x,y)
    ch=int(input('Enter your choice:'))
    if ch==9:
        flag=False
    elif ch<=8 and ch>=1:
        playsound.playsound(songs[ch-1])
    else:
        print('Invalid choice')



