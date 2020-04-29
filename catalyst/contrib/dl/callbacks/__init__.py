# flake8: noqa
import logging
import os

from catalyst.utils.tools import settings

from .criterion import CriterionAggregatorCallback
from .cutmix_callback import CutmixCallback
from .knn import KNNMetricCallback
from .optimizer import SaveModelGradsCallback
from .telegram_logger import TelegramLogger

logger = logging.getLogger(__name__)

try:
    import alchemy
    from .alchemy import AlchemyLogger
except ImportError as ex:
    if settings.alchemy_logger_required:
        logger.warning(
            "alchemy not available, to install alchemy, "
            "run `pip install alchemy`."
        )
        raise ex

try:
    import visdom
    from .visdom_logger import VisdomLogger
except ImportError as ex:
    if settings.visdom_logger_required:
        logger.warning(
            "visdom not available, to install visdom, "
            "run `pip install visdom`."
        )
        raise ex

try:
    import neptune
    from .neptune import NeptuneLogger
except ImportError as ex:
    if settings.neptune_logger_required:
        logger.warning(
            "neptune not available, to install neptune, "
            "run `pip install neptune-client`."
        )
        raise ex

try:
    import wandb
    from .wandb import WandbLogger
except ImportError as ex:
    if settings.wandb_logger_required:
        logger.warning(
            "wandb not available, to install wandb, "
            "run `pip install wandb`."
        )
        raise ex
