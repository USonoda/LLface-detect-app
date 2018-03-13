# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import detect
import io
from PIL import Image


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
app.config['DEBUG'] = True
# 投稿画像の保存先
UPLOAD_FOLDER = './static/images/tmp'


# ルーティング /にアクセス時
@app.route('/')
def index():
    return render_template('index.html')


# 画像投稿時のアクション
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        if not request.files['file'].filename == u'':
            # 適宜フォルダを削除
            if len(os.listdir(UPLOAD_FOLDER)) > 6:
                for i in range(4):
                    os.remove(os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[i]))

            f = request.files['file']
            img_path = os.path.join(UPLOAD_FOLDER, secure_filename(f.filename))
            # f.save(img_path)
            img = Image.open(f)
            # img_bin = io.BytesIO(img_path)

            f, face_num = detect.detect_face(img)
            f.save(img_path)
            # img_bin = io.BytesIO(img_path)
            # result = [test1.evaluation(img_path), img_path, face_num]  # face_num＞1の時の表示処理をしたい（表を消す）
            # test1.evaluationは上位3人の結果を表示したいだけの目的で作っている

            result = ['', img_path, face_num]  # 最初の要素は（後々の）上位3人の表示用
        else:
            result = []
        return render_template('index.html', result=result)
    else:
        # エラーなどでリダイレクトしたい場合
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
