import yt_dlp
from langchain.schema import Document

def load_youtube_content(video_url):
    
    ydl_opts = {
        'quiet': True,           # Don't print progress
        'no_warnings': True,     # No warning messages
        'extract_flat': False    # Get full info
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info
            info = ydl.extract_info(video_url, download=False)
            
            # Extract basic info
            title = info.get('title', 'No Title')
            description = info.get('description', 'No Description')
            
            # Combine title and description
            content = f"Title: {title}\n\nDescription: {description}"
            
            # Create a simple document
            doc = Document(
                page_content=content,
                metadata={'source': video_url, 'title': title}
            )
            
            return [doc]
            
    except Exception as e:
        raise Exception(f"Could not load YouTube video: {str(e)}")