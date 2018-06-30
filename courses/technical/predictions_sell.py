# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:32:52 2018

@author: PRATHAMESH
"""
from technical.models import StockPredictSell
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import csv

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Split a dataset into a train and test set
def train_test_split(dataset, split):
    train = list()
    train_size = split * len(dataset)
    print(train_size)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    print(len(actual))
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        # print("Prediction error for:" +str(actual[i]) +"is " + str(prediction_error))
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
    train, test = train_test_split(dataset, split)
    test_set = list()
    test = StockPredictSell.objects.all().values('sell_price')
    for i in test:
        test_set.append([i['sell_price']])

    # print("test:",test_set)
    # print("train:",train)
    predicted = algorithm(train, test_set, *args)
    # print("Predicted:",predicted)
    actual = [row[-1] for row in test_set]
    # print("Actual:", actual)
    rmse = rmse_metric(actual, predicted)
    return predicted

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + b1 * row[0]
        predictions.append(yhat)
    return predictions

# Simple linear regression on stock dataset
seed(1)
def start_prediction_sell():
    dataset = list()
    with open('/var/www/transactions/courses/technical/sell_data.csv', 'rb') as f:
        data = csv.reader(f)
        for i in data:
            dataset.append(i)
        del dataset[0]

    for i in range(len(dataset[0])):
        str_column_to_float(dataset, i)

# evaluate algorithm
    split = 1.0
    rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
    return rmse
#sets = train_test_split(dataset, split)
