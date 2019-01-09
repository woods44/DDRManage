from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start(self):
        # ローカルホストに素晴らしいDDRの楽曲一覧サイトがあるので思わずパーノォーをクリック
        self.browser.get("http://localhost:8000/music_viewer")

        # サイトの名前がDDRMusicViewerであることを間違いなく把握する
        self.assertIn('DDRMusicViewer', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
