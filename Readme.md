The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirement.txt file included in this repository):


```python
pip install -r requirement.txt
```

Then, you can import the analysis module located in this repository to reproduce the analysis in the (hypothetical) publication that this code supplements (in a Jupyter Notebook, like README.ipynb in this repository, or in any other Python script):


```python
import analysis 
```

You can then use the process_data function in the analysis module to process the data and get it ready to analyze. The plot function will reproduce Figure 1 from the (hypothetical) publication.


```python
df = analysis.process_data('1994.csv')
analysis.plot_data(data=df, save_fig=True, path="figure1.tiff")
```


    
![alt text](http://url/to/img.png)
    


Here, we are testing whether the variable "wheter students expect themselved to graduate from high school" is predictive for their future teen pregnancy possibility. As we can see with this large p, it is not predictive. Therefore, I will need to explore whether other variables will elicit smaller p values and whether combination of variables will be more predictive. 

If you use this repository for a scientific publication, we would appreciate it if you cited the Zenodo DOI "https://doi.org/10.5281/zenodo.6486884"(see the "Cite as" section on our Zenodo page for more details).


```python

```
