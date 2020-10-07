### Single Unit Properties at Zillow: Predicting Values and Identifying Drivers

## Background

From Zillow:

"Zillow is the leading real estate and rental marketplace dedicated to empowering consumers with data, inspiration and knowledge around the place they call home, and connecting them with the best local professionals who can help.

Zillow serves the full lifecycle of owning and living in a home: buying, selling, renting, financing, remodeling and more. It starts with Zillow's living database of more than 110 million U.S. homes - including homes for sale, homes for rent and homes not currently on the market, as well as Zestimate home values, Rent Zestimates and other home-related information. Zillow operates the most popular suite of mobile real estate apps, with more than two dozen apps across all major platforms."


## Goals

This project has two primary goals:
1) Create a model that will acurrately predict the values of single unit properties that the tax district assesses.
2) Identify and report the drivers of the values of single unit properties that the tax district assesses.

We will deliver the following: 

- zillow_project.ipynb
    - A Jupyter Notebook that walks through the data science pipeline as it relates to each phase of this project.
    
- README.md
    - A Markdown file containing the project description with goals, a data dictionary, project planning, instructions for recreaction of the project and its findings, key findings and takeaways. 

- acquire.py
    - A Python file containing a function to acquire the customer data.
    
- prepare.py
    - A Python file containing functions that prepare the customer data to be worked with.

- model.py
    - A Pythong file containing a function that fits, predicts, and evaluates the final model on the test data.
    
- A walkthrough-style presentation that summarize our findings about the drivers of the single unit property values. 

- zillow_presentation.pptx
    - A PowerPoint file that contains the slides used in the presentation

## Data Dictionary

bathroom_count: Represents the number of bathrooms in a house

bathroomcnt: Represents the number of bathrooms in a house

bedroom_count: Represents the number of bedrooms in a house

bedroomcnt: Represents the number of bedrooms in a house

calculatedfinishedsquarefeet: Represents the amount of square footing in a house

lot_size_sq_fee: Represents the amount of square footing in the lot a house is located on

lotsizesquarefeet: Represents the amount of square footing in the lot a house is located on

tax_dollar_value: Represents the values of single unit properties that the tax district assesses

taxvaluedollarcnt: Represents the values of single unit properties that the tax district assesses

unit_sq_feet: Represents the amount of square footing in a house

## Initial Thoughts

As a former real estate agent, Matthew Knight, one of the two data scientists leading this project, believes that the number of bathrooms (bathroom_count), bedrooms (bedroom_count) and size of the house (unit_sq_feet) will be the strongest drivers of value. 

I agree with this assessment and believe that the size of a house (unit_sq_feet) will be the strongest feature to drive value up.

## Initial Hypothesis

House Size
H0 = There is no linear correlation between calculated finished square feet and home value.
H1 = There is a linear correlation between calculated finished square feet and home value.

Bathrooms
H0 = Houses with more than the average number of bathrooms are not valued higher than those with the average number or less
Ha = Houses with more than the average number of bathrooms are valued higher than those with the average number or less

Bedrooms
H0 = Houses with more than the average number of bedrooms are not valued higher than those with the average number or less
Ha = Houses with more than the average number of bedrooms are valued higher than those with the average number or less

## Project Plan

1) Create acquire.py

- steps of phase go here

2) Create prepare.py

- steps of phase go here

3) Explore

- steps of phase go here

3) Model

- steps of phase go here

4) conclusion

- steps of phase go here

## How to Reproduce

Install acquire.py, prepare.py and model.py into your working directory. (You must have access to Codeup data science database)

Run the jupyter notebook.

## Key Findings and Takeaways