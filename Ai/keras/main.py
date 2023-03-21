from keras.models import load_model
from train_model import X_test, y_test

def main():
    model = load_model("models\model.h5")
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"loss: {loss}, accuracy: {acc}")

if __name__ == "__main__":
    main()