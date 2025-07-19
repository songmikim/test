import os
import sys
import json
from wordcloud import WordCloud

if len(sys.argv) < 3:
    sys.exit(-1)

print(sys.argv)

filepath = sys.argv[1] # 이미지 파일 경로
items = json.loads(sys.argv[2]) # 워드 클라우드로 만들 데이터
if not items:
    sys.exit(-1)

wc = WordCloud(font_path=f'{os.path.dirname(os.path.realpath(__file__))}/NanumGothic-ExtraBold.ttf', 
               background_color='white', 
               max_font_size=100, 
               width=500, height=300)
cloud = wc.generate_from_frequencies(items)
cloud.to_file(f"{filepath}")
print(filepath)