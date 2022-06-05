[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6486884.svg)](https://doi.org/10.5281/zenodo.6486884)


# MACS 30200 Project

Author: Juno Wu

## Introduction

I want to build on past studies and add test more predictors that may predict teen pregnancy. Also, I want to test whether these predictors has different predictive power in different racial groups as the teen pregnancy rate is quite different across racial groups. Therefore, I applied Chi-square to first test whether there are correlations between the factors I assessed, the socioeconomic status, whether the young female lives in a single-parent household, whether they expect to graduate from high school, and whether they communicate with adults to the target of whether they will have teen pregnancy. Results has shown that all of them have strong correlations with the target. Then, I tested whether they could predict teen pregnancy using logistic regression, results show that all of them can predict teen pregnancy but communication with adults. I also tested how these factors act in specific racial groups and the results show that different factors may have different predictive power across racial groups.  Further analysis targeting specific racial groups and more recent data are needed to create a stronger and more predictive model for teen pregnancy.

## Dependencies

The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirement.txt file included in this repository):


```python
pip install -r requirement.txt
```

Then, you can import the project jupyter notebook in this repository to reproduce the analysis in the paper that this code supplements.
Notice that the output tables in the notebook is not presented in the paper. They have been extracted and combined on Microsoft before being presented in the paper.  

Alternatively, to reprelicate the analysis and produce all of the figures and quantitative analyses from this paper that this code supplements, build and run the Dockerfile included in this repository via the instructions in the file. 

If you use this repository for a scientific publication, we would appreciate it if you cited the [Zenodo DOI](https://doi.org/10.5281/zenodo.6486884) (see the "Cite as" section on our Zenodo page for more details).

## Results

Here, we are testing whether each variable is associated with future teen pregnancy possibility. To test this, I used Chi-square test. Here, each variable is tested independently. The results are in the graph:
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/Chisquare.png">


Then, I build simple based models with only one variables in them to predict teen pregnancy. The results are shown below:
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/single%20model.png">


We see that all the variables are significant though the significance varies in degrees. I then applied model selection process to see if adding each variable up into a single model would improve the model's performance
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/model%20selection.png">


Another important finding is that these variables do not have the same power when they are tested in different racial groups. For example, when they are tested in Hispanic group:
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/hispanic.png">


The result from black group:
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/black.png">


The result from white group:
<img src="https://github.com/macs30200-s22/replication-materials-JunoWuu/blob/main/white.png">


The results indicate that different variables may have different predictive power in different racial groups. And these predictors from as early as when individuals are in 8th have predictive power for predicting teen pregnancy possibility. 
