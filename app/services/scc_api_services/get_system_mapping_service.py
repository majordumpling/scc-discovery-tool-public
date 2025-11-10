from app import config, logging_config
from app.services import request_service

logger = logging_config.get_logger(__name__)

def call_system_mappings_api(subaccounts: list[str], username: str, password: str) -> list[list[str]]:
    logger.info(f"Starting system mappings retrieval for {len(subaccounts)} subaccounts")
    
    system_mappings: list[list[str]] = [[
        "Subaccount ID",
        "Virtual Host",
        "Virtual Port",
        "Internal Host",
        "Internal Port",
        "Protocol",
        "Authentication"
    ]]

    for idx, subaccount in enumerate(subaccounts, 1):
        try:
            logger.info(f"Processing subaccount {idx}/{len(subaccounts)}: {subaccount}")
            response = request_service.create_request_json(subaccount, username, password, config.CERT_PATH)
            
            if not response:
                logger.warning(f"No response for subaccount: {subaccount}")
                continue
            
            subaccountId: list[str] = subaccount.split("/")
            mappings_count = 0
            
            for value in response:
                system_mappings.append((
                    subaccountId[-2],
                    value.get('virtualHost', ''),
                    value.get('virtualPort', ''),
                    value.get('localHost', ''),
                    value.get('localPort', ''),
                    value.get('protocol', ''),
                    value.get('authenticationMode', '')
                ))
                mappings_count += 1
            
            logger.info(f"Added {mappings_count} mappings for subaccount {idx}/{len(subaccounts)}")
            
        except Exception as e:
            logger.error(f"Error processing subaccount {subaccount}: {str(e)}", exc_info=True)
            # Continue with next subaccount

    total_mappings = len(system_mappings) - 1  # Exclude header
    logger.info(f"Completed system mappings retrieval: {total_mappings} total mappings found")
    return system_mappings