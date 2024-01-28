import time
import pickle
import logging

import pandas as pd
import imutils
import cv2
import numpy as np
import pytest
import plot3d

from .conftest import TEST_DIR, OUTPUTS_DIR

logger = logging.getLogger("plot3d")

EXAMPLE_TRAJECTORY = TEST_DIR / 'data' / 'trajectory.pkl'
MONITOR_PLY = TEST_DIR / 'assets' / 'monitor.ply'
MONITOR_POSE = TEST_DIR / 'assets' / 'tobii_2500.npy'

@pytest.fixture
def plot():
    plot = plot3d.Plot(port=9000)
    plot.reset()
    return plot
    
def test_plot_line(plot):

    N = 100
    line = np.random.uniform(low=0, high=1, size=(N, 3))
    plot.plot_line('test', line)


def test_image_streaming(plot):
    
    for i in range(300):

        frame = np.random.randint(low=0, high=255, size=(720, 1080, 3), dtype=np.uint8)
        logger.debug(f"Frame ID: {i}")
        plot.plot_image(imutils.resize(frame, width=500))
        i += 1
        time.sleep(1/40)
        # time.sleep(0.5)

def test_point_cloud_visualization(plot):

    N = 100
    for i in range(10):
        pts = np.random.uniform(low=0, high=1, size=(N, 3))
        colors = np.random.uniform(low=0, high=1, size=(N,4))
        plot.plot_pointcloud('test', pts, colors)
        time.sleep(0.5)
