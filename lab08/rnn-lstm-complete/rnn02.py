import numpy as np
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN


def create_RNN(hidden_units, dense_units, input_shape, activation):
    model = Sequential()
    model.add(SimpleRNN(hidden_units, input_shape=input_shape, 
                        activation=activation[0]))
    model.add(Dense(units=dense_units, activation=activation[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

demo_model = create_RNN(2, 1, (3,1), activation=['linear', 'linear'])

wx = demo_model.get_weights()[0]  # wejściowe wagi (input -> hidden)
wh = demo_model.get_weights()[1]  # wagi rekurencyjne (hidden -> hidden)
bh = demo_model.get_weights()[2]  # bias warstwy ukrytej
wy = demo_model.get_weights()[3]  # wagi hidden -> output
by = demo_model.get_weights()[4]  # bias wyjścia

print('wx = ', wx, ' wh = ', wh, ' bh = ', bh, ' wy =', wy, 'by = ', by)

x = np.array([1, 2, 3])
# Reshape the input to the required sample_size x time_steps x features 
x_input = np.reshape(x,(1, 3, 1)) # kształt: (batch_size=1, time_steps=3, features=1)
y_pred_model = demo_model.predict(x_input)


m = 2
h0 = np.zeros(m)
h1 = np.dot(x[0], wx) + h0 + bh
h2 = np.dot(x[1], wx) + np.dot(h1,wh) + bh
h3 = np.dot(x[2], wx) + np.dot(h2,wh) + bh
o3 = np.dot(h3, wy) + by

print('h1 = ', h1,'h2 = ', h2,'h3 = ', h3)

print("Prediction from network ", y_pred_model)
print("Prediction from our computation ", o3)

# wx =  [[-0.39050508  0.14897835]]  
# wh =  [[-0.06390333 -0.9979561 ] [ 0.9979561  -0.06390327]]  
# bh =  [0. 0.]  
# wy =  [[-1.0763144] [ 1.1776732]] 
# by =  [0.]

# h1 =  [[ 1.2931546  -0.88471764]] 
# h2 =  [[ 3.59575555 -2.96776399]] 
# h3 =  [[ 7.19151086 -5.93552776]]

# Prediction from network  [[4.2757597]]
# Prediction from our computation  [[4.27575986]]
demo_model.summary()