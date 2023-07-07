# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:42:32 2023

@author: Juan Carlos
"""

country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]
print(country)
"""Create a dictionary of BRICS capitals.
Note that South Africa has
 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary

print(capitals)

print( capitals["South Africa"] [1] )
