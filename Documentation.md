# Welcome to NeatText
NeatText (neattext) is a simple python NLP package for cleaning textual data and for processing text when performing NLP and ML projects.It was designed to solve the following problem

#### Problem Neattext is intended to solve
+ Cleaning of unstructured text data
+ Reduce noise [special characters,stopwords]
+ Reducing repetition of using the same code for text preprocessing


The NeatText project is maintained by @jcharis but contributors are gladly welcomed.

### Features
+ Removing of Noise In Text
 - special characters
 - emails
 - numbers/phone numbers
 - emojis
+ Dealing with stopwords
+ Extracting of emails,numbers,emoji,etc
+ Textmetrics : word statistics
+ Normalizing text


## Getting Started
### Installation
+ using pip
```bash
pip install neattext
```

### Usage
Neattext is designed to be used either via an object oriented approach or a functional/method oriented approach.

### Usage via The OOP Way(Object Oriented Way)
+ Neattext comes with 3 main class or objects for cleaning text and doing your text preprocessing.These classes include:

**TextCleaner**: For cleaning text by either removing or replacing the specific noise eg. emails,special characters,numbers,urls,emojis

**TextExtractor**: For extracting certain terms from a text or document

**TextMetrics**: For checking some basic word statics or metrics such as the count of vowels,consonants,stopwords,etc

### Usage via the MOP(Method/Function Oriented Way)
If you are a fun of functions you can also use `neattext` in such a manner. In that case you will have to import as this

```Python
from neattext.neattext import remove_emails,remove_emojis,clean_text
```

### API reference

This page gives an overview of all `neattext` objects,functions and methods.
### Main Class
+ [TextCleaner](#textcleaner)
+ [TextExtractor](#textextractor)
+ [TextMetrics](#textmetrics)

### General Functions
#### For TextCleaner : remove
+ [remove_emails](#remove_emails)
+ [remove_emails](#remove_emails)
+ [remove_numbers](#remove_numbers)
+ [remove_phone_numbers](#remove_phone_numbers)
+ [remove_urls](#remove_urls)
+ [remove_special_characters](#remove_special_characters)
+ [remove_emojis](#remove_emojis)
+ [remove_stopwords](#remove_stopwords)

#### For TextCleaner : replace
+ [replace_emails](#replace_emails)
+ [replace_numbers](#replace_numbers)
+ [replace_phone_numbers](#replace_phone_numbers)
+ [replace_urls](#replace_urls)
+ [replace_special_characters](#replace_special_characters)
+ [replace_emojis](#replace_emojis)
+ [replace_stopwords](#replace_stopwords)

#### For TextExtract : extract
+ [extract_emails](#extract_emails)
+ [extract_numbers](#extract_numbers)
+ [extract_phone_numbers](#extract_phone_numbers)
+ [extract_urls](#extract_urls)
+ [extract_special_characters](#extract_special_characters)
+ [extract_emojis](#extract_emojis)
+ [extract_stopwords](#extract_stopwords)

#### For TextMetrics : word statistics and counts
+ [count_vowels](#count_vowels)
+ [count_consonants](#count_consonants)
+ [count_stopwords](#count_stopwords)
+ [word_stats](#word_stats)



**TextCleaner**<a name="textcleaner"><a>

The neattext TextCleaner API is a class useful for cleaning text by either removing or replacing emails,numbers,phone numbers,special characters,emojis,etc 
```Python
TextCleaner(text=None)
```

**TextExtractor**<a name="textextractor"><a>

The neattext TextExtractor API is a class useful for extracting as a list emails,numbers,phone numbers,special characters,emojis,etc . In other word the same things that you would want cleaned or removed.In that case when you use the TextExtractor class you inherit all the methods of the TextCleaning class.

```Python
TextExtractor(text=None)
```

**TextMetrics**<a name="textmetrics"><a>

The neattext TextMetrics API is a class useful for cleaning text by either removing or replacing emails,numbers,phone numbers,special characters,emojis,etc 

```Python
TextMetrics(text=None)
```
#### TextCleaner remove methods
***remove_emails***<a name="remove_emails"></a>

Clean text by using custom regex to remove emails

***remove_numbers***<a name="remove_numbers"></a>

Clean text by using custom regex to remove numbers and digits

***remove_phone_numbers***<a name="remove_phone_numbers"></a>

Clean text by using custom regex to remove phone numbers

***remove_urls***<a name="remove_urls"></a>

Clean text by using custom regex to remove urls and websites

***remove_special_characters***<a name="remove_special_characters"></a>

Clean text by using custom regex to remove special characters

***remove_emojis***<a name="remove_emojis"></a>

Clean text by using custom regex to remove emojis and unicode representing emojis

***remove_stopwords***<a name="remove_stopwords"></a>

Clean text by using custom regex to remove english stopwords

#### TextCleaner replace methods
***replace_emails***<a name="replace_emails"></a>

Processes text by using custom regex to replace emails

***replace_numbers***<a name="replace_numbers"></a>

Processes text by using custom regex to replace numbers and digits

***replace_phone_numbers***<a name="replace_phone_numbers"></a>

Processes text by using custom regex to replace phone numbers

***replace_urls***<a name="replace_urls"></a>

Processes text by using custom regex to replace urls and websites

***replace_special_characters***<a name="replace_special_characters"></a>

Processes text by using custom regex to replace special characters

***replace_emojis***<a name="replace_emojis"></a>

Processes text by using custom regex to replace emojis and unicode representing emojis

***replace_stopwords***<a name="replace_stopwords"></a>

Processes text by using custom regex to replace english stopwords



#### TextExtractor Methods

***extract_emails***<a name="extract_emails"></a>

Works on text by using custom regex to extract emails

***extract_numbers***<a name="extract_numbers"></a>

Works on text by using custom regex to extract numbers and digits

***extract_phone_numbers***<a name="extract_phone_numbers"></a>

Works on text by using custom regex to extract phone numbers

***extract_urls***<a name="extract_urls"></a>

Works on text by using custom regex to extract urls and websites

***extract_special_characters***<a name="extract_special_characters"></a>

Works on text by using custom regex to extract special characters

***extract_emojis***<a name="extract_emojis"></a>

Works on text by using custom regex to extract emojis and unicode representing emojis

***extract_stopwords***<a name="extract_stopwords"></a>

Works on text by using custom regex to extract english stopwords



#### TextMetrics Methods

#### Clean Text
+ Clean text by removing emails,numbers,stopwords,emojis,etc
```python
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.clean_text()
```

#### Remove Emails,Numbers,Phone Numbers 
```python
>>> docx.remove_emails()
>>> 'This is the mail  ,our WEBSITE is https://example.com 😊.'
>>>
>>> docx.remove_stopwords()
>>> 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'
>>>
>>> docx.remove_numbers()
>>> docx.remove_phone_numbers()
```


#### Remove Special Characters
```python
>>> docx.remove_special_characters()
```

#### Remove Emojis
```python
>>> docx.remove_emojis()
>>> 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'
```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> docx.replace_emails()
>>> docx.replace_numbers()
>>> docx.replace_phone_numbers()
```

### Using TextExtractor
+ To Extract emails,phone numbers,numbers,urls,emojis from text
```python
>>> from neattext import TextExtractor
>>> docx = TextExtractor()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.extract_emails()
>>> ['example@gmail.com']
>>>
>>> docx.extract_emojis()
>>> ['😊']
```


### Using TextMetrics
+ To Find the Words Stats such as counts of vowels,consonants,stopwords,word-stats
```python
>>> from neattext import TextMetrics
>>> docx = TextMetrics()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.count_vowels()
>>> docx.count_consonants()
>>> docx.count_stopwords()
>>> docx.word_stats()
```

### Usage 
+ The MOP(method/function oriented way) Way

```python
>>> from neattext.neattext import clean_text,extract_emails
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
>>> clean_text(t1,True)
>>>'this is the mail <email> ,our website is <url> .'
>>> extract_emails(t1)
>>> ['example@gmail.com']
```

### More Features To Add
+ unicode explainer
+ currency normalizer

#### Acknowledgements
+ Inspired by packages like `clean-text` from Johannes Fillter


#### By
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot


