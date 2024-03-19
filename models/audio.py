# audio_model.py
import pygame

class AudioModel:
    def __init__(self):
        pygame.mixer.init()
        self.sound_effects = {}  #
        self.music_tracks = {}  
        self.current_track = None
        self.volume = 1.0 

    def load_sound_effect(self, name, filepath):
        try:
            self.sound_effects[name] = pygame.mixer.Sound(filepath)
        except pygame.error as e:
            print(f"Error loading sound effect {name} at {filepath}: {e}")

    def load_music_track(self, name, filepath):
        self.music_tracks[name] = filepath

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))

        for sound in self.sound_effects.values():
            sound.set_volume(self.volume)

        if self.current_track:
            pygame.mixer.music.set_volume(self.volume)

    def get_sound_effect(self, name):
        return self.sound_effects.get(name)

    def get_music_track(self, name):
        return self.music_tracks.get(name)
