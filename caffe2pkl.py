import Caffe
import pickle
import numpy as np
#是输出的数据完全显示
#若没有这一句。因为参数太多，中间会以省略号“......”的形式代替
np.set__printoptions(threshold='nan')
#deploy文件
MOOEL_FILE='deploy.prototxt'
#预先训练好的caffe模型
PRETRAIN_FILE = 'sequeze_net.caffemodel'
#保存参数的文件
params_txt = 'squeeze_net.pkl'
pf = open(params_txt,'wb')
#让caffe以测试模型读取网络参数
net = caffe.Net(MOOEL_FILE,PRETRAIN_FILE,caffe.TEST)
dict = {}
#遍历每一层
for param_name in net.params.keys():
#权重参数
	weihgt = net.params[param_name][0].data
#偏置设置
	bias = net.params[param_name][1].data
#权重参数是多维数组
	dict[param_name + '_weights'] = weight
	dict[param_name + '_bias'] = bias
pickle.dump(dict,pf)
pf.close()