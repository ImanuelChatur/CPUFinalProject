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
    img_name = 'images/kelpy.png'
    img = cv2.imread(img_name)
    #hu_moments = calculate_hu_moments(img)


    print("Initializing DICOM...")
    dicom = DicomEncoder('images/0015.DCM')
    dicom.calculate_hu_moments()
    dicom.view()


if __name__ == '__main__':
    main()