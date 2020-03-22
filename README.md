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


