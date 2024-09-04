import scraping
import datetime
import tkinter
import sys
import pandas as ps
from tkinter import ttk
import constants


def scrapingCommnad():
    """スクレイピング実行"""
    try:
        date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        file_name = './result/SalonBoard_' + date

        scraping.main(userid.get(), password.get(),
                      bln.get(), output_combobox.get(), file_name)

        # CSVをExcelに変換
        excel = ps.read_csv(file_name + '.csv', encoding='utf-8', dtype=object)
        excel.to_excel(file_name + '.xlsx', encoding='utf-8', index=False)
    except Exception as e:
        print(e.args)


def click_close():
    main_win.destroy()
    sys.exit()


# メインウィンドウ
main_win = tkinter.Tk()
main_win.geometry("550x400")
main_win.title('ログインフォーム')

# ユーザーID
userid_label = ttk.Label(main_win, text='ユーザーID')
userid = tkinter.StringVar()
userid_text = ttk.Entry(main_win, textvariable=userid, width=30)

# パスワード
password_label = ttk.Label(main_win, text='パスワード')
password = tkinter.StringVar()
password_text = ttk.Entry(main_win, textvariable=password, show='*', width=30)

# チェックボックス wait時間
bln = tkinter.BooleanVar()
bln.set(False)
waittime_chl = ttk.Checkbutton(
    main_win, variable=bln, text='待ち時間設定')
waittime_label = ttk.Label(main_win, text='ログインに失敗する場合はチェックしてください')

# コンボボックス 取得データ選択
option = constants.COMBBOX
variable = tkinter.StringVar()
output_combobox = ttk.Combobox(main_win, values=option, state='readonly',
                               textvariable=variable, width=30)
output_combobox.current(0)
output_label = ttk.Label(main_win, text='出力項目')

# ログインボタン
app_btn = ttk.Button(main_win, text="ログイン", command=scrapingCommnad)

# ウィジェットの配置
userid_label.place(x=100, y=100)
userid_text.place(x=200, y=100)
password_label.place(x=100, y=130)
password_text.place(x=200, y=130)
output_label.place(x=100, y=170)
output_combobox.place(x=200, y=170)
waittime_chl.place(x=100, y=210)
waittime_label.place(x=100, y=230)
app_btn.place(x=200, y=280)

# ウィンドウ表示継続
main_win.protocol("WM_DELETE_WINDOW", click_close)
main_win.mainloop()
