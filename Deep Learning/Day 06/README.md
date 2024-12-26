> Multi-class classification এর সময় total output node ততগুলো হবে যতগুলো output class থাকবে । এর মধ্যে যার output class node এর probability বেশি হবে সেটাকেই output হিসেবে ধরে নিবো ।
> Output node ১ এর বেশি হলে activation function **'softmax'** নিতে হবে ।
> Use Min-Max scaling when upperbound and lowerbound is visible.
> Output node যদি 1 হয় এবং সেটা যদি একটা regression problem হয়ে থাকে তাহলে activation function **'linear'** দিতে হবে ।
