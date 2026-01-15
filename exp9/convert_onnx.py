import joblib
import numpy as np
import time
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as ort
from sklearn.linear_model import LinearRegression

# train a small model
X = np.array([[1],[2],[3],[4],[5]], dtype=np.float32)
y = np.array([2,4,6,8,10], dtype=np.float32)
model = LinearRegression().fit(X, y)

joblib.dump(model, "model.pkl")

# convert to onnx
initial_type = [("float_input", FloatTensorType([None, 1]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("ONNX model saved as model.onnx")

# sklearn inference timing
test = np.random.rand(10000,1).astype(np.float32)
t1 = time.time()
_ = model.predict(test)
t2 = time.time()
print("Sklearn inference time:", t2 - t1)

# ONNX runtime inference timing
sess = ort.InferenceSession("model.onnx", providers=["CPUExecutionProvider"])
input_name = sess.get_inputs()[0].name

t3 = time.time()
_ = sess.run(None, {input_name: test})
t4 = time.time()
print("ONNX runtime inference time:", t4 - t3)
