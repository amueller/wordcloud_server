from flask import Flask, request, render_template
from wordcloud import WordCloud
import tempfile

app = Flask(__name__)


def display_cloud(raw_text):
    # do some escaping or something, right?
    print(raw_text)
    wc = WordCloud().generate(raw_text)
    fname = tempfile.NamedTemporaryFile(suffix=".png", delete=False, dir="static")
    print(fname.name)
    wc.to_file(fname.name)
    #return "I totally did that thing you asked for: %s" % raw_text
    base_name = "static/" + fname.name.split("/")[-1]
    print(base_name)
    return render_template('show_cloud.html', image=base_name)


@app.route('/', methods=['GET', 'POST'])
def word_cloud():
    if request.method == 'POST':
        return display_cloud(request.form['raw_text'])
    else:
        return render_template('input.html')

if __name__ == "__main__":
    app.run(debug=True)
