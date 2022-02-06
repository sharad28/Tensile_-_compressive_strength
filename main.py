import pandas as pd
from wsgiref import simple_server
from flask import Flask, request, render_template
# from flask import Response
import os
from flask_cors import CORS, cross_origin
# from src.trainingmodel import trainModel
import flask_monitoringdashboard as dashboard
from src.PredictFromModel import prediction
from src.utils.logg import logging
# import json
# import pickle

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/", methods=['GET',"POST"])
@cross_origin()
def home():
    """
    Home page for prediction of strength
    :return: index.html
    """
    try:
        logging.info('The Home Method Call The index.html Page')
        return render_template('index.html')
    except Exception as e:
        logging.info('INFO', 'Something Went Wrong With The Home Method')
        raise Exception()

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    """
    This Method will return the predicted strength of concrete in tension & compression
    :return: Tensile and compressive strength
    """
    try:
        logging.info('Checking The Method Is Post Or Not')
        if request.method == "POST":
            try:
                logging.info("The Post Method Is Call & Calling The Each Feature")

                Compressive_strength_cementfce= float(request.form['Comp_strength_cement'])
                Tensile_strenth_cement = float(request.form['Tensile_strenth_cement'])
                Curing_time = int(request.form['Curing_time'])
                Crushed_stone_size = float(request.form['Crushed_stone_size'])
                Stone_powder_content = float(request.form['Stone_powder_content'])
                Fineness_modulus = float(request.form['Fineness_modulus'])
                Water_binder_ratio = float(request.form['Water_binder_ratio'])
                Water_cement_ratio = float(request.form['Water_cement_ratio'])
                Water = float(request.form['Water'])
                Sand_ratio = float(request.form['Sand_ratio'])

                user_input_data = pd.DataFrame([['Compressive strength of cementfce(MPa)', 'Tensile strength of cementfct(MPa)', 'Curing age (day)', 'Dmax of Crushed stone(mm)', 'Stone powder content in Sand (%)',
                                                 'Fineness modulus of sand ', 'W/B', 'Water to cement ratio mw/mc', 'Water(kg/m3)', 'Sand ratio(%)'],
                                                [Compressive_strength_cementfce,Tensile_strenth_cement,Curing_time,Crushed_stone_size,
                                    Stone_powder_content,Fineness_modulus,Water_binder_ratio,Water_cement_ratio,Water,Sand_ratio]])
                new_header = user_input_data.iloc[0]  # grab the first row for the header
                user_input_data = user_input_data[1:]  # take the data less the header row
                user_input_data.columns = new_header
                #converting dataframe dtype to float as its will cause error in case of object
                user_input_data = user_input_data.astype(float)
                obj_pred = prediction()
                model_comp, model_tensile = obj_pred.predictionFromModel()
                predict_compressive = model_comp.predict(user_input_data)

                predict_tensile = model_tensile.predict(user_input_data)

                return render_template("result.html",
                                       compressive_prediction_text=f"The Uniaxial compressive strength: {predict_compressive}",
                                       tensile_prediction_text = f"The splitting tensile strength: {predict_tensile}")
            except Exception as e:
                logging.exception("Something Went Wrong With The Post From Predict Method")
                raise Exception(f"Exeption is raised in prediction \n{e}")

            else:
                logging.info('The Post Method Is Not Selected')
                return render_template('index.html')

    except Exception as e:
        logging.exception("Something Went Wrong With The Post From Predict Method")
        raise Exception(f"Exeption is raised in prediction \n{e}")

@app.route("/report", methods=['GET', 'POST'])
@cross_origin()
def report():
    """
    :Method_Name: report
    :DESC: This Will Return The  Data Report Page
    :param: None
    :return: report.html
    """

    try:
        logging.info('INFO', 'The Home Method Call The index.html Page')
        return render_template('Tensile_and_compressive_strength_data_from_various_paper.html')

    except Exception as e:
        logging.info('INFO', 'Something Went Wrong With The Home Method')
        raise Exception(f'(Home)- Something Went Wrong With The Method \n' + str(e))


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
