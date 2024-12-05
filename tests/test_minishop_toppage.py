#!/usr/bin/env python

# selenium使います
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# テスト用のライブラリ
import unittest


# テスト用のサーバー(Selenium grid)
REMOTE_URL = "http://selenium:4444/wd/hub"

class TestCase(unittest.TestCase):

    # 今の時間のタイムスタンプを生成しておく(テスト時に結果ファイルに付けるため)
    timestamp = None

    def setUp(self):
        # timestampがNoneの場合、現在時刻を取得
        if self.timestamp is None:
            from datetime import datetime
            self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # selenium gridのサーバーに接続
        self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())

    def tearDown(self):
        # テストサーバー切断
        self.driver.quit()
        # public/testcase.htmlおよびpublic/testcase.phpを削除
        import os

    # ホストwebに接続し、タイトルを取得するテスト
    def test_access(self):
        self.driver.get("http://web/")
        self.driver.get_screenshot_as_file(f"results/{self.timestamp}-01-toppage.png")
        self.assertIn("ショッピングサイト", self.driver.title)


if __name__ == "__main__":
    unittest.main()
