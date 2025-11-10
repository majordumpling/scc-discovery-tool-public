from app import logging_config
from app.ui import dialog
from app.services.scc_api_services import (
    master_instance_service,
    get_subaccounts_service,
    get_system_mapping_service
)
from app.repositories import report_generator

# Initialize logging
logging_config.setup_logging()
logger = logging_config.get_logger(__name__)

def main():
    try:
        logger.info("=" * 50)
        logger.info("Application started")
        logger.info("=" * 50)
        
        # Step 1: Get system environment
        logger.info("Requesting environment selection from user")
        environment = dialog.choose_environment()
        logger.info(f"Environment selected: {environment}")

        # Step 2: Get credentials
        logger.info("Requesting credentials from user")
        username, password = dialog.get_credentials()
        logger.info(f"Credentials received for user: {username}")

        # Step 3: Checks which is the master server
        logger.info("Identifying master server")
        master_server = master_instance_service.return_master_server(environment, username, password)
        logger.info(f"Master server identified: {master_server}")

        # Step 4: Get subaccount list
        logger.info("Retrieving subaccount list")
        subaccounts_list = get_subaccounts_service.call_subaccounts_api(master_server, username, password)
        logger.info(f"Retrieved {len(subaccounts_list)} subaccounts")

        # Step 5: Get system mappings
        logger.info("Retrieving system mappings")
        system_mappings_list = get_system_mapping_service.call_system_mappings_api(subaccounts_list, username, password)
        logger.info(f"Retrieved {len(system_mappings_list) - 1} system mappings")  # -1 for header

        # Step 6: Generate report
        logger.info("Generating report")
        report_generator.generate(system_mappings_list, environment)
        logger.info("Report generated successfully")
        
        logger.info("=" * 50)
        logger.info("Application completed successfully")
        logger.info("=" * 50)
        
    except Exception as e:
        logger.error("=" * 50)
        logger.error(f"Application error: {str(e)}", exc_info=True)
        logger.error("=" * 50)
        raise

if __name__ == "__main__":
    main()