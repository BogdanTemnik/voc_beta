from textblob import TextBlob

d = TextBlob('jacket')

print(d.detect_language())