import random
import json
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

def feature(datum):
    '''
    :param: datum, yelp review item
    :type: dict
    
    '''
    feat = [1]
    attributes = datum['attributes']
    if 'BusinessAcceptsCreditCards' in attributes and attributes['BusinessAcceptsCreditCards'] == True:
        feat.append(1)
    else:
        feat.append(0)
    if 'GoodForKids' in attributes and attributes['GoodForKids'] == True:
        feat.append(1)
    else:
        feat.append(0)
    if 'HappyHour' in attributes and attributes['HappyHour'] == True:
        feat.append(1)
    else:
        feat.append(0)
    if 'HasTV' in attributes and attributes['HasTV'] == True:
        feat.append(1)
    else:
        feat.append(0)
    if 'GoodForGroups' in attributes and attributes['GoodForGroups'] == True:
        feat.append(1)
    else:
        feat.append(0)
    if 'RestaurantsPriceRange2' in attributes:
        feat.append(attributes['RestaurantsPriceRange2'])
    else:
        feat.append(0)
    if 'BusinessParking' in attributes and (attributes['BusinessParking']['garage'] or attributes['BusinessParking']['lot'] or attributes['BusinessParking']['street']):
        feat.append(1)
    else:
        feat.append(0)
    return feat

def MSE(theta, X, y):
    '''
    :param: X,test feature set
    :type: list
    :param: y,test label set
    :type: list
    :param: theta
    :type: list
    '''
    theta = np.matrix(theta).T
    X = np.matrix(X)
    y = np.matrix(y).T
    diff = X*theta - y
    diffSq = diff.T*diff
    diffSqReg = diffSq / len(X)
    return diffSqReg.flatten().tolist()[0][0]

def decision_tree_regression(X, y, X_test):
    '''
    :param: X,training feature set
    :type: list
    :param: y ,training label set
    :type: list
    :param: X_test,test feature set
    :type: list
    '''
    
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X, y)
    return regressor.predict(X_test)

#import data
data1 = []
for line in open('business.json','r'): 
     data1.append(json.loads(line))
   
#Filtering based on categories
x =[]
for d in data1:
    if (d['stars'] ):
        cat = d['categories']
        for c in cat:
            if (c == 'Restaurants'):
                x.append(d)
#shuffle data            
random.shuffle(x)
#split into training and test sets
train_data = x[0:43695]
test_data = x[43695:]
X = [feature(d) for d in train_data]
y = [d['stars'] for d in train_data]
X_test = [feature(d) for d in test_data]
y_test = [d['stars'] for d in test_data]

#Model_1: globalAverage
allRatings = []
for l in train_data:
    allRatings.append(l['stars'])    
globalAverage = sum(allRatings) / len(allRatings)

rate = []
for l in test_data:
     rate.append(l['stars'])
     
squareError = 0
for r in rate:
    squareError += (r - globalAverage)**2
mse_m1 = squareError / (len(rate))
print 'mse of model_1:',mse_m1



#Model_2: regression
theta,residuals,rank,s = np.linalg.lstsq(X, y)
mse_m2=MSE(theta,X_test,y_test)
print 'mse of model_2',mse_m2



#Model_3: decesion_tree regression
y_pred = decision_tree_regression(X,y,X_test)
mse_m3=mean_squared_error(y_test, y_pred)
print 'mse of model_3:',mse_m3