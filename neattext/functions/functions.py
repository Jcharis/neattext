import re
from neattext.pattern_data import EMAIL_REGEX,NUMBERS_REGEX,PHONE_REGEX,SPECIAL_CHARACTERS_REGEX,EMOJI_REGEX,URL_PATTERN,CURRENCY_REGEX,CURRENCY_SYMB_REGEX,STOPWORDS,DATE_REGEX

# Individual Functions
def remove_emails(text):
	"""Returns A String with the emails removed """
	result = re.sub(EMAIL_REGEX,"",text)
	return result

def remove_numbers(text):
	"""Returns A String with the numbers/digits removed """
	result = re.sub(NUMBERS_REGEX,"",text)
	return result

def remove_phone_numbers(text):
	"""Returns A String with the phone numbers removed """
	result = re.sub(PHONE_REGEX,"",text)
	return result


def remove_special_characters(text):
	"""Returns A String with the specified characters removed """
	result = re.sub(SPECIAL_CHARACTERS_REGEX,"",text)
	return result

def remove_emojis(text):
	"""Returns A String with the emojis removed """
	result = re.sub(EMOJI_REGEX,"",text)
	return result

def remove_stopwords(text):
	"""Returns A String with the stopwords removed """
	result = [word for word in text.split() if word not in STOPWORDS]
	return ' '.join(result)

def remove_urls(text):
	"""Returns A String with URLS removed """
	result = re.sub(URL_PATTERN,"",text)
	return result

def remove_currencies(text):
	"""Returns A String with Currencies removed """
	result = re.sub(CURRENCY_REGEX,"",text)
	return result

def remove_currency_symbols(text):
	"""Returns A String with Currency Symbols removed """
	result = re.sub(CURRENCY_SYMB_REGEX,"",text)
	return result


def extract_emails(text):
	"""Returns the emails extracted """
	result = re.findall(EMAIL_REGEX,text)
	return result
	
def extract_numbers(text):
	"""Returns the numbers/digits extracted """
	result = re.findall(NUMBERS_REGEX,text)
	return result
	
def extract_phone_numbers(text):
	"""Returns the phone number extracted """
	result = re.findall(PHONE_REGEX,text)
	return result
	
def extract_special_characters(text):
	"""Returns the specified characters extracted """
	result = re.findall(SPECIAL_CHARACTERS_REGEX,text)
	return result
	
def extract_emojis(text):
	"""Returns the emojis extracted """
	result = re.findall(EMOJI_REGEX,text)
	return result
	
def extract_stopwords(text):
	"""Returns the stopwords as a list """
	result = [word for word in text.split() if word in STOPWORDS]
	return result
	
def extract_urls(text):
	"""Returns the URLS extracted """
	result = re.findall(URL_PATTERN,text)
	return result

def extract_currencies(text):
	"""Returns the currencies extracted """
	result = re.findall(CURRENCY_REGEX,text)
	return result

def extract_currency_symbols(text):
	"""Returns the currency symbols extracted """
	result = re.findall(CURRENCY_SYMB_REGEX,text)
	return result

def extract_dates(text):
		"""Returns the dates extracted """
		result = re.findall(DATE_REGEX,text)
		return result


def clean_text(text,preserve=False):
	"""Clean Entire Text"""
	if preserve == False:
		email_result = re.sub(EMAIL_REGEX,"",text)
		phone_result = re.sub(PHONE_REGEX,"",email_result)
		number_result = re.sub(NUMBERS_REGEX,"",phone_result)
		url_result = re.sub(URL_PATTERN,"",number_result)
		emoji_result = re.sub(EMOJI_REGEX,"",url_result)
		special_char_result = re.sub(SPECIAL_CHARACTERS_REGEX,"",emoji_result)
		final_result = special_char_result.lower()
	else:
		email_result = re.sub(EMAIL_REGEX,"<EMAIL>",text)
		phone_result = re.sub(PHONE_REGEX,"<PHONENUMBER>",email_result)
		number_result = re.sub(NUMBERS_REGEX,"<NUMBERS>",phone_result)
		url_result = re.sub(URL_PATTERN,"<URL>",number_result)
		emoji_result = re.sub(EMOJI_REGEX,"<EMOJI>",url_result)
		final_result = emoji_result.lower()

	return final_result

def replace_emails(text,replace_with="<EMAIL>"):
	"""Replaces the emails in the text with custom label"""
	result = re.sub(EMAIL_REGEX,replace_with,text)
	return result

def replace_phone_numbers(text,replace_with="<PHONENUMBER>"):
	"""Replaces the phone numbers in the text with custom label"""
	result = re.sub(PHONE_REGEX,replace_with,text)
	return result

def replace_numbers(text,replace_with="<NUMBER>"):
	"""Replaces numbers/digits in the text with custom label"""
	result = re.sub(NUMBERS_REGEX,replace_with,text)
	return result

def replace_special_characters(text,replace_with="<SPECIAL_CHAR>"):
	"""Replaces special characters in the text with custom label"""
	result = re.sub(SPECIAL_CHARACTERS_REGEX,replace_with,text)
	return result

def replace_emojis(text,replace_with="<EMOJI>"):
	"""Replaces emojis in the text with custom label"""
	result = re.sub(EMOJI_REGEX,replace_with,text)
	return result

def replace_urls(text,replace_with="<URL>"):
	"""Replaces URLS/HTTP(S) in the text with custom label"""
	result = re.sub(URL_PATTERN,replace_with,text)
	return result

def replace_currencies(text,replace_with="<CURRENCY>"):
	"""Replaces Currencies in the text with custom label"""
	result = re.sub(CURRENCY_REGEX,replace_with,text)
	return result

def replace_currency_symbols(text,replace_with="<CURRENCY_SYMB>"):
	"""Replaces currency symbols in the text with custom label"""
	result = re.sub(CURRENCY_SYMB_REGEX,replace_with,text)
	return result


def replace_dates(text,replace_with="<DATE>"):
	"""Replaces Dates in the text with custom label"""
	result = re.sub(DATE_REGEX,replace_with,text)
	return result