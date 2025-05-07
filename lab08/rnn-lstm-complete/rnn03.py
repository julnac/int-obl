from pandas import read_csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt

# Parameter split_percent defines the ratio of training examples
def get_train_test(url, split_percent=0.8):
    df = read_csv(url, usecols=[1], engine='python')   # Wczytaj tylko 2. kolumnę (indeks 1) z CSV z internetu
    data = np.array(df.values.astype('float32'))       # Konwertuj dane na float32 i NumPy array
    scaler = MinMaxScaler(feature_range=(0, 1))        # Przygotuj skalowanie danych do zakresu 0–1
    data = scaler.fit_transform(data).flatten()        # Zastosuj skalowanie i spłaszcz dane (1D array)
    n = len(data)                                       # Długość danych
    split = int(n*split_percent)                        # Oblicz punkt podziału danych (np. 80%)
    train_data = data[range(split)]                     # Dane treningowe do split
    test_data = data[split:]                            # Dane testowe od split do końca
    return train_data, test_data, data                  # Zwróć dane treningowe, testowe i wszystkie
 
# Prepare the input X and target Y
def get_XY(dat, time_steps):
    Y_ind = np.arange(time_steps, len(dat), time_steps) # Indeksy celu Y co `time_steps` kroków
    Y = dat[Y_ind]                                      # Wartości Y
    rows_x = len(Y)                                     # Liczba sekwencji
    X = dat[range(time_steps*rows_x)]                   # Dane X do wytrenowania Y
    X = np.reshape(X, (rows_x, time_steps, 1))          # Przekształć X do formatu (batch, time_steps, 1)
    return X, Y                                          # Zwróć dane X i Y
 
def create_RNN(hidden_units, dense_units, input_shape, activation):
    model = Sequential()
    model.add(SimpleRNN(hidden_units, input_shape=input_shape, activation=activation[0]))
    model.add(Dense(units=dense_units, activation=activation[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
 
def print_error(trainY, testY, train_predict, test_predict):    
    # Error of predictions
    train_rmse = math.sqrt(mean_squared_error(trainY, train_predict))
    test_rmse = math.sqrt(mean_squared_error(testY, test_predict))
    # Print RMSE - błąd średniokwadratowy
    print('Train RMSE: %.3f RMSE' % (train_rmse))
    print('Test RMSE: %.3f RMSE' % (test_rmse))    
 
# Plot the result
def plot_result(trainY, testY, train_predict, test_predict):
    actual = np.append(trainY, testY)
    predictions = np.append(train_predict, test_predict)
    rows = len(actual)
    plt.figure(figsize=(15, 6), dpi=80)
    plt.plot(range(rows), actual)
    plt.plot(range(rows), predictions)
    plt.axvline(x=len(trainY), color='r')
    plt.legend(['Actual', 'Predictions'])
    plt.xlabel('Observation number after given time steps')
    plt.ylabel('Sunspots scaled')
    plt.title('Actual and Predicted Values. The Red Line Separates The Training And Test Examples')
    filename = 'rnn_plot.png'
    plt.savefig(filename)
    plt.close()

sunspots_url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-sunspots.csv'
time_steps = 12 #12 miesięcy → 1 miesiąc
train_data, test_data, data = get_train_test(sunspots_url)
trainX, trainY = get_XY(train_data, time_steps)
testX, testY = get_XY(test_data, time_steps)
 
# Create model and train
model = create_RNN(hidden_units=3, dense_units=1, 
                   input_shape=(time_steps,1), 
                   activation=['tanh', 'tanh'])
model.fit(trainX, trainY, epochs=20, batch_size=1, verbose=2)
 
# make predictions
train_predict = model.predict(trainX)
test_predict = model.predict(testX)
 
# Print error
print_error(trainY, testY, train_predict, test_predict)
 
#Plot result
plot_result(trainY, testY, train_predict, test_predict)

# Train RMSE: 0.063 RMSE
# Test RMSE: 0.105 RMSE