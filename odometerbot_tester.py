#!/usr/bin/env python
# -*- coding: utf-8 -*-

# odometerbot_tester.py

"""Simple client side Telegram bot test for the odometer bot
"""

import logging
import coloredlogs

# INFO: To show coloredlogs in PyCharm,
#       Edit Configurations, Configuration Tab "Emulate terminal in output console"

# Create a logger object.
logger = logging.getLogger(__name__)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
coloredlogs.install(level='DEBUG')

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
coloredlogs.install(level='DEBUG', logger=logger)

# Some examples from coloredlogs
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")


def main():
    logger.info("Starting odometerbot tester")


if __name__ == "__main__":
    main()
