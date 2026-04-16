import fitz  # This is the PyMuPDF library

# 1. Open your PDF file (make sure the name matches your file)
pdf_document = "D:\Flipbook\Copy of Smart Plastic English Print File with QR (2).pdf" 
doc = fitz.open(pdf_document)

# 2. Loop through every page and save it as a PNG image
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=150) # dpi=150 gives good web quality
    output_filename = f"page_{page_num}.png"
    pix.save(output_filename)
    print(f"Saved {output_filename}")

print("All pages converted successfully!")