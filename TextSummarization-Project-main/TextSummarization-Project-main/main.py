from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import nltk
import re
import pandas as pd

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Function to fetch Wikipedia content
def get_wiki_content(url):
    try:
        req_obj = requests.get(url)
        text = req_obj.text
        soup = BeautifulSoup(text, 'html.parser')
        all_paras = soup.find_all('p')
        wiki_text = ''
        for para in all_paras:
            wiki_text += para.text
        # Remove bracketed content like "[52]" using regex
        wiki_text = re.sub(r'\[\d+\]', '', wiki_text)
        return wiki_text
    except Exception as e:
        return f"Error fetching content: {str(e)}"

# Function to find top 10 sentences
def top10_sentences(url):
    try:
        required_text = get_wiki_content(url)
        stop_words = nltk.corpus.stopwords.words('english')
        sentences = nltk.sent_tokenize(required_text)
        words = nltk.word_tokenize(required_text)
        word_frequencies = {}
        for word in words:
            if word.lower() not in stop_words:  # Ensure lowercase comparison
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        max_word_freq = max(word_frequencies.values())
        for key in word_frequencies.keys():
            word_frequencies[key] /= max_word_freq
        sentences_scores = []
        for sent in sentences:
            curr_words = nltk.word_tokenize(sent)
            curr_score = 0
            for word in curr_words:
                if word in word_frequencies.keys():
                    curr_score += word_frequencies[word]
            sentences_scores.append(curr_score)
        sentences_data = pd.DataFrame({"sent": sentences, "score": sentences_scores})
        sorted_data = sentences_data.sort_values(by="score", ascending=False).reset_index()
        top10rows = sorted_data.iloc[:10, :]  # Top 10 rows
        return "\n".join(list(top10rows["sent"]))  # Join sentences for display
    except Exception as e:
        return f"Error processing text: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            top_sentences = top10_sentences(url)
            return f"<pre>{top_sentences}</pre>"  # Display as preformatted text
        else:
            return "Invalid URL. Please enter a valid Wikipedia URL."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
