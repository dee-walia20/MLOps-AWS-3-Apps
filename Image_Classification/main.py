from tensorflow.keras.applications.xception import Xception

my_model = Xception(weights="imagenet", input_shape=(299,299,3))

my_model.save('model.h5')
print("Model saved in dir")