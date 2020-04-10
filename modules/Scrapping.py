from newspaper import Article

def get_Article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
    except:
        print('url not found')
    return article.text



