from ..glbl import regress as greg


def lin_reg(dataframe, feature):
    feature_data = dataframe[[feature]]

    train_data = greg.train(feature_data)
    test_data = greg.test(feature_data)

    train_model = greg.axes(train_data, feature)
    test_model = greg.axes(test_data, feature)

    greg.lin_reg(train_model[0], test_model[0],
                 train_model[1], test_model[1])
    pass
