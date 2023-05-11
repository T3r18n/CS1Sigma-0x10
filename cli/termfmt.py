esc = "\x1b"

bold = bright = 1
dim = 2
underline = 4
blink = 5
reverse = invert = 7
hidden = 8

simple = 9
black  = 0
red = 1
green = 2
yellow = 3
blue = 4
magenta = 5
cyan = 6
light_gray = 7
dark_grey = 60
light_red = 61
light_green = 62
light_yellow = 63
light_blue = 64
light_magenta = 65
light_cyan = 66
white = 67

foreground = 30

background = 40




__gloabals__ = globals()
resetall = [ __gloabals__.setdefault(f"reset_{i}",__gloabals__[i]+20) for i in __gloabals__ if i in ("bold", "bright", "dim", "blink", "reverse", "invert", "hidden")]