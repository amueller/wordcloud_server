from flask import Flask, request, render_template, send_from_directory
from wordcloud import WordCloud
import tempfile

app = Flask(__name__)


def display_cloud(raw_text):
    # do some escaping or something, right?
    print(raw_text)
    wc = WordCloud().generate(raw_text)
    fname = tempfile.NamedTemporaryFile(suffix=".png", delete=False, dir=".")
    wc.to_file(fname.name)
    #return "I totally did that thing you asked for: %s" % raw_text
    base_name = fname.name.split("/")[-1]
    print(base_name)
    return send_from_directory(".", base_name)


@app.route('/', methods=['GET', 'POST'])
def word_cloud():
    if request.method == 'POST':
        return display_cloud(request.form['raw_text'])
    else:
        return render_template('input.html')

if __name__ == "__main__":
    app.run(debug=True)
