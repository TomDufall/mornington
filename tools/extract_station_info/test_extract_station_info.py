from pathlib import Path

from extract_station_info import read_stations


def test_read_stations():
    filepath = Path(__file__).parent / "stations_test_sample.txt"
    expected = [
        ("Acton Town", ["District", "Piccadilly"]),
        ("Aldgate", ["Metropolitan", "Circle"]),
        ("Woodside Park", ["Northern"]),
    ]
    assert read_stations(filepath) == expected
