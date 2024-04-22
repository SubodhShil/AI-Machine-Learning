u**Features**: All the available input data those are independent.  
**Label**: What we have to predict or guess. Labels are dependent on the features data.

> **Q1**: Can we have multiple numbers of features and labels?

1. **Supervised Learning**
   - **Classification**: Which class or category the data represents. It classifies the data label.
     - Binary classification: Only contains two categories.
     - Multi-class classification: Contains more than two categories.
   - **Regression**: What to predict, guess or forecast *numerical values* based previously trained features.

2. **Unsupervised Learning**: <ins>**No output or label or dependent variable is provided**</ins>, the algorithm divide dataset into multiple groups or clusters based on similarity of features. So, within a cluster the data is share similar traits whereas between clusters there are abundance of differentiable traits.

3. **Reinforcement Learning**: Imitate real-world learning process of humans. Reinforce to do a task by providing rewards (if it continues to do the task in the correct way) or penalize (if it is not providing any good result).

&nbsp;

### ```Practical usecase```

| Example | Description | Paradigm | Explanation |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Predict house prices | Given features like number of bedrooms, square footage, and location, determine the selling price of a house. | **Regression** | As we have to predict house price which is a numerical value (if the problem asked to house will sell or not then it would be a classification problem) |
| Email Spam Detection | Classify emails as spam or non-spam based on their content and characteristics. | **Classification** | As we have to classify between two groups where the mails are spam or non-spam |
| Customer Segmentation  | Group customers into segments based on their purchasing behavior and demographics | **Unsupervised** | We have to cluster or group customers by ourself based on data. Additionally, we're not provided with any labeled class. If we have provided with groups or classes then it would be a classification problem |
| Predicting Student Scores   | Given features like study hours, attendance, and previous grades, predict the final grade of a student. | **Classification** | Grade is a group or class that pre-defined. However if we said to predict score then it would be regression a problem  |
| Image Recognition | Identify whether an image contains a cat or a dog | **Classification** | We have to put images into correct class |
| Market Basket Analysis | Analyze customer purchase data to identify frequently co-purchased items | **Unsupervised**     | Group customers based on previous purchases that senses interest. Now based on interest we can categorize them into various groups where customers with similar interest will fall into a specific group | 
| Predicting Stock Prices  | Given historical stock data, predict the future price of a stock  | **Regression** | We have to predict price which is a numerical value |
| Credit Card Fraud Detection | Detect fraudulent transactions based on transaction history and patterns | **Classification** |  Fraud or not, so classification |
| Document Clustering | Group similar documents together based on their content | **Unsupervised**   | We have to determine traits of the documents by ourself and then group them |
| Predicting Customer Churn   | Determine whether a customer is likely to churn (cancel their subscription) based on their usage patterns  | **Classification** | Churn or not, so classification |

