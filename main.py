import pikepdf

# TODO: #1 Request the PDF files from the official page of the university and parse into file format.
        
def extract_urls(pdf):
    """ 
    Extract the urls embedded in hyperlinks from the PDF requested by the user.
    Returns a list with the urls obtained.
     """

    # Initializations
    pdf_file = pikepdf.Pdf.open(pdf)
    urls = []

    # Iterate over the pages
    for page in pdf_file.pages:
        for annots in page.get("/Annots"):
            uri = annots.get("/A").get("/URI")
            if uri is not None:
                urls.append(str(uri))

    # Return statement
    return urls

def identify_courses(url):
    """ 
    Identify if the url references a course.
    If possible, returns the referenced course, otherwise returns None.
    """

    # Check for the position previous to the course
    index = url.find("sigla=")

    # Check if the position has been found and extracts the course from the string.
    # Otherwise returns None
    if index != -1:
        init_position = index + len("sigla=")
        course = url[init_position:len(url)]

        # Return statement
        return course
    
    # None statement
    return None

# TODO: Add a curriculum "guesser" with the known courses and the nodes between them.
