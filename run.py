data={'user0':{"这里","要把","analysis里的data","也复制过来"}}
userx ={"这个也一样要把datax弄过来"}
print("您的关注为：")
print(userx)
print('正在为您推荐用户'.center(100, '='))
# 63是analysis里计算出来的与其相似度最高的用户号，每用一次都要改的
print("ta与您有着最多的共同关注，推荐您关注：" + "user63" )
AA=set(data['user63'])
print("你们的共同关注有：")
print(AA & userx)
print("ta的关注有：")
print(data['user63'])

