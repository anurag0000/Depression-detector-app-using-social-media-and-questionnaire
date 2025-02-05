
<center><h2>Depression detector app using social media and questionnaire</h2></center>

<h4><a href="#introduction">Introduction</a> | <a href="#project">The Project</a> | <a href="#vd">Video Demo</a> | <a href="#reference">References</a> | <a href="#acknowledgement">Acknowledgement</a></h4>

<img src="https://news.berkeley.edu/wp-content/uploads/2019/10/depressionBW750px.jpg" />


<h2 id="introduction">Introduction </h2>

<p>Mental illness has been prevalent in the world, depression is one of the most common psychological problem i know and i would like to help as much as i can. Being a fan of Anthony Bourdain and Robin Williams, It has propel me to explore in this study. With the use of the Large amount of data tweets and Facebook post online i can use machine learning to data mine it and be able to produce a meaningful and useful outcome.</p><p>Social media generates countless data every day because of millions of active users share and communicate in entire
community, it changes human interaction. For this project, I will be using Python and various modules and libraries.</p>


<h2 id="project">The Project</h2>

<strong>Requirements:</strong>
<p>
	<ul>
		<li>Python 3.6.1 or Higher</li>
		<li>Twitter developer account</li>
		<li>Few modules (Keras, TF, Numpy, sklearns, pandas and itertools)</li>
	</ul>
</p>

<p>The aim of the project is to predict early signs of depression through <strong>Social Media</strong> text mining. Below are the steps to run the python codes using the data sets uploaded in the repositories or you can download your own.</p>

<img src="flowchart.jpg"/>
<p><strong>Follow steps below:</strong></p>

<ol>
	<li>Create a twitter developers account (<a href="https://developer.twitter.com/" target="_new"> Register Here</a>), From that account your would need 4 things.
	</li>
	<code>consumer_key = '', consumer_secret = '', access_token = '', access_secret = ''</code>
	<li>Using the file "Download_twitter_Api.py" insert the credentials and you can download current tweets using keywords such us depression, anxiety or sadness. When data sets are ready you may proceed on the preprocessing stage. 
	<br>
    <img src="https://i.ibb.co/M19tdrd/cc.png" />
	</li>
	<li>Run "preprocessor.py", This stage will go through your data sets and the given dictionary. The dictionary contain words with their corresponding polarity, which is essential to calcualting the sentiment of each tweet, each word will be seperated, tokenized and given its polarity. Every tweet will consist of the summation of all polarity of each word and devided by number of words in that tweet.</li>
	<li>Once preprocess is done. You can find the file in the directory "processed_data/output.xlsx". Opening it you will find that the ID (tweet) and Sentiment of each tweet is seperated into 2 columns. With this output you now have a twitter data set and its corresponding sentiment filtered by depress keywords. (Positive, Neutral and Negative).</li>
	<img src="https://i.ibb.co/NsvFqxm/dd.png" />
	<li>Now for training and Predicting. Make sure all files are located in proper folders, Run "depression_sentiment_analysis.py". The code will run through the output.xlsx file and at the same time recover the tweet corresponding to the id of each sentiment. using this we use the original data and feed them to our classifiers. When everything is done you should have all the AUC of each classifier listed in the console.</li>
	<li>But wait, There's more. You will also have the ability to type in a sample tweet, The tweet will go through the highest AUC in the list of classifier to predict the sentiment of the tweet you wrote.</li>
	<img src="https://i.ibb.co/72F8Vjq/ee.png" />
</ol>

<p>
	What the result could mean? <strong>Postive</strong>, This mean that person is unlikely to have depression or anxiety. <strong>Neutral</strong>, This is the middle level wherein the user may or may not have depression but may also be more prone to being depress. At that stage the user may display some depression like symptoms. lasty, <strong>Negative</strong> is the lowest level where depression and anxiety symptoms are being detected through the users tweets. The more negative words the user uses mean the more negative emotion the tweet has.
</p>



<h2 id="vd">Video Tutorials</h2>
<ul>
	<li><strong>How to download from Twitter: </strong><a href="http://recordit.co/lptv75TqDV">Video Link</a></li>
	<li><strong>How to preprocess data: </strong><a href="http://recordit.co/Y4YSvAokAN">Video Link</a></li>
	<li><strong>How to train and test: </strong><a href="http://recordit.co/eh42r6uAI0">Video Link</a></li>
</ul>

<h2>Results</h2>

Below are the Matrix for the 5 classifier with Decision tree having the highest score.

<img src="https://i.ibb.co/4WTHVGC/ff.png">


Using the same data set to test my accuracy, I trained and tested about 10,000 Tweets:
<p>AUC is an abbrevation for area under the curve. It is used in classification analysis in order to determine which of the used models predicts the classes best.</p>

<h4>Accuracy: </h4>
<ul>
	<li><strong>Naive Bayes  Accuracy: </strong>93.79406648429645 %</li>
	<li><strong>Decision Tree: </strong>98.55668748040587 %</li>
	<li><strong>Support Vector Machine: </strong>50.0 %</li>
	<li><strong>Kneighbors: </strong>81.464022923447 %</li>
	<li><strong>Random Forest: </strong>49.1038137743686 %</li>
</ul>

<h4>Completion Time: </h4>
<ul>
	<li><strong>Naive Bayes  Accuracy: </strong>0.59779 Seconds</li>
	<li><strong>Decision Tree: </strong>3.40457 Seconds</li>
	<li><strong>Support Vector Machine: </strong>29.83311 Seconds</li>
	<li><strong>Kneighbors: </strong>7.99048 Seconds</li>
	<li><strong>Random Forest: </strong>0.60994 Seconds</li>
</ul>


<h2>Future Plans</h2>
<p>This study is not yet perfect and im still aiming to improve it.</p>

<ul>
	<li>Use Contextual Semantic segmentation</li>
	<li>Use Stopwords to increase accuracy of model</li>
	<li>Eliminating features with extremely low frequency</li>
	<li>Use Complex Features: n-grams and part of speech tags</li>
</ul>

<h2 id="reference">References</h2>

<ul>
	<li>https://www.researchgate.net/publication/318136574_Extracting_Depression_Symptoms_from_Social_Networks_and_Web_Blogs_via_Text_Mining</li>
	<li>https://vgpena.github.io/classifying-tweets-with-keras-and-tensorflow/</li>
	<li>https://github.com/AshwanthRamji/Depression-Sentiment-Analysis-with-Twitter-Data</li>
	<li>https://arxiv.org/pdf/1607.07384.pdf</li>
</ul>



