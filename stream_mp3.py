"""
Author:         Pravar Kochar
Date:           25/05/2021
Description:    A program to play, pause, stop audio from
"""

# How to get wave file from net?
import pyaudio
import wave
import io
# import threading
from pynput.keyboard import Listener, KeyCode


class Songs:
    def __init__(self, audio_file_url: str):
        # Song url.
        self.song_url = audio_file_url
        # Binary data of the song, in wave readable format.
        self.song_byte = self.get_audio()
        # Song name.
        self.song_name = self.get_song_name_from_url()

    def get_audio(self):
        """
        ***Problem!!!***
        A function that gets the binary data of the song from the given url.
        :return: Binary form of song data from the given url (readable by wave).
        """
        #raw_binary = self.song_url
        #return io.BytesIO(raw_binary.raw)

    def get_song_name_from_url(self) -> str:
        """
        A function that extracts the name of the song from the url.
        :return: Name of the song
        """
        split_url = self.song_url.split('/')
        # Get the name from the url as best as possible.
        name = split_url[-1][:-4]
        return name


class SongPlayer:
    def __init__(self):
        # To hold Song type of data.
        self.song_playlist = []
        # To track if any song is currently playing.
        self.any_song_playing = False

        self.stream = None

    def append_song(self, song_url: str):
        """
        A function to add a Song type song to the playlist.
        :param song_url: String url for a song to add to the playlist
        """
        self.song_playlist.append(Songs(song_url))

    def start_playing_song(self):
        for each_song in self.song_playlist:
            with wave.open(each_song, 'rb') as song:
                width = song.getsampwidth()
                channels = song.getnchannels()
                rate = song.getframerate()

            p_aud = pyaudio.PyAudio()
            self.stream = p_aud.open(
                format=pyaudio.get_format_from_width(width),
                channels=channels,
                rate=rate,
                output=True
            )
            self.stream.read()
            self.start_song()

    def stop_song(self):
        if self.any_song_playing:
            print("Stopping song...")
            self.stream.stop_stream()
            self.any_song_playing = False

    def start_song(self):
        # Start the song.
        if not self.any_song_playing:
            print("Starting song...")
            self.stream.start_stream()
            self.any_song_playing = True

    def exit(self):
        print("Exiting program.")
        self.stop_song()


sp = SongPlayer()
sp.append_song('https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60' \
                '.wav')
sp.start_playing_song()


def on_press(key):
    start_stop_key = KeyCode(char='q')
    exit_key = KeyCode(char='e')
    if key == start_stop_key:
        if sp.any_song_playing:
            sp.stop_song()
        else:
            sp.start_song()
    elif key == exit_key:
        sp.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
