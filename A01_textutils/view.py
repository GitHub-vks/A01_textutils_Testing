#I have created this file- Vivek Kumar Singh
from django.http import HttpResponse
from django.shortcuts import render
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import openpyxl 
def index(request):
    return render(request, 'index.html')
    
def simple_function(request):
    import tkinter as tk
    from tkinter import filedialog
    # tk=top.lift()
    root=tk.Tk()
    root.withdraw()
    # GUI.attributes('-topmost',0)
    file_path=filedialog.askopenfilename()
    # GUI.attributes('-topmost', 1)
    # df=file_path
    df=pd.read_csv(file_path, sep=" ")
    # df=df.parse('Sheet1')
    # df=df.info()
    # df=df.head(100)
    # print(df)
    return HttpResponse(df)

