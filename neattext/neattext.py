import re
from collections import Counter

EMAIL_REGEX =  re.compile(r"[\w\.-]+@[\w\.-]+")
NUMBERS_REGEX = re.compile(r"\d+")
PHONE_REGEX = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
SPECIAL_CHARACTERS_REGEX = re.compile(r"[^A-Za-z0-9 ]+")
EMOJI_REGEX = re.compile("["
                       u"\U0001F600-\U0001F64F"  # for emoticons
                       u"\U0001F300-\U0001F5FF"  # for symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # for transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # for flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       "]+", flags=re.UNICODE)

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

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# Remove Emails/Phone number/Emoji/Stopwords/etc

class TextCleaner(object):
	""" TextCleaner: removes and cleans emails,numbers,etc from text

	usage
	docx = TextCleaner(text="your text here")
	
	"""
	def __init__(self, text=None):
		super(TextCleaner, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextCleaner(text="{}")'.format(self.text)

	def remove_emails(self):
		result = re.sub(EMAIL_REGEX,"",self.text)
		return result

	def remove_numbers(self):
		result = re.sub(NUMBERS_REGEX,"",self.text)
		return result

	def remove_phone_numbers(self):
		result = re.sub(PHONE_REGEX,"",self.text)
		return result


	def remove_special_characters(self):
		result = re.sub(SPECIAL_CHARACTERS_REGEX,"",self.text)
		return result

	def remove_emojis(self):
		result = re.sub(EMOJI_REGEX,"",self.text)
		return result

	def remove_stopwords(self):
		result = [word for word in self.text.split() if word not in STOPWORDS]
		return ' '.join(result)

	def remove_urls(self):
		result = re.sub(URL_PATTERN,"",self.text)
		return result

	def replace_emails(self,replace_with="<EMAIL>"):
		result = re.sub(EMAIL_REGEX,replace_with,self.text)
		return result
	
	def replace_phone_numbers(self,replace_with="<PHONENUMBER>"):
		result = re.sub(PHONE_REGEX,replace_with,self.text)
		return result

	def replace_numbers(self,replace_with="<NUMBER>"):
		result = re.sub(NUMBERS_REGEX,replace_with,self.text)
		return result

	def replace_special_characters(self,replace_with="<SPECIAL_CHAR>"):
		result = re.sub(SPECIAL_CHARACTERS_REGEX,replace_with,self.text)
		return result

	def replace_emojis(self,replace_with="<EMOJI>"):
		result = re.sub(EMOJI_REGEX,replace_with,self.text)
		return result

	def replace_urls(self,replace_with="<URL>"):
		result = re.sub(URL_PATTERN,replace_with,self.text)
		return result


	def clean_text(self,preserve=False):
		"""Clean entire text """
		if preserve == False:
			email_result = re.sub(EMAIL_REGEX,"",self.text)
			phone_result = re.sub(PHONE_REGEX,"",email_result)
			number_result = re.sub(NUMBERS_REGEX,"",phone_result)
			emoji_result = re.sub(EMOJI_REGEX,"",number_result)
			special_char_result = re.sub(SPECIAL_CHARACTERS_REGEX,"",emoji_result)
			final_result = special_char_result.lower()
			
		else:
			special_char_result = re.sub(r'[^A-Za-z0-9@ ]+',"",self.text)
			email_result = re.sub(EMAIL_REGEX,"<EMAIL>",special_char_result)
			phone_result = re.sub(PHONE_REGEX,"<PHONENUMBER>",email_result)
			number_result = re.sub(NUMBERS_REGEX,"<NUMBERS>",phone_result)
			final_result = number_result.lower()
			
		return final_result





class TextExtractor(TextCleaner):
	""" TextExtractor: extracts emails,numbers,etc from text
	
	docx = TextExtractor(text="your text here")
	docx.extract_emails()
	
	"""
	def __init__(self, text=None):
		super(TextExtractor, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextExtractor(text="{}")'.format(self.text)

	def extract_emails(self):
		result = re.findall(EMAIL_REGEX,self.text)
		return result

	def extract_numbers(self):
		result = re.findall(NUMBERS_REGEX,self.text)
		return result

	def extract_phone_numbers(self):
		result = re.findall(PHONE_REGEX,self.text)
		return result


	def extract_special_characters(self):
		result = re.findall(SPECIAL_CHARACTERS_REGEX,self.text)
		return result

	def extract_emojis(self):
		result = re.findall(EMOJI_REGEX,self.text)
		return result

	def extract_stopwords(self):
		result = [word for word in self.text.split() if word in STOPWORDS]
		return result
	
	def extract_urls(self):
		result = re.findall(URL_PATTERN,self.text)
		return result

class TextMetrics(TextCleaner):
	""" TextMetrics : analyses a text for vowels,consonants,etc

	  t1 = TextMetrics(text="Your text Here")
	  t1.word_stats()
	  t1.count_vowels()
	  t1.count_consonants()

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
		stats_dict = {"Length of Text":len(words),"Num of Vowels":vowels_num,
		"Num of Consonants":consonants_num,"Num of Stopwords":len(result_stopwords),
		"Stats of Vowels":self.count_vowels(),
		"Stats of Consonants":self.count_consonants(),
		}
		return stats_dict


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
		


# Individual Functions
def remove_emails(text):
	result = re.sub(EMAIL_REGEX,"",text)
	return result

def remove_numbers(text):
	result = re.sub(NUMBERS_REGEX,"",text)
	return result

def remove_phone_numbers(text):
	result = re.sub(PHONE_REGEX,"",text)
	return result


def remove_special_characters(text):
	result = re.sub(SPECIAL_CHARACTERS_REGEX,"",text)
	return result

def remove_emojis(text):
	result = re.sub(EMOJI_REGEX,"",text)
	return result

def remove_stopwords(text):
	result = [word for word in text.split() if word not in STOPWORDS]
	return ' '.join(result)


def extract_emails(text):
	result = re.findall(EMAIL_REGEX,text)
	return result
	
def extract_numbers(text):
	result = re.findall(NUMBERS_REGEX,text)
	return result
	
def extract_phone_numbers(text):
	result = re.findall(PHONE_REGEX,text)
	return result
	
def extract_special_characters(text):
	result = re.findall(SPECIAL_CHARACTERS_REGEX,text)
	return result
	
def extract_emojis(text):
	result = re.findall(EMOJI_REGEX,text)
	return result
	
def extract_stopwords(text):
	result = [word for word in text.split() if word in STOPWORDS]
	return result
	