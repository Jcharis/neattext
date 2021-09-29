## The User Guide
The User Guide documentation begins with some background information about NeatText, then focuses on step-by-step instructions for getting the most out of NeatText.



## Getting Started

### Installation of NeatText
+ Neattext is availble on PyPI hence you can use pip to install it as follows

```bash
pip install neattext
```

or specifically for a python version as such
```bash
python3 -m pip install neattext

```

## Quick Start
After install neattext with pypi, you can use neattext in two main ways - the OOP way 
or the Method Oriented way.
Neattext is designed to be used either via an object oriented approach or a functional/method oriented approach.

### Usage via The OOP Way(Object Oriented Way)
+ Neattext comes with 3 main class or objects for cleaning text and doing your text preprocessing.These classes include:

**TextCleaner**: For cleaning text by either removing or replacing the specific noise eg. emails,special characters,numbers,urls,emojis

**TextExtractor**: For extracting certain terms from a text or document

**TextMetrics**: For checking some basic word statics or metrics such as the count of vowels,consonants,stopwords,etc


```Python
>>> from neattext import TextCleaner,TextExtractor,TextMetrics
>>> docx = TextCleaner()
>>> docx.text = "your text goes here"
>>> docx.clean_text()
```

## Usage via the OOP way - Object Oriented Way (General usage)

#### Text Preprocessing
+ Preprocess texts and clean text
```python
>>> import neattext as nt
>>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx = nt.TextFrame(mytext)
>>> docx.describe()
Key      Value          
Length  : 73             
vowels  : 21             
consonants: 34             
stopwords: 4              
punctuations: 8              
special_char: 8              
tokens(whitespace): 10             
tokens(words): 14 
>>>
>>> docx.head(16)
'This is the mail'
>>> docx.tail(16)
'//example.com 😊.'
>>> 
>>> docx.normalize()
'this is the mail example@gmail.com ,our website is https://example.com 😊.'
>>> docx.normalize(level='deep')
'this is the mail examplegmailcom our website is httpsexamplecom '
>>> docx.remove_emojis()

```

#### Simple NLP Task
You can also do some basic Natural Language Preprocessing task such as tokenization,ngrams,text generation,etc
```python
>>> docx.word_tokens()

```
#### Clean Text using the Method Oriented Approach
+ Clean text by removing emails,numbers,stopwords,emojis,etc
+ A simple method for cleaning text by specifying as True/False what to clean from a text.
```python
>>> from neattext.functions import clean_text
>>> 
>>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> 
>>> clean_text(mytext)
'mail example@gmail.com ,our website https://example.com .'
```
+ You can remove punctuations,stopwords,urls,emojis,multiple_whitespaces,etc by setting them to True.
+ You can choose to remove or not remove punctuations by setting to True/False respectively

```python
>>> clean_text(mytext,puncts=True)
'mail example@gmailcom website https://examplecom '
>>> 
>>> clean_text(mytext,puncts=False)
'mail example@gmail.com ,our website https://example.com .'
>>> 
>>> clean_text(mytext,puncts=False,stopwords=False)
'this is the mail example@gmail.com ,our website is https://example.com .'
>>> 
```
+ You can also remove the other non-needed items accordingly
```python
>>> clean_text(mytext,stopwords=False)
'this is the mail example@gmail.com ,our website is https://example.com .'
>>>
>>> clean_text(mytext,urls=False)
'mail example@gmail.com ,our website https://example.com .'
>>> 
>>> clean_text(mytext,urls=True)
'mail example@gmail.com ,our website .'
>>> 

```
#### Remove Punctuations [A Very Common Text Preprocessing Step]
+ You remove the most common punctuations such as fullstop,comma,exclamation marks and question marks by setting most_common=True which is the default
+ Alternatively you can also remove all known punctuations from a text.
```python
>>> import neattext as nt 
>>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊. Please don't forget the email when you enter !!!!!"
>>> docx = nt.TextFrame(mytext)
>>> docx.remove_puncts()
TextFrame(text="This is the mail example@gmailcom our WEBSITE is https://examplecom 😊 Please dont forget the email when you enter ")

>>> docx.remove_puncts(most_common=False)
TextFrame(text="This is the mail examplegmailcom our WEBSITE is httpsexamplecom 😊 Please dont forget the email when you enter ")
```

#### Remove Emails,Numbers,Phone Numbers 
```python
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
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
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx.remove_emojis()
>>> 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'
```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
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



### Usage via the MOP(Method/Function Oriented Way)
If you are a fun of functions you can also use `neattext` in such a manner using the `functions` sub-package. In that case you will have to import as this

```Python
>>> from neattext.functions import remove_emails,remove_emojis,clean_text
```
You can also use the import as feature.
```Python
>>> import neattext.functions as ntf
>>> ntf.remove_emails(your_text)
>>>
```

```python
>>> from neattext.functions import clean_text,extract_emails
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
>>> clean_text(t1,puncts=True,stopwords=True)
>>>'this mail examplegmailcom website httpsexamplecom'
>>> extract_emails(t1)
>>> ['example@gmail.com']
```

+ Alternatively you can also use this approach
```python
>>> import neattext.functions as nfx 
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
>>> nfx.clean_text(t1,puncts=True,stopwords=True)
>>>'this mail examplegmailcom website httpsexamplecom'
>>> nfx.extract_emails(t1)
>>> ['example@gmail.com']
```

### Pipeline Approach using TextPipeline
+ This is a new feature(from version 0.1.2) that introduces the concept of pipeline. 
+ TextPipeline operates like the `clean_text` function but in this case you specify
according as steps a group of functions you need to use to clean a given text.

```python
>>> from neattext.pipeline import TextPipeline
>>> t1 = """This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊. This is visa 4111 1111 1111 1111 and bitcoin 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 with mastercard 5500 0000 0000 0004. Send it to PO Box 555, KNU"""

>>> p = TextPipeline(steps=[remove_emails,remove_numbers,remove_emojis])
>>> p.fit(t1)
'This is the mail  ,our WEBSITE is https://example.com . This is visa     and bitcoin BvBMSEYstWetqTFnAumGFgxJaNVN with mastercard    . Send it to PO Box , KNU'

```
+ Check For steps and named steps
```python
>>> p.steps
>>> p.named_steps
```