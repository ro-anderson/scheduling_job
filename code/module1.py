import json
def teste():
    print('oi')

def read_json(path, label):
    '''
    read json file
    '''
    with open(path +'/'+ label) as json_file:
        data = json.load(json_file)
    return data
