from src.types.subtitle import Subtitle
from src.types.subtitle_track import SubtitleTrack
from src.variables import SUBTITLE_REGEX

# SUBTITLE_NUMBER_REGEX = re.compile(r"^\s*\d+\s*$", re.MULTILINE)


def parse(file_path: str) -> list[Subtitle]:
    with open(file_path, "r", encoding="utf-8") as file:
        subtitle_strings = SUBTITLE_REGEX.finditer(file.read())
        subtitles = [
            Subtitle(
                index=int(index),
                start_time=start_time,
                end_time=end_time,
                text=text.strip(),
            )
            for match in subtitle_strings
            for index, start_time, end_time, text in [match.groups()]
        ]

    return subtitles


def create_subtitle_track(speaker: str, file_name: str) -> SubtitleTrack:
    return SubtitleTrack(speaker, parse(file_name))
