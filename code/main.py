from module1 import read_json

if __name__ == '__main__':
    path_src = '../src'
    label_moc = 'moc.json'
    dir_data = read_json(path_src, label_moc)
    print(dir_data)
