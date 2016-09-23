import os
quality = ["best", "136+140", "135+140"]
with open("download", "r+") as fo:
    for line in fo:
	str = line.rstrip('\n')
	x=str.replace(' ','').split(',')
	print x
	if "playlist" in x[0]:
		os.system("youtube-dl --playlist-start " + x[1] + " -f " + quality[int(x[2])] + " -o './%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s' " + x[0])
	else:
		os.system("youtube-dl -f " + quality[int(x[1])] + "-o './%(title)s.%(ext)s' " + x[0])
