from youtube_transcript_api import YouTubeTranscriptApi
import re
# import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import json
nltk.download('punkt')
nltk.download('stopwords')

def get_sanized_transscript(video_id):
    print("Getting transcript for video_id \"" + video_id + "\".")
    data = YouTubeTranscriptApi.get_transcript(video_id)

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

    return data


# video_ids=["v6tUWk7vC6g", "uipjCTg_PqQ", "J3euEMWC8tg"]
# output_file_path = "../frontend/src/lib/assets/transcripts.json"

# data = {}
# for video_id in video_ids:
#     data[video_id] = get_sanized_transscript(video_id)

# with open(output_file_path, 'w') as file:
#     json.dump(data, file, indent=4)
# print("Transcripts saved to \"" + output_file_path + "\".")