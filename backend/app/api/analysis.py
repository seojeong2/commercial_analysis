import os
from flask import request, Blueprint, jsonify, abort
import pandas as pd

from sqlalchemy import create_engine

analysis = Blueprint('analysis', __name__, url_prefix="/api")

db_connection = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))
conn = db_connection.connect()

@analysis.route("/result", methods=["GET"])
def get_analysis_result():
    '''
    #
    #
    #
    '''
    region = request.args.get("region")
    category = request.args.get("category")

    if region and category:
        df = pd.read_sql_table('closed_group', conn)
        
        df = df[df['지역(구)'] == region]

        x_series = df['폐업연월']
        y_series = df[category]
        
        x_axis = x_series.values.tolist()
        y_axis = y_series.values.tolist()

        ret = {}
        for idx, value in enumerate(x_axis):
            ret[value] = y_axis[idx]
        
        return jsonify(ret), 200

    elif region:
        pass

    elif category:
        pass