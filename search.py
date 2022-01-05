#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A basic search engine from a csv
"""

import os.path
import click
import pandas as pd


class Search():
    "Search engine class"

    def __init__(self, dataframe_path):
        self.dataframe_path = os.path.realpath(dataframe_path)

    def run(self, query):
        "Make a query"
        dataframe = self.__load_dataframe(self.dataframe_path)
        return self.dataframe_path

    def __load_dataframe(dataframe_path):
        "Load data from CSV and return a dataframe"
        return pd.read_csv(dataframe_path)


@click.command()
@click.option('-q', '--query', prompt='What are you looking for?', help='The query')
def cli(query):
    search = Search('./data/transcripts.csv')
    results = search.run(query)
    print(results)


if __name__ == '__main__':
    cli()
