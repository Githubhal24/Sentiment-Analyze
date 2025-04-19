# README
<div id="top"></div>

## 使用技術

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-dotenv-000000.svg?logo=streamlit&style=for-the-badge">
  <img src="https://img.shields.io/badge/-openpyxl-092E20.svg?logo=Pytorch&style=for-the-badge">
  <img src="https://img.shields.io/badge/-request-FF2465.svg?logo=sklearn&style=for-the-badge">
  <img src="https://img.shields.io/badge/-numpy-232F3E.svg?logo=numpy&style=for-the-badge">
  <img src="https://img.shields.io/badge/-pandas-20232A?style=for-the-badge&logo=pandas&logoColor=844EBA">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- その他 -->
  <img src="https://img.shields.io/badge/-openai API-1488C6.svg?&style=for-the-badge">

</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [動作確認](#動作確認)
6. [環境変数の一覧](#環境変数の一覧)

<br />

<!-- プロジェクト名を記載 -->

## プロジェクト名

生成AIを活用した感情分析プログラム 

<!-- プロジェクトについて -->

## プロジェクトについて
### 概要
Pythonを用いて生成AIとAPI連携して、感情分析（ポジティブ・ネガティブ）を行うプログラム

<!-- プロジェクトの概要を記載 -->
| ソースコード               | 機能概要                                                                 |
| ------------------------- | ----------------------------------------------------------------------- |
| scraping.py               | 感情分析対象のデータをスクレイピングする                                    |
| sentiment_analyze.py      | 取得したデータを生成AIとAPI連携して感情分析を行うメイン処理                  |
| .env                      | APIキーを環境変数として格納するenvファイル                                  |

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク一覧とバージョンを記載 -->
### 開発時の環境

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.12.7     |
| request               | 2.32.2     |
| numpy                 | 1.24.3     |
| pandas                | 2.0.3      |
| python-dotenv         | 16.4.5     |
| openpyxl              | 3.1.5      |

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->
.
<p>├── README.md</p>
<p>├── scraping.py</p>
<p>├── sentiment_analyze.py</p>
<p>├── .env</p>

<p align="right">(<a href="#top">トップへ</a>)</p>

## 動作確認
<ol type="1">
<p>
  <li>.envファイルに所有しているAPIキーを設定</li>
  <li>[python scraping.py]を実行して、分析対象のデータを取得</li>
  <li>[python sentiment_analyze.py]を実行して、感情分析結果をExcelファイルで取得</li>
</p>
</ol>  

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境変数の一覧

| 変数名                 | 役割                      | デフォルト値                         |                
| ---------------------- | ------------------------ | ----------------------------------- | 
| AI_API_KEY             | 生成AIのAPIキー           | xxxxx(任意のAPIキーを設定してください) |

<p align="right">(<a href="#top">トップへ</a>)</p>
