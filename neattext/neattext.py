import re

EMAIL_REGEX =  re.compile(r"[\w\.-]+@[\w\.-]+")
NUMBERS_REGEX = re.compile(r"\d+")
PHONE_REGEX = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
SPECIAL_CHARACTERS_REGEX = re.compile(r"[^A-Za-z0-9 ]+")
EMOJI_REGEX = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       "]+", flags=re.UNICODE)

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# Remove Emails/Phone number/Emoji/Stopwords/etc

class TextCleaner(object):
	"""docstring for TextCleaner
	usage
	docx = TextCleaner(text="your text here")
	
	"""
	def __init__(self, text=None):
		super(TextCleaner, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextCleaner(text={})'.format(self.text)

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
	"""docstring for TextExtractor"""
	def __init__(self, text=None):
		super(TextExtractor, self).__init__()
		self.text = text

	def __repr__(self):
		return 'TextExtractor(text={})'.format(self.text)

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
	

class TextMetrics(object):
	"""docstring for TextMetrics"""
	def __init__(self, text=None):
		super(TextMetrics, self).__init__()
		self.text = text
	

	def __repr__(self):
		return 'TextMetrics(text={})'.format(self.text)

	def count_vowels(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'aeiou'}
		return result

	@property
	def vowels(self):
		words = self.text.lower()
		result = {v:words.count(v) for v in 'aeiou'}
		return result



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