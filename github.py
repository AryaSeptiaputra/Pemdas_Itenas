import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print(df)
print()

# Kenaikan Gaji 5%
for a, row in df.iterrows():
    df.loc[a, 'Kenaikan Gaji 5%'] = (lambda gaji: int(gaji + (gaji * 0.05)))(row['Gaji'])
    
print(df)
print('Karyawan mendapatkan kenaikan gaji sebesar 5 persen dari jumlah gaji mereka\n')

# Kenaikan Gaji 2%
for a, row in df.iterrows():
    df.loc[a, 'Kenaikan Gaji 2%'] = (lambda gaji, umur: int(gaji + (gaji * 0.02)) if umur > 30 else int(gaji))(row['Kenaikan Gaji 5%'], row['Usia'])

data_terbaru=df.copy()

df_terbaru=pd.DataFrame(data_terbaru)

# Menampilkan DataFrame yang sudah diperbarui
print(df_terbaru)
print('Karyawan yang berusia diatas 30 tahun mendapatkan kenaikan gaji sebesar 2 persen dari jumlah gaji mereka')
