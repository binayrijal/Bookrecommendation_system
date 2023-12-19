from flask import  Flask,render_template
import pickle
import pandas as pd


popular_df=pickle.load(open('allbook.pkl','rb'))


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

if __name__ == '__main__':
    app.run(debug=True)