# 基于Residual RNN的点云特征提取与分类自动化处理框架

## Abstract:
用传统方法对semantic features进行模板化、公式化的提取特征，虽然可以有效得到结构信息，但其过程对于原始数据信息有一定的损失，且使用范围存在局限性（如室内外场景的特征提取策略一般不同）,无法灵活应对不同场景、特点的数据。使用Residual RNN拟合从原始6维点云数据到分类结果的映射，任务过于复杂，在训练过程中，loss function难以快速而准确的向着最小值收敛，加之训练样本和训练时间的限制，削减了泛化能力强。除特征提取，传统的整合特征进行分类的手段如CFR、SVM等，也不能更好的适应不同场景间的变化。我们提出一种基于Residual RNN网络的，实现从LIDAR点云数据（x,y,z,r,g,b）输入，到指定类别分类结果的自动化处理框架。通过训练网络获得提取多种传统语义特征的能力，再利用RNN自动提取features来弥补前一步对原始数据信息造成的损失，最终利用synthesize network综合所有得到的特征信息，给出分类结果。

## Related Work:


## Method:

### 1.第一部分网络
特征提取网络：
网络提取传统特征+网络自动抽象特征
特征提取网络对每个输入点实现从六维（x,y,z,r,g,b）数据输入到N维特征向量的映射。Residual RNN网络经过监督训练可以提取诸如法向量,spin图等具有语义的传统点云特征,同时也可以得到部分网络自己学习得到的抽象特征（等价于把原始6维数据传入网络并直接和第二部分网络连接，不做单独的监督训练）,将两部分特征串联（concatenate）结合得到第二部分网络的输入。

### 2.第二部分网络

利用Residual RNN 模拟  合成函数(synthesize)。

output = synthesize( feature_1(input), feature_2(input), ... , feature_n(input) )

input: x
output: y
y = Network_2 ( Network_1(x), fNetwork_1(x), fNetwork_2(x), ... , fNetwork_n(x) )


## Experiment:

1.Stanford indoor dataset (12 classes)

2.German 某数据 (8 classes)

3.Tianjin 遥感数据 (4 classes)

与SVM,传统特征提取+CRF,普通RNN, etc 方法分别进行对比。

## Conclusion:
