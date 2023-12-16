## API reference
This page gives an overview of all `neattext` objects,functions and methods.

### Main Class
+ [TextFrame](#textframe)
+ [TextCleaner](#textcleaner)
+ [TextExtractor](#textextractor)
+ [TextMetrics](#textmetrics)
+ [TextPipeline](#textpipeline)

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
+ [remove_terms_in_bracket](#remove_terms_in_bracket)
+ [remove_accents](#remove_accents)

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
+ [extract_terms_in_bracket](#extract_terms_in_bracket)

#### For TextMetrics : word statistics and counts
+ [count_vowels](#count_vowels)
+ [count_consonants](#count_consonants)
+ [count_stopwords](#count_stopwords)
+ [word_stats](#word_stats)
+ [unique](#unique)
+ [nunique](#nunique)
+ [memory_usage](#memory_usage)


#### For TextPipeline : combine neattext function in a pipeline
+ [TextPipeline.fit](#TextPipeline.fit)
+ [TextPipeline.transform](#TextPipeline.transform)
+ [named_steps](#named_steps)


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


**TextPipeline**<a name="textpipeline"><a>

The neattext TextPipeline API is a class useful for combining or chaining several text cleaning functions as one in a format of a pipeline that implement the `fit` method on a given text. 
```Python
TextPipeline(steps=[fxns])
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

***remove_dates***<a name="remove_dates"></a>

Clean text by using custom regex to remove dates

***remove_terms_in_bracket***<a name="remove_terms_in_bracket"></a>

Clean text by using custom regex to remove terms in the specified bracket either [] or {}

***remove_accents***<a name="remove_accents"></a>

Clean text by removing diacritics and accents from a given text



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

***extract_terms_in_bracket***<a name="extract_terms_in_bracket"></a>

Works on text by using custom regex to extract terms inside bracket ([] or {})


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


***unique***<a name="unique"></a>

Returns a list of unique tokens/values in a text


***nunique***<a name="nunique"></a>

Returns the count/number of unique tokens in a text

***memory_usage***<a name="memory_usage"></a>

Returns the amount of memory/bytes used by a given text



#### TextPipeline
***TextPipeline.fit***<a name="TextPipeline.fit"></a>

Fit a group of neattext functions on a given text

***named_steps***<a name="named_steps"></a>

Returns all the functions/steps in a given TextPipeline


***TextPipeline.transform***<a name="TextPipeline.transform"></a>

Transform a given text using a group of neattext functions to a cleaner text

