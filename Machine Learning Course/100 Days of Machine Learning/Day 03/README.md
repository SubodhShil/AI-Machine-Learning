
## **```Business problem to ML problem```**

### **```Churn rate```**
The decreasing rate of users or subscribers after a certain time. 

Steps to convert a business problem into ML problem using the following methods:

1. Identify the actual business problem.
2. **Type of problem and possible solution**: Selected business problem has to be a solveable approach using ML.
3. Current solution
4. **Getting data**: Data engineer will pay an important role here to categorie various factors utilizating users data. These factors are features of the ML model.
5. Metrics to measure the accuracy of the ML model.
6. Online vs batch learning.
7. Check assumptions.

## **```Data Collection```**
Data is the prerequisite for establishing any ML model. A ML is model much accurately predict or forecast result if the model is trained with quality dataset.


**Why to care about good dataset?**  

- The algorithm we've used behind the seen to develop a ML model, is actually predict patterns from the trained dataset and then give result. So, if the dataset is spoiled or faulty it will predict wrong result. 

**Resources for collecting dataset**  

1. [Kaggle](https://www.kaggle.com/datasets?fileType=csv)
2. [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
3. [Google Dataset Search](https://datasetsearch.research.google.com/)

## **```Import dataset through Kaggle API```**

> Downloading and importing dataset is a hectic process and this may take a lot of time if the dataset is large. There is an alternative but easy process to import dataset utilizing the **Kaggle API**. See, [Importing_dataset_through_Kaggle_API.ipynb](./Importing_dataset_through_Kaggle_API.ipynb)

## **```How to handle missing values```**

**Methods of handling missing values**: NaN or null values are missing values. We can handle those values using following techniques:
1. **Dropping**: Simply discard the row that contains the missing value.
   ```python
   dataset = dataset.dropna(how="any")
   ```
2. **Imputation**: For smaller datasets dropping values doesn't seems to be good for accurate result. So, we may use central tendency, a statistical methods to replace missing values in our dataset.    
   1. Central tendency:
      1. Mean: Average value. We can't use mean for skew.
        ```python
        dataset.salary.fillna(dataset.salary.median(), inplace=True)
        ```
      2. Median
        ```python
        dataset.salary.fillna(dataset.salary.mean(), inplace=True)
        ```
      3. Mode
        ```python
        dataset.salary.fillna(dataset.salary.mode(), inplace=True)
        ```


