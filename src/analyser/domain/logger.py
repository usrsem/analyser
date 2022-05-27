from typing import Protocol, Any


class Logger(Protocol):
    def info(self, text: str, *args: Any, **kwargs: Any) -> None:
        ...

    def debug(self, text: str, *args: Any, **kwargs: Any) -> None:
        ...

    def warning(self, text: str, *args: Any, **kwargs: Any) -> None:
        ...

    def error(self, text: str, *args: Any, **kwargs: Any) -> None:
        ...

