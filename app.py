from flask import Flask
import sys
from Housing.logger import logging
from Housing.exception import HousingException
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception ("We are tetsting custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    logging.info("We are testing logging")
    return "Starting Machine learning Project"

if __name__=="__main__":
    
    app.run(debug=True)