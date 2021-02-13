# Single Unit Properties at Zillow: Predicting Values and Identifying Drivers

## Background

From Zillow:

"Zillow is the leading real estate and rental marketplace dedicated to empowering consumers with data, inspiration and knowledge around the place they call home, and connecting them with the best local professionals who can help.

Zillow serves the full lifecycle of owning and living in a home: buying, selling, renting, financing, remodeling and more. It starts with Zillow's living database of more than 110 million U.S. homes - including homes for sale, homes for rent and homes not currently on the market, as well as Zestimate home values, Rent Zestimates and other home-related information. Zillow operates the most popular suite of mobile real estate apps, with more than two dozen apps across all major platforms."


## Goals

This project has two goals:
- Identify variables that have a strong impact on the values of single unit properties that the tax district assesses
- Create a model that will accurately predict the values of single unit properties that the tax district assesses


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
    
- A presentation that summarizes our findings about the drivers of the single unit property values. 

- zillow_presentation.pptx
    - A PowerPoint file that contains the slides used in the presentation

## Data Dictionary

bathroom_count (renamed from bathroomcnt): Represents the number of bathrooms in a house

bedroom_count (renamed from bedroomcnt): Represents the number of bedrooms in a house

lot_size_sq_feet (renamed from lotsizesquarefeet): Represents the amount of square footing in the lot a house is located on

tax_dollar_value (renamed from taxvaluedollarcnt): Represents the values of single unit properties that the tax district assesses

unit_sq_feet (renamed from calculatedfinishedsquarefeet): Represents the amount of square footing in a house

## Reasons for Selected Columns

bathroom_count (bathroomcnt): The names of the alternative columns, fullbathcnt and calculatedbathnbr, did not seem as straightfoward as bathroomcnt, so we opted to use bathroomcnt. We also tested and found that there were only 13 rows that differed in values between bathroomcnt and each of the alternatives so were confident that the differences would not have a serious impact.

bedroom_count (bedroom_count): This was the only column that held solely bedroom counts so we chose it by default.

unit_sq_feet (calculatedfinishedsquarefeet): We tested and found that there were only 13 rows with differing values in calculatedfinishedsquarefeet and finishedsquarefeet12. The "12" in finishedsquarefeet12 suggested to us at that the differing values in this column were not the simple square feet area that we were looking for, so we opted for calculatedfinishedsquarefeet.

lot_size_sq_ft (lotsizesquarefeet): This was the only column that held lot size square feet so we chose it by default.

tax_dollar_value (taxvaluedollarcnt): We used this as our target variable since it is the sum of structuretaxvaluedollarcnt and landtaxvaluedollarcnt. This implied that it was the best column to represent the total value assessed by the tax office. 

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

- Through exploration we discovered that drivers of property value include bathroom_count, bedroom_count, unit_sq_feet, and lot_size_sq_feet
    
- Based on the results of a pearson correlation test, lot_size_sq_feet was thought to have virtually no relationship with property_value, our models performed worse without it

Recursive Feature Elimination ranked the importance of each feature in predicting value as follows:

- 1 - bathroom_count
- 2 - bedroom_count
- 3 - unit_sq_feet
- 4 - lot_size_sq_feet

Recommendations
- When assessing the value of properties, we should focus our attention on these drivers to help improve the accuracy of our value assessments.
- We should also display these features more prominently in our search result thumbnails as currently the font is relatively small.

We've created a linear regression model that uses these variables to predict property values.
- The model outperformed a baseline model that constantly predicts the mean value of homes
- The model's RMSE value on all data sets was consistently lower than all of its competitors 
- In one instance, the model only performed nearly as well on data it had never seen before (test) than it did on the data it was trained on (train). 

In the future
- We'd like to collect a wider range of data since many of the features in our dataset contained a high amount of null values and had to be excluded from our project.
    - With more features available, we may be able to incorporate new ones that improve our model's ability to make accurate predictions on property values.