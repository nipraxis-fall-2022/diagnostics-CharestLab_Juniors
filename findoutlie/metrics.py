""" Scan outlier metrics
"""

__all__ = [
    'dvars'
]

# Any imports you need
import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    data = img.get_fdata()
    diff = np.diff(data, axis=-1)
    diff_2d = diff.reshape(-1, diff.shape[-1])
    return np.sqrt(np.mean(diff_2d ** 2, axis=0))
