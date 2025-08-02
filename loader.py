from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from youtube_loader import load_youtube_content


def data_loader(url):

    if "youtube.com" in url or "youtu.be" in url:
        docs =load_youtube_content(url)
        return docs
    else:
        loader = UnstructuredURLLoader(urls = [url], 
                                       ssl_verify = False,
                                    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    
        docs = loader.load()
        return docs
        
    







