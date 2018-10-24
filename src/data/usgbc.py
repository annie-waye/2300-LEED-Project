import src.data.prepare as prep
import src.data.process as proc
import src.data.clean as cl

if __name__ == '__main__':
    # Get Data
    raw_data = prep.fetch_data()

    # Arrange Data in Columns
    pre_data = prep.pre_arrange_cols(raw_data)
    valid_frames = prep.get_valid_frames(pre_data)
    real_data = prep.arrange_cols(pre_data, valid_frames)

    # Clean/Format Data
    real_data = cl.remove_duplicates(real_data)
    real_data = cl.convert_dates(real_data)

    # Start ML Testing/Training
    proc_data = proc.fit_encode(real_data)
    print(proc_data)