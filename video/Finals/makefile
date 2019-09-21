love.mp4 : single.mp4
	ffmpeg -f concat -i files.txt -i song.mp3 -c copy love.mp4
	rm single.mp4

single.mp4 : song.mp3 files.txt *.jpg
	ffmpeg -framerate 8 -pattern_type glob -i '*.jpg' single.mp4
