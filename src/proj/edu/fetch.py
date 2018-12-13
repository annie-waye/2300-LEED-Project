from . import prepare as eprep
from . import clean as eclean
from ..glbl import prepare as gprep


def get_data(filepath):
    """

    :param filepath: data file path
    :return: accessed data
    """
    # Get data from filepath
    raw_data = gprep.get_data(filepath)

    # Arrange data in proper columns
    pre_data = eprep.arrange_cols(raw_data)
    eprep.add_year(pre_data)
    eprep.check_years(pre_data)

    # Clean/Format data
    eclean.remove_empties(pre_data)
    true_data = eclean.parse_data(pre_data)

    return true_data
