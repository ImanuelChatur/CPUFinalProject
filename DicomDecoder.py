from imwatermark import WatermarkDecoder
class DicomDecoder:

    @staticmethod
    def decode_dicom(dicom):
        print(f"Decoding Dicom File: {dicom.get_name()}")
        print("Decoding Dicom")
        DicomDecoder.extract_watermark(dicom.get_normal_array())



    @staticmethod
    def save_dicom_as(dicom):
        pass

    @staticmethod
    def extract_watermark(normal_array):
        print(f"DECODING NORMAL ARRAY: {normal_array.shape}")
        decoder = WatermarkDecoder(wm_type='bytes', length=64)
        decoded = decoder.decode(normal_array, 'dwtDct')
        decoded_hash = decoded.decode('ascii')
        print(decoded_hash)
