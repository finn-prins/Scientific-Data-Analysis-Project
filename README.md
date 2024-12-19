# Group 11

## Bitcoin & Twitter (x)

### Group Members:  Andrey Bartashevich (14586517), Finn Prins (13458434), Duco Trompert (14591227)

### Research Question:

**Is there a correlation between Twitter (X) posts and Bitcoin price fluctuations or trading volume?**

### Hypothesis:
**Null hypothesis:** There is no correlation between Twitter (X) posts and changes in Bitcoin prices or trading volume.

**Alternative Hypothesis:** Twitter (X) posts are correlated with changes in Bitcoin prices and trading volume.

## Methods

### Data ###
**Twiter dataset: https://www.kaggle.com/datasets/alaix14/bitcoin-tweets-20160101-to-20190329**

**Bitcoin dataset: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data**

**Sentiment analysis dataset: https://drive.google.com/file/d/1rlvUkfD442PeGgEPLrBGxbKD6logsuMg/view?usp=sharing**

To setup the data so that everything works, you need to download the data from the links above and place them in folder called `data` in the root of the project.
The twitter dataset from kaggle is not necessary because this is the data we used for the sentiment analysis, which we have in the file from our google drive.

So the root folder should look like this:

data/

    bitcoin-historical-data.csv

    twitter_sentiment.csv

presentation.pdf

README.md

sentiment_analyser.py

team_11.ipynb

**Code**

We used sentiment_analyser.py to analyse the sentiment of the tweets.
You may run this file yourself but it took us 27 hours to run it.

The main data analysis can be found in the notebook: team_11.ipynb

**Packages**
pip install vaderSentiment
pip install pandas
pip install statsmodels
pip install seaborn
pip install scikit-learn
pip install langdetect
pip install wordcloud
pip install nltk



