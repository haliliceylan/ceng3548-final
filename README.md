# CENG 3548 Final Project

## Team & Roles
#### Özgür Doğan / 170709026 / 
- Data Preprocessing
- Modeling
#### Halil İbrahim Ceylan / 390709073
- Crawling
- Data Preprocessing (Future Extraction)

## Project’s Topic
Predicting Website Blog or Not

## Project’s Goal
Try to detect the website is the blog or not from url

## Project Directory Structure
- `crawling/` -> all source codes related to web crawling part and future extraction.
- `predictive model` -> all source codes related to data preprocessing and modeling.

## Project’s Description
We are going to create some web spiders for collecting data from the internet. These spiders will collect blog and non-blog website urls then we will extract some features from these website urls. Using these features, we will try to detect if it is a website blog or non-blog from url. 

## Project's Abstract
Websites contain very wide information in their structure. In this project, We used the python Scrapy Framework for collection website urls using 3 different web spiders. Also we use the item pipelines feature in Scrapy Framework. With Item Pipelines, we analyze and extract a lot of features from scraped data. We used this data to train our models. In the modelling part, we followed two different paths because we have unbalanced data. In the first path we reduced the number of blogs and matched the number of non-blogs and we created an xgboost model. In the second path  we applied undersampling to the data and we trained 3 different models with the data that we split into 3 parts and we created an ensemble model. In the ensemble model, we applied a voting technique that uses the most voted prediction.
