# import class to create PDF documents
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Import default text styles (fonts , sizes spacing)
from reportlab.lib.styles import getSampleStyleSheet

# os module used for creating folders if they don't exist
import os

def generate_report(name, content):
    """
    Generates a PDF report from interview feedback text
    """
    # Create "reports" folder if it doesn't already exist
    os.makedirs("reports", exist_ok=True)

    # Define full file path where PDF will be saved
    # Example: reports/Allice_interview_report.pdf
    file_path = f"reports/{name}_interview_report.pdf"

    # create pdf document object
    # this defines where the pdf will saved
    doc = SimpleDocTemplate(file_path)

    # Load default style sheet (Normal, Heading styles, etc.)
    styles = getSampleStyleSheet()

    # this list will hold all text element (paragraph) for the pdf
    story = []

    # split the ai-generated content into lines
    # each line becomes a seperate paragraph in pdf
    for line in content.split("\n"):
        if line.strip():
            # convert each line into a styled paragraph
            # styles["normal"] = default text style
            story.append(Paragraph(line, styles["Normal"]))

    # build the final pdf using all paragraph stored in "story"
    doc.build(story)

    # Return the saved file path so app can show/download it
    return file_path