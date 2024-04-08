from pathlib import Path
from re import compile as compile_regex, MULTILINE, DOTALL
from src.types.speaker_srt_file import SpeakerSrtFile


ROOT_DIRECTORY: Path = Path(__file__).parent.parent.resolve()

FILES: list[SpeakerSrtFile] = [
    SpeakerSrtFile(
        "Clair", f"{ROOT_DIRECTORY}/sample_captions/2024-01-04_19-30-04_1920x1080.srt"
    ),
    SpeakerSrtFile(
        "Celeste", f"{ROOT_DIRECTORY}/sample_captions/2024-03-07_20-00-07_1920x1080.srt"
    ),
]

SUBTITLE_REGEX = compile_regex(
    r"^\s*(\d+)\s*(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)\s*(\S.+?)(?:^$|\Z)$",
    MULTILINE | DOTALL,
)
