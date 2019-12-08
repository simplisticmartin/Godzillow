# Team Name: GodZillow

# Members: Jon Tran, Martin, Kieran, Enger

### Project Findings
#### Do you show evidence of making meaningful progress beyond the modeling steps made in lecture 5?
Our original model was a linear regression model. Which gave us decent results of mse around 3 million, But we realize other models may perform better.
Use multiple models, heatmaps, and charts to make progress towards lowering the mse. 
#### Have you applied techniques and strategies demonstrated over the course of the semester? 
- Test different models
- Filled null values
- Cleaned the data

New data set gave us a lower mse for linear regression
New data set gave us a lower mse for polynomial regression
However, the new data set increased our mse for random forest by 200k, but was still the lowest mse out of all the models.
Filling the null values lowered the mse for linear regression but increased it for all over models. However random forest model still is the lowest. 
#### Do you have a well thought designed strategy for improving your model performance before the final due date? (3) Accuracy of predictions for test3.csv.
- Our strategy was to find additional data that would give us better results for our model predictions on test1.
- Cleaning the data and handle null values. 
- After some research Enger realized that random forest regressor performs better with boolean features. So include features like ‘has_doorman’, ‘has_gym’ for our random forest model. 
