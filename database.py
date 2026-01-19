"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""
from collections import defaultdict
import operator
from filters import DateFilter


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # TODO: What additional auxiliary data structures will be useful?
        # SOLUTION: since both neo and CloseApproaches objects have common 'designation' attribute, we can
        # use dictionary can help to
        # 1. create relationship between neo instances and corresponding CloseApproaches 
        # 2. speed up get_neo_by_designation and get_neo_by_name methods
        self._neo_name_dict = dict()
        self._neo_designation_dict = dict()

        # TODO: Link together the NEOs and their close approaches.

        # self._ca_desig_dict = dict()
        # for ca in self._approaches:
        #     if ca._designation not in self._ca_desig_dict:
        #         self._ca_desig_dict[ca._designation] = [ca]
        #     self._ca_desig_dict[ca._designation].append(ca)
        #
        # for neo in self._neos:
        #     ca = self._ca_desig_dict[neo.designation]
        #     neo.approaches = ca
        #     ca[0].neo = neo

        # Build date index: Map dates to lists of CloseApproach objects
        self._date_index = defaultdict(list)
        # creating mapping between designation/human name to neo instance
        for neo in self._neos:
            self._neo_designation_dict[neo.designation] = neo
            if neo.name:
                self._neo_name_dict[neo.name] = neo
        #  for each close approach, determine to which NEO its _designation corresponds, and assign that NearEarthObject to the CloseApproach's .neo attribute 
        for approach in self._approaches:
            neo = self._neo_designation_dict[approach._designation]
            approach.neo = neo
            # add this close approach back to NearEarthObject's .approaches collection attribute
            neo.approaches.append(approach)

            # Extract date portion from approach's time attribute
            app_date = approach.time.date()
            self._date_index[app_date].append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.
        if designation in self._neo_designation_dict:
            return  self._neo_designation_dict[designation]
        return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.
        if name.capitalize() in self._neo_name_dict:
            return self._neo_name_dict[name.capitalize()]
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects

        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        # Solution:  use generator function('yield' instead of 'return'),function donot to return a fully-computed collection of matching result(take a while to compute) - but rather to generate a stream of matching close approaches. 
        # In doing so, we'll make the query method almost instantaneous, and only do the work to determine the next element of the generator (the next matching CloseApproach) if another unit of code asks for it.

        date_filters = [
            f for f in filters 
            if isinstance(f, DateFilter) and f.op is operator.eq
        ]
        # print(date_filters)
        
        if date_filters:
            # Use first equality date filter to get candidate approaches
            target_date = date_filters[0].value
            candidates = self._date_index.get(target_date, [])
            
            # Apply ALL filters to candidates from date index
            for approach in candidates:
                if all(filter(approach) for filter in filters):
                    # print('found')
                    yield approach
            return

        # Fallback to full scan if no equality date filters found
        for approach in self._approaches:
            filter_col = (filter(approach) for filter in filters)
            if all(filter_col):
                yield approach
        
