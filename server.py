from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        data = {'Name': [name], 'Email': [email], 'Phone': [phone]}
        df = pd.DataFrame(data)

        # Save DataFrame to an Excel file
        file_path = r'D:\OneDrive - Adani\D Drive\Work To Do\Insurance\Transit Insurance\{}.xlsx'.format(name)
        df.to_excel(file_path, index=False)

        return 'Data submitted successfully!'

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
