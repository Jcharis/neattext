# neattext
NeatText a simple NLP package for cleaning textual data and text preprocessing


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
#### Clean Text
+ Clean text by removing emails,numbers,stopwords,etc
```python
>>> from neattext import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "your text goes here"
>>> docx.clean_text()
```

#### Remove Emails,Numbers,Phone Numbers 
```python
>>> docx.remove_emails()
>>> docx.remove_numbers()
>>> docx.remove_phone_numbers()
>>> docx.remove_stopwords()
```


#### Remove Special Characters
```python
>>> docx.remove_special_characters()
```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> docx.replace_emails()
>>> docx.replace_numbers()
>>> docx.replace_phone_numbers()
```

### Using TextExtractor
+ To Extract emails,phone numbers,numbers from text
```python
>>> from neattext import TextExtractor
>>> docx = TextExtractor()
>>> docx.text = "your text with example@gmail.com goes here"
>>> docx.extract_emails()
```


### More Features To Add
+ unicode explainer
+ currency normalizer


#### By 
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot
