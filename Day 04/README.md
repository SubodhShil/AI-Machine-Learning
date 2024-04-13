# **```Data Standardization```**

The process of standardizing the data to a common format and common range.

# **```Median, Mean and Mode```**

## **```Mean or average```**
- What is the problem with average values? 
  - Average values are manipulative, since any outlier can lead to inappropriate average values.
  - Outlier are those values that are different from rest of the values or data points. 

## **```Median```**
- While working with dataset, whenever you're getting N/A, missing or null values don't just fill the missing portion with average values. Instead use median values. Here how you can do this in python:

```python 
df = df.fillna(df.column.median())
```

### **```Percentile```**
Usecases:
1. Outlier removal 
2. General data analysis

## **```Mode```**
Mode means most frequently occurring value in a dataset.

## **```Bias, Variance```**

## **```Bias```**

Calculated on observing train error.

1. **Low bias:** Low train error.
2. **High bias:** High train error.

### Underfit
> When a ML model is not performing well in training dataset, and the performance on the test dataset is also poor then the model is said to be underfit and hight biased model. In this case, the difference between training dataset and test dataset also very low. 

**Underfit models tend to be high bias.**

## **```Variance```**

Calculated by observing test error.

1. **Low variance**: Low test error.
2. **High variance**: High test error. 

### Overfit
Suppose our overfit ML model perform like this:
- Train dataset error: 3 (approx.)  
- Test dataset error: 92 (approx.)
> When ML models are performing well in training dataset but when it comes to new or testing datasets (also known as development set data) wrong prediction looms out and thus the model fails to live up the previous standard.

This case is high variance, where the difference between train and test dataset error is large. **Overfit models tend to be high variance.**


### Balance fit 

If a model predict result that has low bias and low variance, then it is likely a balance fit model.


## **```Standard Devation```**

- If the individual value is very close to the average value then, it is **Lower in Standard Deviation**.
- If the individual value is very far from the average value then, it is **Higher in Standard Deviation**.


