# 导入数据：可以用自己爬的数据，也可以用csv文件里的数据集（那个里面是一百个用户每人的最新50个关注）
data={'user0': {"关注一","关注二","中间别忘了用逗号隔开",}, }

# 寻求推荐关注的微博用户自己的关注列表，可以自己写也可以用我的另一国csv文件
userx ={"例子1","例子2","例子3"}
# 计算他们之间的杰卡德系数(交集除以并集)，并存入列表datax里
datax = list()

for i in range(99):
        A=set(data['user'+str(i)])
        cor = (len(A & userx)) / (len(A | userx))
        datax.append(cor)
# 取出列表里的最大值（最大的就是最相似的）
b=max(datax)
'''print(datax)
print(b)
这一部分是为了验证杰卡德距离是不是最大的那个'''
# 寻找最大值所在的下标（即寻找那个相似度最高的user）
def find(datax,a):
    for j in range(0,len(datax)):
        if datax[j]==a:
            print(j)
print(find(datax,b))







