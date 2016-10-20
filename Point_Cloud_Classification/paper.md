# A Deep Learning Framework for PointCloud Understanding - 基于Residual RNN和3D CNN的点云特征提取与分类自动化处理框架


## Abstract:
用传统方法对semantic features进行模板化、公式化的提取特征，虽然可以有效得到结构信息，但其过程对于原始数据信息有一定的损失，且使用范围存在局限性（如室内外场景的特征提取策略一般不同）,无法灵活应对不同场景、特点的数据。除特征提取，传统的整合特征进行分类的手段如CFR、SVM等，也不能更好的适应不同场景间的变化，泛化能力有限。我们提出一种基于Residual RNN和3D CNN的自动化framework，得到从原始LIDAR点云数据（6维/7维输入）映射到指定类别分类结果的自动化处理框架，通过监督训练使网络获得提取多尺度、空间和Intensity、颜色信息的抽象特征的能力,达到了对large-scale scene点云分类state-of-art的效果。  

## Related Work:
3D ShapeNets for 2.5D Object Recognition and Next-Best-View Prediction  
Shape Completion Enabled Robotic Grasping

## Method:

利用深度学习解决图像、语音等识别问题已经日趋成熟，但应用到点云数据上的实例依然很少。我们认为主要是由于点云数据蕴含的信息量极大，对点云作出分类需深度网络学习到一些非常抽象的、与空间结构相关的概念。因此，为了完成对点云数据进行分类的任务，设计出的深度网络需要有能力提取有效的空间结构representation，且有足够的“深度”，以及经过大量的训练,才能达到理解空间结构的目的。


### Network Overview
我们提出一种基于深度RNN和CNN的,具有Residual block的,以LSTM作为神经元的自动化处理框架, 希望可以有效解决过去在点云分类问题上方法的泛化能力差、精度低的问题，同时兼顾到"过深"的网络存在的degradation,训练时间长、收敛慢的问题。我们提出的framework可以自动高效提取多个尺度上的空间特征、颜色特征信息，且能够把高阶、低阶特征进行融合、提炼，获得最佳分类参数,提高分类准确度。


我们的自动化处理框架如下：
![Network](https://github.com/hardyqr/Learning_Notes_of_DL_Models/blob/master/Point_Cloud_Classification/3DCNN%2BResidualRNN.jpeg)
#### Part 1 （Network_1）
特征提取网络：
Residual RNN提取Intensity和颜色特征+3D CNN提取多尺度空间结构特征
特征提取网络对每个输入点实现从六维（x,y,z,r,g,b）/七维（x,y,z,Intensity,r,g,b）数据输入到N维特征向量的映射。

1.由Multi-scale 3D CNN提取多个尺度的空间结构特征并标记回每个individual的点；
先把原始点云数据栅格化成3D Voxel Grid
![Network](https://github.com/hardyqr/Learning_Notes_of_DL_Models/blob/master/Point_Cloud_Classification/PointcloudtoVoxelgrid.jpeg)
输入如下的CNN网络
![Network](https://github.com/hardyqr/Learning_Notes_of_DL_Models/blob/master/Point_Cloud_Classification/3DCNN.png)
（大概是图里这个意思,但我们的有多个尺度的卷积，具体参数也会变）


2.由Residual RNN提取Intensity和颜色的特征


最后,将两部分特征串联（concatenate）结合得到第二部分网络的输入。
![Network](https://github.com/hardyqr/Learning_Notes_of_DL_Models/blob/master/Point_Cloud_Classification/Combine_Representation.png)

input[1]=x,y,z
input[2]=(intensity),r,g,b

Output_1=[CNN_feature_1(input[1]), CNN_feature_2(input[1]), ... ,CNN_feature_n(input[1]), RNN_feature_1(input),RNN_feature_2(input[2]), ..., RNN_feature_n(input[2])]

#### Part 2 (Network_2)

利用Residual RNN 模拟合成函数(synthesize),得到最终分类结果。

Result = Output_2 = synthesize(output_1)


###
#### Multi-Scale 3D CNN
传统点云数据呈无序的离散分布，无法使用诸如CNN的深度学习工具进行特征提取，我们将其栅格化，转化为3D Voxel Grid(O除叛采样Grids),使之具有可以输入CNN的数据格式。CNN应用于图像数据时，体现了对画面结构的良好理解，提取有效特征的强大能力，我们认为映射到三维场景，CNN仍具有相似的特点。但large-scale三维场景不同于图片之处在于，识别对象在空间中的大小存在千差万别的不同，不同种类对象的结构特征可能体现在不同的尺度上。于是我们设计了多个尺度上的卷积核，希望能够学习到multi-scale的物体空间特征，并通过监督学习得到最为有效的representation。

过去的工作通常采取先将点云数据栅格化，再用CNN网络进行3D卷积直接得到了栅格化后点阵的分类结果。如此只能得到整个点集（点阵）的标签，无法应用于large-scale点云的分类，且无法避免栅格化时信息损失的问题。我们不把3D CNN的卷积特征直接用于分类，而是再多尺度卷积后将其拼接进由Residual RNN提取的另一个特征向量中，不仅可以应用于大场景、细化到每个individual点的分类，还有效弥补了栅格化造成的信息损失。

#### Multi-Orientation Learning
为了使我们的自动化处理框架可以识别多角度，朝向（orientation）的物体，我们对3D CNN在训练时采取“旋转输入”的方式。eg.一把椅子分20个角度（相当于20把朝向不同的椅子）输入网络，使Framework在面对不同空间形态的物体时有较好的泛化能力。

#### Residual Block to Solve Degradation
一个过深的网络存在degradation(梯度耗散)的问题，网络深度增加performance会不升反降。在点云分类问题中，一个很deep的网络是必要的，但过深网络很快导致a higher training error, Kaiming He 将其称为degradation(梯度消失)(Deep Residual Learning for Image Recognition, Kaiming He)。我们在前期实验中也在点云数据上验证了这一点。Kaiming He提出的Deep Residual Network很好地解决了degradation的问题。本文借鉴了他的思想，在神经元间进行了搭接,使用了一些Residual Block的结构。

#### LSTM Cell for remembering point sequence
我们在Deep Residual RNN网络中使用LSTM神经元，避免Gradient Vanishing,使网络获得长期记忆的能力，在输入一个较长的点序列后，网络有理解前后点联系间关联的能力，使之在参数发生突变时，意识到输入点的类型可能发生了改变。

#### Deep Neural Network Classifier
*[?]为什么deep learning在本问题上优于SVM*
https://www.quora.com/What-are-the-advantages-of-different-classification-algorithms  
多个尺度的空间特征和Intensity、颜色特征在第二部分网络中竞争，并由网络筛选、融合、提取出合适的高层次特征，再由网络最终给出分类。由于特征信息来自于不同类型、不同尺度的识别对象，因此要求在高维空间中作出多种分类；且为了得到有效的特征，classifier本身需要有向特征提取网络回传参数的能力，进而才能对特征提取网络作出优化。为了得到一个可以整合进特征提取网络、可多分类、泛化能力强、适用于不同场景分类问题的分类器，我们选择了一个Deep Neural Network Classifier。

#### Synthesize Semantic features(representations)
对网络进行预训练，使之在特定位置收敛得到几个空间结构的显著特征，如法向量、spin图，可以有效缩短训练时间。(可看效果考虑加不加)


## Experiment:

1.Stanford indoor dataset (12 classes)

纯RNN泛化能力较差，训练慢，精度欠佳。


2.ETH Zurich数据 (8 classes)

3.Tianjin 遥感数据 (4 classes)

与SVM,传统特征提取+CRF,普通RNN, etc 方法分别进行对比。

## Conclusion:

我们提出的点云分类自动化处理框架相较于传统方法有更高的准确度。第一部分网络在特征提取上可以获得更为完整有效的空间信息，从而为分类提供更可靠的依据，对网络进行预训练提高了在不同场景下分类的学习效率。第二部分网络较传统分类器可以更智能合理地整合特征信息，进一步融合提炼，得到更高准确度的结果。
