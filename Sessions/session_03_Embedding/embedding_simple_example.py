from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence_1 = "I love  AI"
sentence_2 = "I enjoy artificial intelligence"

e1 = model.encode([sentence_1])
e2 = model.encode([sentence_2])

similarity = cosine_similarity(e1, e2)

print(f"Similarity between '{sentence_1}' and '{sentence_2}': {similarity[0][0]:.4f}")