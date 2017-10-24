# SABLE

This readme is a work in progress.

## Introduction

SABLE, which stands for Scraping Assisted by Learning, is a collection of tools for web crawling, web scraping, and classifying text with the help of machine learning.  The idea is to discover potential new sources of data on the web in PDF format, apply a classification model to predict whether the PDF contains useful data, and then scrape the data.  SABLE was initially developed to scrape data on tax revenue collections from state and local government websites but has been applied to other settings such as finding population and housing statistics on the websites of foreign national statical agencies.

## Software

SABLE is based on two main pieces of open-source software: Apache Nutch and Python.  Nutch is used to crawl websites, discover PDFs, and compile a training set of documents for model building.  Python is used to extract text from PDFs and to fit classification models for predicting whether a PDF contains useful data.  For PDFs containing useful data, templates in the form of Python programs can be developed to scrape the data.  SABLE uses the following Python modules: scikit-learn, Natural Language Toolkit (NLTK), PDFMiner (Python 2.X version), and PDFMiner3K (a Python 3.X port of PDFMiner).

## Description of Contents

This repository contains Python programs for converting PDFs to TXT format and fitting classification models for predicting whether the PDF contains useful data based on the extracted text.  Lists of NLTK stop words for multiple languages are provided.  Foreign accent marks have been removed from characters, and some lists have been modified slightly.

## Organization of Files

The following organization of programs, data, and other files on a Linux/Unix system is assumed.  PDFs that are to be converted to TXT format and used as input into building classification models should be manually classified as "positive" (contains useful data) or "negative" and placed accordingly in the /data/pos_pdf/ and /data/neg_pdf/ folders.  The extracted text, which is also known as textual metadata, is output to the /data/pos_meta/ and /data/neg_meta/ folders.  Additional information can be found in the comments in the Python programs. <br />

/data/neg_meta/ <br />
/data/neg_pdf/ <br />
/data/neg_prob/ <br />
/data/neg_xml/ <br />
/data/pos_meta/ <br />
/data/pos_pdf/ <br />
/data/pos_prob/ <br />
/data/pos_xml/ <br /> <br />
/classify_convert.py <br />
/classify_model.py <br /> <br />
/stop_danish.txt <br />
/stop_dutch.txt <br />
/stop_english.txt <br />
/stop_finnish.txt <br />
/stop_french.txt <br />
/stop_german.txt <br />
/stop_hungarian.txt <br />
/stop_italian.txt <br />
/stop_norwegian.txt <br />
/stop_portuguese.txt <br />
/stop_spanish.txt <br />
/stop_swedish.txt
