from DicomDecoder import DicomDecoder
from DicomEncoder import DicomEncoder
from Dicom import Dicom

##Encoding
#1. Calculate Hu moments
#2. Embed watermark
#3. Create Hash
#4. Embed hash + hu moments


def main():
    encoder = DicomEncoder()
    decoder = DicomDecoder()

    print("Initializing DICOM...")
    #brain = Dicom('images/MRBRAIN.DCM')
    test = Dicom('images/0015.DCM')

    encoder.encode_dicom(test)

    test.view()

    new = Dicom('watermarked.dcm')
    new.view()

    decoder.decode_dicom(new)


if __name__ == '__main__':
    main()