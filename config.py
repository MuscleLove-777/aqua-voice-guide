"""Aqua Voice完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Aqua Voice完全ガイド"
BLOG_DESCRIPTION = "開発者向けAI音声入力ツールAqua Voiceの使い方・最新機能・料金を毎日更新。技術用語97%精度の音声コーディングを完全解説。"
BLOG_URL = "https://musclelove-777.github.io/aqua-voice-guide"
BLOG_TAGLINE = "声でコードを書く時代 — Aqua Voice完全ガイド"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/aqua-voice-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Aqua Voice 使い方",
    "Aqua Voice 料金・プラン",
    "Aqua Voice vs Wispr Flow",
    "Aqua Voice 最新ニュース",
    "AI音声入力 開発者向け",
    "Aqua Voice 活用テクニック",
    "音声入力ツール比較",
    "Aqua Voice カスタム辞書",
]

THEME = {
    "primary": "#00BCD4",
    "accent": "#0D47A1",
    "gradient_start": "#00BCD4",
    "gradient_end": "#0D47A1",
    "dark_bg": "#0a1628",
    "dark_surface": "#142240",
    "light_bg": "#e0f7fa",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Aqua Voice": [
        {"service": "Aqua Voice", "url": "https://withaqua.com", "description": "Aqua Voiceに登録する"},
    ],
    "Aqua Voice Pro": [
        {"service": "Aqua Voice Pro", "url": "https://withaqua.com/pricing", "description": "Aqua Voice Proプラン"},
    ],
    "音声入力デバイス": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "Amazonで高性能マイクを探す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "Udemyで音声入力講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8091

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
