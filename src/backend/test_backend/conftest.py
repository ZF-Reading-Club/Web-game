"""Pytest configuration file for the backend tests.

TODO:
    pytest_assertrepr_compare and pytest_assertion_pass hooks are not working.
    The idea is the assertion details are logged when an assertion fails or passes in the HTML report.
    This could be useful for debugging and understanding the test results.
"""

import logging
import pytest
import sys

# Configure logging to output to stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True)
def pytest_assertrepr_compare(op, left, right):
    """Hook to log assertion details when an assertion fails."""
    logger.warning(f"Assertion failed: {left} {op} {right}")
    return None


@pytest.hookimpl(tryfirst=True)
def pytest_assertion_pass(item, lineno, orig, expl):
    """Hook to log assertion details when an assertion passes."""
    logger.info(f"Assertion passed: {orig} -> {expl}")
