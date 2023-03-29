from numpy import loadtxt
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras.layers import Dense

# Load the data
dataset = loadtxt('dataset\pima-indians-diabetes.data.csv', delimiter=',')

x = dataset[:,0:-1]
y = dataset[:,-1]

# Splitting the dataset into the Training set, Validate set, Test set: 0.6 0.2 0.2
X_train_val, X_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.2, random_state=0)

def train_model(X_train, y_train, X_val, y_val):
    model = Sequential()

    # building the model
    # 1 Neural network include: Input Layer, n x Hidden Layer, Output Layer
    # Here, I build the model with 1 input layer (8 neural), 2 hidden layer (16 & 8 neural) and 1 output layer (1 neural).
    # Activation function is non-linear function. (Ex: sigmoid, tanh, relu, elu, Maxout, LeakyRelu -> ex1.jpg) 
    model.add(Dense(16, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.summary()

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=16)
    model.save("models\model.h5")

if __name__ == "__main__":
    train_model(X_train, y_train, X_val, y_val)