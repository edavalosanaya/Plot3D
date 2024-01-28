import pathlib
import os
import logging

import pytest
import cv2

import plot3d

logger = logging.getLogger("plot3d")

TEST_DIR = pathlib.Path(os.path.abspath(__file__)).parent
GIT_ROOT = TEST_DIR.parent
OUTPUTS_DIR = TEST_DIR / 'outputs'

