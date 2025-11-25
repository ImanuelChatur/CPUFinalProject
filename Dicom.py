import cv2
from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt

class Dicom:
    def __init__(self, dicom_name):
        self.dicom_name = dicom_name
        self.dicom = dcmread(dicom_name)
        self.pixels = self.dicom.pixel_array
        self.normal_array = ((self.pixels - self.pixels.min()) / (self.pixels.max() - self.pixels.min()) * 255).astype(
            np.uint8)
        self.normal_array = cv2.cvtColor(self.normal_array, cv2.COLOR_GRAY2BGR)

    def get_dicom(self):
        return self.dicom

    def get_name(self):
        return self.dicom_name

    def get_pixels(self):
        return self.pixels

    def get_normal_array(self):
        return self.normal_array

    def view(self):
        plt.imshow(self.pixels, cmap='gray')
        plt.show()

    def print_metadata(self):
        """
        Print the tags in the DICOM images
        :return:
        """
        for elem in self.dicom:
            tag = elem.tag
            name = elem.keyword
            value = elem.value

            # If the value is bytes, try decoding for readability
            if isinstance(value, bytes):
                try:
                    # Decode ASCII and strip null bytes
                    value_str = value.decode('ascii').rstrip('\x00')
                except UnicodeDecodeError:
                    # If it’s not text, just show the raw bytes length
                    value_str = f"<{len(value)} bytes>"
            else:
                value_str = value

            print(f"Tag: {tag}, Name: {name}, Value: {value_str}")