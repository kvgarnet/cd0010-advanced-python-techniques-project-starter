import json

import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename) as nobel_file:
        nobel_data = json.load(nobel_file)
    return nobel_data['prizes']


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!
    '''
    if year and category: 
        output_data = [ prize for prize in data if prize['year'] == year and prize['category'] == category]
    elif year : 
        output_data = [ prize for prize in data if prize['year'] == year ]
    elif category: 
        output_data = [ prize for prize in data if prize['category'] == category]
    else:
        output_data = data
    '''
    output_data = []
    for prize in data:
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue
        output_data.append(prize)
    print( json.dumps(output_data,indent=4) )

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
