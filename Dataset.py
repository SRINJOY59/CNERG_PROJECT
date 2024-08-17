import numpy as np
data = np.load('BIOS_14k.npy')
Train_data = data[:10000]
dev_data = data[10000:12000]
test_data = data[12000:]
import pandas as pd
df_train = pd.DataFrame(Train_data)
df_dev = pd.DataFrame(dev_data)
df_test = pd.DataFrame(test_data)
df_train = df_train.rename(columns={0: 'Bio', 1: 'Profession', 2: 'Gender'})
df_dev = df_dev.rename(columns={0: 'Bio', 1: 'Profession', 2: 'Gender'})
df_test = df_test.rename(columns={0: 'Bio', 1: 'Profession', 2: 'Gender'})
df_train.to_csv("BIOS_train.csv")
df_dev.to_csv("BIOS_dev.csv")
df_test.to_csv("BIOS_test.csv")