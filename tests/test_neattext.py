from neattext import __version__
from neattext import TextCleaner,TextExtractor,TextMetrics,TextFrame
# from neattext.neattext import clean_text,remove_emails,extract_emails,replace_emails,replace_urls,remove_currencies,remove_currency_symbols,extract_currencies
from neattext.functions import *
from neattext.explainer import *



def test_version():
    assert __version__ == '0.0.9'

def test_remove_emails():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emails()
	assert str(result) == 'This is the mail  ,our WEBSITE is https://example.com 😊.'


def test_extract_emails():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emails()
	assert result == ['example@gmail.com']

def test_remove_emojis():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_emojis()
	assert str(result) == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'

def test_extract_emojis():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_emojis()
	assert result == ['😊']


def test_remove_urls():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_urls()
	assert str(result) == 'This is the mail example@gmail.com ,our WEBSITE is  😊.'


def test_extract_urls():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_urls()
	assert result == ['https://example.com']

def test_remove_currencies():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	result = docx.remove_currencies()
	assert str(result) == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost  to subscribe.'


def test_extract_currencies():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	result = docx.extract_currencies()
	assert result == ['$100']

def test_remove_currency_symbols():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	result = docx.remove_currency_symbols()
	assert str(result) == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost 100 to subscribe.'


def test_extract_currency_symbols():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	result = docx.extract_currency_symbols()
	assert result == ['$']


def test_remove_stopwords():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_stopwords()
	assert str(result) == 'mail example@gmail.com ,our WEBSITE https://example.com 😊.'


def test_extract_stopwords():
	docx = TextExtractor()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.extract_stopwords()
	assert result == ['this', 'is', 'the', 'is']

def test_single_fxn_remove_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = remove_emails(t1)
	assert result == 'This is the mail  ,our WEBSITE is https://example.com 😊.'


def test_single_fxn_extract_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = extract_emails(t1)
	assert result == ['example@gmail.com']

def test_single_fxn_clean_text():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
	result = clean_text(t1,stopwords=True)
	assert result == 'mail example@gmail.com ,our website https://example.com .'

	

def test_single_fxn_clean_text_no_stopword():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
	result = clean_text(t1,stopwords=False)
	assert result == 'this is the mail example@gmail.com ,our website is https://example.com .'



def test_single_fxn_clean_text_all():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = clean_text(t1)
	assert result != 'this is the mail  our website is  '

def test_single_fxn_replace_emails():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = replace_emails(t1)
	assert result == 'This is the mail <EMAIL> ,our WEBSITE is https://example.com 😊.'

def test_single_fxn_replace_urls():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = replace_urls(t1)
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is <URL> 😊.'
	
def test_single_fxn_remove_currencies():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	result = remove_currencies(t1)
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost  to subscribe.'

def test_single_fxn_remove_non_ascii():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is Ø https://example.com . "
	result = remove_non_ascii(t1)
	assert result == 'This is the mail example@gmail.com ,our WEBSITE is  https://example.com . '

def test_single_fxn_remove_bad_quotes():
	t1 = """He “went” home yesterday really ’late’."""
	result = remove_bad_quotes(t1)
	assert result == 'He  went  home yesterday really  late .'

def test_single_fxn_remove_multiple_spaces():
	t1 = 'He  went  home yesterday really  late .'
	result = remove_multiple_spaces(t1)
	assert result == 'He went home yesterday really late .'

def test_multiple_methods_chaining():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
	docx = TextCleaner(t1)
	result = docx.remove_emails().remove_urls().remove_emojis()
	assert str(result) == 'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'

def test_remove_dates():
	docx = TextCleaner()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe 20/12/2005."
	result = docx.remove_dates()
	assert str(result) == "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe ."


def test_emojify():
	result = emojify('Smiley')
	assert result == '😃'

def test_emoji_explainer():
	result = emoji_explainer('😃')
	assert result == 'SMILING FACE WITH OPEN MOUTH'


def test_textframe():
	docx = TextFrame()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.word_tokens()
	assert result == ['This', 'is', 'the', 'mail', 'examplegmailcom', 'our', 'WEBSITE', 'is', 'httpsexamplecom', '😊']

def test_textframe_remove_html():
	docx = TextFrame()
	docx.text = "This is the <h2>example for html tags</h2>"
	result = docx.remove_html_tags()
	assert result.text == "This is the example for html tags"

def test_textframe_remove_stopwords():
	docx = TextFrame()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_stopwords(lang='en')
	assert result.text == "mail example@gmail.com ,our WEBSITE https://example.com 😊."

def test_textframe_remove_puncts():
	docx = TextFrame()
	docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
	result = docx.remove_puncts()
	assert result.text == "This is the mail example@gmailcom our WEBSITE is https://examplecom 😊"


def test_textframe_remove_hashtags():
	docx = TextFrame()
	docx.text = "This is the tag #jesuslives use wisely "
	result = docx.remove_hashtags()
	assert result.text == "This is the tag   use wisely "


def test_textframe_remove_userhandles():
	docx = TextFrame()
	docx.text = "This is the tag @jesuslives use wisely "
	result = docx.remove_userhandles()
	assert result.text == "This is the tag   use wisely "


def test_single_fxn_extract_pattern():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is Ø https://example.com  #hello. "
	result = extract_pattern(t1,r'#\S+')
	assert result == ['#hello.']



def test_single_fxn_clean_text_custom_pattern():
	t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
	result = clean_text(t1,stopwords=False,custom_pattern=r'@\w+')
	assert result == 'this is the mail example .com ,our website is https://example.com .'
