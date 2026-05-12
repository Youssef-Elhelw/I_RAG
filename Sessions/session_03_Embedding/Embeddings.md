# Embeddings

## Table of Contents
### 1. [What are Vectors?](#1-what-are-vectors)
### 2. [What is an Embedding?](#2-what-is-an-embedding)
### 3. [Why Do We Need Embeddings?](#3-why-do-we-need-embeddings)
### 4. [One-Hot Encoding Problem](#4-one-hot-encoding-problem)
### 5. [Dense Vector Representation](#5-dense-vector-representation)
### 6. [Semantic Meaning in Embeddings](#6-semantic-meaning-in-embeddings)
### 7. [Word Embeddings](#7-word-embeddings)
### 8. [Sentence Embeddings](#8-sentence-embeddings)
### 9. [How do LLMs use embeddings?](#9-how-do-llms-use-embeddings)
### 10. [Embedding Dimensions](#10-embedding-dimensions)
### 11. [How Embeddings Are Learned](#11-how-embeddings-are-learned)
### 12. [Popular Embedding Models](#12-popular-embedding-models)
### 13. [Important Terms](#13-important-terms)

---

## 1. ***What are Vectors?***
- A vector is a one dimensional array of numbers containing multiple scalars of the same type of data.
- Vectors represents properties, features in a more machine understandable way.

Here is an example of a vector:

```
[0.5, 0.2, 0.8, 0.1]
```
---

## 2. ***What is an Embedding?***
- An embedding is a dense vector representation of data.
- It Converts:
    1. Text
    2. Images
    3. Audio
    4. Users
    5. Products
    6. Other types of data 
    - into vectors of numbers that AI models can understand.
- It captures the semantic meaning and relationships between data points in a way that can be easily processed by machine learning models.

Vectore embeddings are typically generated using techniques like Word2Vec, GloVe, or transformer-based models like BERT. They allow us to represent complex data in a way that preserves semantic relationships and can be used for various tasks such as classification, clustering, and similarity search.

<div align="center">
<img src="Screenshots/Vector Embedding.png" alt="Vector Embedding" width="600">
</div>

---

## 3. ***Why Do We Need Embeddings?***
- To convert complex data into a format that machine learning models can understand and process.
- To capture semantic meaning and relationships between data points.

---

## 4. ***One-Hot Encoding Problem***

### 4.1 First, What is One-Hot Encoding?
- One-hot encoding is a method of representing categorical data as binary vectors.
- Each category is represented as a vector where only one element is 1 and the rest are 0s.
- for example, if we have three categories: "cat", "dog", and "mouse", they can be represented as:
```
cat:   [1, 0, 0]
dog:   [0, 1, 0]
mouse: [0, 0, 1]
```
### 4.2 Problems with One-Hot Encoding:
1. **High Dimensionality**: As the number of categories increases, the dimensionality of the vectors also increases, leading to sparse representations.
    - imagine we have 10,000 unique words in a vocabulary, one-hot encoding would require 10,000 dimensions for each word, resulting in very sparse vectors.
2. **Lack of Semantic Meaning**: One-hot encoding does not capture any semantic relationships between categories. For example, "cat" and "dog" are more similar to each other than to "mouse", but one-hot encoding treats them as completely unrelated.
3. **Inefficient for Machine Learning Models**: Many machine learning models struggle with high dimensional and sparse data, which can lead to poor performance and increased computational cost.
   
---

## 5. ***Dense Vector Representation***
- Dense vector representation, or embeddings, addresses the problems of one-hot encoding by representing data in a lower-dimensional space where similar data points are closer together.
- For example, instead of representing "cat", "dog", and "mouse" as one-hot vectors, 
  we can represent them as dense vectors that capture their semantic relationships:
```
cat:   [0.8, 0.1, 0.1]
dog:   [0.7, 0.2, 0.1]
mouse: [0.1, 0.1, 0.8]
```
Notice: In this example, "cat" and "dog" have similar vector representations, indicating that they are more similar to each other than to "mouse". This allows machine learning models to better understand the relationships between data points and improve performance on tasks such as classification, clustering, and similarity search.
<p style="text-align: center;">────────────</p>

You can check how similar two vectors are by calculating the `cosine similarity` between them. The closer the cosine similarity value is to 1, the more similar the vectors are. In this example, "cat" and "dog" would have a higher cosine similarity compared to "cat" and "mouse".

<div align="center">
<img src="Screenshots/Cosine Similarity.png" alt="Cosine Similarity" width="700">
</div>
where x,y are the two vectors, and ||x|| and ||y|| are the magnitudes of the vectors. The cosine similarity ranges from -1 to 1, where 1 means the vectors are identical, 0 means they are orthogonal (completely different), and -1 means they are opposite.

<div align="left">
To illustrate the three graphs above:
</div>

- The graph on the left: (Similar Vectors): angle close to 0 degrees, cosine similarity close to 1.
  - "cat" and "dog" would be in this category.
  
- The graph on the middle:(Orthogonal Vectors): angle close to 90 degrees, cosine similarity close to 0.
  - "cat" and "pencil" would be in this category.
  - they are completely different and have no semantic relationship.

- The graph on the right: (Opposite Vectors): angle close to 180 degrees, cosine similarity close to -1.
  - "good" and "bad" would be in this category.
  - "Hot" and "Cold" would be in this category.
  - they are opposite in meaning and have a strong negative relationship.

---


## 6. ***Semantic Meaning in Embeddings***
- Embeddings capture the semantic meaning of data by placing similar data points closer together in the vector space.
- For example, in word embeddings, words that are semantically similar (like "king" and "queen") will have similar vector representations, while words that are different (like "king" and "car") will have more distant vector representations.
- This allows machine learning models to understand the relationships between data points and make better predictions based on those relationships.
  

---

## 7. ***Word Embeddings***
- Word embeddings are a type of embedding that represents words as dense vectors in a continuous vector space.

You can visualize this by plotting the embeddings in a 2D or 3D space, where similar data points will cluster together, and dissimilar data points will be farther apart.

look at this notebook for better understanding:
🟢 Open the notebook: [Word Embeddings Visualization](./embeddings.ipynb)

<p style="text-align:center;">────────────</p>


<div align="center">
<img src="Screenshots/Word Embeddings.png" alt="Word Embeddings" width="700">
</div>

- Some intersting things about word embeddings:
    - They can capture relationships between words, such as analogies (e.g., "king" - "man" + "woman" ≈ "queen").
    - or even more complex relationships (e.g., "Paris" - "France" + "Italy" ≈ "Rome").
<div align="center">
<img src="Screenshots\intersting_thing about word embedding.png" alt="Word Embeddings Analogy" width="700">
</div>

---

## 8. ***Sentence Embeddings***
- Sentence embeddings are a type of embedding that represents entire sentences or paragraphs as dense vectors in a continuous vector space.
- They capture the semantic meaning of the entire sentence, allowing for tasks such as sentence similarity, sentiment analysis, and text classification.
- Sentence embeddings can be generated using models like BERT, RoBERTa, or Universal Sentence Encoder, which are designed to capture the context and meaning of sentences.

```
""I love machine learning!" -> [0.8, 0.1, 0.3, ...]
"Machine learning is great!" -> [0.7, 0.2, 0.4, ...]
"the dog is barking" -> [0.1, 0.9, 0.2, ...]
```

try this simple code: [Sentence Embeddings](embedding_simple_example.py)

---

## 9. ***How do LLMs use embeddings?***
- [LLMs](../session_02_LLM_API/LLM_Specific_Concepts.md) use **Token Embeddings** to convert input text into a format that the model can understand and process.
- Each token (word or subword) in the input text is mapped to a dense vector representation, which captures the semantic meaning of the token.
- These token embeddings are then processed through the layers of the LLM to generate a response based on the input.
- LLMs also use **Positional Embeddings** to capture the order of tokens in the input text, which is crucial for understanding the context and meaning of the text.

---

## 10. ***Embedding Dimensions***
- The number of dimensions in an embedding vector is a hyperparameter that can be chosen based on the specific task and dataset.
- For example, a vector with 3 numbers is a 3-dimensional embedding, while a vector with 300 numbers is a 300-dimensional embedding.
- BUT word embedding tend to have MUCH higher dimensions.
  - for example, GPT-3 uses 12,288 dimensions for its token embeddings.!!!
- Higher-dimensional embeddings can capture more complex relationships between data points, but they also require more computational resources and can lead to overfitting if the dataset is small.

---

## 11. ***How Embeddings Are Learned***
- Embeddings are typically learned through a process called **backpropagation**, where a model is trained on a large dataset to learn the optimal vector representations for the data.
- For example, in word embeddings, a model might be trained on a large corpus of text to learn the relationships between words based on their co-occurrence in the text.
- The model adjusts the embedding vectors during training to minimize a loss function, which measures how well the model is performing on a specific task (like predicting the next word in a sentence).
- Once the model is trained, the learned embeddings can be used for various downstream tasks, such as text classification, sentiment analysis, or similarity search.
  
1. At first, the model starts with random embeddings for each token.
2. As the model processes the training data, it adjusts the embeddings based on the context in which the tokens appear.
3. loss function is used to measure how well the model is performing on a specific task (like predicting the next word in a sentence).
4. The model updates the embeddings to minimize the loss, which allows it to learn meaningful representations of the tokens based on their relationships in the training data. this is called backpropagation.

<div align="center">
<img src="Screenshots/Embedding Training1.png" alt="Embedding Training 2" width="700">
</div>

<p style="text-align:center;">────────────</p>

Claude Version:
<div align="center">
<img src="Screenshots/Embedding Training.png" alt="Embedding Training" width="700">
</div>

---

## 12. ***Popular Embedding Models***

### 12.1 Where are embeddings used?
- Applications:

  - semantic search
  - recommendation systems
  - chatbots
  - RAG
  - clustering
  - anomaly detection
  - document retrieval
  - image search
  
<p style="text-align:center;">────────────</p>

- Real world examples:

  - Google Search uses embeddings to understand the meaning of queries and match them with relevant documents.
  - Netflix uses embeddings in their recommendation system to suggest movies and TV shows based on user preferences.
  - OpenAI's GPT models use token embeddings to process and generate text.
  - Facebook's FastText is a popular model for generating word embeddings.
  - BERT and RoBERTa are widely used models for generating contextualized word and sentence embeddings.
  
---

### 13. ***Important Terms***

| Term | Meaning |
| :--- | :--- |
| Embedding | Dense vector representation |
| Vector Space | Mathematical space of vectors |
| Semantic Similarity | Similarity in meaning |
| Token | Small text unit |
| Embedding Dimension | Size of vector |
| Vector Database | Stores embeddings |
| Similarity Search | Finding close vectors |



<p align="center">
  <strong style="font-size:32px; letter-spacing:6px;">
    — THE END —
  </strong>
</p>