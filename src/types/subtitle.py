from datetime import datetime as DateTime


class Subtitle:
    index: int
    start_time: DateTime
    end_time: DateTime
    text: str

    def __init__(
        self,
        index: int,
        start_time: str | DateTime,
        end_time: str | DateTime,
        text: str,
    ):
        self.index = index

        if isinstance(start_time, str):
            self.start_time = DateTime.strptime(start_time, "%H:%M:%S,%f")
        else:
            self.start_time = start_time

        if isinstance(end_time, str):
            self.end_time = DateTime.strptime(end_time, "%H:%M:%S,%f")
        else:
            self.end_time = end_time

        self.text = text

    @classmethod
    def with_time(cls, index: int, start_time: DateTime, end_time: DateTime, text: str):
        return cls(
            index,
            start_time.strftime("%H:%M:%S,%f")[:-3],
            end_time.strftime("%H:%M:%S,%f")[:-3],
            text,
        )

    def __str__(self):
        return f"{self.index}\n{self.start_time.strftime('%H:%M:%S,%f')[:-3]} --> {self.end_time.strftime('%H:%M:%S,%f')[:-3]}\n{self.text}"

    def __repr__(self):
        return (
            f"Subtitle({self.index}, {self.start_time}, {self.end_time}, {self.text})"
        )
