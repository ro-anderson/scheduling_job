import module1


def test_read_json():

    '''
    test if read json return a dict
    '''

    path_src = '../src'
    label_moc = 'moc.json'
    data_moc = module1.read_json(path_src, label_moc)
    assert type(data_moc) is dict
