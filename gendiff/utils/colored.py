from typing import Dict, Literal, Optional

ColorNameType = Literal[
    "black", "red", "green", "olive", "blue", "magenta", "cyan", "gray"
]
ColorsSetType = Dict[ColorNameType, str]

ColorPropertyType = Literal["font", "bg"]

       
color: Dict[ColorPropertyType, ColorsSetType] = {
    "font": {
        "black": "\x1B[30m",
        "red": "\x1B[31m",
        "green": "\x1B[32m",
        "olive": "\x1B[33m",
        "blue": "\x1B[34m",
        "magenta": "\x1B[35m",
        "cyan": "\x1B[36m",
        "gray": "\x1B[37m",
    },
    "bg": {
        "black": "\x1B[40m",
        "red": "\x1B[41m",
        "green": "\x1B[42m",
        "olive": "\x1B[43m",
        "blue": "\x1B[44m",
        "magenta": "\x1B[45m",
        "cyan": "\x1B[46m",
        "gray": "\x1B[47m",
    }
}

END_COLOR = "\033[0m"


def colored(
    text: str, 
    font_color: Optional[ColorNameType] = None,
    bg_color: Optional[ColorNameType] = None
) -> str:
    text_parts = [text]
    
    if font_color is not None:
        text_parts = [color["font"][font_color]] + text_parts + [END_COLOR]
    
    if bg_color is not None:
        text_parts = [color["bg"][bg_color]] + text_parts + [END_COLOR]
    
    return "".join(text_parts)