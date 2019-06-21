# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:16:02 2019

@author: mas

%bookmark ri3 /Users/mas/learning/python_exercises/MyObjects
%cd ri3


"""
#テスト環境構築モジュール
import unittest

class Bot():
    #初期化
    def __init__(self, owner_name):
        self.name = owner_name
    #応答メソッド
    def reply(self, call):
        msg = call
        return "Hello" if self.name not in msg else "Hello my Boss!"

#テスト環境（クラス）
class TestBot(unittest.TestCase):
    #テスト環境（メソッド）
    def test_bot_reply(self):
        bot = Bot("Angy")
        self.assertEqual("Hello", bot.reply("Hi, I'm Bill.'"))
        self.assertEqual("Hello my Boss!", bot.reply("Hi, I'm Angy."))

if __name__ == "__main__":
    #テスト関数を実行し、想定通りの反応の場合に「OK」を返す
    unittest.main()
    