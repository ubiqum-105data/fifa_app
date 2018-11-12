import json

LOCAL_CONFIG_FILE = 'config/local.json'
DEFAULT_CONFIG_FILE = 'config/default.json'

def get_config():
    try:
        with open(LOCAL_CONFIG_FILE) as json_data:
            d = json.load(json_data)
            return d
    except FileNotFoundError:
        with open(DEFAULT_CONFIG_FILE) as json_data:
            d = json.load(json_data)
            return d

'''
def config_db_string(app):
    app.config['DB_STRING'] = "postgresql+%s://%s:%s@%s/%s" \
        % (DRIVER, USER, PASSWORD, address, DB,)
'''

def get_db_string():
    config = get_config()
    return "postgresql+%s://%s:%s@%s/%s" \
        % (config['driver'], config['user'], config['password'],
           config['address'], config['db'],)

