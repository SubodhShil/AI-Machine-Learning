## What is **Deep Learning**

> Deep learning is a subfield of artificial intelligence and machine learning that inspired by human intelligence and tries to replicate the working process of human brain cells namely **neurons**.
> Classical machine learning works good for less data, whereas deep learning works good with huge amounts of data.

### Classical machine learning uses statistical method whereas, deep learning tires to replicate human intelligence, in the level of neurons.

1. Deep learning refers to training neural network
2. Large or dense neural network works in a way that it combines multiple single neurons.

![](20240607113608.png)

> **`Number of total layers in a neural network = Count of hidden layers + output layer`**

## Supervised learning with neural networks

-   Real estate and online advertisement: ANN
-   Image: CNN (Convolutional Neural Network)
-   Speech, translation or text: RNN (Recurrent Neural Network)
-   Autonomous driving: Hybrid neural network

### To work with data

Two kinds of training data is encountered

1. Structured data: weight, height, age, zip code, income
2. Unstructured data: Image (pixels), audio

> To get better performance out of a neural network, it requires a large amount of labeled dataset. Now being data is generated through various sources in a large amount (often said Big Data) utilizing digital technologies (smart phones), social media, it is quite easier to train the neural network.

### Process

1. We provide data in the input layer.
2. Hidden layers are responsible for feature extraction automatically, this is called **Representation learning**.

-   Sigmoid is slow

-   Logistic regression is like a single neural network.
-   Each neuron of a neural network works on a specified sub-task.
-   If any mistake happens
    -   Error will be reported or propagated to individual neurons thus they can learn about the accurate result. This process is known as **'Backward Error Propagation'**.
-   This is how deep learning work using utilizing trial and error process.

## Perceptron

1. **Weights**: How much the neuron should get activated.
2. **Bias**: It is provided thus the resulting value does not get to 0.
3. **Sigmoid activation function**: This generate a value between 0 and 1. Whether the neuron is activated or not.

## Deep learning decision and black box

একটা deep learning model কিভাবে একটি decision নিচ্ছে সেটা জানা যায় না, এই ব্যাপারটাকে black box বলে । To mitigate this problem, we have another field namely **Explainable AI**.

