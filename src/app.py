# from crypt import methods
# from requests import request
import re
from flask import Flask, render_template,request,send_file
from scraper import get_url_content, download_file

app = Flask(__name__)

@app.route('/')
def index():
    # url = input("Enter full URL:")
    # html = get_url_content(url)
    # download_file(soup=html)
    return render_template('index.html')

@app.route('/handle_data',methods=['POST','GET'])
def handle_data():
    if request.method =='POST':
        url = request.form.get("url")
        if url:
            html = get_url_content(url)
            file_name = download_file(soup=html)
            # print(file_name)
            path = f"../src/{file_name}.txt"
            return send_file(path, as_attachment=True)
    return render_template('index.html')


import os



if __name__ == '__main__':
    app.run()