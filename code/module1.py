import json
from datetime import datetime


def read_json(path, label):

    '''
    read json file
    '''

    with open(path + '/' + label) as json_file:
        data = json.load(json_file)
    return data


def execution_window_to_dtime_list(dict_input):
    dict_items = dict_input.items()

    '''
    return list with workable time boundary.
    '''

    list_window_value = list(dict_items)[0][1].split()
    # inicio da janela
    inf_boundary_Ymd = list_window_value[0]
    sup_boundary_Ymd = list_window_value[3]
    # fim da janela
    inf_boundary_HMS = list_window_value[1]
    sup_boundary_HMS = list_window_value[4]
    # join
    inf_boundary = inf_boundary_Ymd + ' ' + inf_boundary_HMS
    sup_boundary = sup_boundary_Ymd + ' ' + sup_boundary_HMS
    # to datetime format
    dtime_inf_boundary = datetime.strptime(inf_boundary, "%Y-%m-%d %H:%M:%S")
    dtime_sup_boundary = datetime.strptime(sup_boundary, "%Y-%m-%d %H:%M:%S")
    return [dtime_inf_boundary, dtime_sup_boundary]


def dif_datatime_in_s(data_inf, str_data_sup):

    '''
    return dif in seconds (float)
    '''

    data_sup = datetime.strptime(str_data_sup, "%Y-%m-%d %H:%M:%S")
    return (data_sup - data_inf).total_seconds()
