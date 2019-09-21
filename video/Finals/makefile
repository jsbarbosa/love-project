love.mp4 : song.mp3 files.txt *.jpg
	ffmpeg -framerate 8 -pattern_type glob -i '*.jpg' single.mp4
	ffmpeg -f concat -i files.txt -i song.mp3 -c copy high.mp4
	ffmpeg -i high.mp4 -b:v 412k -vcodec libx264 -acodec copy -b:a 52k love.mp4
	rm single.mp4 high.mp4
