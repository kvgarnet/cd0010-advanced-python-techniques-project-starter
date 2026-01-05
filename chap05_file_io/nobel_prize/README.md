prize data: https://api.nobelprize.org/v1/prize.jsonc

This program will print out information about Nobel prizes (in any format you'd like). If a year is specified (not None), only print information about Nobel prizes from that year. If a category is specified (not None), only print information about Nobel prizes from that category.

This program is executed at the command line with arguments determined by a parser we wrote in the helper module.

So, you can run

$ python3 nobel.py
...
$ python3 nobel.py --year 2020
...
$ python3 nobel.py --category Physics
...
$ python3 nobel.py --year 1901 --category Economics
...
