# adaptee - sth which will be adapted
class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        print(f"Using advanced media player for vlc {file_name}")

    def play_mp4(self, file_name):
        print(f"Using advanced media player for mp4 {file_name}")

# adapter - sth which will adapt adaptee to the target
class MediaAdapter:
    def __init__(self, audio_type):
        self.advanced_media_player = AdvancedMediaPlayer()
        self.audio_type = audio_type

    def play(self, audio_type, file_name):
        if audio_type == 'vlc':
            self.advanced_media_player.play_vlc(file_name)
        elif audio_type == 'mp4':
            self.advanced_media_player.play_mp4(file_name)

# help class for our old audio player (mp3) - OLD, should not be changed
class MediaPlayer:
    def play(self, audio_type, file_name):
        print(f"Simple old player {audio_type}, {file_name}")

# target - our dream destination! (old code)
class AudioPlayer:
    def play(self, audio_type, file_name):
        if audio_type == 'mp3':
            MediaPlayer().play(audio_type, file_name)
        else:
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)

# New class to connect to audio devices
class AudioConnector:
    def connect(self, device_type):
        print(f"Connecting to {device_type}")

    def play(self, device_type, audio_type, file_name):
        self.connect(device_type)
        audio_player = AudioPlayer()
        audio_player.play(audio_type, file_name)
        print(f"Playing {file_name} on {device_type}")

# Example usage
audio_connector = AudioConnector()
audio_connector.play("speakers", "mp3", "song1.mp3")
audio_connector.play("headphones", "mp4", "song1.mp4")
audio_connector.play("bluetooth", "vlc", "song1.vlc")
