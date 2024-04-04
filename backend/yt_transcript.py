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
    additional_stopwords = set(['uh', 'um', 'im', 'em',
                                'oh', 'uhh', 'umm', 'uhm',
                                'ah', 'hmm', 'huh', 'yeah',
                                'ok', 'okay', 'like', 'well',
                                'really', 'just', 'also', 'yeah',
                                'right', 'gonna'])
    stop_words.update(additional_stopwords)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    coherent_text = ' '.join(filtered_tokens)
    item['text'] = coherent_text

# Add introductory text
intro_text = "Please take a look at the following data:"

# Prompt 1: Introduction
prompt1 = intro_text

# Prompt 2: Data
prompt2 = " ".join(item['text'] for item in data)

# Prompt 3: Extract text containing "Martin Luther"
prompt3 = "Extract timestamp and text that includes \"Martin Luther\""

# Define all prompts in a dictionary
prompts = {
    "prompt1": prompt1,
    "prompt2": prompt2,
    "prompt3": prompt3
}

# Set your OpenAI API key
openai.api_key = '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'

# Run a loop over the prompts and print responses
for prompt_key, prompt_value in prompts.items():
    print(f"Prompt: {prompt_key}")
    print(f"{prompt_value}\n")

    # Call the OpenAI API with the prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_value}
        ]
    )

"""
# Define the file path
output_file_path = "transcript-" + videoId + ".json"  # You can change the file name and extension as needed

with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=4)
print("Transcript saved to \"" + output_file_path + "\".")
"""