import cv2
from imwatermark import WatermarkEncoder
from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np
import hashlib
#from imwatermark import WatermarkEncoder


class DicomEncoder:
    """
    Utility class for Encoding a Dicom File with various features to ensure image integrity
    """
    def encode_dicom(self, dicom_name):
        """
        Encode dicom image
        :param dicom_name: Location of the DICOM file
        :return: Final pixel array of the encoded DICOM
        """
        print(f"Encoding Dicom file {dicom_name}")
        dicom = dcmread(dicom_name)
        print("Extracting Pixels")
        pixels = dicom.pixel_array
        normal_array = ((pixels - pixels.min()) / (pixels.max() - pixels.min()) * 255).astype(np.uint8)
        normal_array = cv2.cvtColor(normal_array, cv2.COLOR_GRAY2BGR)

        print("Calculating Hu Moments")
        hu = self.calculate_hu_moments(pixels)

        print("Creating Hash")
        hash = self.create_hash(normal_array)

        print("Watermarking Pixels")
        watermarked_array = self.embed_watermark(normal_array, hash)

        print("Embedding hash + hu moments")
        #final_array = self.embed_hash()

        self.view(watermarked_array)

        #return final_array


    def view(self, pixel_array):
        plt.imshow(pixel_array, cmap='gray')
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
    def calculate_hu_moments(self, pixels):
        moments = cv2.moments(pixels)
        hu_moments = cv2.HuMoments(moments).flatten()
        for i, moment in enumerate(hu_moments):
            print(f"Moment {i+1}: {moment}")
        return hu_moments

    #2. Embed Watermark
    def embed_watermark(self, normal_array, embedded):
        encoder = WatermarkEncoder()
        encoder.set_watermark('bytes', embedded.encode('ascii'))
        return encoder.encode(normal_array, 'dwtDct')

    #3. Create Hash
    def create_hash(self, normal_array):
        c_arr = np.ascontiguousarray(normal_array)
        arr_bytes = c_arr.tobytes()
        hasher = hashlib.sha256()
        hasher.update(arr_bytes)
        return hasher.hexdigest()

    #4. Embed Hash + Hu moments
    def embed_hash(self):
        return 0