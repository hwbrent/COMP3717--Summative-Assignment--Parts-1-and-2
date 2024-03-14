import os

from music21 import converter

this_dir = os.path.dirname(__file__)
Data_dir = os.path.join(
    this_dir,
    os.path.pardir,
    "data",
    "CoCoPops",
    "RollingStone",
    "Data",
)


# ------------------------------------------------------------------------


def main():
    file_path = os.path.join(Data_dir, "BobDylan_MrTambourineMan_1965.hum")

    # Need to specify the "humdrum" format, otherwise the parser won't know
    # how to parse the file
    score = converter.parse(file_path, format="humdrum")
    print(score)


# ------------------------------------------------------------------------


if __name__ == "__main__":
    main()
