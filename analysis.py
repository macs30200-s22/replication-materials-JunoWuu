import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import statsmodels.api as sd
import matplotlib.pyplot as plt

def process_data(data):
    '''
    Input: CSV filename (str)
    Returns: Pandas DataFrame (processed and ready to analyze)
    '''
    var_list = ['BIRTHYR', 'F1S76', 'F2S76', 'F1SEX', 'F1D63', 'F2D66', 'F1D6G', 'F2D9AF', 'BYS46']
    data = pd.read_csv(data, header = 0, dtype = str, usecols=var_list, chunksize=10000000)
    df = pd.concat((x.query("F1SEX == '2'") for x in data), ignore_index=True)
    preg_set = set()
    for rows in df.iterrows():
        if rows[1]['F1S76'] == '1':
            preg_set.add(rows[0])
        elif rows[1]['F1D63'] == '1':
            preg_set.add(rows[0])
        elif rows[1]['F1D6G'] == '1':
            preg_set.add(rows[0])
        elif rows[1]['F2S76'] == '1':
            if rows[1]['BIRTHYR'] != ' ':
                if int(rows[1]['BIRTHYR']) >= 74:
                    preg_set.add(rows[0])
        elif rows[1]['F2D66'] == '1':
            if rows[1]['BIRTHYR'] != ' ':
                if int(rows[1]['BIRTHYR']) >= 74:
                    preg_set.add(rows[0])
        elif rows[1]['F2D9AF'] == '1':
            if rows[1]['BIRTHYR'] != ' ':
                if int(rows[1]['BIRTHYR']) >= 74:
                    preg_set.add(rows[0]) 
    add_list = []
    for x in range(7500):
        if x in preg_set:
            add_list.append(1)
        else:
            add_list.append(2)
    df['pregnant'] = add_list
    def f(row):
        if row['BYS46'] == '1':
            val = 1
        elif row['BYS46'] == '2':
            val = 1
        else:
            val = 2
        return val
    df['expectation'] = df.apply(f, axis=1)
    df2 = df[['expectation', 'pregnant']].copy()
    
    # class count
    class_count_0, class_count_1 = df2['pregnant'].value_counts()
    #class0 means not pregnant
    # Separate class
    class_0 = df2[df2['pregnant'] == 2] #not pregnant
    class_1 = df2[df2['pregnant'] == 1]
    
    class_0_under = class_0.sample(class_count_1)
    test_under = pd.concat([class_0_under, class_1], axis=0)
    return test_under

def plot_data(data, save_fig=False, path="./figure1.tiff"):
    '''
    Input: 'data': Pandas DataFrame with two columns of data (float64),
           'save_fig': bool indicating whether to save figure to file (tiff)
           'path': string indicating path for saving figure if 'save_fig' is
                   True (defaults to "figure1.tiff" in working directory)
    Returns: Nothing (produces plot and optionally saves to file)
    '''
    X = data['expectation'].tolist()
    y = data['pregnant'].tolist()
    y = np.array(y)-1
    sd_model = sd.Logit(y, X).fit(disp=0)
    sd_model.summary()
    plt.rc('figure', figsize=(12, 3))
    plt.text(0.02, 0.07, str(sd_model.summary()), {'fontsize': 15}, fontproperties = 'monospace') 
    plt.axis('off')
    plt.tight_layout()
    if save_fig:
        plt.savefig(path,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})
    return

if __name__ == "__main__":
    # When running script in Docker Container, save figure to /figures/
    # directory
    df = process_data('1994.csv')
    plot(data=df, save_fig=True, path="/figure1.tiff")