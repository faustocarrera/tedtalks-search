#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A basic search engine from a csv
"""

import os.path
import click
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Search:
    "Search engine class"

    def __init__(self, dataframe_path):
        self.label = 'transcript'
        self.dataframe_path = os.path.realpath(dataframe_path)
        self.min_results = 50

    def run(self, query):
        "Make a query"
        dataframe = self.__load_dataframe(self.dataframe_path)
        search_weights, weights_matrix = self.__tf_idf(query, dataframe, self.label)
        result_ids = self.__similarity(search_weights, weights_matrix, self.min_results)
        results = self.__results(result_ids, dataframe)
        return results

    @staticmethod
    def __load_dataframe(dataframe_path):
        "Load data from CSV and return a dataframe"
        return pd.read_csv(dataframe_path)

    @staticmethod
    def __tf_idf(keys, dataframe, label):
        "Calculate term frequency and inverse document frequency"
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_weights_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])
        search_query_weights = tfidf_vectorizer.transform([keys])
        return search_query_weights, tfidf_weights_matrix

    @staticmethod
    def __similarity(search_weights, weights_matrix, min_results):
        "Check the similarity between results"
        simil = cosine_similarity(search_weights, weights_matrix)
        similarity_list = simil[0]
        results = []
        while min_results > 0:
            index = np.argmax(similarity_list)
            results.append(index)
            similarity_list[index] = 0
            min_results -= 1
        return results
    
    @staticmethod
    def __results(result_ids, dataframe):
        "Return results"
        results = []
        for result_id in result_ids:
            results.append((dataframe.loc[result_id, 'url'], dataframe.loc[result_id, 'transcript'][0:25]))
        return results


@click.command()
@click.option("-q", "--query", prompt="What are you looking for?", help="The query")
def cli(query):
    search = Search('./data/transcripts.csv')
    results = search.run(query)
    for result in results:
        print(result)


if __name__ == "__main__":
    cli()
