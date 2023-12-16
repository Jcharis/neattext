# -*- coding: utf-8 -*-
import re
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

DATE_REGEX = re.compile(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})|([0-9]{4}\/[0-9]{2}\/[0-9]{2})")
PUNCT_REGEX = re.compile(r"""[!"&'()*,-./:;?@[\\]^_`{|}]""")
# modified for full stops, question marks, commas, colons and semi-colons, exclamation marks and quotation marks.
MOST_COMMON_PUNCT_REGEX = re.compile(r"""[!"&',-.;?_`]""")
HTML_TAGS_REGEX = re.compile(r'<[^<]+?>')
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

HASTAG_REGEX = re.compile(r"#\S+")
USER_HANDLES_REGEX = re.compile(r"@\S+")
# PHONE_REGEX = re.compile(
#     r"(?:^|(?<=[^\w)]))(\+?1[ .-]?)?(\(?\d{3}\)?[ .-]?)?(\d{3}[ .-]?\d{4})"
#     r"(\s?(?:ext\.?|[#x-])\s?\d{2,6})?(?:$|(?=\W))",
#     flags=re.UNICODE | re.IGNORECASE)

STREET_ADDRESS_REGEX  = re.compile(r"\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?`")
PoBOX_REGEX  = re.compile(r"(?i)P\.? ?O\.? Box \d+")
ZIP_REGEX  = re.compile(r"\b\d{5}(?:[-\s]\d{4})?\b")

BTC_ADDRESS_REGEX = re.compile(r"[13][a-km-zA-HJ-NP-Z1-9]{25,34}")
CreditCard_REGEX     = re.compile(r"(?:(?:(?:\d{4}[- ]?){3}\d{4}|\d{15,16}))")
VISACard_REGEX = re.compile(r"4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}")
MASTERCard_REGEX  = re.compile(r"5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}")

# MD5,SHA REGEX
MD5_SHA_REGEX = re.compile(r"([0-9a-fA-F]{32})|([0-9a-fA-F]{40})|([0-9a-fA-F]{64})")




STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

AUTOMATED_READ_INDEX = {"1":"5-6 years (Kindergarten)","2":"6-7 years (First/Second Grade)","3":"7-9 years (Third Grade)","4":"9-10 years (Fourth Grade)","5":"10-11 years (Fifth Grade)","6":"11-12 years (Sixth Grade)","7":"12-13 years (Seventh Grade)","8":"13-14 years (Eighth Grade)","9":"14-15 years (Ninth Grade)","10":"15-16 years (Tenth Grade)","11":"16-17 years (Eleventh Grade)","12":"17-18 years (Twelfth grade)","13":"18-24 years (College student)","14":"24+ years (Professor)"}

CONTRACTIONS_DICT = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "I'd": "I would",
  "I'd've": "I would have",
  "I'll": "I will",
  "I'll've": "I will have",
  "I'm": "I am",
  "I've": "I have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have"
}

FUNCTORS_WORDLIST = ["a","about", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "be", "became", "because", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "both", "but", "by", "can", "cannot", "could", "dare", "despite", "did", "do", "does", "done", "down", "during", "each", "eg", "either", "else", "elsewhere", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "first", "for", "former", "formerly", "from", "further", "furthermore", "had", "has", "have", "he", "hence", "her", "here", "hereabouts", "hereafter", "hereby", "herein", "hereinafter", "heretofore", "hereunder", "hereupon", "herewith", "hers", "herself", "him", "himself", "his", "how", "however", "i", "ie", "if", "in", "indeed", "inside", "instead", "into", "is", "it", "its", "itself", "last", "latter", "latterly", "least", "less", "lot", "lots", "many", "may", "me", "meanwhile", "might", "mine", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "namely", "near", "need", "neither", "never", "nevertheless", "next", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "oftentimes", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "per", "perhaps", "rather", "re", "same", "second", "several", "shall", "she", "should", "since", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "still", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereabouts", "thereafter", "thereby", "therefore", "therein", "thereof", "thereon", "thereupon", "these", "they", "third", "this", "those", "though", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "under", "until", "up", "upon", "us", "used", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "whyever", "will", "with", "within", "without", "would", "yes", "yet", "you", "your", "yours", "yourself", "yourselves"]

# STOPWORDS LIST FOR LANGUAGES
STOPWORDS_en = {'a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'ain', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'aren', "aren't", 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'bottom', 'but', 'by', 'ca', 'call', 'can', 'cannot', 'could', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'done', 'down', 'due', 'during', 'each', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'if', 'in', 'indeed', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'll', 'm', 'ma', 'made', 'make', 'many', 'may', 'me', 'meanwhile', 'might', 'mightn', "mightn't", 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'mustn', "mustn't", 'my', 'myself', 'name', 'namely', 'needn', "needn't", 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'o', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'quite', 'rather', 're', 'really', 'regarding', 's', 'same', 'say', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'show', 'side', 'since', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 't', 'take', 'ten', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'under', 'unless', 'until', 'up', 'upon', 'us', 'used', 'using', 'various', 've', 'very', 'via', 'was', 'wasn', "wasn't", 'we', 'well', 'were', 'weren', "weren't", 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'won', "won't", 'would', 'wouldn', "wouldn't", 'y', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'}
STOPWORDS_es = {'agregó', 'poder', 'debe', 'cerca', 'intentais', 'está', 'todas', 'durante', 'pesar', 'estoy', 'ello', 'buenas', 'hacemos', 'adelante', 'mismas', 'trabajo', 'quién', 'desde', 'cierta', 'suyas', 'próximos', 'ahí', 'ningunos', 'casi', 'dicho', 'cual', 'ex', 'vais', 'empleais', 'despues', 'siendo', 'general', 'sean', 'otras', 'deprisa', 'dónde', 'esta', 'aún', 'nueva', 'cuántos', 'intenta', 'porque', 'bueno', 'podría', 'vuestras', 'debido', 'través', 'enseguida', 'lleva', 'sé', 'alrededor', 'horas', 'trabajar', 'mía', 'hacen', 'medio', 'algún', 'mayor', 'habrá', 'conseguimos', 'mis', 'tendrá', 'mios', 'aproximadamente', 'eramos', 'buen', 'además', 'emplean', 'quiere', 'conocer', 'expresó', 'ti', 'empleo', 'buenos', 'cuanto', 'sus', 'no', 'tras', 'raras', 'ante', 'cuándo', 'posible', 'estan', 'vaya', 'vuestro', 'éstas', 'arribaabajo', 'arriba', 'trabajas', 'cualquier', 'mismo', 'salvo', 'sino', 'este', 'contra', 'delante', 'soyos', 'asi', 'de', 'dentro', 'informó', 'podriamos', 'sabemos', 'trabaja', 'hacer', 'eres', 'aquellas', 'partir', 'otros', 'quienes', 'cuánta', 'mediante', 'qué', 'empleas', 'haces', 'aquí', 'todo', 'parece', 'dicen', 'ser', 'vuestros', 'somos', 'tuvo', 'total', 'nos', 'va', 'quiza', 'segundo', 'si', 'cuánto', 'luego', 'estar', 'ampleamos', 'hacia', 'mia', 'informo', 'también', 'existe', 'igual', 'eso', 'te', 'ella', 'nadie', 'estas', 'ningunas', 'largo', 'consideró', 'llegó', 'quizás', 'momento', 'diferentes', 'ademas', 'nuestros', 'llevar', 'detras', 'dieron', 'propio', 'ese', 'sois', 'cuáles', 'ciertos', 'suya', 'alguna', 'manifestó', 'esa', 'veces', 'actualmente', 'todavía', 'muchas', 'tengo', 'tan', 'serán', 'hizo', 'nuevo', 'gran', 'se', 'intentamos', 'es', 'demás', 'cuantas', 'vosotros', 'aquellos', 'tiempo', 'tuyos', 'lugar', 'cuatro', 'estamos', 'toda', 'alguno', 'como', 'hago', 'propios', 'mal', 'ocho', 'tres', 'diferente', 'el', 'mí', 'adrede', 'breve', 'hemos', 'fueron', 'nosotros', 'verdad', 'nunca', 'sobre', 'pasada', 'después', 'quizá', 'con', 'intento', 'podria', 'contigo', 'mencionó', 'quedó', 'modo', 'misma', 'apenas', 'ha', 'encima', 'consigue', 'nuevos', 'pudo', 'poca', 'consigues', 'otra', 'bajo', 'aquello', 'saben', 'hacerlo', 'tuya', 'fuera', 'dia', 'cuando', 'dio', 'mejor', 'ellas', 'tenga', 'al', 'tambien', 'conseguir', 'podemos', 'estados', 'hicieron', 'tenía', 'hablan', 'despacio', 'según', 'junto', 'así', 'lejos', 'último', 'conmigo', 'habia', 'pocos', 'antaño', 'cierto', 'vamos', 'incluso', 'día', 'queremos', 'temprano', 'demasiado', 'más', 'supuesto', 'muchos', 'primera', 'algunas', 'propia', 'debajo', 'ninguno', 'tú', 'estado', 'mismos', 'pero', 'proximo', 'usas', 'esos', 'podrán', 'muy', 'repente', 'trabajan', 'ya', 'usamos', 'emplear', 'nuevas', 'dos', 'ésas', 'intentas', 'cuanta', 'soy', 'tercera', 'quizas', 'ver', 'hasta', 'considera', 'las', 'cuenta', 'alli', 'aquéllos', 'aquéllas', 'decir', 'ahi', 'usais', 'paìs', 'sabes', 'próximo', 'ultimo', 'usan', 'lado', 'indicó', 'pronto', 'éstos', 'podrían', 'aquél', 'primeros', 'cuántas', 'sigue', 'ahora', 'intentan', 'ningún', 'os', 'teneis', 'añadió', 'cuál', 'estos', 'primer', 'unas', 'estaba', 'excepto', 'bien', 'antano', 'solamente', 'aseguró', 'pocas', 'buena', 'tanto', 'cuantos', 'afirmó', 'podriais', 'por', 'pues', 'aqui', 'yo', 'acuerdo', 'ellos', 'él', 'dado', 'menos', 'comentó', 'son', 'estará', 'tal', 'tenemos', 'tuyas', 'le', 'aquélla', 'unos', 'atras', 'realizado', 'respecto', 'tendrán', 'nada', 'consiguen', 'trabajais', 'eras', 'sera', 'explicó', 'intentar', 'señaló', 'cómo', 'cinco', 'bastante', 'esas', 'consigo', 'segunda', 'haber', 'solos', 'seis', 'propias', 'ayer', 'final', 'había', 'sabe', 'sí', 'claro', 'tienen', 'mío', 'usa', 'varias', 'fue', 'verdadero', 'ésos', 'mucho', 'mi', 'fui', 'realizó', 'algo', 'era', 'antes', 'nosotras', 'para', 'hay', 'haceis', 'sólo', 'sin', 'sola', 'enfrente', 'cuales', 'grandes', 'principalmente', 'tus', 'vez', 'sea', 'qeu', 'segun', 'peor', 'un', 'poco', 'la', 'manera', 'mucha', 'embargo', 'puedo', 'encuentra', 'fin', 'detrás', 'gueno', 'su', 'anterior', 'da', 'ir', 'tampoco', 'tuyo', 'vosotras', 'en', 'lo', 'todavia', 'han', 'parte', 'solo', 'pasado', 'dar', 'allí', 'aunque', 'saber', 'creo', 'podeis', 'últimas', 'días', 'donde', 'deben', 'tarde', 'esto', 'estaban', 'ése', 'sería', 'dias', 'cosas', 'aquella', 'mas', 'ni', 'fuimos', 'voy', 'pueda', 'aun', 'mientras', 'pueden', 'tu', 'tenido', 'solas', 'tener', 'cada', 'última', 'habían', 'entonces', 'todos', 'siguiente', 'haciendo', 'tiene', 'últimos', 'mías', 'ninguna', 'trabajamos', 'ejemplo', 'sabeis', 'ambos', 'ciertas', 'dijo', 'hubo', 'usted', 'podrá', 'los', 'mio', 'nuestro', 'hace', 'les', 'usar', 'éste', 'menudo', 'aquel', 'realizar', 'primero', 'hecho', 'dijeron', 'haya', 'habla', 'dan', 'siempre', 'quiénes', 'eran', 'trata', 'uso', 'nuestra', 'podrias', 'ustedes', 'quien', 'he', 'dejó', 'varios', 'míos', 'pais', 'mias', 'del', 'poner', 'estuvo', 'nuestras', 'están', 'que', 'existen', 'vuestra', 'hoy', 'me', 'suyo', 'ésta', 'valor', 'será', 'entre', 'algunos', 'podrian', 'puede', 'siete', 'van', 'dice', 'ésa', 'sido', 'otro', 'uno', 'verdadera', 'estais', 'una'}
STOPWORDS_fr = {'allo', 'derriere', 'onzième', 'oust', 'vôtres', 'durant', 'troisièmement', 'rendre', 'serait', 'olé', 'sept', 'comme', 'souvent', 'suivants', 'soit', 'desormais', 'hou', 'ore', 'quand', 'lesquelles', 'boum', 'toi', 'prealable', 'dix-huit', 'sixième', 'trois', 'ceux-ci', 'derrière', 'différentes', 'hi', 'ouf', 'houp', 'fait', 'o', 'etant', 'dont', 'suffisante', 'aucune', 'suivre', 'minimale', 'pendant', 'sauf', 'specifiques', 'seul', 'vais', 'suivantes', 'beau', 'd’', 'possibles', 'avait', 'leur', 'plouf', 'peux', 'quels', 'dixième', 'différent', 'huitième', 'puis', 'vlan', 'relativement', 'anterieures', 'était', 'bravo', 'tiens', 'ayant', 'seulement', 'quelle', 'pfft', 'suivant', 'particulièrement', 'quatorze', 'pouah', 'deuxièmement', 'seize', 'ohé', 'quinze', 'autrui', 'alors', 'tien', 'probable', 'divers', 'avons', 'parfois', 'pan', 'dessus', 'ça', 'chez', 'allô', 'celles-là', 'notre', 'aux', 'quel', 'etc', 'pouvait', 'ô', 'troisième', 'seraient', 'apres', 'restant', 'pure', 'soi', 'hors', 'memes', 'de', 'auraient', 'rare', 'soixante', 'sacrebleu', 'celui-ci', 'mon', 'ho', 'subtiles', 's’', 'hep', "qu'", 'reste', 'on', 'celui-là', 'pas', 'quiconque', 'toutes', 'par', 'deja', 'naturelle', 'specifique', 'nos', 'va', 'si', 'malgre', 'doit', 'lesquels', 'quatre-vingt', 'tel', 'ces', 'depuis', 'onze', 'brrr', 'ce', 'tous', 'aie', 'lui', 'te', 'celui', 'moi', 'douze', 'cependant', 'zut', 'mes', 'au', 'laquelle', 'gens', 'différente', 'voici', 'là', 'sien', 'parle', 'nôtres', 'c’', 'toujours', 'quatre', 'restrictif', 'basee', 'trop', 'très', 'peu', 'tes', 'huit', 'chaque', 'procedant', 'superpose', 'tsoin', 'avec', 'speculatif', 'vont', 'parce', 'pense', 'voilà', 'telle', 'outre', 'se', 'vous', 'eux', 'es', 'désormais', 'etais', 'personne', 'elle', 'ceci', 'proche', 'passé', 'quoique', 'sont', 'siennes', 'derniere', 'aura', 'clac', "m'", 'néanmoins', 'pire', 'quant-à-soi', 'rares', 'flac', 'vu', 'tres', 'meme', 'uns', 'vif', 'laisser', "l'", "t'", 'ont', 'hue', 'ès', 'auquel', 'suivante', 'assez', 'quelques', 'egales', 'fi', 'vas', 'nombreuses', 'etre', 'sent', 'crac', 'ses', 'clic', 'precisement', 'ha', 'necessairement', 'psitt', 'importe', 'premièrement', 'debout', 'encore', 'malgré', 'font', 'ouverts', 'vous-mêmes', 'remarquable', 'auront', 'ai', 'tend', 'possessifs', 'couic', 'quant', 'exterieur', 'tels', 'plus', 'toi-même', 'elles-mêmes', 'avaient', 'moins', 'pu', 'sait', 'tente', 'suffit', 'sienne', 'trente', 'suis', 'toc', 'tenir', 'feront', 'ouverte', 'ailleurs', 'enfin', 'nous-mêmes', 'tellement', 'allaient', 'bah', 'possible', 'abord', 'pour', 'eux-mêmes', 'elle-même', 'neuvième', 'floc', 'dring', 'stop', 'celles', 'moindres', "c'", 'sa', 'vé', 'hui', 'uniques', 'moi-meme', 'afin', 'celles-ci', 'exactement', 'faisant', 'lès', 'neanmoins', 'semblable', 'et', 'treize', 'allons', 'probante', 'las', 'tardive', 'aucun', 'uniformement', 'nous', 'ou', 'retour', 'vives', 'celle-là', 'differentes', 'moyennant', 'tout', 'dix', 'devant', 'vive', 'cette', 'cet', 'dite', 'bien', 'lorsque', 'absolument', 'quelconque', 'juste', 'hum', 'hop', 'directe', 'ait', 'different', 'rend', 'je', 'chacune', 'â', 'ceux', 'nombreux', 'na', 'après', 'cinquante', 'egale', 'peuvent', 'surtout', 'hé', 'comment', 'son', 'chère', 'nul', 'avais', 'ta', 'auxquels', 'effet', 'il', 'votre', 'le', 'sein', 'avant', 'certaines', 'ma', 'est', 't’', 'ceux-là', 'notamment', 'sera', 'delà', 'près', 'sans', 'diverse', 'pourrais', 'mien', 'vifs', 'siens', 'vivat', 'lui-même', 'mais', 'elles', 'première', 'qui', 'plutôt', 'autres', 'tsouin', 'touchant', 'dernier', 'plein', 'hormis', 'suffisant', 'suit', 'premier', 'ils', "n'", 'vingt', 'avoir', 'merci', 'cinq', 'eu', 'contre', 'combien', 'parlent', 'quanta', 'étais', 'restent', 'dans', 'celle', 'tienne', 'dessous', 'aussi', 'nouveau', 'unique', 'sapristi', 'anterieure', 'duquel', 'excepté', 'fais', 'bas', 'longtemps', 'neuf', 'holà', 'semblaient', 'telles', 'hurrah', 'plusieurs', 'a', 'quatrièmement', 'donc', 'differents', 'particulier', 'strictement', 'chacun', 'quarante', 'as', 'pourrait', 'certaine', 'semble', 'etaient', 'mille', 'pourquoi', 'un', 'bat', 'tic', 'maint', 'différents', 'la', 'nôtre', 'oh', 'attendu', 'lequel', 'eh', 'aujourd', 'leurs', 'paf', 'diverses', 'dix-sept', 'douzième', 'autrement', 'maintenant', "s'", 'da', 'etait', 'n’', 'moi-même', 'en', 'cinquantaine', 'desquels', 'parler', 'vers', 'certes', 'unes', 'lors', 'dit', 'dehors', 'lui-meme', 'pfut', "d'", 'façon', 'j’', 'étaient', 'tant', 'peut', 'partant', 'desquelles', 'hein', 'rien', 'possessif', 'aupres', 'auxquelles', 'envers', 'quelles', 'pur', 'via', 'toutefois', 'ni', 'ainsi', 'revoilà', 'chers', 'pres', 'parseme', 'quelque', 'tu', 'ton', 'maximale', 'toute', 'cher', 'autre', 'deux', 'étant', 'cela', 'hélas', 'celle-ci', 'chiche', 'faisaient', 'environ', 'pff', 'autrefois', 'té', 'des', 'devra', 'hem', 'i', 'miennes', 'chut', 'cent', 'du', 'necessaire', 'soi-même', "aujourd'hui", 'dits', 'ouste', 'relative', 'les', 'certain', 'revoici', 'concernant', 'miens', 'doivent', 'euh', 'non', 'tac', 'vôtre', 'anterieur', 'seule', 'egalement', 'm’', 'dire', 'sur', 'dès', 'selon', 'aurait', 'six', 'rarement', 'pif', 'car', 'été', 'cinquième', 'certains', 'seront', 'dix-neuf', 'même', "quelqu'un", 'être', 'bigre', 'ouvert', 'cinquantième', 'semblent', 'naturelles', 'que', 'dedans', 'beaucoup', 'directement', 'vos', 'ah', 'jusque', 'sous', 'ci', 'tenant', 'une', 'l’', 'ouias', 'mêmes', 'parmi', 'me', 'septième', 'quoi', 'naturel', 'devers', 'où', 'tiennes', 'qu’', 'deuxième', 'particulière', 'extenso', 'à', 'chères', 'comparables', 'entre', 'mince', 'ne', 'permet', 'quatrième', 'mienne', 'puisque', 'jusqu', 'ollé', "j'", 'sinon', 'compris', 'comparable'}
STOPWORDS_ru = {'моего', 'все', 'нашей', 'такая', 'нею', 'его', 'ем', 'от', 'моя', 'свою', 'своих', 'бы', 'будучи', 'нет', 'нему', 'сами', 'ела', 'это', 'когда', 'одним', 'кого', 'которою', 'ней', 'одному', 'свое', 'этою', 'нашею', 'моими', 'мое', 'всей', 'одних', 'мочь', 'ест', 'они', 'который', 'наш', 'тою', 'он', 'кто', 'всю', 'чтобы', 'наше', 'такого', 'нашим', 'всея', 'из', 'которого', 'эти', 'по', 'те', 'них', 'едим', 'мой', 'буду', 'может', 'на', 'ей', 'мы', 'есть', 'одни', 'самим', 'свой', 'которым', 'таком', 'этих', 'мне', 'могут', 'всеми', 'нее', 'она', 'такой', 'для', 'такую', 'теми', 'вот', 'которой', 'сама', 'саму', 'её', 'наши', 'которыми', 'что', 'оно', 'с', 'одну', 'этот', 'будете', 'могу', 'себе', 'такие', 'ними', 'которую', 'тех', 'могла', 'самом', 'нам', 'одно', 'тот', 'ему', 'всем', 'этими', 'но', 'своей', 'во', 'будем', 'всём', 'вами', 'своем', 'сам', 'эту', 'их', 'тобою', 'том', 'ею', 'еще', 'одна', 'своего', 'и', 'был', 'будь', 'всех', 'комья', 'как', 'такому', 'самими', 'можешь', 'можете', 'одними', 'только', 'чего', 'моё', 'моей', 'свои', 'своя', 'тобой', 'той', 'будешь', 'один', 'моим', 'мог', 'своею', 'же', 'ты', 'или', 'этому', 'могли', 'могло', 'своим', 'ел', 'моею', 'собой', 'наших', 'которые', 'вся', 'моему', 'мою', 'не', 'мои', 'я', 'ее', 'уже', 'да', 'одного', 'этой', 'была', 'нашем', 'можем', 'а', 'этим', 'которому', 'само', 'эта', 'за', 'себя', 'этом', 'кому', 'нашему', 'будьте', 'чему', 'наса', 'неё', 'одном', 'которое', 'томах', 'него', 'того', 'вам', 'емъ', 'тому', 'нами', 'которая', 'таким', 'тем', 'ко', 'у', 'ещё', 'самих', 'в', 'так', 'такое', 'своём', 'меня', 'самого', 'всему', 'будет', 'ими', 'моём', 'при', 'собою', 'одной', 'ешь', 'та', 'тебя', 'чем', 'ним', 'оне', 'вы', 'всего', 'к', 'об', 'будут', 'ком', 'если', 'наша', 'ту', 'были', 'было', 'моем', 'едят', 'могите', 'всею', 'своими', 'своему', 'до', 'то', 'нашими', 'нашего', 'такою', 'нем', 'им', 'которых', 'нас', 'имъ', 'мною', 'одною', 'самому', 'вас', 'кем', 'мной', 'нём', 'всё', 'тебе', 'котором', 'моги', 'такими', 'чём', 'моих', 'весь', 'нашу', 'быть', 'о', 'своё', 'таких', 'этого'}
STOPWORDS_yo = {'fún', 'è', 'ní', 'rẹ̀', 'k', 'sínú', 'àwọn', 'n', 'j', 'á', 'ti', 'ọ', 'mo', 'mọ̀', 'ù', 'ì', 'kì', 'tí', 'ṣùgbọ́n', 'p', 'máa', 'nítorí', 'nígbà', 'jẹ', 'u', 'm', 'púpọ̀', 'í', 'padà', 'jẹ́', 'náà', 'bí', 'bá', 'wọ́n', 'ẹ', 'wọn', 'ni', 'àti', 'b', 'gbogbo', 'yìí', 'ò', 'ṣé', '́', 't', 'f', 'láti', '̣', 'ẹmọ́', 'bẹ̀rẹ̀', 'ọ̀pọ̀lọpọ̀', 'w', '̀', 'mi', 'ǹ', 'sí', 'd', 'r', 'pẹ̀lú', 'wà', 'inú', 'ó', 'òun', 'wá', 'à', 'y', 'kò', 'fẹ́', 'i', 'e', 'ńlá', 'sì', 'nǹkan', 'lè', 'kan', 'jù', 'l', 'pé', 'é', 's', 'o', 'ọjọ́', 'g', 'ń', 'ṣe', 'an', 'a', 'lọ', 'ú', 'kí', 'ṣ'}
STOPWORDS_de = {'dieselbe', 'nahm', 'drei', 'eigen', 'vielen', 'guter', 'nun', 'würden', 'zu', 'sollten', 'derselben', 'vergangenen', 'dasselbe', 'grosse', 'könnte', 'á', 'wegen', 'bereits', 'demgegenüber', 'acht', 'mögen', 'meinem', 'rechter', 'jedermanns', 'weiteres', 'dir', 'trotzdem', 'wohl', 'wird', 'des', 'durchaus', 'her', 'je', 'außer', 'machte', 'infolgedessen', 'erst', 'später', 'während', 'derselbe', 'unsere', 'bisher', 'wir', 'großer', 'allen', 'dürft', 'ihre', 'hätten', 'in', 'jahr', 'wenn', 'dermassen', 'ihrem', 'gibt', 'recht', 'erstes', 'schon', 'überhaupt', 'sei', 'eigenen', 'achte', 'hat', 'jemand', 'eines', 'ausser', 'sonst', 'hoch', 'siebentes', 'immer', 'unter', 'gekonnt', 'denn', 'habe', 'hast', 'jenes', 'einmal', 'alles', 'sollte', 'lange', 'jeder', 'weniges', 'gar', 'wem', 'seine', 'fünfte', 'währenddessen', 'elf', 'gegen', 'dahin', 'wenigstens', 'besser', 'zwar', 'weiteren', 'allein', 'seitdem', 'kein', 'sechstes', 'vier', 'damals', 'zehnten', 'endlich', 'der', 'früher', 'wurde', 'war', 'mögt', 'los', 'rechte', 'zunächst', 'dieses', 'dasein', 'ganzen', 'siebte', 'nur', 'gemusst', 'ihm', 'jedermann', 'große', 'drin', 'jetzt', 'eine', 'danach', 'solchem', 'mussten', 'doch', 'siebtes', 'niemanden', 'ausserdem', 'etwas', 'davon', 'dementsprechend', 'da', 'hatten', 'dem', 'am', 'jemanden', 'jahren', 'hier', 'er', 'sollen', 'sowie', 'kann', 'tag', 'nie', 'deren', 'auf', 'magst', 'hatte', 'zusammen', 'konnten', 'zehn', 'ganz', 'diesem', 'desselben', 'statt', 'nachdem', 'gab', 'meines', 'seien', 'einigen', 'neunter', 'zehntes', 'weitere', 'im', 'manches', 'würde', 'hin', 'bald', 'als', 'daneben', 'lang', 'kleiner', 'willst', 'sieben', 'mag', 'ach', 'gleich', 'daß', 'deinem', 'selbst', 'gesagt', 'siebente', 'zwei', 'darfst', 'möchte', 'beide', 'dies', 'denselben', 'worden', 'ihn', 'allgemeinen', 'das', 'wie', 'zwanzig', 'sind', 'zeit', 'demzufolge', 'demgemäss', 'groß', 'kleine', 'uhr', 'fünftes', 'gut', 'nicht', 'meinen', 'so', 'nein', 'ihres', 'welcher', 'ihren', 'zweites', 'weniger', 'manchen', 'darf', 'dann', 'einige', 'allem', 'ab', 'ist', 'anderen', 'bekannt', 'möglich', 'werde', 'meiner', 'dabei', 'sein', 'mir', 'dank', 'dein', 'diejenige', 'soll', 'jeden', 'manchem', 'kam', 'jener', 'dafür', 'heißt', 'dieselben', 'beim', 'dich', 'leicht', 'weit', 'solang', 'aller', 'zur', 'über', 'demselben', 'alle', 'ihr', 'ersten', 'viele', 'jene', 'en', 'einen', 'beispiel', 'durfte', 'noch', 'rechten', 'dessen', 'keinen', 'tat', 'ganzes', 'dagegen', 'wessen', 'einander', 'seinem', 'kommen', 'richtig', 'neuntes', 'eigener', 'seinen', 'großen', 'ihrer', 'a', 'darunter', 'darauf', 'ehrlich', 'mittel', 'bin', 'waren', 'was', 'übrigens', 'dort', 'vom', 'wollte', 'darum', 'vierten', 'dritter', 'drittes', 'macht', 'wenige', 'unserer', 'genug', 'einiges', 'neunten', 'bist', 'mochte', 'dahinter', 'ein', 'siebenten', 'unser', 'allerdings', 'daran', 'dritte', 'gerade', 'sehr', 'muß', 'dazu', 'den', 'dieser', 'teil', 'muss', 'erster', 'damit', 'neben', 'neue', 'mich', 'oben', 'sie', 'kannst', 'gewesen', 'keiner', 'könnt', 'keinem', 'nach', 'mehr', 'will', 'musste', 'einiger', 'deiner', 'jedem', 'natürlich', 'eigenes', 'ende', 'schlecht', 'achten', 'werden', 'zweiter', 'jedoch', 'sechste', 'sechster', 'jahre', 'ich', 'tel', 'wann', 'zweite', 'vergangene', 'gutes', 'neuen', 'seines', 'die', 'gekannt', 'wollt', 'offen', 'heisst', 'ins', 'rechtes', 'dadurch', 'satt', 'ihnen', 'solches', 'zehnter', 'kurz', 'grosses', 'von', 'können', 'seiner', 'na', 'niemandem', 'zehnte', 'uns', 'anderem', 'einem', 'solchen', 'hinter', 'währenddem', 'geworden', 'rund', 'jemandem', 'manche', 'einmaleins', 'grossen', 'durften', 'siebter', 'welche', 'siebten', 'diejenigen', 'denen', 'achter', 'müsst', 'weil', 'diesen', 'deswegen', 'kleines', 'sechsten', 'solche', 'ganze', 'müssen', 'nichts', 'ag', 'derjenigen', 'fünfter', 'mochten', 'hätte', 'konnte', 'sondern', 'wahr', 'vielleicht', 'auch', 'sich', 'wollten', 'indem', 'dürfen', 'grosser', 'lieber', 'haben', 'etwa', 'daher', 'daraus', 'darüber', 'eben', 'davor', 'ohne', 'zweiten', 'fünf', 'mancher', 'zuerst', 'wo', 'außerdem', 'jenem', 'sagte', 'man', 'andere', 'neun', 'zurück', 'gemocht', 'welches', 'oder', 'gehabt', 'gewollt', 'heute', 'um', 'geht', 'geschweige', 'niemand', 'dazwischen', 'dermaßen', 'also', 'musst', 'wurden', 'jenen', 'demgemäß', 'keine', 'wer', 'durch', 'tage', 'daselbst', 'deshalb', 'wirklich', 'mein', 'darin', 'vielem', 'viel', 'bis', 'euch', 'vierte', 'entweder', 'vor', 'gedurft', 'ja', 'morgen', 'dritten', 'werdet', 'siebenter', 'du', 'leider', 'irgend', 'seit', 'machen', 'wollen', 'besonders', 'zum', 'ob', 'zwischen', 'warum', 'wart', 'ganzer', 'gegenüber', 'kaum', 'tun', 'andern', 'wäre', 'achtes', 'aber', 'ging', 'einer', 'besten', 'wenig', 'kommt', 'gute', 'weiter', 'und', 'großes', 'vierter', 'erste', 'gemacht', 'mit', 'fünften', 'für', 'wirst', 'kleinen', 'viertes', 'jede', 'meine', 'aus', 'solcher', 'gern', 'diese', 'welchem', 'oft', 'beiden', 'habt', 'sechs', 'zugleich', 'sah', 'bei', 'gross', 'es', 'tagen', 'dass', 'sagt', 'seid', 'wen', 'eigene', 'derjenige', 'neunte', 'ebenso', 'an', 'deine', 'anders', 'wieder', 'welchen', 'gehen'}
