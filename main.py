from tkinter import Tk, filedialog
from src.variables import ROOT_DIRECTORY, FILES
from src.types.subtitle_track import SubtitleTrack
from src.srt_generator.parser.srt_parser import create_subtitle_track
from src.srt_generator.merger.combine import combine_subtitle_tracks
from src.types.speaker_srt_file import SpeakerSrtFile


def main():

    root = Tk()
    root.withdraw()

    file_paths = (
        FILES
        if FILES
        else [
            SpeakerSrtFile(
                input(f"What is the speaker's name? File: {file_path}\n"), file_path
            )
            for file_path in filedialog.askopenfilenames(
                filetypes=[("SRT files", "*.srt")], initialdir=ROOT_DIRECTORY
            )
        ]
    )

    subtitle_tracks: list[SubtitleTrack] = [
        create_subtitle_track(file.speaker, file.filename) for file in file_paths
    ]

    new_subtitles = combine_subtitle_tracks(subtitle_tracks)

    for i in range(10):
        print(new_subtitles[i])

    # Your code here


if __name__ == "__main__":
    main()
