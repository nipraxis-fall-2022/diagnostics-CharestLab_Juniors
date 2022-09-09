""" Module with routines for finding outliers
"""

__all__ = [
    'detect_outliers',
    'find_outliers'
]

from pathlib import Path
import numpy as np
import nibabel as nib
from .metrics import dvars
from .detectors import iqr_detector

def detect_outliers(fname):
    """ Return outlier indices for a specified image.

    Parameters
    ----------
    fname : str
        Filename of image to check for outliers.

    Returns
    -------
    outlier_idcs : np.array
        Array of outlier indices for given image.
    """
    img = nib.load(fname)
    metrics = dvars(img)
    is_outlier = iqr_detector(metrics)
    return np.nonzero(is_outlier)


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = Path(data_directory).glob('**/sub-*.nii.gz')
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
