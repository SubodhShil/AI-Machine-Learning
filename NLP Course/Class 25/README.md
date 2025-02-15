> # **`Llama Index`**

> Most of the transformers models or LLMs are generalized. To create an application that is entirely based on or specific to custom workflow or task, it need much context of the data which might not fulfilled in the original training. Such as we want to create a **SpaceGPT**. Beyond this, private LLMs needs to be trained with custom dataset.

If we distribute the knowledge base into two parts, they might categories into:

1. Original knowledge base
2. Custom knowledge or secondary knowledge base

It includes two stages:

1. **Indexing stage**: To create the knowledge base or make the LLM accustomed with your data.
2. **Querying stage**: Create the context based on the custom data. It result the appropriate knowledge base based on the prompt which is most related to the available knowledge base.


