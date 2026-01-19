"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        if results:
            for approach in results:
                # use list to save values will hit error like 'AttributeError: 'list' object has no attribute 'keys'
                # Create dictionary with fieldnames as keys to solve it
                elem = {
                    'datetime_utc': approach.time,
                    'distance_au': approach.distance,
                    'velocity_km_s': approach.velocity,
                    'designation': approach._designation,
                    'name': approach.neo.name if approach.neo and approach.neo.name else '',
                    'diameter_km': approach.neo.diameter if approach.neo and approach.neo.diameter else '',
                    'potentially_hazardous': approach.neo.hazardous == 'Y'  
                }
                writer.writerow(elem)

    print(f"CSV file {filename!r} created successfully!")



def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    json_out_list = list()
    for approach in results:
        approach_dict = dict()
        approach_dict["datetime_utc"] = approach.time_str
        approach_dict["distance_au"] = approach.distance
        approach_dict["velocity_km_s"] = approach.velocity
        approach_dict["neo"] = dict()
        approach_dict["neo"]['designation'] = approach._designation
        approach_dict["neo"]['name'] = approach.neo.name if approach.neo and approach.neo.name else ''
        approach_dict["neo"]['diameter_km'] = approach.neo.diameter if approach.neo and approach.neo.diameter else ''
        approach_dict["neo"]['potentially_hazardous'] = 'true' if approach.neo.hazardous == 'Y' else 'false' 
        json_out_list.append(approach_dict)
    with open(filename,'w') as json_outfile:
        json.dump(json_out_list,json_outfile,indent=2)

