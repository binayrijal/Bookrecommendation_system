from flask import  Flask,render_template,request
import pickle
import pandas as pd
import numpy as np


popular_df=pickle.load(open('allbook.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('book.pkl','rb'))
similar_score=pickle.load(open('similar.pkl','rb'))


app=Flask(__name__)


@app.route('/')

def index():
    return render_template('home.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author= list(popular_df['Book-Author'].values),
                           image= list(popular_df['Image-URL-M'].values),
                           num_rating= list(popular_df['num-rating'].values),
                           avg_rating= list(popular_df['avg-rating'].values)

                         )
@app.route('/recom')
def recom():
    return  render_template('recom.html')
@app.route('/recommendation',methods=['POST'])
def recommendation():
    if request.method=="POST":
        text=request.form.get('text')
        index_no = np.where(pt.index == text)[0][0]
        similar_book = sorted(list(enumerate(similar_score[index_no])), key=lambda x: x[1], reverse=True)[1:6]
        data = []
        for i in similar_book:
            item = []
            temp = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)
        return render_template('recom.html',
                               data=data

                               )


if __name__ == '__main__':
    app.run(debug=True)