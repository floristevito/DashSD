# DashSD
This project uses <a href="https://pysd.readthedocs.io/en/master/">PySD</a> and <a href="https://dash.plotly.com/">Dash</a> Dash to simulate a System Dynymics model build in <a href="https://vensim.com/">Vensim</a> and visualize the results on a interactive dashboard. The SD model is build in the context of the Bachelor final project. The goal of this research is to inform policymakers at the MWRI best about possible effects of improved irrigation efficiency. In consideration of this goal, a interactive dashboard using Python is build to enable policymakers to simulate the constructed model in this research without any additional knowledge requirements about simulations and visualizations. Furthermore, the dashboard enables policymakers to test a wide range of variations in model input combinations, since the model is simulated in real time.

# Dependencies
This project uses a couple of external resources in order to contruct the interactive dashboard:

PySD version 0.10.0 (<a href="https://pysd.readthedocs.io/en/master/">Can be found here</a>) <br>
Dash version 1.12.0 (<a href="https://dash.plotly.com/">Can be found here</a>) <br>
Python version 3.7.7 <br>
Dash stylesheet made by Chris P (<a href="https://codepen.io/chriddyp/pen/dZVMbK">Can be found here</a>) <br>

# Usage
A live version of the interactive dashboard (<a href="https://dash.plotly.com/">can be found here</a>). This version simulates the SD model in real time, making it possible for the user to select any combination of input variables. 

# Source
All source code is include in this repository in the folder named “source”. This folder includes both a standard Python file (.py) of the code ass well as a python Jupyter Notebook file (.ipynb). The latest version of the constructed SD model and a copy of the thesis is included in this folder as well. 

# Further research
This interactive dashboard can be modified to be used for any further research. In order to do so, download the included source files from this repository and install the dependencies as listed above. 
