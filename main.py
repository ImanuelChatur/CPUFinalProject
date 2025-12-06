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
    test = Dicom('images/MRBRAIN.DCM')

    test.print_metadata()
    encoder.encode_dicom(test)

   # test.view()

    new = Dicom('watermarked.dcm')
    try:
        new.view()
    except Exception as e:
        print(e)

    decoder.decode_dicom(new)
    print("FIN")


if __name__ == '__main__':
    main()