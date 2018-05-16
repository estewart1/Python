import re

def removeBracket(file):
	removed = re.sub(r'\[\d+\]', '', file)
	return removed

f = "The kanji that make up Japans name mean 'sun origin', and it is often called the 'Land of the Rising Sun'. Japan is a stratovolcanic archipelago consisting of about 6,852 islands. The four largest are Honshu, Hokkaido, Kyushu, and Shikoku, which make up about ninety-seven percent of Japans land area and often are referred to as home islands. The country is divided into 47 prefectures in eight regions, with Hokkaido being the northernmost prefecture and Okinawa being the southernmost one. The population of 127 million is the worlds tenth largest. Japanese people make up 98.5% of Japans total population. About 9.1 million people live in Tokyo,[15] the capital of Japan.[15]"
print removeBracket(f)