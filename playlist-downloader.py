
import pafy

# create a list of videos
videolist = []

# fill up the list
print("Enter youtube URL, one per line. Press 'DONE' when finished...")
v=""
while v.upper() != 'DONE':
    v = input()
    if v.upper() != 'DONE':
        # add video to the list
        videolist.append(v)


counter = 0
while counter <= len(videolist):
    print("Printing Video 1:")
    print("title: " + str(videolist[counter].title))
    video = pafy.new(videolist[counter])
    video.download(quiet=False)
    counter = counter+1




