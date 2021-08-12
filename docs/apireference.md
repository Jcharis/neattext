## API reference
This page gives an overview of all `neattext` objects,functions and methods.

### Main Class
+ [TextFrame](#textframe)
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


**TextFrame**<a name="textframe"><a>

The neattext TextFrame API is a frame-like class useful for cleaning text.It inherits all the methods of the TextCleaner hence it can be used for removing or replacing emails,numbers,phone numbers,special characters,emojis,etc 

It can receive a text file and process it for a better output.
```Python
TextFrame(text=None)
```

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


#### TextFrame Basics
***read_text***<a name="read_text"></a>

Reads a text file and Creates A TextFrame for cleaning text


***describe***<a name="describe"></a>

Gives a basic description of the text which includes length,tokens,vowel and consonant count,etc


***head***<a name="head"></a>

Returns the first N characters in a text


***tail***<a name="tail"></a>

Returns the last N characters in a text


***normalize***<a name="normalize"></a>

Normalizes a text using two levels(shallow and deep) that removes all necessary noise to generate a clean text 


***word_tokens***<a name="word_tokens"></a>

Generate a word token of the text supplied using white-space or words


***sent_tokens***<a name="sent_tokens"></a>

Generate a sentence token of the text supplied 


***ngrams***<a name="ngrams"></a>

Generate an N-gram of the text supplied


***bow***<a name="bow"></a>

Generate a simple bag of words of text