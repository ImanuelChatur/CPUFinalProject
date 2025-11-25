from DicomEncoder import DicomEncoder
from Dicom import Dicom
##Encoding
#1. Calculate Hu moments
#2. Embed watermark
#3. Create Hash
#4. Embed hash + hu moments


def main():
    print("Initializing DICOM...")
    brain = Dicom('images/MRBRAIN.DCM')
    encoder = DicomEncoder()
    encoder.encode_dicom(brain)


if __name__ == '__main__':
    main()