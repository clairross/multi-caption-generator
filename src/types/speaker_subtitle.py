from datetime import datetime as DateTime
from src.types.subtitle import Subtitle


class SpeakerSubtitle(Subtitle):
    speaker: str

    def __init__(
        self,
        index: int,
        start_time: str | DateTime,
        end_time: str | DateTime,
        speaker: str,
        text: str,
    ):
        super().__init__(index, start_time, end_time, text)
        self.speaker = speaker

    def __str__(self):
        return f"{self.index}\n{self.start_time.strftime('%H:%M:%S,%f')[:-3]} --> {self.end_time.strftime('%H:%M:%S,%f')[:-3]}\n{self.speaker}: {self.text}"

    def __repr__(self):
        return f"SpeakerSubtitle({self.index}, {self.start_time}, {self.end_time}, {self.speaker}, {self.text})"
