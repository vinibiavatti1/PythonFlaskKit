from __future__ import annotations
from abc import ABC, abstractmethod


class MenuOptions:
    def __init__(self) -> None:
        self.options = []

    def add_option(self, label: str, url: str, icon: str = None) -> None:
        self.options.append((label, url, icon))

    def with_option(self, label: str, url: str,
                    icon: str = None) -> MenuOptions:
        self.add_option(label, url, icon)
        return self

    def get_options(self) -> list[tuple]:
        return self.options


class Menu(ABC):

    @abstractmethod
    def rule(self) -> bool:
        pass

    @abstractmethod
    def build(self) -> MenuOptions:
        pass
