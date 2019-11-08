from datetime import date, datetime, timedelta


def calculate_from(n):
	end = date.isoformat(date.today())
	end = datetime.strptime(end, "%Y-%m-%d")
	
	if(n=='d'):
		days = 1
	elif(n=='m'):
		days = 30
	elif(n=='y'):
		days = 365
	elif(n=='D'):
		days = 3650
	else:
		days = 7	

	start = end - timedelta(days=days)
	return date.strftime(start, "%Y-%m-%d"), date.strftime(end, "%Y-%m-%d")

def match_article_query(query_terms, keywords):	
	matches_left = len(query_terms)
	keywords = keywords.lower()

	for i in query_terms:
		if(keywords.find(i)!=-1):
			matches_left-=1

	if(matches_left==0):
		return True

	return False
