# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:16:02 2019

@author: mas

%bookmark ri3 /Users/mas/learning/python_exercises/MyObjects
%cd ri3


"""
#ログ用パッケージ
from logging import getLogger, StreamHandler, DEBUG

#ログの作成関数
def create_logger(name, log_level):
    """create logger"""
    # __file__には当ファイル名が入る
    logger = getLogger(name if name else __file__)
    handler = StreamHandler()
    handler.setLevel(log_level)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger

def main():
    """show how to handle and log the exception"""
    #ログの作成
    logger = create_logger("my_logger", DEBUG)
    #INFOレベルの出力確認
    logger.info("Now try to open file that does not exist!")

    #ログをテスト
    try:
        with open("not_exist_file.txt") as f:
            lines = f.readlines()
    except IOError as e:
        #criticalレベルのエラーの場合は表示
        logger.critical("You faced Exception! {}".format(e))

if __name__ == "__main__":
    main()