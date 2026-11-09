from enum import Enum
from typing import Text

class TextType(Enum):
    BOLD = 1 
    ITALIC = 2
    CODE = 3


class TextNode:
    def __init__(self, text : str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url : str | None = url

    def __eq__(self, other: object, /) -> bool:
        return isinstance(other, TextNode) and self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
