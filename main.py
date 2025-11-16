import cv2

##Encoding
#1. Calculate Hu moments
#2. Embed watermark
#3. Create Hash
#4. Embed hash + hu moments

def calculate_hu_moments(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 150, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print("Number of Contours detected:", len(contours))

    cnt = contours[0]
    M = cv2.moments(cnt)
    Hm = cv2.HuMoments(M) #Hu moments

    for i, cont in enumerate(contours):
        cv2.drawContours(img, cont, -1, (0, 255, 255), 3)
        x, y = cont[0,0]
        #cv2.putText(img, f'Contour {i}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    print("Hu-Moments of first contour:\n", Hm)
    cv2.imshow("Hu-Moments", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return Hm

#Embed Watermark
def embed_watermark(img):
    pass


def main():
    print("Hello World")
    img_name = 'images/kelpy.png'

    img = cv2.imread(img_name)

    #Get hu moments
    hu_moments = calculate_hu_moments(img)

    #Embed Watermark


if __name__ == '__main__':
    main()