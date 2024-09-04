# salonboard-scraping
Scraping customer information from Salon Board (Hot Pepper Beauty).

## Attention: webdriverを環境変数に設定する必要あり

Pythonファイルをexe化するコマンド
```
pip install pipenv
cd D:\ダウンロード\SALONBOARDscraping
pipenv --python 3.10
pipenv shell
pipenv install pandas
pipenv install selenium
pip install pyinstaller
pyinstaller D:\ダウンロード\salonboard-scraping-repository-main\src\app.pyw --onefile --name=SalonBordTool
```
