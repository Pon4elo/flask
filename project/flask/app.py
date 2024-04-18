from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = [
    {'id': 1, 'name': 'Пример 1'},
    {'id': 2, 'name': 'Пример 2'},
    {'id': 3, 'name': 'Пример 3'}
]

company_name = "Компания ООО «Xsoft»"

@app.route('/')
def index():
    return render_template('index.html', data=data, company_name=company_name)

@app.route('/add', methods=['POST'])
def add_data():
    if request.method == 'POST':
        new_name = request.form['name']
        new_id = len(data) + 1
        data.append({'id': new_id, 'name': new_name})
        return redirect('/')
    else:
        return 'Ошибка'

@app.route('/delete/<int:id>', methods=['POST'])
def delete_data(id):
    for item in data:
        if item['id'] == id:
            data.remove(item)
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0')
