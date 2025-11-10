from app import config, logging_config
from app.services import request_service

logger = logging_config.get_logger(__name__)

def call_subaccounts_api(server: str, username: str, password: str) -> list[str]:
    logger.info(f"Calling subaccounts API on server: {server}")
    
    subaccounts: list[str] = []
    
    try:
        data = request_service.create_request_json(server + config.SUBACCOUNTS_API, username, password, config.CERT_PATH)
        
        if not data:
            logger.warning("No data returned from subaccounts API")
            return subaccounts
        
        logger.info(f"Processing {len(data)} items from subaccounts API")
        
        for item in data:
            systemMappings = item['_links'].get('systemMappings', {}).get('href', None)
            if systemMappings:
                subaccounts.append(systemMappings)
        
        logger.info(f"Found {len(subaccounts)} subaccounts with system mappings")
        
    except Exception as e:
        logger.error(f"Error calling subaccounts API: {str(e)}", exc_info=True)
        raise
    
    return subaccounts