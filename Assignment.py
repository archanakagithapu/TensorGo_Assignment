import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Label, Button
import numpy as np

def analyze_csv():
    
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])


    data = pd.read_csv(file_path)

    for column in data.columns:
        data[column] = data[column].apply(lambda x: 1 if isinstance(x, str) else x)

    
    for column in data.columns:
        mean = np.nanmean(data[column])
        median = np.nanmedian(data[column])
        mode = data[column].mode()
        if not mode.empty:
            mode = mode.iloc[0]
        else:
            mode = np.nan
        std_dev = np.nanstd(data[column])
        print(f"Column: {column}")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {std_dev}")

    
    data.hist()
    plt.show()

    data.plot(kind='scatter', x=data.columns[0], y=data.columns[1])
    plt.show()

root = Tk()
button = Button(root, text="Analyze CSV", command=analyze_csv)
button.pack()

root.mainloop()

