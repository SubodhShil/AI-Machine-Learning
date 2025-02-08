> # **`Transformers`**

-   It can capture dependencies between words in a sentence (even in a very long text).
-   It first convert the input text into a sequence of vectors.
-   Encoding is done using self attention mechanism or attention layer which is to establish relationship between words and sentence.
-   The model decodes the sequence vectors into output tokens.
-   Transformers generate vector as output, the it convert it to into tokens thus human can understand.
-   The self attention layer generates new sequence of vector based on input sequence.
-   Encoding only models doesn't contain the decoder of the transformer. It is good for faster processing and lightweight task like text classification.
-   Decoder only models are suitable for machine translation tasks. Decoders are generative since it generates new text. <ins>**ChatGPT is a decoder only problem**.</ins>

### Usecases

1. Machine translations: English to Bangla.

### A transformers consist of several layers such as:

1. **Embedding layer**: Converts the input text into sequence of vectors.
2. **Self-attention layer**: Allows to learn long-range dependencies.
3. **Positional layer**: Establish relationship between words by measuring which words are close to each other.
4. **Decoder**: Takes vector output from the self attention layer and converts it to textual tokens.

## Training techniques of a transformer

1. **Masked Language Modeling**: Input text would have missing words, transformers model will learn by predict those words. Simply, it learns by fill in the blanks.
2. **Attention Masking**: Rather than predicting based on the future words, the technique enforces itself attain prediction within current context (most relevant words that come before the current word).
3. **Gradient Clipping**: During training of a transformers model the gradient might increase drastically which causes the model's parameter to change frequently. This may lead to an unstable and overfitted model. So, gradient clipping comes across with a threshold for the maximum allowed gradient value.

## BERT

It is a bidirectional (both left to right and vice versa) transformer model. Focus both future and past context of a text resource.

-   Transfer learning: Solving task using pretrained models.
-   NSP: Next Sentence Prediction

## BERT vs GPT

1. BERT is better for classification task and generative task.
