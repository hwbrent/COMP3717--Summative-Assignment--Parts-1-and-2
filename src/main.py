import os
import sys

from music21.converter import parse
from music21.stream import Score, Part, Opus

this_dir = os.path.dirname(__file__)
Data_dir = os.path.join(
    this_dir,
    os.path.pardir,
    "data",
    "CoCoPops",
    "RollingStone",
    "Data",
)

MrTambourineMan = os.path.join(Data_dir, "BobDylan_MrTambourineMan_1965.hum")


# ------------------------------------------------------------------------


def load_file() -> Score | Part | Opus:
    """
    Loads a `.hum` file into a format recognisable by `music21`. If a file
    path is provided via the command line, that file will be used. Otherwise,
    we use
    `data/CoCoPops/RollingStone/Data/BobDylan_MrTambourineMan_1965.hum`
    """

    hum_path = None

    # If an argument is provided via the command line, and it's a file, use
    # that as our path
    args = sys.argv
    if len(args) == 2 and os.path.isfile(args[1]):
        hum_path = args[1]

    # Else, default to using Mr Tambourine Man
    else:
        hum_path = MrTambourineMan

    return parse(hum_path, format="humdrum")


# ------------------------------------------------------------------------


def main():
    file = load_file()
    print(file)


# ------------------------------------------------------------------------


if __name__ == "__main__":
    main()
