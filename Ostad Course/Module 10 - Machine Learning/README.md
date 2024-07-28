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

# Feature Scaling, PCA

## Supervised Learning

Two types

-   **Classification**: যদি target column এর result গুলো কয়েকটি নির্দিষ্ট value এর মধ্যে সীমাবদ্ধ থাকে (যেমন, Yes, No, Good, Bad, Pass, Fail, etc.), তাহলে সেগুলোকে class হিসেবে চিন্তা করা যায় । এগুলোকেই classification problem বলে ।
-   **Regression**: যখন target column এর result গুলো কোন নির্দিষ্ট value এর মধ্যে সীমাবদ্ধ থাকে না, সেগুলোকে regression problem বলে ।

### Target: 

### Feature: 
