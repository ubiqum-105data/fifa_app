USER = 'postgres'
PASSWORD = '1234'
DRIVER = 'psycopg2'
DB = 'fifa'

def config_db_string(app):
    app.config['DB_STRING'] = "postgresql+%s://%s:%s@localhost/%s" \
        % (DRIVER, USER, PASSWORD, DB,)

def get_db_string():
    return "postgresql+%s://%s:%s@localhost/%s" \
        % (DRIVER, USER, PASSWORD, DB,)


