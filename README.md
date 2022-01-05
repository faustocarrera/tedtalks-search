# TED talks search engine

It's a basic text search experiment

## The basics

I'm researching about how to create a basic search engine for work and fun, I'm gonna be using the readme as a way to share links, ideas and concepts.

## Concepts

When someone search for something, they expect accuracy, so, there's some basic metrics we could use to measure the accuracy of the results against a search query.

__Forward Index__: This is a data structure holding a list of documents with their associated words, in order.

```
{
    "document_001": ["lorem", "ipsum", "dolor", "sit", "ammet"],
    "document_002": ["lorem", "ipsum", "dolor"],
}
```

__Inverted Index__: This is a data structure holding a list of words with documents with that word. 

```
{
    "lorem": ["document_001", "document_002"],
    "ipsum": ["document_001", "document_002"],
    "dolor": ["document_001", "document_002"],
    "sit": ["document_001"],
    "ammet": ["document_001"]
}
```

__Term Frequency (TF)__: This is a metric stored for each unique word in each document. It is commonly calculated as the number of occurrences of that word divided by the number of words in a document, resulting in a value between 0 and 1. Some words may get weighted more heavily (e.g. special tags) and the TF may be normalized, preventing extreme values.

__Inverse Document Frequency (IDF)__: This is a metric stored for each unique word. It is commonly calculated as the number of documents with that word divided by the total number of documents. Given that it requires the number of documents, it is usually calculated after crawling or at query time. It may be normalized to prevent extreme values.

## The solution

We gonna weight terms in documents by calculating the product between their frequency and inverse document frequency `weight = tf * df`.

- remove stop words
- remove common words
- apply two common techniques of natural language processing: stemming and lemmatization, that is removing prefixes, suffixes and inflections
- normalize and calculate the term frequency
- calculate the inverse document frequecy


## Links

- [https://medium.com/@deangela.neves/how-to-build-a-search-engine-from-scratch-in-python-part-1-96eb240f9ecb](https://medium.com/@deangela.neves/how-to-build-a-search-engine-from-scratch-in-python-part-1-96eb240f9ecb)
- [https://blog.devgenius.io/building-your-own-search-engine-from-scratch-e542a1068c44](https://blog.devgenius.io/building-your-own-search-engine-from-scratch-e542a1068c44)
