import os
import tkinter
from tkinter import filedialog

def change_ext(pathname,new_ext):
    pre, ext = os.path.splitext(pathname)
    os.rename(pathname, pre + new_ext)
    
print("----------------Gerber Name Chnager-----------------")
root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)
    Flist=os.listdir(tempdir)
    for Fname in Flist:
        if(Fname == "copper_bottom.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gbl"
            change_ext(FFname,n_ext)
            print("--changed gbr file Copper bottom--  "+FFname)
        elif(Fname == "copper_top.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gtl"
            change_ext(FFname,n_ext)
            print("--changed gbr file Copper top--  "+FFname)
        elif(Fname == "silkscreen_bottom.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gbo"
            change_ext(FFname,n_ext)
            print("--changed gbr file Silkscreen bottom--  "+FFname)
        elif(Fname == "silkscreen_top.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gto"
            change_ext(FFname,n_ext)
            print("--changed gbr file Silkscreen top--  "+FFname)
        elif(Fname == "soldermask_bottom.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gbs"
            change_ext(FFname,n_ext)
            print("--changed gbr file Soldermask bottom--  "+FFname)
        elif(Fname == "soldermask_top.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gts"
            change_ext(FFname,n_ext)
            print("--changed gbr file Soldermask top--  "+FFname)
        elif(Fname == "solderpaste_bottom.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gbp"
            change_ext(FFname,n_ext)
            print("--changed gbr file Solderpaste bottom--  "+FFname)
        elif(Fname == "solderpaste_top.gbr"):
            FFname=tempdir+'/'+Fname
            n_ext=".gtp"
            change_ext(FFname,n_ext)
            print("--changed gbr file Solderpaste top--  "+FFname)
        else:
            FFname=tempdir+'/'+Fname
            print("--not to be changed gbr file--  "+FFname)
            