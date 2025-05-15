import os
import fitz
from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
from werkzeug.utils import secure_filename
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

app.config['Upload_folder'] = 'Uploads'
os.makedirs(app.config['Upload_folder'], exist_ok=True)

model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_text_from_PDF(PDF_path):
    text = ""

    with fitz.open(PDF_path) as doc:
        for page in doc:
            text = text + page.get_text()

        return text.strip()


def cosine_simil(CV_text, job_description):
    emeddings = model.encode(CV_text, job_description)
    similarity = cosine_similarity([emeddings[0], emeddings[1]])

    return round(similarity[0][0] * 100, 2)


# fetch from front end
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if "CV" not in request.file:
            return "No file was uploaded.", 400

        file = request.files(['CV'])
        job_description = request.form['job_description']

        if file.filename == "" or job_description == "":
            return "Invalid input.", 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['Upload_folder'], filename)
        file.save(filepath)

        CV_text = extract_text_from_PDF(filepath)

        score = cosine_simil(CV_text=CV_text, job_description=job_description)

        return render_template('index.html', score=score)
    return render_template('index.html', score=None)

if __name__ == "__main__":
    app.run(debug=True)