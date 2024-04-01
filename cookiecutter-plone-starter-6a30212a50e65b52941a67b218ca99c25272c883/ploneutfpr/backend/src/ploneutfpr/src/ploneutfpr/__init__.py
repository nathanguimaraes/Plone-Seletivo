"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "ploneutfpr"

_ = MessageFactory("ploneutfpr")

logger = logging.getLogger("ploneutfpr")
