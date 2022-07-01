# import ffmpeg_streaming
# from ffmpeg_streaming import Formats

# movie_id = 7
# video = ffmpeg_streaming.input('https://www.imdb.com/video/vi3821650457/?listId=ls053181649?ref_=ext_shr_lnk')
# dash = video.dash(Formats.h264())
# dash.auto_generate_representations()
# dash.output(f'/tmp/dash/{movie_id}.mpd')

# print(type(video))