from random import choice
from locustfile import HttpUser, task, between

class NotLoginUser(HttpUser):
  """非会員ユーザーがページを巡回する様子をシミュレートする"""
  wait_time = between(1, 5)

  @task
  def view_pages(self):
    urls = [
      '/',  # トップページ
      '/post/slug/example', # 導入事例
      '/post/list/download', # お役立ち資料
      '/post/category/release', # ニュースリリース
      '/post/category/53',  # カテゴリ スキャナ・プリンタ
      '/post/category/fit_seminar',  # カテゴリ フォーラム・セミナー紹介
      '/post/category/clooud',  # カテゴリ クラウド

      '/post/detail/fm0141',  # 金融DXと人材育成：地域変革への取り組み
      '/post/detail/S-5420',  # オンライン窓口システム「LiveOn Call」
      '/post/detail/nozomi_sl1'  # Nozomi Networks、OT/IoTのセキュリティー対策の営業体制を強化
    ]
    self.client.get(choice(urls))


class LoginUser(HttpUser):
  """FIT会員ログインユーザーがログイン後の行動をシミュレートする"""
  wait_time = between(1, 5)

  def on_start(self):
    """ユーザーログイン"""
    pass

  @task
  def view_pages(self):
    urls = [
      # 巡回するページを記載
    ]
    self.client.get(choice(urls))

  def on_stop(self):
    """ユーザーログアウト"""
    pass
