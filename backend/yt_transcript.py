from youtube_transcript_api import YouTubeTranscriptApi
import re
# import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import openai

# nltk.download('punkt')
# nltk.download('stopwords')

# Sample yt video
videoId="NiKtZgImdlY"

data = YouTubeTranscriptApi.get_transcript(videoId)

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
# Set your OpenAI API key
openai.api_key = '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'

# Extract text and timestamps from data
openai_input = [{'text': item['text'], 'start': item['start']} for item in data]

# Define your prompt
prompt = "Please take a look at the following data:"

# Call the OpenAI API with the structured data
response = openai.Completion.create(
    engine="davinci-002",
    prompt=prompt,
    examples_context=openai_input,
    max_tokens=100
)

# Retrieve and print the response
for choice in response.choices:
    print(choice.text.strip())
"""
# Define the file path
output_file_path = "transcript-" + videoId + ".json"  # You can change the file name and extension as needed

with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=4)
print("Transcript saved to \"" + output_file_path + "\".")
"""