import cv2
def orb_sim(image1, image2):
    orb = cv2.ORB_create()
    try:
        kp_a, desc_a = orb.detectAndCompute(image1, None)
        kp_b, desc_b = orb.detectAndCompute(image2, None)
    except:
        print("Error image1")
        return 1
    if desc_a is None:
        print("image2 is blank")
        return 1
    elif desc_b is None:
        print("Image1 is blank")
        return 0
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.match(desc_a, desc_b)
    similar_regions = [i for i in matches if i.distance < 50]
    if(len(matches)) == 0:
        return 0
    return len(similar_regions) / len(matches)
img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")
similarity_ratio = orb_sim(img1, img2)

print("Similarity Ratio is: ", similarity_ratio)
