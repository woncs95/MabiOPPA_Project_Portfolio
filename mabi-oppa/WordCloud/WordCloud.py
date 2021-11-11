from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import wikiscrapper
from random import shuffle

# Random WordCloud with Scrapped Data from Wikipedia & Contributor Name

stopwords = set(STOPWORDS)
mask_logo = np.array(Image.open('heart.png'))
text1 = wikiscrapper.new_n
text2 = ["Hisagawa", "OPPADA", "Rebekah", "Aera", "Sukja", "Sylow", "Soultama", "mochidduk", "Yoshi"]
shuffle(text2)
text = text1 + text2
font_wgt = np.concatenate((np.repeat(40, 395), np.repeat(80, 7)), axis=0)
d = dict(zip(text, font_wgt))

wc = WordCloud(
    background_color='white',
    mask=mask_logo,
    stopwords=stopwords,
    max_font_size=80,
    max_words=402,
    height=1000,
    width=1000
)

wc.generate_from_frequencies(d)
image_colors = ImageColorGenerator(mask_logo)
print(image_colors)
print(wc.width, wc.height)

plt.figure(figsize=[10, 10])
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
