from newspaper import Article 
from newspaper.article import ArticleException
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer

def text_summarizer(raw_docx):
	parser = PlaintextParser.from_string(raw_docx, Tokenizer("english"))

	# Using Luhn
	summarizer = LuhnSummarizer()

	#Summarize the document with 3 sentences
	summary = summarizer(parser.document, 3);

	sent_list = [i._text for i in summary];	

	return ' '.join(sent_list)

def get_article_summary(url):
	article = Article(url)

	try:
	  article.download()
	except Exception:
	  return ''

	article.parse()
	 
	#Clean unrecognized unicode from article
	article.text = article.text.encode('ascii', 'ignore').decode('utf-8')

	return text_summarizer(article.text)