from app import config, logging_config
from app.services import request_service

logger = logging_config.get_logger(__name__)

def _find_master(server_list: list[str], username: str, password: str, CERT_PATH: str) -> str:
    logger.info(f"Searching for master server among {len(server_list)} servers")
    
    for server in server_list:
        try:
            logger.info(f"Checking if {server} is master server")
            server_response = request_service.create_request_text(server + config.CHECK_MASTER_API, username, password, CERT_PATH)
            
            if server_response and server_response.strip().lower() == "true":
                logger.info(f"Master server: {server}")
                return server
            else:
                logger.info(f"{server} is not the master server")
                
        except Exception as e:
            logger.warning(f"Failed to check {server}: {str(e)}")
            continue
    
    logger.error("No master server found in the provided list")
    return None

def return_master_server(environment: str, username: str, password: str) -> str:
    logger.info(f"Determining master server for environment: {environment}")
    
    if environment == "Dev":
        logger.info(f"Master server: {config.DEV_SERVER}")
        return config.DEV_SERVER
    elif environment == "QA":
        logger.info("Searching for QA master server")
        return _find_master(config.QA_URLS, username, password, config.CERT_PATH)
    else:
        logger.info("Searching for Prod master server")
        return _find_master(config.PROD_URLS, username, password, config.CERT_PATH)