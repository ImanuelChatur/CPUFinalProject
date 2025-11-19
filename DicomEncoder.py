import cv2
from imwatermark import WatermarkEncoder
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
        self.pixels = self.dicom.pixel_array
        self.normal_array = ((self.pixels - self.pixels.min()) / (self.pixels.max() - self.pixels.min()) * 255).astype(np.uint8)
        self.normal_array = cv2.cvtColor(self.normal_array, cv2.COLOR_GRAY2BGR)


    def view(self):
        plt.imshow(self.dicom.pixel_array, cmap='gray')
        plt.show()

    def print_metadata(self):
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

    #1. Calculate Hu Moments
    def calculate_hu_moments(self):
        print("Calculating Hu moments")
        moments = cv2.moments(self.pixels)
        hu_moments = cv2.HuMoments(moments).flatten()
        for i, moment in enumerate(hu_moments):
            print(f"Moment {i+1}: {moment}")

    #2. Embed Watermark
    def embed_watermark(self):
        encoder = WatermarkEncoder()
        encoder.set_watermark('bytes', self.create_hash().encode('ascii'))
        watermarked_array = encoder.encode(self.normal_array, 'dwtDct')

    #3. Create Hash
    def create_hash(self):
        c_arr = np.ascontiguousarray(self.normal_array)
        arr_bytes = c_arr.tobytes()
        hasher = hashlib.sha256()
        hasher.update(arr_bytes)
        print(hasher.hexdigest())
        return hasher.hexdigest()

    #4. Embed Hash + Hu moments
    def embed_hash(self):
        pass