import csv
import json

import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]
            if source not in routes:
                routes[source] = []
            routes[source].append(dest)
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    return {}

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    # Don't forget to write the output to JSON!

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
