# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:37:32 2022

@author: emhl0
"""
# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# 処理ファイル名の出力
tkinter.messagebox.showinfo('○×プログラム',file)

print(file)