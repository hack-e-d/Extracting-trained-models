from sklearn.externals import joblib
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)
result = loaded_model
print(result)