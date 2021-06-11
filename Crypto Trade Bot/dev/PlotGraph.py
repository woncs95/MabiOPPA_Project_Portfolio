from VolBreakOut import *
from matplotlib.pyplot import *

##show floor lines 예측을 도와주는 도구

def plot_floor(x,y):
    x, sp, df=spline(x,y)
    df_mean = df.rolling(20).mean()
    figure(figsize=(12, 4))
    plot(x, sp)
    plot(x, df_mean * 1.15)
    plot(x, df_mean * 0.85)
    show()
