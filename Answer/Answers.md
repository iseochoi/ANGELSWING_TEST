# ANGELSWING DEVELPMENT TEST

This repository represents the submission of ANGELSWING DEVELPMENT TEST.


----------
## Qustion 1

According to our research, a machine learning algorithm has an accuracy of 80%. However, when we applied the algorithm to practical use, the accuracy was below the expected accuracy. Describe two or more causes to this.

## > Answer
The first reason is overfitting. If the complexity of the model becomes excessively high during the training process, performance may decrease in practical use. To prevent this, various methods exist, for example, regularization, early stopping, learning rate scheduling, drop out, k-fold ensemble, etc.

The second reason is the lack of train datasets. Therefore, data augmentation techniques are usually applied. However, if appropriate data augmentation techniques are not applied, the model exhibits inconsistent predictions on some subgroups of data.



------
## Qustion 2
Please suggest and describe two industry applicable Deep Learning projects you would carry out using a dataset of aerial images.

## > Answer
First, I propose a program that draws out the optimal solution for Tower crane layout planning (TCLP). TLCP is one of the important decisions in the large-scale construction project. The site manager should establish TCLP in consideration of numerous constraints such as site conditions, lifting targets, and T/C specifications. Since there is a gap between the site drawing and the actual site, it is necessary to find the optimal TCLP based on the actual site. Therefore, a model that derives the optimal TCLP by applying reinforcement learning will be quite helpful.

Second, I propose a process control program for construction sites. Pre-con can be performed through aerial photography of the construction site. Through the pretrained model, it automatically calculates the optimal due for unit process and establishes optimal construction plan. The proposed model can present a dense construction plan as construction progresses. Also, it can be applied as an evolved model in a similar project of that company.


----------
## Qustion 3
You have a large data set consisting of high-resolution aerial orthophotos. Your objective is to create an API that detects small objects within an orthophoto (e.g. Trees, Cars, People, etc). Please explain how you would create a Deep Learning Pipeline by elaborating on how you would approach the following steps. (No more than 300 words in total)

## > Answer
### 1. Data Preprocessing/labeling:
  - First, I would set the standard for normal data and remove the inconsistent data. Additionally, I would convert the data to a Hadoop format that is easy to manage high-resolution images. 
  - I would annotate the image manually using annotation tools such as YOLO mark. However, the work would be time-consuming. So, I would obtain pseudo-labeled images with high confidence through pretrained model.
### 2. Model selection:
  - It might vary depending on the purpose of serving. In my case, I would choose YOLOv5. The reason is that YOLOv5 has high performance with the fastest prediction speed among the latest models. In addition, it has a well-written code base, so it is convenient to apply various alternatives according to purpose of the project.
### 3. Model training
  - I would decide whether to train the model in parallel according to the computing power. Then I would set priorities according to the purpose and combine metrics accordingly.
### 4. Model optimization/hyperparameter tuning
  - I would apply Bayesian optimization by setting the appropriate range. In some cases, AutoML can be used. Then I would try to manually tune the model for practical use.
  - I would apply pruning and quantization methods for model optimization.

### 5. Model hosting/deployment/management
- If the purpose is simply detecting images, I would deploy using Flask. However, I would try to use TorchServe framework and MLflow for continuous MLOps lifecycle management. But I haven't tried it with large images yet. 
