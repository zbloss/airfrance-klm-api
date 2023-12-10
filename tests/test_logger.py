import pytest
import logging
from pydantic import ValidationError
from airfrance_klm_api.logger import Logger


class TestLogger:
    def test___init__(self):
        logger = Logger(module=__name__)
        assert isinstance(logger.module, str)
        assert isinstance(logger.log_level, str)
        assert isinstance(logger.logging_format, str)

    def test_get_logger(self):
        logger = Logger(module=__name__)
        assert isinstance(logger.get_logger(), logging.Logger)
        assert isinstance(logger.get_logger().level, int)
        assert isinstance(logger.get_logger().handlers, list)
        assert isinstance(logger.get_logger().filters, list)
        assert isinstance(logger.get_logger().propagate, bool)
        assert isinstance(logger.get_logger().disabled, bool)
        assert isinstance(logger.get_logger().manager, logging.Manager)
        assert isinstance(logger.get_logger().name, str)
        assert isinstance(logger.get_logger().parent, logging.Logger)
        assert isinstance(logger.get_logger().getChild(__name__), logging.Logger)
        assert isinstance(logger.get_logger().handlers, list)
        assert isinstance(logger.get_logger().filters, list)
        assert isinstance(logger.get_logger().propagate, bool)
        assert isinstance(logger.get_logger().disabled, bool)
        assert isinstance(logger.get_logger().manager, logging.Manager)
        assert isinstance(logger.get_logger().name, str)
        assert isinstance(logger.get_logger().parent, logging.Logger)
        assert isinstance(logger.get_logger().getChild(__name__), logging.Logger)
        assert isinstance(logger.get_logger().handlers, list)
        assert isinstance(logger.get_logger().filters, list)
        assert isinstance(logger.get_logger().propagate, bool)
        assert isinstance(logger.get_logger().disabled, bool)
        assert isinstance(logger.get_logger().manager, logging.Manager)
        assert isinstance(logger.get_logger().name, str)
        assert isinstance(logger.get_logger().parent, logging.Logger)
        assert isinstance(logger.get_logger().getChild(__name__), logging.Logger)
        assert isinstance(logger.get_logger().handlers, list)
        assert isinstance(logger.get_logger().filters, list)
        assert isinstance(logger.get_logger().propagate, bool)
        assert isinstance(logger.get_logger().disabled, bool)
        assert isinstance(logger.get_logger().manager, logging.Manager)
        assert isinstance(logger.get_logger().name, str)
        assert isinstance(logger.get_logger().parent, logging.Logger)
        assert isinstance(logger.get_logger().getChild(__name__), logging.Logger)
        assert isinstance(logger.get_logger().handlers, list)
        assert isinstance(logger.get_logger().filters, list)
        assert isinstance(logger.get_logger().propagate, bool)
        assert isinstance(logger.get_logger().disabled, bool)

    def test_invalid_log_level(self):
        with pytest.raises(ValidationError):
            logger = Logger(module=__name__, log_level="INVALID")
            logger.get_logger()
