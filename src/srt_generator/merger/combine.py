from copy import deepcopy
from src.types.subtitle import Subtitle
from src.types.speaker_subtitle import SpeakerSubtitle
from src.types.multi_speaker_subtitle import MultiSpeakerSubtitle
from src.types.subtitle_track import SubtitleTrack


def combine_subtitle_tracks(subtitle_tracks: list[SubtitleTrack]) -> list[Subtitle]:
    sorted_subtitles = sorted(
        [
            (subtitle.start_time, subtitle, subtitle_track.speaker)
            for subtitle_track in subtitle_tracks
            for subtitle in subtitle_track.subtitles
        ]
    )

    index = 0
    previous_subtitle: Subtitle | None = None
    current_speakers: list[str] = []
    combined_subtitles: list[Subtitle] = []

    for _, subtitle, speaker in sorted_subtitles:
        # print(
        #     f"{speaker}: {index}\n{subtitle.start_time} --> {subtitle.end_time}\n{subtitle.text}\n"
        # )

        current_speakers.append(speaker)
        index += 1
        speaker_subtitle = SpeakerSubtitle(
            index,
            subtitle.start_time,
            subtitle.end_time,
            speaker,
            subtitle.text,
        )

        if not previous_subtitle:
            previous_subtitle = speaker_subtitle
            continue

        if previous_subtitle.end_time < subtitle.start_time:
            combined_subtitles.append(previous_subtitle)
            previous_subtitle = speaker_subtitle
            continue

        print("Overlap!")

        previous_subtitle.end_time = subtitle.start_time
        combined_subtitles.append(previous_subtitle)

        previous_subtitle = (
            MultiSpeakerSubtitle(
                index,
                subtitle.start_time,
                subtitle.end_time,
                [previous_subtitle, speaker_subtitle],
            )
            if isinstance(previous_subtitle, SpeakerSubtitle)
            else MultiSpeakerSubtitle.generate_with_new_line(
                index,
                previous_subtitle,
                speaker_subtitle,
            )
        )

        previous_subtitles_copy = deepcopy(previous_subtitle)
        for previous_speaker_subtitle in previous_subtitles_copy.speaker_lines:
            if previous_speaker_subtitle.end_time < subtitle.start_time:
                previous_subtitle.end_time = previous_speaker_subtitle.end_time
                combined_subtitles.append(previous_subtitle)
                previous_subtitle.speaker_lines = [
                    speaker_line
                    for speaker_line in previous_subtitle.speaker_lines
                    if speaker_line.speaker != previous_speaker_subtitle.speaker
                ]

    return combined_subtitles
