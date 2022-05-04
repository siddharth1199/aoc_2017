import csv
import click
import itertools
from collections import namedtuple
import math
from typing import List, Dict
import re

EARTH_RADIUS = 6.371e6  # In metres

Place = namedtuple('Place', ('name', 'latitude', 'longitude'))


def parse(row: Dict) -> Place:
    return Place(row['name'], float(row['latitude']), float(row['longitude']))


def read_csv(input_file) -> List[Place]:
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, ["name", "latitude", "longitude"])
        _ = next(reader)  # Skip header
        rows = [parse(row) for row in reader if re.fullmatch(r'[a-zA-Z]*', row['name'])]

    return rows


def haversine(src: Place, dst: Place) -> float:
    def deg_to_rad(angle): return math.pi * angle / 180

    def hav(angle): return (1 - math.cos(deg_to_rad(angle))) / 2

    return 2 * EARTH_RADIUS * math.sqrt(hav(dst.latitude - src.latitude) +
                                        math.cos(deg_to_rad(src.latitude)) * math.cos(deg_to_rad(dst.latitude)) *
                                        hav(dst.longitude - src.longitude))


@click.command()
@click.argument("input_file")
@click.argument("output_file")
@click.option("--max-rows", default=11)
def main(input_file, output_file, max_rows):
    rows = read_csv(input_file)[:max_rows]
    with open(output_file, 'w') as f:
        for src, dst in itertools.combinations(rows, 2):
            f.write("{} to {} = {}\n".format(src.name, dst.name, int(haversine(src, dst))))

    return


if __name__ == "__main__":
    main()
