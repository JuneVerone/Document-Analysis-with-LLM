import pdfplumber

pdf_path = r"C:\Users\JUNE VERON\OneDrive\Desktop\Document Analysis with LLM\google_terms_of_service_en_in.pdf"

output_text_file = "extracted_text.txt"

with pdfplumber.open(pdf_path) as pdf:
    extracted_text = ""
    for page in pdf.pages:
        extracted_text += page.extract_text()

with open(output_text_file, "w") as text_file:
    text_file.write(extracted_text)

print(f"Text extracted and saved to {output_text_file}")


# reading pdf content
with open("C:\\Users\\JUNE VERON\\OneDrive\\Desktop\\Document Analysis with LLM\\google_terms_of_service_en_in.pdf", "r") as file:
    document_text = file.read()

# preview the document content
print(document_text[:500])  # preview the first 500 characters