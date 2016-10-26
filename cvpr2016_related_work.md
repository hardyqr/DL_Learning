# 2016 CVPR Related Work

1. Learning Dense Correspondence via 3D-Guided Cycle Consistency
2. Interactive Segmentation on RGBD Images via Cue Selection. 
3. Scene Recognition With CNNs: Objects, Scales and Dataset Bias. 
4. Sample and Filter: Nonparametric Scene Parsing via Efficient Filtering. 
5. DeLay: Robust Spatial Layout Estimation for Cluttered Indoor Scenes. 
6. Reversible Recursive Instance-Level Object Segmentation. 
7. Deep Sliding Shapes for Amodal 3D Object Detection in RGB-D Images. 
8. 3D Shape Attributes
9. Three-Dimensional Object Detection and Layout Prediction Using Clouds of Oriented Gradients. 
10. 3D Semantic Parsing of Large-Scale Indoor Spaces. 
11. Contour Detection in Unstructured 3D Point Clouds. 
12. Monocular 3D Object Detection for Autonomous Driving. 
13. Hierarchically Gated Deep Networks for Semantic Segmentation. 
14. CNN-RNN: A Unified Framework for Multi-Label Image Classification. 
这个思想还比较新颖，考虑的是多标签分类，因为一般的多标签都是视作多分类或者独立的，各个无相关性，这里考虑其相关性，用RNN来考虑，也是CNN+RNN。Traditional approaches to multi-label image classification learn independent classifiers for each category and employ ranking or thresholding on the classification results. These techniques, although working well, fail to explicitly exploit the label dependencies in an image. In this paper, we utilize recurrent neural networks (RNNs) to address this problem. Combined with CNNs, the proposed CNN-RNN framework learns a joint image-label embedding to characterize the semantic label dependency as well as the image-label relevance, and it can be trained end-to-end from scratch to integrate both information in an unified framework.
15. Local Background Enclosure for RGB-D Salient Object Detection
16. G-CNN: An Iterative Grid Based Object Detector. 
17. Discriminative Multi-Modal Feature Fusion for RGBD Indoor Scene Recognition. 
18. Large-Scale Semantic 3D Reconstruction: An Adaptive Multi-Resolution Model for Multi-Class Volumetric Labeling. 
19. Semantic Object Parsing With Local-Global Long Short-Term Memory. 
利用局部以及全局的LSTM做分割，这个分割是parsing， In this work, we propose a novel deep Local-Global Long Short-Term Memory (LG-LSTM) architecture to seamlessly incorporate short-distance and long-distance spatial dependencies into the feature learning over all pixel positions. In each LG-LSTM layer, local guidance from neighboring positions and global guidance from the whole image are imposed on each position to better exploit complex local and global contextual information. Individual LSTMs for distinct spatial dimensions are also utilized to intrinsically capture various spatial layouts of semantic parts in the images, yielding distinct hidden and memory cells of each position for each dimension. In our parsing approach, several LG-LSTM layers are stacked and appended to the intermediate convolutional layers to directly enhance visual features, allowing network parameters to be learned in an end-to-end way. 
20. DAG-Recurrent Neural Networks For Scene Labeling. 
21. Attention to Scale: Scale-Aware Semantic Image Segmentation. 
22. Joint Multi-view Segmentation and Localization of RGB-D Images Using Depth-Induced Silhouette Consistency. 
23. DenseCap: Fully Convolutional Localization Networks for Dense Captioning. 
24. Volumetric and Multi-View CNNs for Object Classification on 3D Data.


# DQN从入门到放弃
1. DQN 从入门到放弃1 DQN与增强学习  
https://zhuanlan.zhihu.com/p/21262246
2. DQN 从入门到放弃2 增强学习与MDP
https://zhuanlan.zhihu.com/p/21292697
3. DQN 从入门到放弃3 价值函数与Bellman方程
https://zhuanlan.zhihu.com/p/21340755
4. 
