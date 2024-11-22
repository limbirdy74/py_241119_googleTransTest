import googletrans

trans = googletrans.Translator()  # 구글 번역 클래스로 객체 생성

str = "오늘은 날씨가 춥습니다."
# print(googletrans.LANGCODES)  # 번역 언어의 이름

result_eng = trans.translate(str, dest="en")  # 해당 한국어를 영어로 번역
result_jap = trans.translate(str, dest="ja")  # 일본어
result_chn = trans.translate(str, dest="zh-cn")  # 중국어

print(result_eng.text)
print(result_jap.text)
print(result_chn.text)