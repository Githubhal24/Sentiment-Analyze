import pandas as pd
import requests
from io import ByteIO

#Webページ上のExcelファイルを取得
url = "https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/ea851c04-54d0-43ab-b352-4cb537ee5347/20210609_resources"

# Excelデータをダウンロードして、DataFrameに変換
response = requests.get(url, verify=r"C:User\workspace\xxx")
excel_data = response.content
df = pd.DataFrame(ByteIO(excel_data)) 

#カラムの名前を設定
df.columns = ['No', '地方公共団体コード', '地方公共団体名', '内容']
df = df.drop(index = range(0,5))

#データの範囲を適用（１～２２９の番号が割り振られたデータ）
df_filter = df[df["No"].between(1, 229)]

#ランダムに100件抽出
random_data = df_filter.sample(n=100, random_state=1)

print(random_data)
random_data.to_xlsx('./dataset/web_data.xlsx', index=False)
# random_data.to_csv('./dataset/web_data.csv', index=False, encoding='shift-jis')
