import logging
import parameters as cfg
logger = logging
logger.basicConfig(filename=cfg.logfile, level=cfg.loglevel)
