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
####  Data Usage. (a) What outside data have you appended to the original data set? Why did you choose this data? 

- Our original intent was to find the racial demographic statistics based on zip code. We had hoped to find some correlation with rent and the racial demographics of the area. However, after running the racial demographic data frame through a heatmap. We saw there was no correlation with rent whatsoever. It may be that his particular dataset just wasn’t useful for us. Here is the link to the original dataset https://catalog.data.gov/dataset/demographic-statistics-by-zip-code-acfc9.
- We chose to include income data from the US Census Bureau. This data contained the median income of every zip code in the United States. We merged this data with our original rent price data on zip codes so each data point would have an income level to associate with.
- Our main reason for choosing income data was the idea that people who have more money would have more money available for spending on rent. With this theory in mind, it would follow logically that higher income areas would have higher rent costs

#### Does the inclusion of this additional data raise any ethical considerations? 

- There is an ethical problem with high income demographics moving into low income areas. Populations that until recent years paid lower rents because of their lower income suddenly have to pay more in rent because of higher income populations moving in. This is a common symptom of gentrification and is a part of the issue with it. 

#### What outliers present issues for your analysis? How have you chosen to handle them? Why? 

There were some very odd outliers. For example, there were a few instances where the number of bedrooms would be greater than 5, but rent would be under 10k. This is odd because if number of rooms correlates with rent. Then any room number greater than 5 should have a much higher rent. A few instances where number of bedrooms were zero also, mostly a studio apartment.
Bathrooms also had the same problem as bedrooms. There were at least 3 instances where the number of bathrooms would be greater than 10, but the rent price would be below 10k. There’s also one instance where the number of bathrooms was 20, but the rent was below 10k.

The square footage suffered the same problem as bathrooms and bedrooms. There were some instances where the square footage was zero, but had a rent prices. There were two instances where square footage was around 10k but rent was below 10k. 
 We removed outliers multiple times, but due to our lack of experience it gave us a slightly higher mean square error. Which we didn’t know how to handle. In the end, we decided to keep the outliers as is because the mean squared error didn’t show significant change or it increased our mean squared error in some way. As a result, we decided on the random forest regressor. The random forest regressor gave us a mean square error we find acceptable. 

#### To what extent do missing values pose a challenge for your analysis? How have you chosen to handle them? Why?

There weren't many missing values to begin with, but we didn’t want to remove any important data. Dropping the null values and filling the null values with the median of the columns didn’t affect the mean squared error by much; as a result, we filled most of the null values with the median for random forest. 

#### Are there any other aspects of the data your exploration shows might be problematic?

Other than some of the odd outliers. We didn’t run into anything problematic.

#### Describe 5 features you think play the biggest role in your model. 

1. The External Dataset had a “Median Household Income” column that had a correlation of 0.3 with rent.
2. Bathroom 0.61
3. Size_sqft 0.65
4. Bin -0.33
5. BBl -0.34
6. Floor_count 0.25

The median Household income was chosen as the external dataset feature because income provides a positive correlation with rent and it allows people who rent to rent more premium buildings which also relates to 0.27 which makes them quite relatable and might even go hand in hand(similar reasoning). The number of bathrooms may be very relative to the (Square Footage)size of the place of rent. This is why we think there is such similar positive correlation(0.61 to 0.65) to rent. BIN(Building Identification Number negative correlation of -0.33 is negatively correlated with rent) gives us a rough estimate to borough or place which gives a relative area to where the place may be more affluent and other factors in the nearby region of the building. (if BBL stands of Borough, Building and lot, this would give us a similar correlation to BIN(negative correlation -0.34) also based on the same types of factors as BIN. Has_doorman has the least positive correlation out of the list of features we’ve selected but still relevant as we think it pertains to perhaps the location having a premium service.

#### Describe how you are implementing your model. Why do you think this works well? 

We selected a total of 6 classification variables. Thus, I make a hot encoding for all the classification variables first. Then we clean the data from empty and NaN values by filling them with media of the column. Once data was cleaned. We passed our dataset containing features and an array containing our target variable, rent. The random forest works by creating multiple decision trees that make predictions on different parts of our data. It thens averages those predictions into in final prediction for a particular input. Decision trees within the forest work perfectly for our classification variables. For our quantitative variables, we notice that many values repeat given similar conditions. Thus, they can be classified by a random forest despite error and still get an accurate prediction.


#### Describe your methodology for selecting your model. Why do you think this type of model works well? (4) Metrics, Validation, and Evaluation. 3

We began with a simple model of a linear regression, and we stuck with this until we could find another model to replace it which would perform better. This model turned out to be a random forest. The Mean Square Error of our final model ended up being 1,797,974. 

#### How well do you think you model will perform on the hold out test set? How do you know? 

I think our model will perform reasonably well. Our MSE is approximately 1.7 million. Which means that the error  was on average $1000 dollars for the rent values of test1.csv. We expected to see similar results in test3.csv because we split up our test data and worked to not overtrain our model.

#### Is your model useful? Why or why not?

Yes, it is useful because it can predict rent to an acceptable average error.

#### Are there any special cases in which your model works particularly well or particularly poorly?

Random Forest model are very prompt to overfitting the data. If we were to increase the number of features of our model, there is the possibility that the model will overfit the training dataset increase the mse and thus, giving unreliable predictions.

### Conclusion 

Our original intent was to use racial demographic information by zip code for our model, but the dataset we found gave us no correlation with rent whatsoever. It maybe that this particular dataset wasn’t useful. Instead we chose to include income data from the US Census Bureau. This data contained the median income of every zip code in the United States. With this in mind, it would follow logically that higher income areas would have higher rent costs. 

After testing linear regression, polynomial regression, decision trees, k-nearest neighbors with test1.csv, and finally random forest. We found that random forest gave us the lowest mean square value for test1.csv.. Linear regression and polynomial regression are the simplest models, but gave us a mean square error of less than 4 million, while polynomial regression gave a mse of less than 3 million with test1.csv, we weren’t satisfied with the mean squared error because our original model was a simple linear regression which only gave us a mse of around 2 million for test2.csv. As a result, we used random forest; which gave us the lowest mean squared error against test1.csv. With this, we hope that our random forest model 
