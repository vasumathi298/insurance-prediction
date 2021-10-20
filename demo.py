from pycaret.regression import *
import pandas as pd
import mlflow

def run():
    data=pd.read_csv("insurance.csv")
    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    s=setup(data, target='charges', session_id=123, silent=True, log_experiment=True, experiment_name='insurance_prediction',log_plots=True)
    models=['lr','dt', 'rf', 'gbr', 'lightgbm']
    all_models=[create_model(i) for i in models]
    
if __name__ =="__main__":
    run()
    