# Social CRM
This repository contains code for mining, preprocessing and modeling Facebook data for customer segmentation, profiling and personalization purposes.

## Setup

We recommend running the code in a virtual environment with Python > 3.5.x (fully tested on Python 3.6.5):
```
virtualenv -p python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Run `jupyter notebook`

## Files
* data_processing_age_gender_network_graph.ipynb
  * Extract age,number of likes and number of posts information from Facebook raw dataset
  * Construct a network graph to visualize users' relationships 
* gender_imputation.ipynb
  * Build a decision tree model using first 1/2/3 letters and last 1/2/3 letters of users' first name to predict gender
* fb_raw_data_analysis.ipynb
  * clean and preprocess each features in the raw data to extract necessary information of users 
