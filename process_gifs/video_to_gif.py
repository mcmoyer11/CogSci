from moviepy import *

movie_folder = "C:\Users\\tjdawson\Dropbox\Alon_Felix_shared\utterance_events_matching_project\media\michotte_stimuli_resized\\"

movie = "launch_angle90.mp4"

clip = (VideoFileClip(movie))
clip.write_gif("launch_angle90.gif")

import moviepy
