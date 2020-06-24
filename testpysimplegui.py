# Headers
import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
import os
import os.path as osp

# Path definitions
currDir = osp.dirname(os.path.realpath(__file__))
mediaDir = osp.join(currDir, 'media')
videoPath = osp.join(mediaDir, 'dices_1.mp4')
# video_path = "C:\\Users\\renoi\\OneDrive\\Documentos\\RPG\\CODE\\media\\dices_1.mp4"

def PlayVideo(videoPath):
    video = cv2.VideoCapture(videoPath)
    player = MediaPlayer(videoPath)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame                            # Audio
    video.release()
    cv2.destroyAllWindows()

PlayVideo(videoPath)