# -*- coding: utf-8 -*-
# This file is part of the NEAT Project suite of libraries
# Please see the LICENSE file that should have been included as part of this 
# package. 

import re
from collections import Counter
import string
import csv
import heapq

# PATTERNS
EMAIL_REGEX =  re.compile(r"[\w\.-]+@[\w\.-]+")
NUMBERS_REGEX = re.compile(r"\d+")
PHONE_REGEX = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
MOST_COMMON_PUNCT_REGEX = re.compile(r"""[!"&',-.;?_`]""")
SPECIAL_CHARACTERS_REGEX = re.compile(r"[^A-Za-z0-9 ]+")
EMOJI_REGEX = re.compile("["
					   u"\U0001F600-\U0001F64F"  # for emoticons
					   u"\U0001F300-\U0001F5FF"  # for symbols & pictographs
					   u"\U0001F680-\U0001F6FF"  # for transport & map symbols
					   u"\U0001F1E0-\U0001F1FF"  # for flags (iOS)
					   u"\U00002702-\U000027B0"
					   u"\U000024C2-\U0001F251"
					   "]+", flags=re.UNICODE)

DATE_REGEX = re.compile(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})|([0-9]{4}\/[0-9]{2}\/[0-9]{2})")

# modified source :https://gist.github.com/dperini/729294
URL_PATTERN = re.compile(
	r"(?:^|(?<![\w\/\.]))"
	# protocol identifier
	# r"(?:(?:https?|ftp)://)"  <-- alt?
	r"(?:(?:https?:\/\/|ftp:\/\/|www\d{0,3}\.))"
	# user:pass authentication
	r"(?:\S+(?::\S*)?@)?" r"(?:"
	# IP address exclusion
	# private & local networks
	r"(?!(?:10|127)(?:\.\d{1,3}){3})"
	r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
	r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
	# IP address dotted notation octets
	# excludes loopback network 0.0.0.0
	# excludes reserved space >= 224.0.0.0
	# excludes network & broadcast addresses
	# (first & last IP address of each class)
	r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
	r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
	r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
	r"|"
	# host name
	r"(?:(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)"
	# domain name
	r"(?:\.(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)*"
	# TLD identifier
	r"(?:\.(?:[a-z\\u00a1-\\uffff]{2,}))" r")"
	# port number
	r"(?::\d{2,5})?"
	# resource path
	r"(?:\/[^\)\]\}\s]*)?",
	flags=re.UNICODE | re.IGNORECASE,
)

CURRENCY_REGEX = re.compile(
	r"[$¢£¤¥ƒ֏؋৲৳૱௹฿៛ℳ元円圆圓﷼\u20A0-\u20C0]\d+",
	flags=re.UNICODE)

CURRENCY_SYMB_REGEX = re.compile(
	r"[$¢£¤¥ƒ֏؋৲৳૱௹฿៛ℳ元円圆圓﷼\u20A0-\u20C0]",
	flags=re.UNICODE)

# PHONE_REGEX = re.compile(
#     r"(?:^|(?<=[^\w)]))(\+?1[ .-]?)?(\(?\d{3}\)?[ .-]?)?(\d{3}[ .-]?\d{4})"
#     r"(\s?(?:ext\.?|[#x-])\s?\d{2,6})?(?:$|(?=\W))",
#     flags=re.UNICODE | re.IGNORECASE)

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
AUTOMATED_READ_INDEX = {"1":"5-6 years (Kindergarten)","2":"6-7 years (First/Second Grade)","3":"7-9 years (Third Grade)","4":"9-10 years (Fourth Grade)","5":"10-11 years (Fifth Grade)","6":"11-12 years (Sixth Grade)","7":"12-13 years (Seventh Grade)","8":"13-14 years (Eighth Grade)","9":"14-15 years (Ninth Grade)","10":"15-16 years (Tenth Grade)","11":"16-17 years (Eleventh Grade)","12":"17-18 years (Twelfth grade)","13":"18-24 years (College student)","14":"24+ years (Professor)"}

# Metrics
class TextMetrics(object):
	""" TextMetrics : analyses a text for vowels,consonants,etc

	  Parameters
	  ----------
	  self.text : Main Text
		
	  Example
	  ----------
	  t1 = TextMetrics(text="Your text Here")
	  t1.word_stats()
	  t1.count_vowels()
	  t1.count_consonants()
	  t1.noise_scan()

	"""
	def __init__(self, text=None):
		super(TextMetrics, self).__init__()
		self.text = text
	

	def __repr__(self):
		return 'TextMetrics(text="{}")'.format(self.text)

	def count_vowels(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'aeiou'}
		return result

	def count_consonants(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'bcdfghjklmnpqrstvwxyz'}
		return result

	def count_stopwords(self):
		result = [word for word in self.text.lower().split() if word in STOPWORDS]
		final_res = Counter(result)
		return final_res

	def word_stats(self):
		words = self.text.lower()
		result_all_words = Counter(words.split())
		result_stopwords = [word for word in self.text.lower().split() if word in STOPWORDS]
		vowels_num = sum(self.count_vowels().values())
		consonants_num = sum(self.count_consonants().values())
		stats_dict = {"text_length":len(words),"num_of_vowels":vowels_num,
		"num_of_consonants":consonants_num,"num_of_stopwords":len(result_stopwords),
		"vowels_stats":self.count_vowels(),
		"consonants_stats":self.count_consonants(),
		}
		return stats_dict

	def noise_scan(self):
		"""Returns a Percentage of Noise/Dirt in our Text

		
		Formula : (sum_of_noise)/length of text * 100%
		noise: punctuations,special characters,stopwords,emojis,urls
		--------

	
		"""
		result_stopwords = [word for word in self.text.lower().split() if word in STOPWORDS]
		result_punct = {v: self.text.lower().count(v) for v in """!"&'()*,-./:;?@[\\]^_`{|}"""}
		punct_num = sum(result_punct.values())
		stopwords_num = len(result_stopwords)
		emoji_num = len(re.findall(EMOJI_REGEX,self.text))
		url_num = len(re.findall(URL_PATTERN,self.text))
		sum_of_noise = sum([punct_num + stopwords_num + emoji_num,url_num])
		# Handle ZeroDivisionError
		percentage_of_noise = (sum_of_noise/self.length * 100) if sum_of_noise != 0 else 0
		result_dict = {"text_noise":percentage_of_noise,"text_length":self.length,"noise_count":sum_of_noise}
		return result_dict




	@property
	def vowels(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'aeiou'}
		return result

	@property 
	def consonants(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'bcdfghjklmnpqrstvwxyz'}
		return result

	@property 
	def length(self):
		return len(self.text.lower())


	def readability(self):
		"""Returns the readability indices of the text using Automated Readability index

		------------
		ARI is derived from ratios that represent word difficulty (number of letters per word) and sentence difficulty (number of words per sentence).
		Automated Readability Index formula: 4.71 x (characters/words) + 0.5 x (words/sentences) - 21.43.

		"""
		num_of_characters = len(self.text)
		num_of_words = len(self.text.split(' '))
		num_of_sentences = len(self.text.split('.'))
		ari = 4.71 * (num_of_characters/num_of_words) + 0.5 * (num_of_words/num_of_sentences) - 21.43
		ari_desc = AUTOMATED_READ_INDEX.get(str(round(ari)))
		return {'automated readability':ari,"description":ari_desc}


# Remove Emails/Phone number/Emoji/Stopwords/etc

class TextCleaner(TextMetrics):
	""" TextCleaner: removes and cleans emails,numbers,etc from text
	
	Parameters
	----------
	  self.text : Main Text

	usage
	-------
	docx = TextCleaner(text="your text here")
	
	"""
	def __init__(self, text=None):
		super(TextCleaner, self).__init__()
		self.text = text

	def __str__(self):
		return '{}'.format(self.text)

	def __repr__(self):
		return 'TextCleaner(text="{}")'.format(self.text)
		

	def remove_emails(self):
		"""Returns A String with the emails removed """
		self.text = re.sub(EMAIL_REGEX,"",self.text)
		return self

	def remove_numbers(self):
		"""Returns A String with the numbers/digits removed """
		self.text = re.sub(NUMBERS_REGEX,"",self.text)
		return self

	def remove_phone_numbers(self):
		"""Returns A String with the phone numbers removed """
		self.text = re.sub(PHONE_REGEX,"",self.text)
		return self

	def remove_puncts(self,most_common=True):
		"""Returns A String with punctuations remove
		
		Params:
		most_common:boolen (True/False)
			- Use the most common punctuations(.,?! &-_"`)

		"""
		if most_common:
			MOST_COMMON_PUNCT_REGEX = re.compile(r"""[!"&',-.;?_`]""")
			self.text = re.sub(MOST_COMMON_PUNCT_REGEX,"",self.text)
		else:
			self.text = str(self.text).translate(str.maketrans('','',string.punctuation))
		return self

	def remove_special_characters(self):
		"""Returns A String with the specified characters removed """
		self.text = re.sub(SPECIAL_CHARACTERS_REGEX,"",self.text)
		return self

	def remove_emojis(self):
		"""Returns A String with the emojis removed """
		self.text = re.sub(EMOJI_REGEX,"",self.text)
		return self

	def remove_stopwords(self):
		"""Returns A String with the stopwords removed """
		result = [word for word in self.text.split() if word.lower() not in STOPWORDS]
		self.text = ' '.join(result)
		return self

	def remove_urls(self):
		"""Returns A String with URLS removed """
		self.text = re.sub(URL_PATTERN,"",self.text)
		return self

	def remove_currencies(self):
		"""Returns A String with Currencies removed """
		self.text = re.sub(CURRENCY_REGEX,"",self.text)
		return self

	def remove_currency_symbols(self):
		"""Returns A String with Currency Symbols removed """
		self.text = re.sub(CURRENCY_SYMB_REGEX,"",self.text)
		return self

	
	def remove_dates(self):
		"""Returns A String with Dates Removed """
		self.text = re.sub(DATE_REGEX,"",self.text)
		return self

	def remove_html_tags(self):
		"""Returns A String with HTML Tags removed"""
		self.text = re.sub('<[^<]+?>',"",self.text)
		return self

	def remove_non_ascii(self):
		"""Returns A String with Non ASCII removed"""
		import unicodedata
		self.text = unicodedata.normalize('NFKD',self.text).encode('ascii','ignore').decode('utf-8','ignore')
		return self 

	def remove_multiple_spaces(self):
		"""Returns A String with multiple whitespaces removed"""
		self.text = re.sub('\\s{2,}',' ',self.text)
		return self


	def remove_bad_quotes(self):
		"""Returns a string with bad quotes removed"""
		self.text = re.sub('[‘’“”…]',' ', self.text)
		return self


	def replace_emails(self,replace_with="<EMAIL>"):
		"""Replaces the emails in the text with custom label"""
		result = re.sub(EMAIL_REGEX,replace_with,self.text)
		return result
	
	def replace_phone_numbers(self,replace_with="<PHONENUMBER>"):
		"""Replaces the phone numbers in the text with custom label"""
		result = re.sub(PHONE_REGEX,replace_with,self.text)
		return result

	def replace_numbers(self,replace_with="<NUMBER>"):
		"""Replaces numbers/digits in the text with custom label"""
		result = re.sub(NUMBERS_REGEX,replace_with,self.text)
		return result

	def replace_special_characters(self,replace_with="<SPECIAL_CHAR>"):
		"""Replaces special characters in the text with custom label"""
		result = re.sub(SPECIAL_CHARACTERS_REGEX,replace_with,self.text)
		return result

	def replace_emojis(self,replace_with="<EMOJI>"):
		"""Replaces emojis in the text with custom label"""
		result = re.sub(EMOJI_REGEX,replace_with,self.text)
		return result

	def replace_urls(self,replace_with="<URL>"):
		"""Replaces URLS/HTTP(S) in the text with custom label"""
		result = re.sub(URL_PATTERN,replace_with,self.text)
		return result

	def replace_currencies(self,replace_with="<CURRENCY>"):
		"""Replaces Currencies in the text with custom label"""
		result = re.sub(CURRENCY_REGEX,replace_with,self.text)
		return result

	def replace_currency_symbols(self,replace_with="<CURRENCY_SYMB>"):
		"""Replaces currency symbols in the text with custom label"""
		result = re.sub(CURRENCY_SYMB_REGEX,replace_with,self.text)
		return result

	def replace_dates(self,replace_with="<DATE>"):
		"""Replaces Dates in the text with custom label"""
		result = re.sub(DATE_REGEX,replace_with,self.text)
		return result

	def replace_term(self,old_term,new_term):
		"""Replaces term in the text with another term"""
		result = re.sub(old_term,new_term,self.text)
		return result

	def fix_contractions(self):
		"""Fix contractions in a text"""
		text = self.text.lower()
		text = re.sub(r"i'm", "i am", text)
		text = re.sub(r"he's", "he is", text)
		text = re.sub(r"she's", "she is", text)
		text = re.sub(r"that's", "that is", text)        
		text = re.sub(r"what's", "what is", text)
		text = re.sub(r"where's", "where is", text) 
		text = re.sub(r"\'ll", " will", text)  
		text = re.sub(r"\'ve", " have", text)  
		text = re.sub(r"\'re", " are", text)
		text = re.sub(r"\'d", " would", text)
		text = re.sub(r"\'ve", " have", text)
		text = re.sub(r"won't", "will not", text)
		text = re.sub(r"don't", "do not", text)
		text = re.sub(r"did't", "did not", text)
		text = re.sub(r"can't", "can not", text)
		text = re.sub(r"it's", "it is", text)
		text = re.sub(r"couldn't", "could not", text)
		text = re.sub(r"have't", "have not", text)
		# New
		text = re.sub(r"ain't","am not",text)
		text = re.sub(r"aren't","are not",text)
		text = re.sub(r"can't","cannot",text)
		text = re.sub(r"can't've","cannot have",text)
		text = re.sub(r"'cause","because",text)
		text = re.sub(r"could've","could have",text)
		text = re.sub(r"couldn't","could not",text)
		text = re.sub(r"couldn't've","could not have",text)
		text = re.sub(r"didn't","did not",text)
		text = re.sub(r"doesn't","does not",text)
		text = re.sub(r"don't","do not",text)
		text = re.sub(r"hadn't","had not",text)
		text = re.sub(r"hadn't've","had not have",text)
		text = re.sub(r"hasn't","has not",text)
		text = re.sub(r"haven't","have not",text)
		text = re.sub(r"he'd","he would",text)
		text = re.sub(r"he'd've","he would have",text)
		text = re.sub(r"he'll","he will",text)
		text = re.sub(r"he'll've","he will have",text)
		text = re.sub(r"he's","he is",text)
		text = re.sub(r"how'd","how did",text)
		text = re.sub(r"how'd'y","how do you",text)
		text = re.sub(r"how'll","how will",text)
		text = re.sub(r"how's","how is",text)
		text = re.sub(r"I'd","I would",text)
		text = re.sub(r"I'd've","I would have",text)
		text = re.sub(r"I'll","I will",text)
		text = re.sub(r"I'll've","I will have",text)
		text = re.sub(r"I'm","I am",text)
		text = re.sub(r"I've","I have",text)
		text = re.sub(r"isn't","is not",text)
		text = re.sub(r"it'd","it had",text)
		text = re.sub(r"it'd've","it would have",text)
		text = re.sub(r"it'll","it will",text)
		text = re.sub(r"it'll've","it will have",text)
		text = re.sub(r"it's","it is",text)
		text = re.sub(r"let's","let us",text)
		text = re.sub(r"ma'am","madam",text)
		text = re.sub(r"mayn't","may not",text)
		text = re.sub(r"might've","might have",text)
		text = re.sub(r"mightn't","might not",text)
		text = re.sub(r"mightn't've","might not have",text)
		text = re.sub(r"must've","must have",text)
		text = re.sub(r"mustn't","must not",text)
		text = re.sub(r"mustn't've","must not have",text)
		text = re.sub(r"needn't","need not",text)
		text = re.sub(r"needn't've","need not have",text)
		text = re.sub(r"o'clock","of the clock",text)
		text = re.sub(r"oughtn't","ought not",text)
		text = re.sub(r"oughtn't've","ought not have",text)
		text = re.sub(r"shan't","shall not",text)
		text = re.sub(r"sha'n't","shall not",text)
		text = re.sub(r"shan't've","shall not have",text)
		text = re.sub(r"she'd","she would",text)
		text = re.sub(r"she'd've","she would have",text)
		text = re.sub(r"she'll","she will",text)
		text = re.sub(r"she'll've","she will have",text)
		text = re.sub(r"she's","she is",text)
		text = re.sub(r"should've","should have",text)
		text = re.sub(r"shouldn't","should not",text)
		text = re.sub(r"shouldn't've","should not have",text)
		text = re.sub(r"so've","so have",text)
		text = re.sub(r"so's","so is",text)
		text = re.sub(r"that'd","that would",text)
		text = re.sub(r"that'd've","that would have",text)
		text = re.sub(r"that's","that is",text)
		text = re.sub(r"there'd","there had",text)
		text = re.sub(r"there'd've","there would have",text)
		text = re.sub(r"there's","there is",text)
		text = re.sub(r"they'd","they would",text)
		text = re.sub(r"they'd've","they would have",text)
		text = re.sub(r"they'll","they will",text)
		text = re.sub(r"they'll've","they will have",text)
		text = re.sub(r"they're","they are",text)
		text = re.sub(r"they've","they have",text)
		text = re.sub(r"to've","to have",text)
		text = re.sub(r"wasn't","was not",text)
		text = re.sub(r"we'd","we had",text)
		text = re.sub(r"we'd've","we would have",text)
		text = re.sub(r"we'll","we will",text)
		text = re.sub(r"we'll've","we will have",text)
		text = re.sub(r"we're","we are",text)
		text = re.sub(r"we've","we have",text)
		text = re.sub(r"weren't","were not",text)
		text = re.sub(r"what'll","what will",text)
		text = re.sub(r"what'll've","what will have",text)
		text = re.sub(r"what're","what are",text)
		text = re.sub(r"what's","what is",text)
		text = re.sub(r"what've","what have",text)
		text = re.sub(r"when's","when is",text)
		text = re.sub(r"when've","when have",text)
		text = re.sub(r"where'd","where did",text)
		text = re.sub(r"where's","where is",text)
		text = re.sub(r"where've","where have",text)
		text = re.sub(r"who'll","who will",text)
		text = re.sub(r"who'll've","who will have",text)
		text = re.sub(r"who's","who is",text)
		text = re.sub(r"who've","who have",text)
		text = re.sub(r"why's","why is",text)
		text = re.sub(r"why've","why have",text)
		text = re.sub(r"will've","will have",text)
		text = re.sub(r"won't","will not",text)
		text = re.sub(r"won't've","will not have",text)
		text = re.sub(r"would've","would have",text)
		text = re.sub(r"wouldn't","would not",text)
		text = re.sub(r"wouldn't've","would not have",text)
		text = re.sub(r"y'all","you all",text)
		text = re.sub(r"y'alls","you alls",text)
		text = re.sub(r"y'all'd","you all would",text)
		text = re.sub(r"y'all'd've","you all would have",text)
		text = re.sub(r"y'all're","you all are",text)
		text = re.sub(r"y'all've","you all have",text)
		text = re.sub(r"you'd","you had",text)
		text = re.sub(r"you'd've","you would have",text)
		text = re.sub(r"you'll","you you will",text)
		text = re.sub(r"you'll've","you you will have",text)
		text = re.sub(r"you're","you are",text)
		text = re.sub(r"you've","you have",text)
		return text		


	def clean_text(self,preserve=False):
		"""
		Clean entire text 
		
		Parameters
		----------
		self

		preserve:Boolean(True/False) default is True
			preserves or keeps the original labels of what was cleaned.

		Returns
		-------
		string
	
		"""
		if preserve == False:
			email_result = re.sub(EMAIL_REGEX,"",self.text)
			phone_result = re.sub(PHONE_REGEX,"",email_result)
			number_result = re.sub(NUMBERS_REGEX,"",phone_result)
			url_result = re.sub(URL_PATTERN,"",number_result)
			emoji_result = re.sub(EMOJI_REGEX,"",url_result)
			special_char_result = re.sub(SPECIAL_CHARACTERS_REGEX,"",emoji_result)
			final_result = special_char_result.lower()
			
		else:
			special_char_result = re.sub(r'[^A-Za-z0-9@ ]+',"",self.text)
			email_result = re.sub(EMAIL_REGEX,"<EMAIL>",special_char_result)
			phone_result = re.sub(PHONE_REGEX,"<PHONENUMBER>",email_result)
			number_result = re.sub(NUMBERS_REGEX,"<NUMBERS>",phone_result)
			url_result = re.sub(URL_PATTERN,"<URL>",number_result)
			emoji_result = re.sub(EMOJI_REGEX,"<EMOJI>",url_result)
			final_result = emoji_result.lower()
			
		return final_result


	




class TextExtractor(TextCleaner):
	""" TextExtractor: extracts emails,numbers,etc from text
	 
	Parameters
	----------
	self.text : Main Text
	
	Usage
	--------
	docx = TextExtractor(text="your text here")
	docx.extract_emails()
	
	"""
	def __init__(self, text=None):
		super(TextExtractor, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextExtractor(text="{}")'.format(self.text)

	def extract_emails(self):
		"""Returns the emails extracted """
		result = re.findall(EMAIL_REGEX,self.text)
		return result

	def extract_numbers(self):
		"""Returns the numbers/digits extracted """
		result = re.findall(NUMBERS_REGEX,self.text)
		return result

	def extract_phone_numbers(self):
		"""Returns the phone number extracted """
		result = re.findall(PHONE_REGEX,self.text)
		return result


	def extract_special_characters(self):
		"""Returns the specified characters extracted """
		result = re.findall(SPECIAL_CHARACTERS_REGEX,self.text)
		return result

	def extract_emojis(self):
		"""Returns the emojis extracted """
		result = re.findall(EMOJI_REGEX,self.text)
		return result

	def extract_stopwords(self):
		"""Returns the stopwords as a list """
		result = [word for word in self.text.split() if word in STOPWORDS]
		return result
	
	def extract_urls(self):
		"""Returns the URLS extracted """
		result = re.findall(URL_PATTERN,self.text)
		return result

	def extract_html_tags(self):
		"""Returns A String with HTML Tags removed"""
		result = re.findall(r'<[^<]+?>',self.text)
		return result

	def extract_currencies(self):
		"""Returns the currencies extracted """
		result = re.findall(CURRENCY_REGEX,self.text)
		return result

	def extract_currency_symbols(self):
		"""Returns the currency symbols extracted """
		result = re.findall(CURRENCY_SYMB_REGEX,self.text)
		return result

	def extract_dates(self):
		"""Returns the dates extracted """
		result = re.findall(DATE_REGEX,self.text)
		return result

	def extract_btwn_squares(self):
		"""Returns the text in the square bracket
		
		Example
		>>> docx = nt.TextExtractor("he was [here] yesterday (early)")
		>>> docx.extract_btwn_squares()
		['here']

		"""
		# return re.findall('\\[[^]]*\\]',self.text)
		return re.findall('\\[[.*]\\]',self.text)

	def extract_btwn_brackets(self):
		"""Returns the text in the [] brackets

		Example
		>>> docx = nt.TextExtractor("he was [here] yesterday (early)")
		>>> docx.extract_btwn_brackets()
		['here']

		"""
		return re.findall('\\[(.*)\\]',self.text)

	def extract_btwn_parenthesis(self):
		"""Returns the text in the parenthesis/round () brackets
		
		Example
		>>> docx = nt.TextExtractor("he was [here] yesterday (early)")
		>>> docx.extract_btwn_parenthesis()
		['early']

		"""
		return re.findall('\\(([^)]+)',self.text)




def _pretty_table(my_dict):
	print("{:<8} {:<15}".format('Key','Value'))
	for k, v in my_dict.items():
		print("{:<8}: {:<15}".format(k, v))

class TextFrame(TextCleaner):
	"""Creates a TextFrame For Analyzing Text
	
	Parameters
	----------
	self.text : Main Text
	

	Returns
	----------
	Returns a TextFrame for text

	"""
	def __init__(self, text=None):
		super(TextFrame, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextFrame(text="{}")'.format(self.text)

	
	def head(self,n=5):
		"""Returns the First N Characters of a Text Default is 5
		
		"""
		return self.text[:n]


	def tail(self,n=5):
		"""Returns the Last N Characters of a Text Default is 5
		
		"""
		return self.text[-n:]

	@property
	def length(self):
		"""Returns the Length of the Text"""
		return len(self.text)

	def count_vowels(self):
		"""Returns the Count of Each Vowel"""
		words = self.text.lower()
		result = {v:words.count(v) for v in 'aeiou'}
		return result

	def count_consonants(self):
		"""Returns the Count of Each Consonant"""
		words = self.text.lower()
		result = {v:words.count(v) for v in 'bcdfghjklmnpqrstvwxyz'}
		return result

	def count_stopwords(self):
		"""Returns the Count of Stopwords"""
		result = [word for word in self.text.lower().split() if word in STOPWORDS]
		final_res = Counter(result)
		return dict(final_res)


	def count_special_char(self):
		"""Returns the Count of Each Special Char"""
		words = self.text.lower()
		sp_char_pattern = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
		# use double \\ to avoid invalid escape sequence
		result = {v:words.count(v) for v in sp_char_pattern }
		return result

	def count_puncts(self):
		"""Returns the Count of Each Punctuation"""
		words = self.text.lower()
		result = {v:words.count(v) for v in """!"&'()*,-./:;?@[\\]^_`{|}"""}
		return result


	def word_stats(self):
		"""Returns the Word Stats"""
		words = self.text.lower()
		result_all_words = Counter(words.split())
		result_stopwords = [word for word in self.text.lower().split() if word in STOPWORDS]
		vowels_num = sum(self.count_vowels().values())
		consonants_num = sum(self.count_consonants().values())
		stats_dict = {"Length of Text":len(words),"Num of Vowels":vowels_num,
		"Num of Consonants":consonants_num,"Num of Stopwords":len(result_stopwords),
		"Stats of Vowels":self.count_vowels(),
		"Stats of Consonants":self.count_consonants(),
		}
		return stats_dict


	def describe(self):
		"""Returns A Simple Table Describing the Text"""
		words = self.text.lower()
		result_all_words = Counter(words.split())
		result_stopwords = [word for word in self.text.lower().split() if word in STOPWORDS]
		vowels_num = sum(self.count_vowels().values())
		consonants_num = sum(self.count_consonants().values())
		punct_num = sum(self.count_puncts().values())
		special_char_num = sum(self.count_special_char().values())
		tokens_num_by_ws = len(self.text.split())
		token_words = re.split(r'\W+', self.text)
		tokens_num_by_words = len(token_words)
		stats_dict = {"Length":len(words),
		"vowels":vowels_num,
		"consonants":consonants_num,
		"stopwords":len(result_stopwords),
		"punctuations":punct_num,
		"special_char":special_char_num,
		"tokens(whitespace)":tokens_num_by_ws,
		"tokens(words)":tokens_num_by_words
		}
		return _pretty_table(stats_dict)

	
	def noise_scan(self):
		"""Returns a Percentage of Noise/Dirt in our Text

		
		Formula : (sum_of_noise)/length of text * 100%
		noise: punctuations,special characters,stopwords,emojis,urls
		--------

	
		"""
		result_stopwords = [word for word in self.text.lower().split() if word in STOPWORDS]
		punct_num = sum(self.count_puncts().values())
		stopwords_num = len(result_stopwords)
		emoji_num = len(re.findall(EMOJI_REGEX,self.text))
		url_num = len(re.findall(URL_PATTERN,self.text))
		sum_of_noise = sum([punct_num + stopwords_num + emoji_num,url_num])
		# Handle ZeroDivisionError
		percentage_of_noise = (sum_of_noise/self.length * 100) if sum_of_noise != 0 else 0
		# percentage_of_noise = sum_of_noise/self.length * 100
		result_dict = {"text_noise":percentage_of_noise,"text_length":self.length,"noise_count":sum_of_noise}
		return result_dict



	def read_txt(self,filename):
		"""
		Read a Text File and Create A TextFrame From it

		
		Parameters
		----------
		self : Main Text
		filename : file with text to read

		Returns
		----------
		Returns a TextFrame for text
		

		"""
		with open(filename,'r') as f:
			text_read = f.read()
			self.text=text_read
			docx_tf = TextFrame(self.text)
		return docx_tf

	def word_tokens(self,split_by='whitespace',remove_punct=True):
		"""
		Return a Word Tokens of the Text
		
		Parameters
		----------
		self : Main Text
		split_by : whitespace,words
			Split text into tokens using whitespace or words
		remove_punct: Remove/Strip off Punctuation Default is True
		Returns
		-------
		word tokens as a list

		Examples
		--------
		>>> docx.word_tokens()
				
		"""
		if remove_punct is True:
			# Split by White Space
			if split_by == 'whitespace':
				token_words = str(self.text).split()
			# Split by Words using Regex
			elif split_by == 'words':
				token_words = re.split(r'\W+', self.text)	
			# Strip/Remove of Punctuations and Special Characters
			table = str.maketrans('', '', string.punctuation)
			final_tokens = [w.translate(table) for w in token_words]			
		elif remove_punct is False:

			# Split by White Space
			if split_by == 'whitespace':
				final_tokens = str(self.text).split()
			# Split by White Space
			elif split_by == 'words':
				final_tokens = re.split(r'\W+', self.text)				

		return final_tokens

	def sent_tokens(self):
		"""Return a sentence token of text"""

		# split into text by punctuation
		sentences = self.text.split('.')
		# final_sentences = [sent  for i in sentences if '?' in sent ]
		final_sentences = []
		for _sent in sentences:
			if '?' in _sent:
				final_sentences.append(_sent.split('?'))
			else:
				final_sentences.append(_sent)

		# final_sentences = [_sent.split('?') for _sent in sentences if '?' in _sent]
		return final_sentences

	def bow(self):
		"""Returns a Bag of Words

		 Bow is matrix where each row represents a document and columns representing the individual token. 

		"""
		# Tokenize
		all_sents = self.text.split('.')

		# Counting
		bagsofwords = [ Counter(re.findall(r'\w+', txt)) for txt in all_sents]
		
		# Sum
		sum_of_bow = sum(bagsofwords, Counter())
		return sum_of_bow

	def ngrams(self,n_number=3):
		"""Returns N-gram of a text """

		# Tokenize
		token_words = self.text.split()

		# Split by N Words
		grams = [token_words[i:i+int(n_number)] for i in range(len(token_words)-int(n_number)+1)]

		for gr in grams:
			print(gr)



	def to_txt(self,filename):
		"""
		Save/Write a Text  to A File 

		
		Parameters
		----------
		self : Main Text
		filename : file with text to write/save to

		Returns
		----------
		Creates A New File with Text on it
		

		"""
		with open(filename,'w') as f:
			f.write(self.text)

	
	def to_csv(self,filename,count_str=False):
		"""Write Text to CSV file 

		Return a CSV of the Sentence Tokenized Text with/without string length
		
		Parameters
		----------
		self : Main Text
		filename : name of file to save as
			
		count_str: Compute/Count the length of each tokenized sentence/string

		Returns
		-------
		a csv file

		Examples
		--------
		>>> docx.to_csv("myfile.csv",count_str=True)


		"""
		
		with open(filename, "w") as csv_file:
			writer = csv.writer(csv_file,delimiter=",",quoting=csv.QUOTE_MINIMAL)
			# Split Text to Sentence Tokens
			data = self.sent_tokens()
			if count_str is True:
				# Create Column Headers
				writer.writerow(['sentence','count'])
				for i in data:
					writer.writerow([i,len(i)])
			else:
				for i in data:
					writer.writerow([i])

	

	def nshortest(self,n=3):
		"""Returns N list of the Shortest Tokens in a text"""
		
		token_list = self.word_tokens()
		result = heapq.nsmallest(n,token_list)
		return result


	def nlongest(self,n=3):
		"""Returns N list of the Longest Tokens in a text"""
		
		token_list = self.word_tokens()
		result = heapq.nlargest(n,token_list)
		return result

	def longest_token(self):
		"""Returns the Longest Token by length"""
		token_list = self.word_tokens(split_by='words')
		result = max(token_list,key=len)
		return result 

	def shortest_token(self):
		"""Returns the Shortest Token by length"""
		token_list = self.word_tokens(split_by='whitespace')
		result = min(token_list,key=len)
		return result 

	
	def normalize(self,level='shallow'):
		"""Normalize Text by converting to lowercase,removing punctuations and square brackets

		Parameters
		----------
		self : Main Text
		level : level of normalization (shallow/deep)
			shallow:lowercase,remove text in brackets and digits
			deep: shallow + removing puncts,emojis,bad commas,etc
		Returns
		----------
		Returns a new clean and normalized sentence
		

		"""
		
		if level == 'shallow':
			# Lowercase
			text = self.text.lower() 
			# Remove Txt in Square Bracket
			text = re.sub('\\[.*?\\]', '', text) 
			text = re.sub('\\w*\\d\\w*', '', text)
			# Strip html tags
			text = re.sub('<[^<]+?>','',text) 

		elif level == 'deep':
			# Lowercase
			text = self.text.lower() 
			# Remove Txt in Square Bracket
			text = re.sub('\\[.*?\\]', '', text) 
			# Remove Digit containing words
			text = re.sub('\\w*\\d\\w*', '', text) 

			# Fix Contractions
			text = self.fix_contractions()
			# Strip html tags
			text = re.sub('<[^<]+?>','',text) 
			
			# Remove Punct
			text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
			# Remove Bad Quotations
			text = re.sub('[‘’“”…]', '', text)
			# Remove emojis
			text = re.sub(EMOJI_REGEX,"",text)

		return text



	def term_freq(self):
		""" Returns the Term Frequency of Words in a Sentence

		Definition
		---------
		The number of times a word appears in a document divided by the total number of words in the document. 
			
		Formular
		---------
		TF = (Frequency of the word in the sentence) / (Total number of words in the sentence)

		"""
		stopwords = list(STOPWORDS)
		# Build Bag of Words or Word Frequency(bag) # 
		term_frequencies = {}  
		for word in self.text.split():  
			if word not in stopwords:
				if word not in term_frequencies.keys():
					term_frequencies[word] = 1
				else:
					term_frequencies[word] += 1

		
		maximum_frequency = max(term_frequencies.values())

		for word in term_frequencies.keys():  
			term_frequencies[word] = (term_frequencies[word]/maximum_frequency)
		
		return term_frequencies