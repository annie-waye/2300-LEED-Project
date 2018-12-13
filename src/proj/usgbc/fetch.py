from . import prepare as uprep
from . import clean as uclean
from ..glbl import prepare as gprep


def get_data(filepath):
    """

    :param filepath: data file path
    :return: data
    """
    # Get data from filepath
    raw_data = gprep.get_data(filepath)

    # Arrange data in columns
    pre_data = uprep.pre_arrange_cols(raw_data)
    valid_frames = uprep.get_valid_frames(pre_data)
    true_data = uprep.arrange_cols(pre_data, valid_frames)

    # Clean/Format data
    true_data = uclean.remove_duplicates(true_data)
    true_data = uclean.convert_dates(true_data)
    true_data = uclean.sort_dates(true_data)

    return true_data
