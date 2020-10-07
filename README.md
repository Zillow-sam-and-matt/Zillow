# Single Unit Properties at Zillow: Predicting Values and Identifying Drivers

## Background

From Zillow:

"Zillow is the leading real estate and rental marketplace dedicated to empowering consumers with data, inspiration and knowledge around the place they call home, and connecting them with the best local professionals who can help.

Zillow serves the full lifecycle of owning and living in a home: buying, selling, renting, financing, remodeling and more. It starts with Zillow's living database of more than 110 million U.S. homes - including homes for sale, homes for rent and homes not currently on the market, as well as Zestimate home values, Rent Zestimates and other home-related information. Zillow operates the most popular suite of mobile real estate apps, with more than two dozen apps across all major platforms."


## Goals

This project has three primary goals:
1) Create a model that will acurrately predict the values of single unit properties that the tax district assesses.
2) Identify and report the drivers of the values of single unit properties that the tax district assesses.
3) Provide a dataframe that contains the state, county, tax rate and county tax rate of each property as well as a dataframe that reflects the each county and their respective tax rate.

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

1) Acquire:
- Acquire data from zillow table in Codeup data science database server 
- Create acquire.py file using function(s) that acquired data

2) Preparation:
- Address null values (drop or fill)
- Ensure data types are good fit for data
- Rename columns if they are not easily understood or read
- Scale data if needed
- Split data into train, validate, test
- Create prepare.py that contains function(s) to automate these changes

3) Exploraton:
- Create heatmap to see correlation of viable features with one another and target variable
- Create visualizations to further identify relationships between features and target variable
- Run hypothesis tests to accept or reject hypothesis that are informed by our discoveries

4) Model:
- Create baseline model using mean of target variable to gauge what performance metric (RMSE)  our model must surpass
- Use feature engineering function (RFE) to rank features based on how well they can be used to predict house values
- Creates several linear regression models and use on train data
- Select 2-3 models that performed the best on train data and use on validate
- Select model that performed the best on validate dataset and use on test dataset
- Evaluate all findings

5) Additional item: Tax Rates by County
- Create dataframe that includes requested data per property
- Create dataframe that includes requested data per county

6) Conclusion
- Documents all key takeaways
- Provide recommendations based on findings
- Inform about plans for the future of project


## How to Reproduce

Install acquire.py, prepare.py and model.py into your working directory. (You must have access to Codeup data science database)

Run the jupyter notebook.

## Key Findings and Takeaways