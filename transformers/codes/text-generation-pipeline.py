from transformers import pipeline

generator = pipeline("text-generation")

print(generator("The quick brown fox ", num_return_sequences=2, max_length=15))
