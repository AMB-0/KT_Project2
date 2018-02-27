=========================================================================================

					ASSIGNMENT 2 : Knowledge Technologies 		S02/2017

=========================================================================================

Program tested in python 2.7.13

-----------------------------------------------------------------------------------------
I. USAGE
-----------------------------------------------------------------------------------------

- Before running the program, the following set-up tasks should be made:

	1. Set PATH variable
	
	A PATH variable should be set in order to show the program where is the "train.arff" input file location.
	For this task, open the corresponding file "NewFeaturesTrain.py" or "NewFeaturesTest.py" and set the path
	variable with the path where the "train" and "test" folder are located. 
	
	Ex. path = 'C:\\Users\\XXXXXX\\Knowledge Technologies (COMP90049)\\Project 2\\'

Inside that path, a "train" and "test" folder should exists.


	2. Copy both files: drug_list.csv and side_effect.csv to the PATH. Both files should be located in the same
	path defined in the previous step.
	
	Ex. 'C:\\Users\\XXXXXX\\Knowledge Technologies (COMP90049)\\Project 2\\drug_list.csv'
	Ex. 'C:\\Users\\XXXXXX\\Knowledge Technologies (COMP90049)\\Project 2\\side_effect.csv'

- Once the path variable is set and both files exists, both programs are OK to run by using the command:

	Ex1. python NewFeaturesTrain.py
	Ex2. python NewFeaturesTest.py

	
-----------------------------------------------------------------------------------------
II. OUTPUT
-----------------------------------------------------------------------------------------  

- Each program will generate the corresponding output files: train.csv and test.csv. Both of them contains
the corresponding datasets with the following new features:

	a. Drug and Side Effect Indicator
	b. Sentiment Analysis
	c. Tweet Structure
		1. Length of tweet
		2. Punctuation_Ind