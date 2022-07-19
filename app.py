from distutils.log import debug
from flask import Flask
from censusip.logger import logging
app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)