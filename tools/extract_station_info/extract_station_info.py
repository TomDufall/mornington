"""
Convert the Wikipedia underground stations table into a nice JSON list.
#https://en.wikipedia.org/wiki/List_of_London_Underground_stations
"""
import json
from pathlib import Path
from typing import List, Tuple

DIR = Path(__file__).parent
IN_FILE = DIR / "wikipedia_stations_list.txt"
OUT_FILE = DIR / "stations.json"


def read_stations(filepath: Path = IN_FILE) -> List[Tuple[str, List[str]]]:
    """
    Read from the Wikipedia table of underground stations and return a
    list of stations and the lines available at them.

    :param filepath: Path to Wikipedia table as a text file
    :return: List of (station name, [lines]) tuples
    """
    with open(filepath) as f:
        text = f.read()

    entries = text.split("|-")
    # discard header section
    entries = entries[1:]

    stations = []
    for entry in entries:
        station = entry.split("|")[2].split("]", 1)[0]
        lines_text = entry.split("||")[1]
        lines = []
        for line_text in lines_text.split("[[")[1:]:
            line = line_text.split("|", 1)[1].split("]]", 1)[0]
            lines.append(line)
        stations.append((station, lines))
    return stations


if __name__ == "__main__":
    stations = read_stations()
    with open(OUT_FILE, "w") as f:
        json.dump(stations, f, sort_keys=True, indent=4)
