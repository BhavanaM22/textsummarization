# Text Summarization Project

This project aims to summarize text content provided through a URL, using Natural Language Processing techniques.

## Features

- Accepts a URL as input.
- Retrieves text content from the provided URL.
- Applies text summarization algorithms to generate a concise summary.
- Displays the summarized text to the user.

## Technologies Used

- Python (Flask) for the backend.
- HTML, CSS, and JavaScript for the frontend.
- Natural Language Toolkit (NLTK) for text processing.

## Setup Instructions

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:
- pip install flask requests beautifulsoup4 nltk pandas

Note: NLTK requires additional downloads. Run the following commands in your Python environment:
import nltk
nltk.download('punkt')
nltk.download('stopwords')


3. Run the Flask application:
- python main.py


4. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Enter a valid URL containing text content into the input field.
2. Click the "Summarize" button.
3. View the summarized text displayed on the same page.

## Contributors

- Nidha Ahmed Mohammad [link-to-github-profile](https://github.com/nidhaahmed)

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

