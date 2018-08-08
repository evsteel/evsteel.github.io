from __future__ import unicode_literals

AUTHOR = 'Evan Li'
SITENAME = 'Arctos Bulletin'
SITEURL = 'https://evsteel.github.io/'
GITHUB_URL = 'https://evsteel.github.io/'
TIMEZONE = 'Asia/Shanghai'

PATH = 'content'
PAGE_PATHS = ['pages']
OUTPUT_PATH = 'output/'

USE_FOLDER_AS_CATEGORY = True
# DEFAULT_CATEGORY = ''
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = True


STATIC_PATHS = ['images']
STATIC_EXCLUDE_SOURCES = True
DEFAULT_PAGINATION = 10

WITH_FUTURE_DATES = True

# Theme Settings
THEME = 'elegant'
THEME_STATIC_DIR = 'elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
