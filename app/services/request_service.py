import requests
import os
from app import logging_config

logger = logging_config.get_logger(__name__)

def create_request_text(url: str, username: str, password: str, CERT_PATH: str) -> str:
    CERT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'certs', 'ca_bundle.cer')
    
    try:
        logger.info(f"Making request to: {url}")
        response = requests.get(url, auth=(username, password), verify=CERT_PATH)
        
        if response.status_code == 200:
            logger.info(f"Successfully retrieved response (status: {response.status_code})")
            return response.text
        else:
            logger.warning(f"Request returned status code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}", exc_info=True)
        raise
    
def create_request_json(url: str, username: str, password: str, CERT_PATH: str) -> dict:
    CERT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'certs', 'ca_bundle.cer')
    
    try:
        logger.info(f"Making JSON request to: {url}")
        response = requests.get(url, auth=(username, password), verify=CERT_PATH)
        
        if response.status_code == 200:
            logger.info(f"Successfully retrieved JSON response (status: {response.status_code})")
            return response.json()
        else:
            logger.warning(f"Request returned status code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}", exc_info=True)
        raise