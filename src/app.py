# from crypt import methods
# from requests import request
import re
from flask import Flask, render_template,request,send_file
from scraper import get_url_content, download_file
import shutil

app = Flask(__name__)



from zipfile import ZipFile
import os
from os.path import basename
# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
   # create a ZipFile object
   with ZipFile(zipFileName, 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
               if filter(filename):
                   # create complete filepath of file in directory
                   filePath = os.path.join(folderName, filename)
                   # Add file to zip
                   zipObj.write(filePath, basename(filePath))

@app.route('/')
def index():
    # url = input("Enter full URL:")
    # html = get_url_content(url)
    # download_file(soup=html)
    return render_template('index.html')

@app.route('/handle_data',methods=['POST','GET'])
def handle_data():
    if request.method =='POST':
        if os.path.exists('content_text.zip'):
          os.remove('content_text.zip')
        list_of_path = []
        url = request.form['url']
        if url:
          if os.path.exists('temp'):
            shutil.rmtree('temp')
            os.mkdir('temp')
          else:
            os.mkdir('temp')
          for item in url.split(','):

            html = get_url_content(item)
            file_name = download_file(soup=html)
            # print(file_name)
            path = f"temp/{file_name}.txt"
            list_of_path.append(path)
            # return send_file(path, as_attachment=True)

        with ZipFile('content_text.zip', 'w') as zipObj:
          # Iterate over all the files in directory
          # for folderName, subfolders, filenames in os.walk(dirName):
          for filename in list_of_path:
            # if filter(filename):
              # create complete filepath of file in directory
              # filePath = os.path.join(folderName, filename)
              # Add file to zip
              zipObj.write(filename, basename(filename))
          path = '../src/content_text.zip'
          shutil.rmtree('temp')
          zipObj.close()
          return send_file(path, as_attachment=True)

    return render_template('index.html')


import os



if __name__ == '__main__':
    app.run()
