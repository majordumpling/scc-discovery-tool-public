import os
import json
import sys

def get_base_path():
    """Get the base path for the application, works with PyInstaller."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return os.path.dirname(sys.executable)
    else:
        # Running as script
        return os.path.dirname(os.path.abspath(sys.argv[0]))

BASE_PATH = get_base_path()
CONFIG_FILE = os.path.join(BASE_PATH, "config.json")
CERT_PATH = os.path.join(BASE_PATH, 'certs', 'ca_bundle.cer')

with open(CONFIG_FILE, "r") as f:
    _config = json.load(f)

SUBACCOUNTS_API: str = _config["SUBACCOUNTS_API"]
CHECK_MASTER_API: str = _config["CHECK_MASTER_API"]
DEV_SERVER: str = _config["DEV_SERVER_HOST"]
QA_URLS: list[str] = _config["QA_HOSTS"]
PROD_URLS: list[str] = _config["PROD_HOSTS"]
LOG_LEVEL: str = _config.get("LOG_LEVEL", "INFO").upper()