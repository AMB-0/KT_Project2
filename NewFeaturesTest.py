
# -*- coding: utf-8 -*-
"""
Created on Mon Sept 25 11:36:27 2017

"""

"""

==============================================================================================================

                                    IMPORT LIBRARIES SECTION

==============================================================================================================

"""

import pandas as pd
import numpy as np
from textblob import TextBlob
from collections import OrderedDict
import re
import csv

"""
==============================================================================================================

                                    CONSTANTS SECTION

==============================================================================================================

"""
punctuation = "[\\\"#$%&'()*+,-./:;<=>@[\]^_`{|}~]"
num_attr = 94
path = 'C:\\Users\\Andres\\Google Drive\\Andres\\University Of Melbourne\\2017-02\\Knowledge Technologies (COMP90049)\\Project 2\\Assignment\\'
drug_list = list(pd.read_csv(path + 'drug_list.csv', sep = ',', header = None, skiprows=0).values[:,0])
se_list = list(pd.read_csv(path + 'side_effect.csv', sep = ',', header = None, skiprows=0).values[:,0])


"""
==============================================================================================================

                                    MAIN PROGRAM SECTION

==============================================================================================================

"""

#-------------------------------------------------------------------------------------------------------------
#								 STEP 1: READING THE RAW TEST SET
#-------------------------------------------------------------------------------------------------------------

# We read the test set raw data
raw_test_set = pd.read_csv(path + 'test\\test.txt', sep = '	', header = None, skiprows=0 , quoting=csv.QUOTE_NONE, error_bad_lines=False)



#-------------------------------------------------------------------------------------------------------------
#								 STEP 2: ADDING NEW FEATURES
#-------------------------------------------------------------------------------------------------------------

# We create temporary lists for storing new features
sentiment_polarity = []
length = []
punctuation_ind = []
drugs_side_effect_ind = []

# We iterate the tweet list
for tweets in raw_test_set.values[:,2]:


	#	STEP 2.1) 	Pre-processing of raw data
	tweets_ascii = re.sub(r'[^\x00-\x7f]',r'', tweets)														# Step 2.1.a : 		Cleaning of raw data (Remove all Non-Ascii characters)
	tweets_ascii = tweets_ascii.lower()																		# Step 2.1.b : 		Change the tweet to lowercase
	text = re.sub(punctuation,"", tweets_ascii)																# Step 2.1.c :		Remove punctuation


	#	STEP 2.2) 	Sentiment Polarity
	sentiment_polarity.append(TextBlob(text).sentiment.polarity)											# Step 2.2:			Calculates polarity of the tweets


	#	STEP 2.3) 	Text Structure Features: Length of Tweet, Punctuation Indicator, Drugs mention indicator, Side effect indicator
	d_ind = 0
	se_ind = 0

	length.append(len(tweets_ascii.split()))																# Step 2.3.a :  	Calculate the length of the tweet in words 
	punctuation_ind.append(int(bool(re.search(r'[!?]', tweets_ascii))))										# Step 2.3.b :  	Calculate if the tweet has any interrogation mark or exclamation mark present 
	for drug in drug_list:																					# Step 2.3.c :  	Calculate if the tweet mention any specific drug 
		if drug in tweets_ascii:
			d_ind = 1

	for effect in se_list:																					# Step 2.3.d :  	Calculate if the tweet mention any side effect 
		if effect in tweets_ascii:
			se_ind = 1

	drugs_side_effect_ind.append(d_ind and se_ind)

#-------------------------------------------------------------------------------------------------------------
#								 STEP 3: GENERATING THE OUTPUT FILE
#-------------------------------------------------------------------------------------------------------------

# We read the given test dataset and extract the header from it
header = pd.read_csv(path + 'test\\test.arff', sep = ' ', header = None, skiprows=1 )


# Then, we read the test set in the test.arff file, we add the header to it and save it in a pandas dataframe
test_set = pd.read_csv(path + 'test\\test.arff', sep = ',', header = None, skiprows=96, quoting=csv.QUOTE_NONE, error_bad_lines=False, names = list(header.values[:num_attr,1]))
del test_set["id"]

# We add the features to the new pandas dataframe
test_set["sentiment_polarity"] = np.array(sentiment_polarity)											# Adds polarity to pandas dataframe
test_set["tweet_length"] = np.array(length)																# Adds tweet length to pandas dataframe
test_set["punctuation_ind"] = np.array(punctuation_ind)													# Adds punctuation indicator to pandas dataframe
test_set["drugs_side_effect_ind"] = np.array(drugs_side_effect_ind)										# Adds drugs and side effect indicator to pandas dataframe


# Export the final dataframe to a CSV file
test_set.to_csv(path + 'test\\out.csv', sep=",", index=False)
