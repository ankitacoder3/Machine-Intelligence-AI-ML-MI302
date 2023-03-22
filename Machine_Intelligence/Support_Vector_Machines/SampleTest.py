import sys
import importlib
import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--NAME', required=True)

args = parser.parse_args()
subname = args.SRN


try:
    mymodule = importlib.import_module(subname)
except Exception as e:
    print(e)
    print("Run python3.7 SampleTest.py --NAME Support_Vector_Machines ")
    sys.exit()

data = pd.read_csv('test.csv')
X_test = data.iloc[:, 0:-1]
y_test = data.iloc[:, -1]

try:
    model = mymodule.SVM('train.csv').solve()
    print(f'Accuracy: {model.score(X_test, y_test)*100:.2f}%')
except Exception as e:
    print(f'Failed {e}')
