"""
    This file contains the TerminalColors class which is used to print colored text to the terminal.
    ANSI escape codes are used to print colored text to the terminal.

The format \033[...m is an ANSI escape code used to control the appearance of text output in terminals.
    Let's break it down:

\033: This is the escape character (often represented as ESC or \e).
[: This is the CSI (Control Sequence Introducer).
...: This is where the various numeric codes go.
m: This indicates the end of the control sequence.
The numeric codes in the ... section determine the actual effect. These codes are usually separated by ;.

Let's explain the code '\033[0;37;40m'

\033: Escape character.
0: Reset or normal.
37: Set foreground color to white.
40: Set background color to black.
Here's a breakdown of common codes:

Text attributes:
0: Reset/normal.
1: Bold or increased intensity.
2: Faint (decreased intensity, not widely supported).
3: Italic (not widely supported).
4: Underline.
5: Slow blink (less than 150 per minute, not widely supported).
6: Rapid blink (more than 150 per minute, not widely supported).
7: Reverse video (swap foreground and background colors).
8: Conceal (not widely supported).
9: Crossed-out (characters should be struck through, not widely supported).
10: Primary (default) font.
11–19: Alternate font.

There are more codes, especially when considering extended colors (like 256-color modes) and other advanced features of
some terminals. The ones provided above are the basic ones and are generally widely supported across different terminals

For extended color support, the sequences can be more complex, but the above should give you a good starting point.

If you're looking to do a lot of color work in your terminal, you might find libraries like colorama for Python to be
incredibly helpful, as they abstract away a lot of the specifics of these codes and provide a more user-friendly
interface.
"""


class TerminalColors:
    ansi_escape = '\033'
    csi = '['
    end = 'm'
    # color of text
    foreground = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
    }
    # color of text background
    background = {
        'black': 40,
        'red': 41,
        'green': 42,
        'yellow': 43,
        'blue': 44,
        'magenta': 45,
        'cyan': 46,
        'white': 47,
    }
    # text style
    style = {
        'reset': 0,
        'bold': 1,
        'faint': 2,
        'italic': 3,
        'underline': 4,
        'slow blink': 5,
        'rapid blink': 6,
        'reverse video': 7,
        'conceal': 8,
        'crossed-out': 9,
        'default': 10,
    }

    def __init__(self):
        self.ansi_front = f"{self.ansi_escape}{self.csi}"
        self.ansi_back = TerminalColors.end
        self.text_styler = f'{self.ansi_front}' + '{}' + f'{self.ansi_back}'
        self.foreground = TerminalColors.foreground
        self.background = TerminalColors.background
        self.style = TerminalColors.style
        self.text_reset = f"{self.ansi_front}{self.style.get('reset')}{self.ansi_back}"

    def _create_ansi_modifier(self, fore=None, back=None, style=None):
        components = []
        try:
            key_err = '{} is not a valid color'
            if fore:
                fore = fore.lower()
                if fore not in self.foreground:
                    raise KeyError(key_err.format(fore))
                components.append(str(self.foreground.get(fore)))
            if back:
                back = back.lower()
                if back not in self.background:
                    raise KeyError(key_err.format(back))
                components.append(str(self.background.get(back)))
            if style:
                style = style.lower()
                if style not in self.style:
                    raise KeyError(key_err.format(style))
                components.append(str(self.style.get(style)))
        except KeyError as key_err:
            return print(key_err)

        # Join the components with semicolons
        styling_sequence = ';'.join(components)

        styler = self.text_styler.format(styling_sequence)
        return styler


class TerminalHandler(TerminalColors):
    def __init__(self, **kwargs):
        super().__init__()
        self.styler = self._create_ansi_modifier(**kwargs)

    def print(self, message) -> None: print(f"{self.styler}{message}{self.text_reset}")

    def wrap(self, message) -> str: return f"{self.styler}{message}{self.text_reset}"

    def change_style(self, **kwargs) -> None: self.styler = self._create_ansi_modifier(**kwargs)


if __name__ == '__main__':
    term = TerminalHandler(fore='black', back='RED', style='Bold')
    term.print("Test")
