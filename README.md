# DashSD
This project uses <a href="https://pysd.readthedocs.io/en/master/">PySD</a> and <a href="https://dash.plotly.com/">Dash</a> to simulate a System Dynamics model build in <a href="https://vensim.com/">Vensim</a> and visualizes the results on an interactive dashboard. The SD model is built in the context of a bachelor final project on effects of irrigation efficiency improvements in Egypt. This research is performed in the context of the Technology, Policy and Management bachelor thesis program of the Technical University Delft. The goal of this research is to inform local policymakers in Egypt best about possible effects of improved irrigation efficiency. In consideration of this goal, an interactive dashboard using Python is built to enable policymakers to simulate the constructed model in this research without any additional knowledge requirements about simulations and visualizations. Furthermore, the dashboard enables policymakers to test a wide range of variations in model input combinations, since the model is simulated in the background (PySD) in real time.

# Dependencies
This project uses a couple of external resources in order to construct the interactive dashboard:

PySD version 0.10.0 (<a href="https://pysd.readthedocs.io/en/master/">Can be found here</a>) <br>
Dash version 1.12.0 (<a href="https://dash.plotly.com/">Can be found here</a>) <br>
Dash stylesheet made by Chris P (<a href="https://codepen.io/chriddyp/pen/dZVMbK">Can be found here</a>) <br>
Python version 3.7.7 <br>

# Usage
A live version of the interactive dashboard <a href="http://dashsd.herokuapp.com/">can be found here</a>. This version simulates the SD model in real time, making it possible for the user to select any combination of input variables. 

![Alt text](AdditionalSources/DashSDScreenshot.jpg?raw=true "Live version")

# Source
All the needed python code is included in the "app.py" file in the root of this repository. An extensive list of all requirements is included in the "requirements.txt" file. 
Additional sources are include in this repository in the folder named “AdditionalSources”. This folder includes a python Jupyter Notebook file (.ipynb), with all the code of the main python app with some additional data exploring and a more stepwise approach. This file might help when exploring the code. 

# Further research
This interactive dashboard can be modified to be used for any further research. In order to do so, download the included source files from this repository and install the dependencies as listed above. 
