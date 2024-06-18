import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib_venn import venn2

# Data
data = {
    'Tanggal': ['1 Januari 2024', '1 Januari 2024', '1 Januari 2024', '1 Januari 2024', '1 Januari 2024',
                '1 Januari 2024', '1 Januari 2024', '1 Januari 2024', '1 Januari 2024', '1 Januari 2024'],
    'Maskapai': ['Garuda Indonesia', 'Lion Air', 'AirAsia', 'Singapore Airlines', 'Qatar Airways',
                 'Citilink', 'Emirates', 'Thai Airways', 'Batik Air', 'Cathay Pacific'],
    'Rute': ['Jakarta - Surabaya', 'Jakarta - Denpasar', 'Kuala Lumpur - Jakarta', 'Singapore - Bali', 'Doha - Jakarta',
             'Jakarta - Medan', 'Dubai - Jakarta', 'Bangkok - Denpasar', 'Jakarta - Makassar', 'Hong Kong - Jakarta'],
    'Jenis Tiket': ['Domestik', 'Domestik', 'Internasional', 'Internasional', 'Internasional',
                    'Domestik', 'Internasional', 'Internasional', 'Domestik', 'Internasional'],
    'Jumlah Penjualan': [120, 95, 80, 65, 45, 110, 55, 70, 85, 60],
    'Harga Taksiran (USD)': [110, 100, 150, 200, 300, 90, 250, 180, 95, 280]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Maskapai', y='Jumlah Penjualan', hue='Jenis Tiket', data=df, s=100, palette='bright')
plt.title('Penjualan Tiket Pesawat pada Tanggal 1 Januari 2024')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('scatterplot.png')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Jumlah Penjualan'], bins=5, kde=True, color='skyblue')
plt.title('Distribusi Jumlah Penjualan Tiket Pesawat')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(df.groupby('Jenis Tiket')['Jumlah Penjualan'].sum(), labels=df['Jenis Tiket'].unique(),
        autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'], startangle=140)
plt.title('Persentase Penjualan Tiket Pesawat berdasarkan Jenis Tiket')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Maskapai', y='Jumlah Penjualan', hue='Jenis Tiket', data=df, palette='pastel')
plt.title('Penjualan Tiket Pesawat berdasarkan Maskapai')
plt.xlabel('Maskapai')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# Line chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='Maskapai', y='Harga Taksiran (USD)', hue='Jenis Tiket', data=df, palette='Set1', marker='o')
plt.title('Harga Taksiran Tiket Pesawat per Maskapai')
plt.xlabel('Maskapai')
plt.ylabel('Harga Taksiran (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line_chart.png')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Jenis Tiket', y='Harga Taksiran (USD)', data=df, palette='Set3')
plt.title('Distribusi Harga Taksiran Tiket Pesawat berdasarkan Jenis Tiket')
plt.xlabel('Jenis Tiket')
plt.ylabel('Harga Taksiran (USD)')
plt.tight_layout()
plt.savefig('boxplot.png')
plt.show()

# Diagram Venn (contoh dengan dua set)
set1 = set(df[df['Jenis Tiket'] == 'Domestik']['Maskapai'])
set2 = set(df[df['Jenis Tiket'] == 'Internasional']['Maskapai'])

plt.figure(figsize=(6, 6))
venn2([set1, set2], ('Domestik', 'Internasional'))
plt.title('Diagram Venn Jenis Tiket Pesawat')
plt.tight_layout()
plt.savefig('venn_diagram.png')
plt.show()
