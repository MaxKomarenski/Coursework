""" Tumblr API Example - Python CLI
"""

import sys
import pytumblr

client = pytumblr.TumblrRestClient(
  'YSulZe4hHAhGEyVzjxqdyuUvbID6jKm639MXz3ueK3cYOciWjJ',
  'mLpw6UwGPx1e7nX5zZbGtgZGAl5wCVKxopeQJuCHlR85vYpQse',
  'utnLdOTw6hBXqSb5UDMTNTS0QmHv4CeW3xE4prqLp21KUWALVC',
  'KTobG7O9V5aSNJnadGezmetGGN0ZvYjcfC9uUCZlVA9HSJsixo'
)


client.blog_info('userX')['blog']['posts']

print(client.posts('userX', offset=0, limit=10))
