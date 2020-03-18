from neattext import __version__
from neattext import TextCleaner,TextExtractor,TextMetrics


def test_version():
    assert __version__ == '0.0.1'

def test_remove_emails():
	docx = TextCleaner()
	docx.text = "This is our email example@gmail.com"
	result = docx.remove_emails()
	assert result == 'This is our email '


def test_extract_emails():
	docx = TextExtractor()
	docx.text = "This is our email example@gmail.com"
	result = docx.extract_emails()
	assert result == ['example@gmail.com']





