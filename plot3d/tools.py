import numpy as np

def string_to_numpy(string):
    string = string.replace('[', '').replace(']', '').replace('\n', '')
    array = np.fromstring(string, sep=' ')
    array = array.reshape((4, 4))
    return array


def apply_rt_to_pts(pts, rt):
    homo_pts = np.hstack((pts, np.ones((pts.shape[0],1))))
    t_homo_pts = np.dot(rt, homo_pts.T).T
    return t_homo_pts[:, :3]
