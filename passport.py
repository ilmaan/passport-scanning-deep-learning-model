# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


from passporteye.mrz.image import MRZPipeline
file = 'img1.jpeg'
p = MRZPipeline(file, extra_cmdline_params='--oem 0')
mrz = p.result
print(mrz)
