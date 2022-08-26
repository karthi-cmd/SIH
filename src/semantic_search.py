import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# embedder = SentenceTransformer('all-MiniLM-L6-v2')

# def semmantic(faqslist,user_message):
    
#     answer = pd.read_csv('src/data/Working/Greetings.csv')['Answer'].tolist()
        
#     corpus_embeddings = embedder.encode(answer, convert_to_tensor=True)
#     top_k = min(1, len(answer))
#     for query in user_message:
#         query_embedding = embedder.encode(query, convert_to_tensor=True)

#     # We use cosine-similarity and torch.topk to find the highest 5 scores
#         cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
#         top_results = torch.topk(cos_scores, k=top_k)
#         print("Query:", query)
  

#         for score, idx in zip(top_results[0], top_results[1]):
#             print(answer[idx])
            


# faqslist = ['src/data/Working/Greetings.csv']
# user_message = "hi"
# semmantic(faqslist,user_message)


from sentence_transformers import SentenceTransformer, util
import torch
import pandas  as pd 
embedder = SentenceTransformer('all-MiniLM-L6-v2')
def semmantic(faqslist,user_message):
    for i in range(0,len(faqslist)):
        # print(pd.read_csv(faqslist[i]))
        question = pd.read_csv(faqslist[i])['Question'].tolist()
        answer = pd.read_csv(faqslist[i])['Answer'].tolist()
        
    # answer = pd.read_csv('src/data/Working/Greetings.csv')['Answer'].tolist()
# print(answer)
# Corpus with example sentences
    corpus = answer
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
    #print(corpus)
    
# Query sentences:
    queries = [user_message]


# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    top_k = min(1, len(corpus))
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)

    # We use cosine-similarity and torch.topk to find the highest 5 scores
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=top_k)

  
    print("Query:", query)
  

    for score, idx in zip(top_results[0], top_results[1]):
        print(corpus[idx])
        return corpus[idx]
