from src.types.subtitle import Subtitle


class SubtitleTrack:
    speaker: str
    subtitles: list[Subtitle]

    def __init__(self, speaker: str, subtitles: list[Subtitle]):
        self.speaker = speaker
        self.subtitles = subtitles
