# Data and Algorithmic Bias in Recommender Systems
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Dependency Status](https://david-dm.org/boennemann/badges.svg)](https://david-dm.org/boennemann/badges)
[![Open Source Love](https://badges.frapsoft.com/os/gpl/gpl.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[Ludovico Boratto](https://www.ludovicoboratto.com/)<sup>1</sup> and [Mirko Marras](https://www.mirkomarras.com/)<sup>2</sup>
<br/><sup>1</sup> EURECAT, Spain<br/>
<sup>2</sup> University of Cagliari, Italy 

A Python toolbox for experimenting with data and algorithmic bias in recommender systems. 

## Installation

Install Python (>=3.6):
```
sudo apt-get update
sudo apt-get install python3.6
```

Clone this repository:
```
git clone https://github.com/biasinrecsys/umap2020.git
```

Install the requirements:

```
cd umap2020
pip install -r requirements.txt
```

## Getting Started

#### Notebook 1: Design and evaluation of a recommendation algorithm [[Colab link]](http://bit.ly/BiasInRecSysTutorial-NB1-UMAP2020)
In this notebook, we become familiar with the Python recommendation toolbox, in the simplest 
possible way. First, we setup the working environment in GDrive. Then, we go through the 
experimental pipeline, by:

- loading the Movielens 1M dataset;
- performing a train-test splitting;
- creating a pointwise / pairwise / random / mostpop recommendation object;
- training the model (if applicable);
- computing the user-item relevance matrix;
- calculating some of the recommendation metrics (e.g., NDCG, Item Coverage, Diversity, Novelty).

The trained models, together with the partial computation we will save (e.g., user-item relevance 
matrix or metrics), will be the starting point of the investigation and the treatment covered by 
the other Jupyter notebooks.

#### Notebook 2: Investigation on item popularity bias [[Colab link]](http://bit.ly/BiasInRecSysTutorial-NB2-UMAP2020)

This notebook will outline a short study of item popularity in recommender systems. We assume 
that the number of ratings is a proxy of the popularity of the item. First, we will compare 
the characteristics of the items recommended by pairwise, pointwise, random and mostpop strategies.
Then, we will show how to setup and perform a post-processing mitigation approach against popularity. 

#### Notebook 3: Investigation on item provider fairness [[Colab link]](http://bit.ly/BiasInRecSysTutorial-NB3-UMAP2020)

This notebook will consider the directors of movies in Movielens 1M as the item providers and 
investigates how unfairness based on gender groups affects providers' group visibility and 
exposure with respect to their representation in the item catalog. Then, we introduce a
pre-processing strategy that upsamples interations involving items of a minority group to 
improve fairness, while resulting in a small loss in utility. 

## Contribution
This code is provided for educational purposes and aims to facilitate reproduction of our results, and further research 
in this direction. We have done our best to document, refactor, and test the code before the tutorial.

If you find any bugs or would like to contribute new models, training protocols, etc, please let us know.

Please feel free to file issues and pull requests on the repo and we will address them as we can.

## Citations

If you find our code useful in your work, please reference the studies that led to them:

Notebook 1:

```
@inproceedings{boratto2019effect,
  title={The effect of algorithmic bias on recommender systems for massive open online courses},
  author={Boratto, Ludovico and Fenu, Gianni and Marras, Mirko},
  booktitle={European Conference on Information Retrieval},
  pages={457--472},
  year={2019},
  organization={Springer}
}
```

Notebook 2:

```
@article{boratto2020connecting,
  title={Connecting User and Item Perspectives in Popularity Debiasing for Collaborative Recommendation},
  author={Boratto, Ludovico and Fenu, Gianni and Marras, Mirko},
  journal={arXiv preprint arXiv:2006.04275},
  year={2020}
}
```

Notebook 3:

```
@article{boratto2020interplay,
  title={Interplay between Upsampling and Regularization for Provider Fairness in Recommender Systems},
  author={Boratto, Ludovico and Fenu, Gianni and Marras, Mirko},
  journal={arXiv preprint arXiv:2006.04279},
  year={2020}
}
```

## License
This code is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for details.

You should have received a copy of the GNU General Public License along with this source code. If not, go the following link: http://www.gnu.org/licenses/.


