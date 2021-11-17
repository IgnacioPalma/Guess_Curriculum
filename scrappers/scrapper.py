import pandas as pd

def properties(course):
    """ 
    Fetch and returns the properties of the course requested by the user.
    """
 
    # Extract information from "Catalogo UC" into data frames
    data_frames = pd.read_html(f"http://catalogo.uc.cl/index.php?tmpl=component&option=com_catalogo&view=requisitos&sigla={course}")
    
    # Convert the first table into a dictionary
    first_table = data_frames[0].to_dict(orient='records')

    # Initialization statement
    properties = {}

    # Loop through every row in the first table given by "Catalogo UC" and 
    # assign values into the dictionary
    for row in first_table:

        items = list(row.values())
        properties[items[0]] = items[1]
    
    # Return statement
    return properties
