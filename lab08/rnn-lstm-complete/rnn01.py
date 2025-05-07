import numpy as np
from keras.layers import SimpleRNN

#tworzenie danych wejściowych 
# 32 – liczba próbek w batchu,
# 10 – liczba kroków czasowych (sekwencja) („głębokość sięgania w przeszłość”),
# 8 – liczba cech (features) na każdy krok, wielkość_inputu_x

inputs = np.random.random([32, 10, 8]).astype(np.float32)
print("Inputs: ")
print(inputs)

# recurrent neural network
simple_rnn = SimpleRNN(4) #4 neurony

output = simple_rnn(inputs)  # The output has shape `[32, 4]`.
print("Output: ")
print(output)

simple_rnn = SimpleRNN(
    4, return_sequences=True, return_state=True)

# whole_sequence_output has shape `[32, 10, 4]`.
# final_state has shape `[32, 4]`.
whole_sequence_output, final_state = simple_rnn(inputs)