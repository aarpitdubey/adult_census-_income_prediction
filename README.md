## Problem Statement:
 The Goal is to predict whether a person has an income of more than 50K a year or not.

 This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.



### Approach: 
The classical machine learning tasks like Data Exploration, Data Cleaning,
Feature Engineering, Model Building and Model Testing. Try out different machine
learning algorithms that’s best fit for the above case.

2

### Dataset:
Dataset Link :- Dataset
Project Evaluation metrics:

### Code:
• You are supposed to write a code in a modular fashion

• Safe: It can be used without causing harm.

• Testable: It can be tested at the code level.

• Maintainable: It can be maintained, even as your codebase grows.

• Portable: It works the same in every environment (operating system)

• You have to maintain your code on GitHub.

• You have to keep your GitHub repo public so that anyone can check your code.

• Proper readme file you have to maintain for any project development.

• You should include basic workflow and execution of the entire project in the readme
file on GitHub

• Follow the coding standards: https://www.python.org/dev/peps/pep-0008/

### Database:
• You are supposed to use a given dataset for this project which is a Cassandra
database.
• https://astra.dev/ineuron

### Cloud:
• You can use any cloud platform for this entire solution hosting like AWS, Azure or
GCP

### API Details or User Interface:
• You have to expose your complete solution as an API or try to create a user
interface for your model testing. Anything will be fine for us.

### Logging:
• Logging is a must for every action performed by your code use the python logging
library for this.

### Ops Pipeline:


• If possible, you can try to use AI ops pipeline for project delivery Ex. DVC, MLflow
, Sagemaker , Azure machine learning studio, Jenkins, Circle CI, Azure DevOps ,
TFX, Travis CI

### Deployment:
• You can host your model in the cloud platform, edge devices, or maybe local, but
with a proper justification of your system design.

### Solutions Design:
• You have to submit complete solution design strategies in HLD and LLD document


### System Architecture:

• You have to submit a system architecture design in your wireframe document and
architecture document.


### Latency for model response:
• You have to measure the response time of your model for a particular input of a
dataset.

### Optimization of solutions:
• Try to optimize your solution on code level, architecture level and mention all of
these things in your final submission.

• Mention your test cases for your project.

---------------------------------------------------------

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = deployprojectatheroku@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = adult-census-ip

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
.....
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir

