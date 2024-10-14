import tensorflow as tf

# 列出所有可用的物理 GPU
gpus = tf.config.list_physical_devices('GPU')

if gpus:
    print(f"可用的 GPU 數量: {len(gpus)}")
    for gpu in gpus:
        print(f"GPU: {gpu}")
else:
    print("未檢測到可用的 GPU")
