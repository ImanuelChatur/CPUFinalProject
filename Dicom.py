import cv2
from pydicom import dcmread
import numpy as np


class Dicom:
    def __init__(self, dicom_name):
        self.dicom_name = dicom_name
        self.dicom = dcmread(dicom_name)
        self.pixels = self.dicom.pixel_array
        self.normal_array = ((self.pixels - self.pixels.min()) / (self.pixels.max() - self.pixels.min()) * 255).astype(
            np.uint8)
        self.normal_array = cv2.cvtColor(self.normal_array, cv2.COLOR_GRAY2BGR)
