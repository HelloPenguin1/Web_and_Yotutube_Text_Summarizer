from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader



def data_loader(url):
    if "youtube.com" in url:
        loader = YoutubeLoader.from_youtube_url(url,add_video_info = True)
    else:
        loader = UnstructuredURLLoader(urls = [url], ssl_verify = False,
                                    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    
    docs = loader.load()

    return docs
        
    







