import cv2
from imwatermark import WatermarkEncoder
from pydicom import dcmread
import matplotlib.pyplot as plt
from DicomEncoder import DicomEncoder

##Encoding
#1. Calculate Hu moments
#2. Embed watermark
#3. Create Hash
#4. Embed hash + hu moments


def main():
    print("Initializing DICOM...")
    encoder = DicomEncoder()
    encoder.encode_dicom('images/MRBRAIN.DCM')


if __name__ == '__main__':
    main()