from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def data_loader(url):

    loader = UnstructuredURLLoader(
                                urls = [url], 
                                ssl_verify = False,
                                headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})           
    docs = loader.load()

    text_splitter =  RecursiveCharacterTextSplitter(chunk_size = 1500, chunk_overlap = 200)
    chunks = text_splitter.split_documents(docs)

    
    return chunks
        
    







