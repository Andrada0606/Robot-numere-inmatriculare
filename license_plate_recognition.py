import cv2
import easyocr

# Inițializarea cititorului OCR
reader = easyocr.Reader(['en'], gpu=False)

def recognize_license_plate(image_path):
    # Citirea imaginii
    frame = cv2.imread(image_path)

    # Conversia imaginii în tonuri de gri
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Citirea textului din imagine folosind EasyOCR
    result = reader.readtext(gray)
    
    # Parcurgerea rezultatelor pentru identificarea textului din placa de înmatriculare
    for detection in result:
        text = detection[1]  # Extrage textul detectat
        print('Text detectat:', text)

        # Aici poți adăuga logica suplimentară pentru a verifica dacă textul corespunde unei plăcuțe de înmatriculare

    reader.close()

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Schimbă această cale cu calea către imaginea ta
    recognize_license_plate(image_path)
