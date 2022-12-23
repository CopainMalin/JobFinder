#!/bin/bash

# Création et installation de l'environnement anaconda sur la machine utilisée
set -euo pipefail 

conda create -y --name jobfinderenv python=3.7 pip numpy pip pandas 
conda activate jobfinderenv
conda install -c numpy
conda install -c pandas 