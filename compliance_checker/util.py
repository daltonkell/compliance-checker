"""
General purpose utility functions to aid in compliance checking tasks
"""
import isodate
import pendulum
from collections import OrderedDict


def datetime_is_iso(date_str):
    """Attempts to parse a date formatted in ISO 8601 format"""
    try:
        if len(date_str) > 10:
            dt = isodate.parse_datetime(date_str)
        else:
            dt = isodate.parse_date(date_str)
        return True, []
    except:  # Any error qualifies as not ISO format
        return False, ['Datetime provided is not in a valid ISO 8601 format']


def dateparse(date_str):
    '''
    Returns a naive datetime. parsed from an ISO-8601 input string

    :param str date_str: An ISO-8601 string
    '''

    return pendulum.parse(date_str)


def kvp_convert(input_coll):
    '''
    Converts a list of string attributes and/or tuples into an OrderedDict.
    If passed in an OrderedDict, function is idempotent.
    Key/value pairs map to `first_tuple_element` -> `second_tuple_element` if
    a tuple, or `scalar_value` -> None if not a tuple.

    :param input_coll: An iterable with string and/or 2-tuple elements
    :returns: collections.OrderedDict
    '''
    if isinstance(input_coll, OrderedDict):
        return input_coll
    else:
        return OrderedDict((l, None) if not isinstance(l, tuple) else
                           (l[0], l[1]) for l in input_coll)
