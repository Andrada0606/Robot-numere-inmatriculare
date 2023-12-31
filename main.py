import cv2
from PIL import Image
import pytesseract
import os


directory = (r"C:\users\andrada\Documents\poze nr inmatriculare")
def is_image(file_path):
    pass
for filename in os.listdir(directory):
    if "nr_inmatriculare" in filename:
        file_path = os.path.join(directory, filename)
        if is_image(file_path):
            with Image.open(file_path) as img:
                img.show()
        else:
         print(f"{filename} nu este o imagine.")
    else:
        print(f"{filename} nu se potrivește formatului cerut.")

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Reducerea zgomotului cu un filtru Gaussian
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return gray

def localize_license_plate(image):
    edges = cv2.Canny(image, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        plate_region = image[y:y + h, x:x + w]
        return plate_region
    return None


def recognize_registration_number(plate_region):
    if plate_region is not None:
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(plate_region, config=custom_config)
        return text.strip()
    return None


# Citim imaginea
image = cv2.imread('nr_inmatriculare.jpg')

# Preprocesam imaginea
processed_image = preprocess_image(image)

#Localizarea placii de inmatriculare
plate_region = localize_license_plate(processed_image)

if plate_region is not None:
    #Afiseaza regiunea extrasa
    cv2.imshow('Detected Plate Region', plate_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Recunoaste numarul de inmatriculare
    registration_number = recognize_registration_number(plate_region)

    if registration_number:
        print("Detected Registration Number:", registration_number)
    else:
        print("Registration number recognition failed.")
else:
    print("License plate localization failed.")
