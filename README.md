# Toxic-Comment-Classification
Individual Submission for Toxic Comment Classification Competition (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## Iteration 1

To start off the project, I wanted to create a working application that produced a correctly formatted csv file for submission. I did not care for accuracy at this point, just an application that took in training and test data and produced an output. I would improve the accruacy in following iterations.

The baseline application consisted of two Python Scripts, a data cleaner and a data classifier. The data cleaner took the training data as input and created dictionaries of words for the following categories of comments: toxic, severe toxic, insult, obscene, threat and identity hate. No further data cleaning was implemented in this iteration.

The data classifier took the dictionaries produced by the cleaner and test comment data and classified each of the comments with a percentage that represented the liklihood of it being each of the categories defined above. The percentages were based on the percent of words that appeared in the comment and each dictionary. The percents were then normalized to 100% and used as the classifier. As expected, this classifier did not give me an accurate result, but it did produce a correctly formatted output.


## Iteration 2

This iteration was focused on cleaning up the training data for a more accurate model. I first ignored stop words, i.e 'the', 'is', or 'are', found in the comments to not put weight on commonly used words. I also used a tokenizer to simplify words to their stems to not put extra weight on the same word but in a different tense or connotation. 
