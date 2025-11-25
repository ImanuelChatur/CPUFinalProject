import hashlib
import cv2
import numpy as np
from imwatermark import WatermarkEncoder
from numpy.random import normal
from pydicom import dcmwrite

class DicomEncoder:
    """
    Utility class for Encoding a Dicom File with various features to ensure image integrity
    - Many cool features!
    """
    @staticmethod
    def encode_dicom(dicom):
        """
        Encode dicom image
        :param dicom: Dicom object
        :return: Final pixel array of the encoded DICOM
        """
        print(f"Encoding Dicom file {dicom.get_name()}")
        print("Extracting Pixels")
        pixels = dicom.get_pixels()
        normal_array = dicom.get_normal_array()

        print("Calculating Hu Moments")
        hu = DicomEncoder.calculate_hu_moments(pixels)

        print("Creating Hash")
        h = DicomEncoder.create_hash(normal_array)

        print("Watermarking Pixels")
        watermarked_array = DicomEncoder.embed_watermark(normal_array, h)

        print("Saving as...")
        DicomEncoder.save_dicom_as(dicom, watermarked_array)

        print("Embedding hash + hu moments")
        #final_array = self.embed_hash()

        #view(watermarked_array)

        #return final_array
    @staticmethod
    def save_dicom_as(dicom, watermarkedData):
        dicomFile = dicom.get_dicom()
        pixels = dicom.get_pixels()
        #Un-normalize pixel data
        normalWatermarked = (watermarkedData / 255 * (pixels.max() - pixels.min()) + pixels.min()).astype(pixels.dtype)

        if normalWatermarked.ndim == 3:
            normalWatermarked = normalWatermarked[:, :, 0]

        dicomFile.PixelData = normalWatermarked.tobytes()


        dicomFile.save_as('watermarked.dcm')


    #1. Calculate Hu Moments
    @staticmethod
    def calculate_hu_moments(pixels):
        """
        Calculates the 7 hu moments to capture the shape of an image
        through minor adjustments such as scale and rotation.
        :param pixels: Pixel array of the DICOM
        :return: Array of the 7 hu moments in floating-point
        """
        moments = cv2.moments(pixels)
        hu_moments = cv2.HuMoments(moments).flatten()
        for i, moment in enumerate(hu_moments):
            print(f"Moment {i+1}: {moment}")
        return hu_moments

    #2. Embed Watermark
    @staticmethod
    def embed_watermark(normal_array, embedded):
        """
        Takes the normalized pixel array and adds an invisible watermark
        of the embedded string (in this case SHA-256 Hash)
        :param normal_array: Pixel array
        :param embedded: String to be encoded
        :return: Normal_array with watermark hidden inside
        """
        encoder = WatermarkEncoder()
        encoder.set_watermark('bytes', embedded.encode('ascii'))
        return encoder.encode(normal_array, 'dwtDct')

    #3. Create Hash
    @staticmethod
    def create_hash(normal_array):
        """
        Takes the normalized array, turns into SHA-256 Hash
        :param normal_array: Normalized array
        :return: SHA-256 Hash
        """
        c_arr = np.ascontiguousarray(normal_array)
        arr_bytes = c_arr.tobytes()
        hasher = hashlib.sha256()
        hasher.update(arr_bytes)
        return hasher.hexdigest()

    #4. Embed Hash + Hu moments
    @staticmethod
    def embed_hash():
        return 0