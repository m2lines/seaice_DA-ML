# Learning sea ice model errors from data assimilation increments

This repository is part of the larger [M2LInES](https://m2lines.github.io) project. M2LInES involves developing climate model parameterizations using machine learning, in order to improve phyiscs and reduce systematic model biases. Here we use Convolutional Neural Networks to derive a mapping from model state variables to sea ice concentration analysis increments from an ice-ocean data assimilation experiment. The model which this study has been applied to is an ice-ocean configuration of the Geophysical Fluid Dynamics Laboratory (GFDL) Seamless system for Prediction and EArth system Research (SPEAR) model.

### Offline learning

The `offline_learning` folder contains code and data relating to the article [Gregory et al., 2023a](https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2023MS003757), with an example jupyter notebook of how the CNN was trained and model selection performed by carrying out 5-fold cross-validation tests. 

### Online ice-ocean

The `online_iceocean` folder contains example scripts of how to implement the trained CNN into SPEAR ice-ocean simulations, by updating the sea ice restart files, as a way to correct short-forecasts. This methodology is outlined in the article [Gregory et al., 2023b](https://arxiv.org/pdf/2310.02488.pdf).


To cite the code please use the Zenodo DOI: [![DOI](https://zenodo.org/badge/604827831.svg)](https://zenodo.org/badge/latestdoi/604827831)
