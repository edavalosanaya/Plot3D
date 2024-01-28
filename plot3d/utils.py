import logging
import pickle

import numpy as np
import simplejpeg
import blosc
import socket

logger = logging.getLogger("plot3d")

def get_ip_address() -> str:
    """Get the IP address of the current machine."""

    # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)

    try:
        # doesn't even have to be reachable
        s.connect(("10.254.254.254", 1))
        ip = str(s.getsockname()[0])
    except:  # noqa E722
        ip = "127.0.0.1"
    finally:
        s.close()

    return ip

def serialize(data):
    return blosc.compress(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))

def deserialize(data_bytes):
    return pickle.loads(blosc.decompress(data_bytes))

def serialize_image(image: np.ndarray):
    return simplejpeg.encode_jpeg(np.ascontiguousarray(image))

def deserialize_image(image_bytes: bytes):
    return simplejpeg.decode_jpeg(image_bytes)
