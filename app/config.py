import os
import json
import sys

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
CONFIG_FILE = os.path.join(BASE_PATH, "config.json")
CERT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'certs', 'ca_bundle.cer')

with open(CONFIG_FILE, "r") as f:
    _config = json.load(f)

SUBACCOUNTS_API: str = _config["SUBACCOUNTS_API"]
CHECK_MASTER_API: str = _config["CHECK_MASTER_API"]
DEV_SERVER: str = _config["DEV_SERVER_HOST"]
QA_URLS: list[str] = _config["QA_HOSTS"]
PROD_URLS: list[str] = _config["PROD_HOSTS"]
LOG_LEVEL: str = _config.get("LOG_LEVEL", "INFO").upper()