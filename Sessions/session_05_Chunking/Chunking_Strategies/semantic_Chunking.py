# Note this code is AI generated

import re
import nltk
from nltk.tokenize import sent_tokenize
from typing import List
import numpy as np

nltk.download('punkt')


# ============================================================================
# APPROACH 1: Sentence-Based Chunking (Simple)
# ============================================================================
def simple_sentence_chunking(text: str, sentences_per_chunk: int = 3) -> List[str]:
    """
    Basic semantic chunking: group sentences together
    
    Args:
        text: Input document text
        sentences_per_chunk: Number of sentences per chunk
    
    Returns:
        List of text chunks
    """
    sentences = sent_tokenize(text)
    chunks = []
    
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = ' '.join(sentences[i:i + sentences_per_chunk])
        chunks.append(chunk)
    
    return chunks


# ============================================================================
# APPROACH 2: Paragraph-Based Chunking (Common)
# ============================================================================
def paragraph_based_chunking(text: str) -> List[str]:
    """
    Split by paragraphs (logical divisions in text)
    
    Args:
        text: Input document text
    
    Returns:
        List of paragraph chunks
    """
    # Split by double newlines (standard paragraph separator)
    paragraphs = text.split('\n\n')
    
    # Clean up whitespace
    chunks = [p.strip() for p in paragraphs if p.strip()]
    
    return chunks


# ============================================================================
# APPROACH 3: Semantic Similarity-Based Chunking
# ============================================================================
class SemanticChunker:
    """
    Advanced semantic chunking using sentence embeddings and similarity.
    Requires: pip install sentence-transformers
    """
    
    def __init__(self, threshold: float = 0.5):
        """
        Initialize with similarity threshold
        
        Args:
            threshold: Similarity threshold for grouping sentences (0-1)
                      Higher = stricter boundaries
        """
        self.threshold = threshold
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except ImportError:
            print("Install sentence-transformers: pip install sentence-transformers")
            self.model = None
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors"""
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    def chunk(self, text: str) -> List[str]:
        """
        Chunk text based on semantic similarity between sentences
        
        Args:
            text: Input document text
        
        Returns:
            List of semantically coherent chunks
        """
        if self.model is None:
            return simple_sentence_chunking(text)
        
        sentences = sent_tokenize(text)
        
        if len(sentences) <= 1:
            return sentences
        
        # Get embeddings for all sentences
        embeddings = self.model.encode(sentences)
        
        chunks = []
        current_chunk = [sentences[0]]
        
        for i in range(1, len(sentences)):
            # Calculate similarity with previous sentence
            similarity = self._cosine_similarity(
                embeddings[i-1], 
                embeddings[i]
            )
            
            # If similarity is above threshold, add to current chunk
            if similarity >= self.threshold:
                current_chunk.append(sentences[i])
            else:
                # Start new chunk (boundary detected)
                chunks.append(' '.join(current_chunk))
                current_chunk = [sentences[i]]
        
        # Add remaining sentences
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks


# ============================================================================
# APPROACH 4: Recursive Chunking (Content-Aware)
# ============================================================================
def recursive_semantic_chunking(
    text: str,
    max_chunk_size: int = 500,
    separators: List[str] = None
) -> List[str]:
    """
    Recursively split text by meaningful separators.
    Tries separators in order until chunks fit max_chunk_size.
    
    Args:
        text: Input document text
        max_chunk_size: Maximum characters per chunk
        separators: List of separators to try in order
                   (use from coarse to fine)
    
    Returns:
        List of text chunks
    """
    if separators is None:
        # Order from coarse to fine granularity
        separators = ["\n\n", "\n", "(?<=[.!?])\s+", " "]
    
    def _recursive_split(text: str, separators: List[str]) -> List[str]:
        chunks = []
        
        # If text fits, return as is
        if len(text) <= max_chunk_size:
            return [text] if text.strip() else []
        
        # Try each separator in order
        for separator in separators:
            # Split by separator
            if separator == " ":
                parts = text.split(separator)
            else:
                parts = re.split(separator, text)
            
            # If we got multiple parts, recursively process them
            if len(parts) > 1:
                good_chunks = []
                current = ""
                
                for part in parts:
                    if len(current) + len(part) + 1 <= max_chunk_size:
                        current += part + separator if separator != " " else part + " "
                    else:
                        if current:
                            good_chunks.append(current.strip())
                        current = part
                
                if current:
                    good_chunks.append(current.strip())
                
                # Recursively split any oversized chunks
                for chunk in good_chunks:
                    if len(chunk) > max_chunk_size:
                        chunks.extend(_recursive_split(chunk, separators[separators.index(separator) + 1:]))
                    elif chunk.strip():
                        chunks.append(chunk)
                
                return chunks
        
        return [text]
    
    return _recursive_split(text, separators)


# ============================================================================
# APPROACH 5: Topic-Based Chunking (Using Markers)
# ============================================================================
def topic_based_chunking(text: str) -> List[str]:
    """
    Split by topic markers (headers, keywords)
    
    Args:
        text: Input document text
    
    Returns:
        List of topic-based chunks
    """
    # Patterns for headers and topic markers
    header_pattern = r'^#+\s+.+$|^[A-Z][A-Z\s]+:$|^[A-Z][A-Za-z\s]+\n-{5,}$'
    
    lines = text.split('\n')
    chunks = []
    current_chunk = []
    
    for line in lines:
        # Check if line is a header
        if re.match(header_pattern, line.strip()):
            # Save previous chunk if exists
            if current_chunk:
                chunks.append('\n'.join(current_chunk).strip())
            # Start new chunk with header
            current_chunk = [line]
        else:
            current_chunk.append(line)
    
    # Add final chunk
    if current_chunk:
        chunks.append('\n'.join(current_chunk).strip())
    
    return [c for c in chunks if c]  # Remove empty chunks


# ============================================================================
# DEMONSTRATION
# ============================================================================
if __name__ == "__main__":
    # Sample document
    sample_text = """
    Semantic chunking is a technique for dividing documents intelligently. 
    It considers the meaning and structure of content rather than arbitrary boundaries.
    
    The first advantage is context preservation. When you chunk semantically, 
    you maintain the relationship between ideas. This prevents losing important connections.
    
    Another benefit is improved relevance. Chunks are more likely to match user queries 
    because they represent complete concepts. This improves retrieval accuracy.
    
    However, semantic chunking has some trade-offs. It's more complex to implement 
    than simple size-based chunking. You may need NLP tools and extra processing time.
    
    When should you use this approach? Use it for structured documents like articles and reports.
    It's especially valuable when retrieval quality matters more than speed.
    """
    
    print("=" * 70)
    print("1. SIMPLE SENTENCE CHUNKING (3 sentences per chunk)")
    print("=" * 70)
    simple_chunks = simple_sentence_chunking(sample_text, sentences_per_chunk=3)
    for i, chunk in enumerate(simple_chunks, 1):
        print(f"\nChunk {i}:")
        print(f"  {chunk[:100]}..." if len(chunk) > 100 else f"  {chunk}")
    
    print("\n" + "=" * 70)
    print("2. PARAGRAPH-BASED CHUNKING")
    print("=" * 70)
    para_chunks = paragraph_based_chunking(sample_text)
    for i, chunk in enumerate(para_chunks, 1):
        print(f"\nChunk {i}:")
        print(f"  {chunk[:100]}..." if len(chunk) > 100 else f"  {chunk}")
    
    print("\n" + "=" * 70)
    print("3. RECURSIVE CHUNKING (max 300 chars)")
    print("=" * 70)
    recursive_chunks = recursive_semantic_chunking(sample_text, max_chunk_size=300)
    for i, chunk in enumerate(recursive_chunks, 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(f"  {chunk[:100]}..." if len(chunk) > 100 else f"  {chunk}")
    
    print("\n" + "=" * 70)
    print("4. SEMANTIC SIMILARITY-BASED CHUNKING")
    print("=" * 70)
    print("(Requires: pip install sentence-transformers)")
    print("Uncomment to test with embeddings")
    chunker = SemanticChunker(threshold=0.5)
    semantic_chunks = chunker.chunk(sample_text)
    for i, chunk in enumerate(semantic_chunks, 1):
        print(f"\nChunk {i}:")
        print(f"  {chunk[:100]}..." if len(chunk) > 100 else f"  {chunk}")
    
    print("\n" + "=" * 70)
    print("5. TOPIC-BASED CHUNKING")
    print("=" * 70)
    topic_chunks = topic_based_chunking(sample_text)
    for i, chunk in enumerate(topic_chunks, 1):
        print(f"\nChunk {i}:")
        print(f"  {chunk[:100]}..." if len(chunk) > 100 else f"  {chunk}")