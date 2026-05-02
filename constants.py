# constants.py
# Maps each HANA environment label to the Windows user environment variable NAMES
# that hold the actual connection credentials.
# To add a new environment, add a new key block below and set the corresponding
# env vars via:  setup_credentials  (or  setx HANA_<ENV>_HOST "..."  etc.)

HANA_ENV_CONFIG = {
    'DEV': {
        'host':     'HANA_DEV_HOST',
        'port':     '30041',       # default 30041 if not set
        'user':     'HANA_USER',
        'password': 'HANA_DEV_PASSWORD',
    },
    'QAS': {
        'host':     'HANA_QAS_HOST',
        'port':     'HANA_PORT',       # default 30041 if not set
        'user':     'HANA_USER',
        'password': 'HANA_QAS_PASSWORD',
    },
    'PRD': {
        'host':     'HANA_PRD_HOST',
        'port':     '30041',       # default 30041 if not set
        'user':     'HANA_USER',
        'password': 'HANA_PRD_PASSWORD',
    },
}

# Default port used when HANA_<ENV>_PORT env var is not set
HANA_DEFAULT_PORT = 30041
