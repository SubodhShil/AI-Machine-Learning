-   K Fold Cross Validation
    -   Validation data: Randomly chosen.
-   Over fitting
    -   Training with big portion of a dataset
-   Under fitting
    -   Data is inaccurate
    -   Fix
        -   Providing sufficient training data

## Confusion Matrix

-   Accuracy is not the sole criteria or parameter to evaluate how good an algorithm is. There are several other factor such as precision, recall etc involve in evaluating an algorithm.
-   Precision formula: `TP/(TP + FP)`
-   Recall formula: `TP/(TP + FN)`
-   F1 Score: `2 * (Precision * Recall) / (Precision + Recall)`
-   In real world scenario, suppose you have a dataset where two different algorithms are collied with a similar accuracy. In this case, precision or other parameters may be used for better pick an algorithm.

&nbsp;

# Feature Scaling

Feature scaling is also known as feature transformation. কতগুলো random value কে একটা নির্দিষ্ট range (often in smaller numeric range) এর মধ্যে নিয়ে আসাটাই হচ্ছে feature scaling.

-   Scaling is mandatory for KNN, K Means algorithm

### Rules of scaling

-   Only features should be scaled, target value shouldn't be scaled
-   Only numeric, quantitative features should be scaled
-   **Normalization or Min-Max Scaler**: After scaling the features should range between 0 and 1.

![](20240729195418.png)

# PCA (Principal Component Analysis)

Problem with features:

1. A bigger feature size could be an overhead. So, reducing less important features or compressing is good for model training.
2. Less features can contribute to significantly faster model training and performance.

Before we get know about PCA, we need to have idea on feature selection.

-   Feature selection is filtering out the most important features or columns and get rid of less important feature columns.

---

-   PCA is not feature selection.
-   PCA is a feature reduction technique, also known as **'dimensionality reduction technique'**.
-   Feature or column or dimensions are determined and reduced to a suitable size that easily be trained.
-   Using the PCA technique, N feature columns would be converted into suitable or target column sizes. Unlike feature selection the values would not be wipe out entirely from the dataset rather it would be compress into those target column size.
-   Feature scaling is mandatory before PCA.
-   Accuracy might drop if PCA take place.

&nbsp;

# Feature extraction

-   One example of feature extraction could be retrieving numerical value from image data.

# EDA

# Null value handling

## Supervised Learning

### Two types

-   **Classification**: যদি target column এর result গুলো কয়েকটি নির্দিষ্ট value এর মধ্যে সীমাবদ্ধ থাকে (যেমন, Yes, No, Good, Bad, Pass, Fail, etc.), তাহলে সেগুলোকে class হিসেবে চিন্তা করা যায় । এগুলোকেই classification problem বলে ।
-   **Regression**: যখন target column এর result গুলো কোন নির্দিষ্ট value এর মধ্যে সীমাবদ্ধ থাকে না, সেগুলোকে regression problem বলে ।

## Clustering

Grouping করা । কোন target দেওয়া থাকবে না, ML model নিজে থেকেই grouping করে নিবে ।

### Feature

### Target
