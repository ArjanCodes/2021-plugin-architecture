"""Game extension that adds a bard character."""

from dataclasses import dataclass
from typing import Callable

@dataclass
class Bard:

    name: str
    instrument: str = "flute"

    def make_a_noise(self) -> None:
        print(
            f"I am {self.name} and I play the {self.instrument}. Toss a coin to your Witcher!"
        )


def register(register_fcn: Callable) -> None:
    register_fcn("bard", Bard)
