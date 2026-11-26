from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat.",
    "A kitten is resting on a rug.",
    "Stock markets fell sharply today.",
]
query = "Where is the cat sitting?"

scores = util.cos_sim(model.encode(query), model.encode(sentences))[0]
for s, score in zip(sentences, scores):
    print(f"{score:.3f}  {s}")