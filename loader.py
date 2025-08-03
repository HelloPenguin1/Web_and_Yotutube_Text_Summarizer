from langchain_community.document_loaders import  UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from unstructured.partition.auto import partition
from langchain.schema import Document



def data_loader(url):

    try:
        elements = partition(url=url,
                            ssl_verify=False,
                            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"},
                            strategy="hi-res",
                            include_page_breaks = False)
        
        text_parts = []
        for element in elements:
            element_text = str(element).strip()
            if len(element_text > 10):
                text_parts.append(element_text)

        full_text = "\n\n".join(text_parts)
        
        if not full_text.strip():
            raise Exception("No content extracted with partition")
        
        #create a document
        doc = Document(
            page_content=full_text,
            metadata ={
                'source':url,
                'extraction_method': 'unstructured_partition_url'
            }
        )

        text_splitter =  RecursiveCharacterTextSplitter(chunk_size = 1500, chunk_overlap = 200)
        chunks = text_splitter.split_documents([doc])

        return chunks
    
    
    except Exception as e:

        print(f"Unstructured partition method failed : {e}. Using fallback with UnstructuredURLLoader")
        loader = UnstructuredURLLoader(
                                    urls = [url], 
                                    ssl_verify = False,
                                    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})           
        docs = loader.load()

        text_splitter =  RecursiveCharacterTextSplitter(chunk_size = 1500, chunk_overlap = 200)
        chunks = text_splitter.split_documents(docs)

        
        return chunks
        
    







