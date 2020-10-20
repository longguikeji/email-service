CONFIG_FILE = 'config.toml'
CONFIG_PROD_FILE = 'config.prod.toml'

def get_app_config():
    import os
    import toml
    data = toml.load(CONFIG_FILE)

    if os.path.exists(CONFIG_PROD_FILE):
        new_data = toml.load(CONFIG_PROD_FILE)
        data.update(new_data)

    return data