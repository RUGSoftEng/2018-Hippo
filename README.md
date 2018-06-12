# Hippo

## Abstract

Hippo is a platform for entrepreneurs with the goal of finding market-validated business ideas. Hippo crawls Twitter for ideas, categorises them using natural language processing, and presents these ideas and their metadata to the users.

## Introduction

The project has 3 main parts: data analysis, frontend, and backend. Data analysis and backend are Python based, whereas frontend is Vue based.

Data analysis contains a Twitter streamer, as well as the NLP keyword extraction code, which uses nltk. Once ideas are received using the Twitter streaming API, they are analysed using NLP and sent to Elasticsearch. NLP analysis is used to determine tweets indicating desire for a product or service, in other words a business idea.

Front end provides a graphical interface for the web site and allows users to interact with the data, from requesting data sets to signing up for accounts. Front end communicates with back end using a RESTful API.

Back end communicates with front end in order to fetch tweets/ideas from Elasticsearch, dynamically create categories, as well as manage user accounts and demographics. Communication is done using REST/JSON.

## Project structure

The project it's code is structured as described below. These directory contain an README.md file as well with instructions how to use the components.

### Frontend application
`~/Sources/App`

### Data analysis and NLP
`~/Sources/DataAnalysis`

### Web API
`~/Sources/WebApi`

## Licensing 

This project is licensed under an proprietary licence, usage, distribution or modification of the project is not allowed, unless explicit permission by the licensor is given.

This project is currently only licensed to Juicy Story: http://www.binpress.com/license/view/l/cf13bae2d3eea7ff7f10d6073848c0a7

