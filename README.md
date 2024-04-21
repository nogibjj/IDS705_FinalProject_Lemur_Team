# IDS705 Machine Learning Final Project - Lemur Team

- Bárbara Flores, Jiechen Li, Jeremy Tan, Yulei Xia

## Project Overview

**Title:** Identifying Factors Influencing Income Levels in the US  
**Objective:** Comparative analysis of machine learning models for predicting income levels, focusing on key factors influencing individuals earning more than $50,000 in the US in 1994.

## Abstract

This project examines demographic, educational, and other variables to understand what drives income levels above $50,000, distinguishing middle-class earners from others. We utilized various machine learning models including Linear Regression, Naive Bayes, Decision Trees, Neural Networks, GAM, and ensemble models like XGBoost and CatBoost. Performance was measured using Accuracy, F1 Score, and AUC ROC. SHAP and partial dependence plots helped in identifying significant variables affecting income thresholds.

## Table of Contents

- [Introduction](#introduction)
- [Background](#background)
- [Data](#data)
- [Methodology](#methodology)
- [Experiments](#experiments)
- [Conclusion](#conclusion)
- [Contributors](#contributors)
- [License](#license)

## Repository Structure

- **00_original_data/**: This folder holds all the raw datasets as obtained before any processing or cleaning.
- **01_clean_data/**: After initial preprocessing, such as one-hot encoding and handling of missing data, the cleaned datasets are stored here.
- **10_code/**: Scripts for preliminary data processing, including data cleaning and preparation of AUC curves, are located in this directory.
- **30_code/**: This directory contains all the scripts used to develop the machine learning models employed in this project.
- **40_results/**: Results from the various machine learning models, particularly AUC curves, are stored here in CSV format.
- **50_website/**: Here lies the frontend and backend code for the web application that allows users to interact with the models developed.
- **README.md**: Provides an overview of the project, including its purpose, structure, and instructions for navigating the repository.

## Introduction

This project addresses income inequalities in the US by exploring factors that influence earning capacities. Through comprehensive data analysis, we focus on identifying features that significantly affect income levels.

## Background

Reviewing decades of income data has revealed increasing disparities, influenced by policy, technological advancements, and education. This project uses datasets like the "Adult" and "Census-Income" datasets from UCI, employing advanced machine learning models to predict and understand these income variations.

## Data

The dataset includes approximately 48,000 entries from 1994, covering various demographic, educational, and occupational features essential for our analysis. The primary goal with this data is to understand factors predicting annual earnings exceeding $50,000.

## Methodology

We first clean and preprocess the data, applying techniques like one-hot encoding to prepare for machine learning models. Our selection of models aims to optimize the AUC-ROC, with a focus on ensemble models and GAM due to their superior performance.

## Experiments

### Model Development

- We tested models such as Naive Bayes, Logistic Regression, Decision Trees, GAM, Ensemble Models (Catboost and XGBoost), and Neural Networks.
- Models were evaluated using metrics suitable for imbalanced data, such as AUC-ROC, with a detailed focus on feature importance using SHAP and partial dependence plots.

### Interpretability

- SHAP values and partial dependence plots were used to understand the influence of top features like marital status, education, age, and hours worked on income.
- We emphasized transparency and interpretability in our models to facilitate understanding of the impact of each feature on the predictions.

## Conclusion

The project demonstrates that ensemble models and GAM yield the best results in predicting income levels above the middle-class threshold. Key factors identified include marital status, educational level, and age, among others. Future work could refine the model focusing on the most impactful and non-sensitive features.

## Presentation

- [Project Presentation](https://docs.google.com/presentation/d/1oio74NdTgzOLcROIZhVj2cbJUIHmBKIBLGGRZwsiwxA/edit#slide=id.g25f6af9dd6_0_0): Try our prediction model to discover your archetype by entering our website! :)
