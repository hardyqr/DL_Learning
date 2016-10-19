# 基于Residual RNN和CNN的点云特征提取与分类自动化处理框架
A Deep Learning Framework for PointCloud Understanding
Part 1: Residual RNN; Classification
Part 2: 3D CNN; Object Detection

todo:
1. 测试ETH Zurich数据集
2. CNN试验

## Abstract:
用传统方法对semantic features进行模板化、公式化的提取特征，虽然可以有效得到结构信息，但其过程对于原始数据信息有一定的损失，且使用范围存在局限性（如室内外场景的特征提取策略一般不同）,无法灵活应对不同场景、特点的数据。使用Residual RNN拟合从原始6维点云数据到分类结果的映射，任务过于复杂，在训练过程中，loss function难以快速而准确的向着最小值收敛，加之训练样本和训练时间的限制，削减了泛化能力强。除特征提取，传统的整合特征进行分类的手段如CFR、SVM等，也不能更好的适应不同场景间的变化。我们提出一种基于Residual RNN网络的，实现从LIDAR点云数据（x,y,z,r,g,b）输入，到指定类别分类结果的自动化处理框架。通过训练网络获得提取多种传统语义特征的能力，再利用RNN自动提取features来弥补前一步对原始数据信息造成的损失，最终利用synthesize  

## Related Work:


## Method:
![Network](https://github.com/hardyqr/Learning_Notes_of_DL_Models/blob/master/Point_Cloud_Classification/WechatIMG3.jpeg)

利用深度学习解决图像、语音等识别问题已经日趋成熟，但应用到点云数据上的实例依然很少。我们认为主要是由于点云数据蕴含的信息量极大，对点云作出分类需深度网络学习到一些非常抽象的、与空间结构相关的概念。因此，为了完成对点云数据进行分类的任务，设计出的深度网络需要有足够的“深度”，以获得足够的参数和复杂度；以及经过大量的训练，达到理解空间结构的目的。
### 1.几个特点

a. 对网络进行预训练，使之在特定位置收敛得到几个空间结构的显著特征，如法向量、spin图，可以有效缩短训练时间。

b. 一个过深的网络存在degradation(梯度耗散)的问题，网络深度增加performance会不升反降。在点云分类问题中，一个很deep的网络是必要的，但过深网络很快导致a higher training error, Kaiming He 将其称为degradation(梯度消失)(Deep Residual Learning for Image Recognition, Kaiming He)。我们在前期实验中也在点云数据上验证了这一点。Kaiming He提出的Deep Residual Network很好地解决了degradation的问题。本文借鉴了他的思想，在神经元间进行了搭接,使用了一些Residual Block的结构。

c. 我们在Deep Residual RNN网络中使用LSTM神经元，使网络获得长期记忆的能力，在输入一个较长的点序列后，依然可以记忆靠前的输入，达到对物体空间结构进行理解的目的。

d. 不同的识别对象可能有不同的空间结构、颜色特点，为了尽快得到有效特征，需要在学习速度和特征有效性（也即识别精度）间寻找到一个平衡。因此我们对于不同识别对象，应用了不同深度的特征提取网络，以期在有效提取特征的同时加速网络收敛。

### Network
我们提出一种基于深度RNN的,具有Residual block的,以LSTM作为神经元的自动化处理框架, 希望可以有效解决应用在点云分类问题上的"过深"的网络存在的degradation,训练时间长、收敛慢的问题, 高效提取空间信息特征，且能够把高阶、低阶特征进行融合、提炼，获得最佳分类参数,提高分类准确度。

我们的自动化处理框架如下：


#### 第一部分网络
特征提取网络：
网络提取传统特征+网络自动抽象特征
特征提取网络对每个输入点实现从六维（x,y,z,r,g,b）数据输入到N维特征向量的映射。Residual RNN网络经过监督训练可以提取诸如法向量,spin图等具有语义的传统点云特征,同时也可以得到部分网络自己学习得到的抽象特征（等价于把原始6维数据传入网络并直接和第二部分网络连接，不做单独的监督训练）,将两部分特征串联（concatenate）结合得到第二部分网络的输入。


#### 第二部分网络

利用Residual RNN 模拟  合成函数(synthesize)。

output = synthesize( feature_1(input), feature_2(input), ... , feature_n(input) )

input: x
output: y
y = Network_2 ( Network_1(x), fNetwork_1(x), fNetwork_2(x), ... , fNetwork_n(x) )

多个尺度的、semantic的或网络自动抽象的特征在第二部分网络中竞争，并由网络筛选、融合、提取出合适的高层次特征。

## Experiment:

1.Stanford indoor dataset (12 classes)

实验中，我们将第一部分网络去掉提取传统特征的部分，仅使用Residual RNN自动提取网络特征,发现最终效果与我们提出的网络相近，但收敛明显更慢。


2.German 某数据 (8 classes)

3.Tianjin 遥感数据 (4 classes)

与SVM,传统特征提取+CRF,普通RNN, etc 方法分别进行对比。

## Conclusion:

我们提出的点云分类自动化处理框架相较于传统方法有更高的准确度。第一部分网络在特征提取上可以获得更为完整有效的空间信息，从而为分类提供更可靠的依据，对网络进行预训练提高了在不同场景下分类的学习效率。第二部分网络较传统分类器可以更智能合理地整合特征信息，进一步融合提炼，得到更高准确度的结果。
