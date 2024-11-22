from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([26], GPIO.OUT)
song = AudioSegment.from_mp3("/home/bryceg-26/L3D/Christmas.mp3")
def main():
    while True:
        button = GPIO.input(26)
        
        if button == 1:
            play(song)
main()