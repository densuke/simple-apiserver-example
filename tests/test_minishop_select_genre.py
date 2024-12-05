#!/usr/bin/env python

# selenium使います
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# テスト用のライブラリ
import unittest

# ロガーを作成、出力先はstdout, ログレベルはINFO
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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

    # 接続して、ジャンルを選択して商品一覧を取得するテスト
    def test_access(self):
        self.driver.get("http://web/")
        # ラジオボタン、name=genreの要素から、value=musicを選択
        genre = self.driver.find_elements(By.NAME, "genre")
        genre[2].click()
        self.driver.get_screenshot_as_file(f"results/{self.timestamp}-01-select-music.png")

        # 送信ボタンをクリック
        self.driver.find_element(By.XPATH, "/html/body/form/input[2]").click()
        self.driver.get_screenshot_as_file(f"results/{self.timestamp}-02-list-musics.png")

        # ジャンル別商品一覧に遷移しているはずなので、最初のh3タグに「ジャンル別商品一覧」という文字列があるかどうかを確認
        logger.info(self.driver.find_element(By.XPATH, "/html/body/h3").text)
        self.assertIn("ジャンル別商品一覧", self.driver.find_element(By.XPATH, "/html/body/h3").text)
        # データもきちんと入っているかの確認
        # /html/body/table/tbody/tr[3]/td[3]/ = Eric Clapton
        logger.info(self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[3]").text)
        self.assertIn("Eric Clapton", self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td[3]").text)


if __name__ == "__main__":
    unittest.main()
