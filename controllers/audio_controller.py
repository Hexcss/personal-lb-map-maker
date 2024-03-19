import pygame.mixer

class AudioController:
    def __init__(self, model):
        self.model = model
        pygame.mixer.init()

    def play_sound_effect(self, name):
        sound = self.model.sound_effects.get(name)
        if sound:
            sound.play()

    def play_music(self, name):
        track_path = self.model.music_tracks.get(name)
        if track_path:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play(-1)  # The '-1' makes the music loop

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        self.model.set_volume(volume)
        pygame.mixer.music.set_volume(volume)

        for sound in self.model.sound_effects.values():
            sound.set_volume(volume)
