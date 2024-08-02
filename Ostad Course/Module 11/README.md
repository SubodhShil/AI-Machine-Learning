# Outlier

An outlier in a dataset is a significantly different value than all other values in a dataset.

## Outlier or anomaly detection

Three ways to remove outlier:

1. IQR
2. Z score
3. Standard deviation

&nbsp;

# Encoding

> Classical machine learning algorithms can't digest string data. Encoding is a technique that provide the solution of converting non-numerical categorical data into a machine learning processable representation thus algorithm can run prediction on the data.

## Ordinal encoding

-   Works for feature data.
-   Explicitly assigns order wise numerical value to the categories. For example, "Good", "Better", "Best" are three categorical feature data of a student result dataset. Now, ordinal encoding make sure assign order wise value such this way:
    -   **Good**: 0
    -   **Better**: 1
    -   **Best**: 2

## Label encoding

-   Works for target data.
-   Should be use when order wise value is not required.

## One hot encoding

-   Works for nominal feature data.
-   Each category of a feature has to convert into a single column feature.

## **`ColumnTransformer`** sklearn class

Column transformer is useful when have two different kinds of categorical data and have to do the encoding task with ease.

