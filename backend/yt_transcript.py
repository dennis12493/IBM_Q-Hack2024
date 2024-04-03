from youtube_transcript_api import YouTubeTranscriptApi
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample yt video
data = YouTubeTranscriptApi.get_transcript("kV1ru-Inzl4")

# Remove punctuation and convert to lowercase for each 'text' key
for item in data:
    text = item['text']
    text = re.sub(r'[^\w\s]', '', text.lower())
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    additional_stopwords = set(['uh', 'um', 'im', 'em', 'oh', 'uhh', 'umm', 'uhm', 'ah', 'hmm', 'huh', 'yeah', 'ok', 'okay', 'like', 'well', 'really', 'just', 'also', 'yeah', 'right', 'gonna'])
    stop_words.update(additional_stopwords)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    coherent_text = ' '.join(filtered_tokens)
    item['text'] = coherent_text