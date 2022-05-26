from typing import Protocol


class Logger(Protocol):
    def info(self, text: str, *args) -> None:
        ...

    def debug(self, text: str, *args) -> None:
        ...

    def warning(self, text: str, *args) -> None:
        ...

    def error(self, text: str, *args) -> None:
        ...

