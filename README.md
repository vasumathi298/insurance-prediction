# insurance-prediction
 This model that was trained and tested using PyCaret and is uploaded and registered in MLFlow to deploy in spark.
 
 Firstly create a new environment to install PyCaret
# create a conda environment
conda create --name yourenvname python=3.6
# activate environment
conda activate yourenvname
# install pycaret
pip install pycaret-nightly
# update pycaret-nightly
pip install --upgrade pycaret-nightly
# to start MLFlow
mlflow ui --backend-store-uri sqlite:///mlruns.db

