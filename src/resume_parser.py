import pdfplumber

def extract_text(pdf_file):
    """
    Extract raw text from uploaded PDF resume
    """
    text = ""

    # open pdf file stream
    with pdfplumber.open(pdf_file) as pdf:

        # iterate through each page
        for page in pdf.pages:
            page_text = page.extract_text()

            # Append only if text exists
            if page_text:
                text += page_text +"\n"

    return text