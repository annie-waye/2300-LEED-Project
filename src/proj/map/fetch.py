from ..glbl import prepare as gprep


def get_data(filepath):
    raw_data = gprep.get_data(filepath, 'csv')
    return raw_data
