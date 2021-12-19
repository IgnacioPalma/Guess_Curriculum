import pandas as pd

class Course:
    """ Define a course with his proper properties. """

    def __init__(self, id):

        # Extract information from "Catalogo UC" into data frames
        data_frames = pd.read_html(f"http://catalogo.uc.cl/index.php?tmpl=component&option=com_catalogo&view=requisitos&sigla={id}")
        
        # Convert the first table into a dictionary
        first_table = data_frames[0].to_dict(orient='records')

        # Initializations
        self.id = id
        self.properties = {}
        
        # Loop through every row in the first table given by "Catalogo UC" and 
        # assign values into the dictionary
        for row in first_table:

            items = list(row.values())
            self.properties[items[0]] = items[1]


    def prerequisites(self):
        """ Fetches and returns the prerequisites of the course. """
        
        # Check if there are prerequisites, if not, return None.
        if self.properties["Prerrequisitos"] == "No tiene":
            return None
        
        else:
            # Initializations
            init = 0
            last_condition = None
            prerequisites = []
            courses = []
            prerrequisitos_length = len(self.properties["Prerrequisitos"])

            # Loop through every character in the "Prerequisitos" section in order to order the courses
            # in sets exclusive and inclusive.
            for ind, char in enumerate(self.properties["Prerrequisitos"]):

                # Check if the string has a separation of conditions
                if char == "y" or char == "o":
                    
                    # Append the prerequisite course into the courses list and fix the init int
                    courses.append(self.properties["Prerrequisitos"][init:ind-1])
                    init = ind + 2

                    # Check for a change in the conditions, if so, append the checked courses into the final list,
                    # clear the courses list and stablish the type of last condition.
                    if last_condition != char and last_condition is not None:
                        prerequisites.append(courses)
                        courses = []
                    
                    last_condition = char

                # Check if we have got to the end of the string in order to append the final course
                elif ind == prerrequisitos_length - 1:
                    courses.append(self.properties["Prerrequisitos"][init:ind+1])
                    prerequisites.append(courses)

            # Positive return statement
            return prerequisites

        
        

