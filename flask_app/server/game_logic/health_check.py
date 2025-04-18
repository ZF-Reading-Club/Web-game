import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def health_check_response(status: str = "ok") -> dict:
    """Create a response dictionary with status and timestamp.

    Args:
        status (str): The status of the response. Defaults to "ok".

    Returns:
        dict: A response dictionary with status and timestamp.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {"status": status, "message": f"Server response at {current_time}"}
    logger.info(f"Response: {response}")
    return response
