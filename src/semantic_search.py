

from sentence_transformers import SentenceTransformer, util
import torch
import pandas  as pd 
embedder = SentenceTransformer('all-MiniLM-L6-v2')
def semmantic(faqslist,user_message):
    for i in range(0,len(faqslist)):

        question = pd.read_csv(faqslist[i])['Question'].tolist()
        answer = pd.read_csv(faqslist[i])['Answer'].tolist()
        

    corpus = answer
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    queries = [user_message]


# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    top_k = min(1, len(corpus))
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)

    # We use cosine-similarity and torch.topk to find the highest 5 scores
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=top_k)

  
    # print("Query:", query)
  

    for score, idx in zip(top_results[0], top_results[1]):
        print(corpus[idx])
        return corpus[idx]
