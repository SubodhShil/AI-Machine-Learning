-   **Corpus**: A paragraph is called a corpus.
-   **Documents**: Sentences are also called as documents.
-   **Vocabulary**: Total number of unique words in a paragraph.
-   **Words**:

## Tokenization

-   A way to split tokens out of a corpus or paragraph or document or sentence.
-   The tokens are a set of documents or sentences.
    -   In further usecase, the tokenization can conduct to convert a sentence into a word.

## Lemmatization

Some set of fixed rules that are used for retrieving base word.

```md
    talking => talk
    eating  => eat
    looking => look
```

### Issues with stemming

Sometime grammatical rules are not up to mark to evaluate correct lemma.

```md
    history => histori
    ate     => ate
    ability => abil
```

-   To fix the lemmatization problem we will be using stemming process avoid such mistakes.

## Stemming

Stemming is a set of linguistic and grammatical rules to retrieve a base word (<ins>also known as **lemma**</ins>) from the current given word.
