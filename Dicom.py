import cv2
from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt

class Dicom:
    def __init__(self, dicom_name):
        self.dicom_name = dicom_name
        self.dicom = dcmread(dicom_name)
        self.pixels = self.dicom.pixel_array
        self.normal_array = (((self.pixels - self.pixels.min()) / (self.pixels.max() - self.pixels.min()) * 255)
                             .astype(np.uint8))
        try:
            self.normal_array = cv2.cvtColor(self.normal_array, cv2.COLOR_GRAY2BGR)
        except Exception as e:
            print(e)

        print(f"Initializing dicom {self.dicom_name}")
        print(f"Pixels shape: {self.pixels.shape}")
        print(f"Normal_array shape: {self.normal_array.shape}")

    def get_dicom(self):
        return self.dicom

    def get_name(self):
        return self.dicom_name

    def get_pixels(self):
        return self.pixels

    def get_normal_array(self):
        return self.normal_array

    def view(self):
        print(f"{type(self.pixels)} << type of pixel!")
        print(self.pixels.shape)
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