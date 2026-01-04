# -*- coding: utf-8 -*-
import logging
from pathlib import Path

def main():
    logger = logging.getLogger(__name__)
    logger.info('predicting with model')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
