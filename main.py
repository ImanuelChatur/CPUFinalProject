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
    dicom = DicomEncoder('images/MRBRAIN.DCM')

    print("Calculating Hu moments...")
    dicom.calculate_hu_moments()

    print("Creating hash...")
    dicom.create_hash()

    print("Embedding Watermark...")
    #dicom.embed_watermark()

    print("Metadata printing...")
    dicom.print_metadata()
    print("Viewing image")
    #dicom.view()


if __name__ == '__main__':
    main()