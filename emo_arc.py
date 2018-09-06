#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 00:55:42 2018

@author: home
"""


from os import listdir, mkdir
from os.path import isfile, join, isdir
from json import loads
from re import findall,UNICODE
import sys
sys.path.append("/Users/home/Dropbox/dialogues.ai/Software/dialogues-writers-suite/dialogues_wp/tools")
from dogtoys import *
from labMTsimple.speedy import LabMT
my_LabMT = LabMT()
from labMTsimple.storyLab import *
import numpy as np
import pickle

import os
sys.path.append('/Volumes/SSD01/dialogues/database')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','gutenbergdb.settings')
import django
django.setup()

from tools.library.models import *
from tools.bookclass import *

from tqdm import tqdm
import collections
import dialogues_config as dc
import re


# all our essentials
from matplotlib import rc,rcParams
rc('font', family='sans-serif') 
rc('font', serif='Helvetica Neue')
rc('text', usetex='false')

rc('font', family='serif')
rc('font', family='cmr10')
rc('text', usetex='false')
# this should accomplish the same thing
rcParams['text.usetex'] = False
rcParams['text.latex.preamble'] = r'\usepackage{hyperref}'
rcParams['text.latex.unicode'] = True

rcParams.update({'font.size': 12})
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


#Runs time-series for books in list

timeseries = []

def get_timeseries(books = [], *args):
    for p in books:
        b = Book.objects.get(gutenberg_id=p)
        b_data = Book_raw_data(b)
        print(b.txt_file_path)
        try:
            b_data.chopper_sliding(my_LabMT,num_points=200,stop_val=1.0,randomize=False,use_cache=True)
        except:
            print("couldn't find",b.title)
            pass
        print(b_data.timeseries)
        timeseries.append(b_data.timeseries)
        
#Plots a graph of book
    for i,t in enumerate(timeseries):
        if t is not None:
            plt.figure(figsize=(8,5))
            plt.plot(t,linewidth=1.5,color=".2")
            plt.ylabel(r"$h_{textrm{avg}}$")
            plt.xlabel("Narrative Time")
            b = Book.objects.get(gutenberg_id=books[i])
            plt.title(b.title, b.authors)
            #Saves plot of books to chosen directory as .pdf
            plt.savefig("/Users/home/Desktop/dialogues.ai/media-files/timeseries-arcs/{}.pdf".format(books[i]),bbox_inches="tight")