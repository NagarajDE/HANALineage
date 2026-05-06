# constants.py
# Maps each HANA environment label to the Windows user environment variable NAMES
# that hold the actual connection credentials.
# To add a new environment, add a new key block below and set the corresponding
# env vars via:  setup_credentials  (or  setx HANA_<ENV>_HOST "..."  etc.)

HANA_ENV_CONFIG = {
    'DEV': {
        'host':     'HANA_DEV_HOST',
        'port':     '30041',       # default 30041 if not set
        # 'user':     'HANA_USER',          # commented out — using SSO
        # 'password': 'HANA_DEV_PASSWORD',  # commented out — using SSO
    },
    'QAS': {
        'host':     'HANA_QAS_HOST',
        'port':     '30041',       # default 30041 if not set
        # 'user':     'HANA_USER',          # commented out — using SSO
        # 'password': 'HANA_QAS_PASSWORD',  # commented out — using SSO
    },
    'PRD': {
        'host':     'HANA_PRD_HOST',
        'port':     '30041',       # default 30041 if not set
        # 'user':     'HANA_USER',          # commented out — using SSO
        # 'password': 'HANA_PRD_PASSWORD',  # commented out — using SSO
    },
}

# Default port used when HANA_<ENV>_PORT env var is not set
HANA_DEFAULT_PORT = 30041

# SSO certificate paths — shared across environments (client identity + server CA)
# Set these env vars once:
#   setx HANA_SSL_KEYSTORE   "C:\path\to\client.pem"    # client cert + private key
#   setx HANA_SSL_TRUSTSTORE "C:\path\to\server-ca.pem" # server CA cert
HANA_SSL_CONFIG = {
    'ssl_keystore':   'HANA_SSL_KEYSTORE',    # client cert + private key (.pem)
    'ssl_truststore': 'HANA_SSL_TRUSTSTORE',  # server CA cert (.pem)
}
