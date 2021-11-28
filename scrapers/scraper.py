import pandas as pd

def properties(course):
    """ 
    Fetch and returns the properties of the course requested by the user in a dictionary.
    """
 
    # Extract information from "Catalogo UC" into data frames
    data_frames = pd.read_html(f"http://catalogo.uc.cl/index.php?tmpl=component&option=com_catalogo&view=requisitos&sigla={course}")
    
    # Convert the first table into a dictionary
    first_table = data_frames[0].to_dict(orient='records')

    # Initializations
    properties = {}
    
    # Loop through every row in the first table given by "Catalogo UC" and 
    # assign values into the dictionary
    for row in first_table:

        items = list(row.values())
        properties[items[0]] = items[1]
    
    # Initializations
    init = 0
    lista = [] # TODO: Change name later
    courses = []
    prerrequisitos_length = len(properties["Prerrequisitos"])
    last_condition = None

    # Loop through every character in the "Prerequisitos" section in order to order the courses
    # in sets exclusive and inclusive.
    for ind, char in enumerate(properties["Prerrequisitos"]):

        # Check if the string has a separation of conditions
        if char == "y" or char == "o":

            courses.append(properties["Prerrequisitos"][init:ind-1])
            init = ind + 2

            # Check for a change in the conditions
            if last_condition != char and last_condition is not None:
                lista.append(courses)
                courses = []
            
            last_condition = char

        # Check if we have got to the end of the string in order to append the final course
        elif ind == prerrequisitos_length - 1:
            courses.append(properties["Prerrequisitos"][init:ind+1])
            lista.append(courses)
    
    print(lista)

        
        

