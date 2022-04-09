# neattext
NeatText:a simple NLP package for cleaning textual data and text preprocessing

[![Build Status](https://travis-ci.org/Jcharis/neattext.svg?branch=master)](https://travis-ci.org/Jcharis/neattext)

[![GitHub license](https://img.shields.io/github/license/Jcharis/neattext)](https://github.com/Jcharis/neattext/blob/master/LICENSE)

#### Problem
+ Cleaning of unstructured text data
+ Reduce noise [special characters,stopwords]
+ Reducing repetition of using the same code for text preprocessing

#### Solution
+ convert the already known solution for cleaning text into a reuseable package


#### Installation
```bash
pip install neattext
```

### Usage
+ The OOP Way(Object Oriented Way)
+ NeatText offers 5 main classes for working with text data
    - TextFrame : a frame-like object for cleaning text
    - TextCleaner: remove or replace specifics
    - TextExtractor: extract unwanted text data
    - TextMetrics: word stats and metrics
    - TextPipeline: combine multiple functions in a pipeline

### Overall Components of NeatText
<!-- ![](images/neattext_features_jcharistech.png) -->
![NeatText](https://raw.githubusercontent.com/Jcharis/neattext/master/images/neattext_features_jcharistech.png)

### Using TextFrame
+ Keeps the text as `TextFrame` object. This allows us to do more with our text. 
+ It inherits the benefits of the TextCleaner and the TextMetrics out of the box with some additional features for handling text data.
+ This is the simplest way for text preprocessing with this library alternatively you can utilize the other classes too.


```python
>>> import neattext as nt 
>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>> docx = nt.TextFrame(text=mytext)
>>> docx.text 
"This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
>>>
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
>>> docx.length
73
>>> # Scan Percentage of Noise(Unclean data) in text
>>> d.noise_scan()
{'text_noise': 19.17808219178082, 'text_length': 73, 'noise_count': 14}
>>> 
>>> docs.head(16)
'This is the mail'
>>> docx.tail()
>>> docx.count_vowels()
>>> docx.count_stopwords()
>>> docx.count_consonants()
>>> docx.nlongest()
>>> docx.nshortest()
>>> docx.readability()
```
#### Basic NLP Task (Tokenization,Ngram,Text Generation)
```python
>>> docx.word_tokens()
>>>
>>> docx.sent_tokens()
>>>
>>> docx.term_freq()
>>>
>>> docx.bow()
```
#### Basic Text Preprocessing
```python
>>> docx.normalize()
'this is the mail example@gmail.com ,our website is https://example.com 😊.'
>>> docx.normalize(level='deep')
'this is the mail examplegmailcom our website is httpsexamplecom '

>>> docx.remove_puncts()
>>> docx.remove_stopwords()
>>> docx.remove_html_tags()
>>> docx.remove_special_characters()
>>> docx.remove_emojis()
>>> docx.fix_contractions()
```

##### Handling Files with NeatText
+ Read txt file directly into TextFrame
```python
>>> import neattext as nt 
>>> docx_df = nt.read_txt('file.txt')
```
+ Alternatively you can instantiate a TextFrame and read a text file into it
```python
>>> import neattext as nt 
>>> docx_df = nt.TextFrame().read_txt('file.txt')
```

##### Chaining Methods on TextFrame
```python
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
>>> docx = TextFrame(t1)
>>> result = docx.remove_emails().remove_urls().remove_emojis()
>>> print(result)
'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'
```



#### Clean Text
+ Clean text by removing emails,numbers,stopwords,emojis,etc
+ A simplified method for cleaning text by specifying as True/False what to clean from a text
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

#### Removing Punctuations [A Very Common Text Preprocessing Step]
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

#### Removing Stopwords [A Very Common Text Preprocessing Step]
+ You can remove stopwords from a text by specifying the language. The default language is English
+ Supported Languages include English(en),Spanish(es),French(fr)|Russian(ru)|Yoruba(yo)|German(de)

```python
>>> import neattext as nt 
>>> mytext = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊. Please don't forget the email when you enter !!!!!"
>>> docx = nt.TextFrame(mytext)
>>> docx.remove_stopwords(lang='en')
TextFrame(text="mail example@gmail.com ,our WEBSITE https://example.com 😊. forget email enter !!!!!")
```


#### Remove Emails,Numbers,Phone Numbers,Dates,Btc Address,VisaCard Address,etc 
```python
>>> print(docx.remove_emails())
>>> 'This is the mail  ,our WEBSITE is https://example.com 😊.'
>>>
>>> print(docx.remove_stopwords())
>>> 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'
>>>
>>> print(docx.remove_numbers())
>>> docx.remove_phone_numbers()
>>> docx.remove_btc_address()
```


#### Remove Special Characters
```python
>>> docx.remove_special_characters()
```

#### Remove Emojis
```python
>>> print(docx.remove_emojis())
>>> 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'
```


#### Remove Custom Pattern
+ You can also specify your own custom pattern, incase you cannot find what you need in the functions using the `remove_custom_pattern()` function
```python
>>> import neattext.functions as nfx 
>>> ex = "Last !RT tweeter multiple &#7777"
>>> 
>>> nfx.remove_custom_pattern(e,r'&#\d+')
'Last !RT tweeter multiple  '



```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> docx.replace_emails()
>>> docx.replace_numbers()
>>> docx.replace_phone_numbers()
```

#### Chain Multiple Methods
```python
>>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
>>> docx = TextCleaner(t1)
>>> result = docx.remove_emails().remove_urls().remove_emojis()
>>> print(result)
'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'

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
>>> docx.memory_usage()
```

### Usage 
+ The MOP(method/function oriented way) Way

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

### Explainer
+ Explain an emoji or unicode for emoji 
    - emoji_explainer()
    - emojify()
    - unicode_2_emoji()


```python
>>> from neattext.explainer import emojify
>>> emojify('Smiley')
>>> '😃'
```

```python
>>> from neattext.explainer import emoji_explainer
>>> emoji_explainer('😃')
>>> 'SMILING FACE WITH OPEN MOUTH'
```

```python
>>> from neattext.explainer import unicode_2_emoji
>>> unicode_2_emoji('0x1f49b')
    'FLUSHED FACE'
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



### Documentation
Please read the [documentation](https://github.com/Jcharis/neattext/wiki) for more information on what neattext does and how to use is for your needs.You can also check 
out our readthedocs page [here](https://jcharis.github.io/neattext/)

### More Features To Add
+ basic nlp task
+ currency normalizer

#### Acknowledgements
+ Inspired by packages like `clean-text` from Johannes Fillter and `textify` by JCharisTech


#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot


#### By
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



