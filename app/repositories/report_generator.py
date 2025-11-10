from datetime import datetime
from app.ui import dialog
from app import logging_config

import os
import pandas as pd

logger = logging_config.get_logger(__name__)

def generate(matrix: list[list[str]], file_name: str) -> None:
    logger.info(f"Generating report with {len(matrix) - 1} data rows")
    
    date_str = datetime.now().strftime("%m.%d.%Y")
    
    desktop_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        f"{file_name} - {date_str}.xlsx"
    )
    
    logger.info(f"Report will be saved to: {desktop_path}")
    
    try:
        df = pd.DataFrame(matrix)
        df.to_excel(desktop_path, index=False, header=False)
        logger.info("Report successfully written to file")
        
        dialog.display_messagebox(desktop_path)
        logger.info("Success message displayed to user")
        
    except Exception as e:
        logger.error(f"Error generating report: {str(e)}", exc_info=True)
        raise