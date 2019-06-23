# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:16:02 2019

@author: mas

%bookmark ri3 /Users/mas/learning/python_exercises/MyObjects
%cd ri3


"""
#Web API用パッケージ
import requests
import json

def main(user_name, repo_name):
    #Issuesを取得
    GITHUB_URL_PTN = "https://api.github.com/repos/{0}/{1}/issues"
    url = GITHUB_URL_PTN.format(user_name, repo_name)
    #リクエスト
    r = requests.get(url)
    if r.ok:
        #取得データをjsonに変換
        issues = r.json()
        for issue in issues:
            print(issue["title"])

if __name__ == "__main__":
    user_name = "tensorflow"
    repo_name = "tensorflow"
    main(user_name, repo_name)