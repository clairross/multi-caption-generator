from datetime import datetime as DateTime
from src.types.subtitle import Subtitle
from src.types.speaker_subtitle import SpeakerSubtitle


class MultiSpeakerSubtitle(Subtitle):
    # Use a list because the order matters
    speaker_lines: list[SpeakerSubtitle]

    def __init__(
        self,
        index: int,
        start_time: str | DateTime,
        end_time: str | DateTime,
        speaker_lines: list[SpeakerSubtitle],
    ):
        reversed_speaker_lines = speaker_lines[::-1]
        super().__init__(
            index,
            start_time,
            end_time,
            "\n".join(
                [
                    f"{speaker_line.speaker}: {speaker_line.text}"
                    for speaker_line in reversed_speaker_lines
                ]
            ),
        )
        self.speaker_lines = speaker_lines

    @classmethod
    def generate_with_new_line(
        cls,
        index: int,
        old_multi_speaker_line: "MultiSpeakerSubtitle",
        new_line: SpeakerSubtitle,
    ) -> "MultiSpeakerSubtitle":
        if new_line.speaker in [
            speaker_line.speaker
            for speaker_line in old_multi_speaker_line.speaker_lines
        ]:
            new_speaker_lines = [
                speaker_line if speaker_line.speaker != new_line.speaker else new_line
                for speaker_line in old_multi_speaker_line.speaker_lines
            ]
            return cls(
                index,
                new_line.start_time,
                new_line.end_time,
                new_speaker_lines,
            )

        return cls(
            index,
            new_line.start_time,
            new_line.end_time,
            old_multi_speaker_line.speaker_lines + [new_line],
        )
