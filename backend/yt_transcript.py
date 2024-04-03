from youtube_transcript_api import YouTubeTranscriptApi
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data = YouTubeTranscriptApi.get_transcript("kV1ru-Inzl4")

# Merge 'text' values into one coherent text
merged_text = ' '.join(item['text'] for item in data)

# Remove punctuation and convert to lowercase
merged_text = re.sub(r'[^\w\s]', '', merged_text.lower())

# Tokenize the text
tokens = word_tokenize(merged_text)

# Remove stopwords including specified words
stop_words = set(stopwords.words('english'))
additional_stopwords = set(['uh', 'um', 'im', 'em', 'oh', 'uhh', 'umm',
                            'uhm', 'ah', 'hmm', 'huh', 'yeah', 'ok',
                            'okay', 'like', 'well', 'really', 'just',
                            'also', 'yeah', 'right', 'gonna', 'going', 'please'])
stop_words.update(additional_stopwords)
filtered_tokens = [word for word in tokens if word not in stop_words]

# Join the filtered tokens into a coherent text
coherent_text = ' '.join(filtered_tokens)

# Assuming 'coherent_text' is defined as above
text_length = len(coherent_text)
half_length = text_length // 2

# Split the coherent_text into two parts
text_part1 = coherent_text[:half_length]
text_part2 = coherent_text[half_length:]

print(text_part1)
print(text_part2)
