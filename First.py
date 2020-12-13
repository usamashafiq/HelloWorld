from pygame import mixer
import time
import datetime

def getdate():
    return datetime.datetime.now()


# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("song.mp3")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()

# infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input(" ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break
# a=time.time()
# print(a)
x= datetime.time(10, 5)
print(x)
local_time = time.ctime(time.time())
print("Local time:", local_time)

#a = input("Enter your Name : ")
#print("HI PROGRAMER", a,x)
y=datetime.datetime.now().time()
#print(y-x)
#while(True):
start = time.time()

#time.sleep(10)  # or do something more productive

done = time.time()
print(start)
print(done)
elapsed = done - start
print(elapsed)


# while(True):
#
#     print()


old_time = datetime.datetime.now()
print(old_time)
new_time = old_time - time.timedelta(2,10)
print(new_time)

