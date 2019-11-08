from flask import Flask, render_template, jsonify, request
from summarization import text_summarizer, get_article_summary
from misc import calculate_from
from newsAPI import newsAPI_content, newsAPI_content_everything

app = Flask(__name__)

@app.route('/') 
def hello_world():
    print("In flask app")
    return render_template("index.html")

@app.route('/search_form', methods=['POST'])
def search_summary():
    content = ''
    search_terms = {}
    _q = request.form['search-query']
    if(_q):
        search_terms['q'] = _q.strip().replace(' ', '+')

    _from, _to = calculate_from(request.form['search-time'])
    if(_from and _to):
        search_terms['from'] = _from
        search_terms['to'] = _to

    _category = request.form['search-category']
    if(_category):
        search_terms['category'] = _category

    _sortBy = request.form['search-sort']    
    if(_sortBy):
        search_terms['sortBy'] = _sortBy
    (results, sources, url, title) = newsAPI_content(search_terms)

    if(url!=[]):
        for i in url:            
            content = content + get_article_summary(i)
    else:
        (results, sources, url, title) = newsAPI_content_everything({'q':search_terms['q']})        
        if(url!=[]):
            for i in url:            
                content = content + get_article_summary(i)             

    return jsonify( (   (text_summarizer(content), [sources, url, title]), ("No news found for this search query, try different search terms", [sources, url, title]) )[len(content)==0]  )
    
    


@app.route('/link_form', methods=['POST'])
def link_summary():
    content = '';
    for i in range(0, len(request.form)):
        url = request.form['link-text-' + str(i)]
        content = content + get_article_summary(url)

    return jsonify(text_summarizer(content))

@app.route('/clipboard_form', methods=['POST'])
def clipboard_summary():
    content = '';    
    for i in range(0, len(request.form)):
        content = content + text_summarizer(request.form['clipboard-text-' + str(i)])
    summary =  text_summarizer(content)
    
    return jsonify(summary)
