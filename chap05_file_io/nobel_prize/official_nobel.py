import json
import helper

def load_nobel_prizes(filename='prize.json'):
    with open(filename) as f:
        return json.load(f)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']

    for prize in prizes:
        if 'laureates' not in prize:
            continue  # rare few Nobel prizes were never awarded
        if category and prize['category'].lower() != category.lower():
            continue # prize's category doesn't match, we skip it  same with the year.
        if year and prize['year'] != year:
            continue

        print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '') # winning organizations have no surname
            print(f"{firstname} {surname}: {laureate['motivation']}")


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
