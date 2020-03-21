from neattext import __version__
from neattext import TextCleaner,TextExtractor,TextMetrics


def test_version():
    assert __version__ == '0.0.2'

def test_remove_emails():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emails()
	assert result == 'This is the mail  ,our WEBSITE is https://example.com 😊.'


def test_extract_emails():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emails()
	assert result == ['example@gmail.com']

def test_remove_emojis():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emojis()
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'

def test_extract_emojis():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emojis()
	assert result == ['😊']


def test_remove_urls():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_urls()
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is  😊.'


def test_extract_urls():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_urls()
	assert result == ['https://example.com']

def test_remove_stopwords():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_stopwords()
	assert result == 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'


def test_extract_stopwords():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_stopwords()
	assert result == ['is', 'the', 'is']





