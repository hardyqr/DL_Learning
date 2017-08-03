### What is `Softmax`

[Softmax 函数的特点和作用是什么？](https://www.zhihu.com/question/23765351)

- SVM只选自己喜欢的男神，`Softmax`把所有备胎全部拉出来评分，最后还归一化一下

- 看名字就知道了，就是如果某一个$z_j$大过其他$z$,那这个映射的分量就逼近于1,其他就逼近于0，主要应用就是多分类，`sigmoid`函数只能分两类，而`softmax`能分多类，`softmax`是`sigmoid`的扩展。


[softmax算法为什么采用softmax function作为每一个类别的概率？](https://www.zhihu.com/question/29435973)

本质上，linear，Logistic，Softmax 都是一个东西推导出来的。就是广义线性模型。
这些分布之所以长成这个样子，是因为我们对y进行了假设。
当y是正太分布-------->linear model
当y是两点分布-------->Logistic model
当y是多项式分布-------->Softmax
只要y的分布是指数分布族的（还有若干假设），都可以用一种通用的方法推导出h(x)。
所以你去了解一下广义线性模型，他推导出来就是这个样子的。

[Softmax回归](http://ufldl.stanford.edu/wiki/index.php/Softmax%E5%9B%9E%E5%BD%92)
