from module1 import read_json
from module1 import execution_window_to_dtime_list


if __name__ == '__main__':
    path_src = '../src'
    label_moc = 'moc.json'

    # read to dict from json
    dir_data = read_json(path_src, label_moc)

    # get list of dtime objetct (inf and sup boundry)
    list_dtime_window = []
    list_dtime_window = execution_window_to_dtime_list(dir_data)
    #print(execution_window_to_dtime_list(dir_data))
