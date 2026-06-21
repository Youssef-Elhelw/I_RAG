def fixed_size_chunking(text, chunk_size=512, overlap=0):
    """
    Splits the input text into fixed-size chunks with optional overlap.
    
    Parameters:
    - text (str): The input text to be chunked.
    - chunk_size (int): The size of each chunk in characters.
    - overlap (int): The number of characters to overlap between chunks.
    
    Returns:
    - List[str]: A list of text chunks.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    if overlap < 0:
        raise ValueError("Overlap must be a non-negative integer.")
    
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    
    return chunks


# ======================================================================================================

# using langchain's text splitter for fixed size chunking
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

def fixed_size_chunking_with_langchain(text, chunk_size=512, overlap=0):
    text_splitter = CharacterTextSplitter(
        separator=" ", # this is a separator for splitting text, you can change it to any character or string that you want to use as a separator
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len # here we are using the built-in len function to calculate the length of the text, but you can also use a custom function if you want to calculate the length in a different way
    )

    chunks =text_splitter.split_text(text)
    print(f"Number of chunks created: {len(chunks)}")

    documents = [Document(page_content=chunk) for chunk in chunks]
    return documents


if __name__ == "__main__":
    print("Demonstrating fixed-size chunking with overlap using the custom function:")
    sample_text = "This is a sample text to demonstrate fixed-size chunking. " * 10  # Repeat to increase length
    chunk_size = 50
    overlap = 1
    
    chunks = fixed_size_chunking(sample_text, chunk_size, overlap)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")

    print("Demonstrating fixed-size chunking with overlap using LangChain's text splitter:")
    sample_text="This is a sample text to demonstrate fixed-size chunking using LangChain. " * 10 
    langchain_chunks = fixed_size_chunking_with_langchain(sample_text, chunk_size=10, overlap=1)
    for i, doc in enumerate(langchain_chunks):
        print(f"Document {i+1}:\n{doc.page_content}\n")