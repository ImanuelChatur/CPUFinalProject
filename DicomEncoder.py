import cv2
from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np
import hashlib
#from imwatermark import WatermarkEncoder


class DicomEncoder:
    def __init__(self, dicom_name):
        #Get Dicom file
        self.dicom_name = dicom_name
        self.dicom = dcmread(self.dicom_name)

        #Get Pixels
        self.pixel_array = self.dicom.pixel_array


    def view(self):
        plt.imshow(self.dicom.pixel_array, cmap='gray')
        plt.show()

    #1. Calculate Hu Moments
    def calculate_hu_moments(self):
        print("Calculating Hu moments")
        moments = cv2.moments(self.pixel_array)
        hu_moments = cv2.HuMoments(moments).flatten()
        for moment in hu_moments:
            print(moment)

    #2. Embed Watermark
    def embed_watermark(self):
        pass

    #3. Create Hash
    def create_hash(self):
        c_arr = np.ascontiguousarray(self.pixel_array)
        arr_bytes = c_arr.tobytes()
        hasher = hashlib.sha256()
        hasher.update(arr_bytes)
        print(hasher.hexdigest())
        return hasher.hexdigest()

    #4. Embed Hash + Hu moments
    def embed_hash(self):
        pass