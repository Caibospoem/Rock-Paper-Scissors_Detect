# 训练一个自己的目标检测模型

## 1.数据集准备

> 我这里使用的是这个网站 <a href="https://app.roboflow.com/" title="roboflow">Roboflow</a>

在这个网站里可以找到一些已经标注好的数据集和一些训练好的模型，我这边只使用这个网站的数据标注功能。

在Versions就可以将已经标注好的数据进行导出。

记得导出前可以划分训练集、测试集和验证集。

<img src="https://raw.githubusercontent.com/Caibospoem/IMAGE/main/2024/12/image-20241224145119181.png" alt="image-20241224145119181" style="zoom: 50%;" />

按照如下步骤导出格式的为YOLOv8，并下载压缩包。

<img src="https://raw.githubusercontent.com/Caibospoem/IMAGE/main/2024/12/image-20241224145241379.png" alt="image-20241224145241379" style="zoom: 33%;" />

## 2.训练模型

下载下来的压缩包有如下组成，将其解压到工作目录。

<img src="https://raw.githubusercontent.com/Caibospoem/IMAGE/main/2024/12/image-20241224145629226.png" alt="image-20241224145629226" style="zoom:50%;" />

我们先打开data.yaml文件做如下更改

```yaml
# 由我们没有指定测试集，所以我们把测试集的路径删除，然后将指定训练集和验证集的路径。
train: /yolov8/detect/train/images
val: /yolov8/detect/valid/images
# test: ../test/images

# 这里是我们的类别标签。
nc: 3
names: ['Paper', 'Rock', 'Scissors']

# 这个不需要修改，默认即可。
roboflow:
  workspace: lab-ilth7
  project: rock-paper-scissors-sxsw-9yqvv
  version: 2
  license: Private
  url: https://universe.roboflow.com/lab-ilth7/rock-paper-scissors-sxsw-9yqvv/dataset/2


# 然后我们在终端输入如下命令：
# yolo task=detect mode=train model=/yolov8/detect/yolov8n.pt data=/yolov8/detect/data.yaml epochs=20 workers=0 imgsz=640

# 首先他会在YOLO官网下载模型参数
# 随后，程序会自动开始训练，并在训练过程中保存模型。

# 然后，我们新建一个test.py文件来进行模型的测试。
```

## 3.模型的测试

训练完成后我们会得到一个runs文件夹，里面记录了模型训练的相关信息。

打开test.py 进行模型的测试