[![DOI](https://zenodo.org/badge/747828803.svg)](https://zenodo.org/doi/10.5281/zenodo.10565027)
# PLOSOne-Ecig

These following files include the code necessary to conudct the research in the "Public perceptions of synthetic cooling agents in electronic cigarettes on Twitter" study.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a `<Windows/Linux/Mac>` machine.
* You have installed the latest version of [Python](https://www.python.org/downloads/).

## Installation

To install this project, follow these steps:

### Python Environment Setup

This project uses `pyenv` to manage Python versions. To set up `pyenv` and the local environment, follow these instructions:

1. Install `pyenv` following the instructions on the [pyenv GitHub repository](https://github.com/pyenv/pyenv#installation).

2. Install Python 3.9.18 with `pyenv`:

   ```sh
   pyenv install 3.9.18
3. Create a virtualenv with Python 3.9.18:

    ```sh
    pyenv virtualenv 3.9.18 project
4. Activate said version:

   ```sh
   pyenv activate project
6. Install the necessary Python packages using pip:
    ```sh
    pip install -r requirements.txt
## Usage
The outline of each folder and code is as follows:

- ### preprocessing
    - ***e-cig_filter.py***: filters out non e-cig tweets
    - ***promo_filter.py***: filters out promotional tweets
    - ***flavor_filter.py***: filters out everything non-synthetic cooling agent related
    - ***pre_bertopic.py***: prepares .csv tweet data for bertopic analysis by removing unecessary columns
    - ***pre_sentiment.py***: prepares .json for sentiment by converting to .csv in acceptable format
- ### roBERTa_training
    - ***roBERTa_training_sentiment.py***: trains roBERTa model on manually labeled tweets for sentiment
    - ***roBERTa_training_sentiment.py***: trains roBERTa model on manually labeled tweets for user/non-users
- ### labeling
    - ***sentiment_roBERTa.py***: applies sentiment roBERTa model to classify tweets
    - ***user_roBERTa.py***: applies user/non-users roBERTa model to classify tweets
    - ***BERTopic.py***: applies BERTopic model to tweets
- ### figure_code
    - ***longitudinal_user_proportion.py***: generates figure showing the proportion of users over time.
    - ***sentiment_by_user_significance.py***: checks significance of sentiment across user/non-users
    - ***sentiment_by_user.py***:  generates figures showing sentiment counts by user/non-users
    - ***sentiment_user_counts.py***: provides total amounts of users/non-users and sentiment
    - ***sentiment_counts_sentiment_proportions***: provides number and proportion of each sentiment
    - ***sentiment_counter_biweekly***: Counts the number of each sentiment for each biweek
    - ***separate_by_sentiment.py***: separates into multiple files by sentiment
    - ***separate_by_user.py***: separates into multiple files by user/non-user
    - ***biweekly_unfiltered_tweets_counts.py***: counts total, unfiltered tweets for each biweek
    - ***biweekly_proportions_unfiltered_vs_filtered_tweets.py***: calculates proportions of unfiltered tweets vs filtered tweets and saves to Excel file

To conduct a similar study to what we've done, the following can be referenced as a general outline. The .json and .csv filenames should work as is. 

1. **e-cig_flavor.py**
2. **promo_filter.py**
3. **flavor_filter.py**
4. **pre_sentiment.py**
5. **roBERTa_training_sentiment.py** + **roBERTa_user_sentiment.py**
6. **sentiment_roBERTa.py** + **user_roBERTa.py**

   
1. **pre_bertopic.py**
2. **BERTopic.py**
   
X. figure-code scripts as necessary

To run each file, you can use the following format from the root directory:

    python3 folder_name/script_name.py
Replace folder_name/your_script.py with the actual path to the script you want to run.

## Misc

Each file will have accompanying code comments
