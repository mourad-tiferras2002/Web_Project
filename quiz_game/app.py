from flask import Flask, render_template, request, redirect, url_for
from quiz_data import questions

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def enumerate_function(sequence):
        return enumerate(sequence)
    return dict(enumerate=enumerate_function)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form.to_dict()
        score = 0
        for i, question in enumerate(questions):
            if user_answers.get(f'question{i}') == question['answer']:
                score += 1
        return redirect(url_for('result', score=score))

    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = request.args.get('score', type=int)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
