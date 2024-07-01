import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
df = pd.read_excel(r'C:\Users\lucia\downloads\encuesta_salud_madrid_2017.xlsx')


# Renombrar las columnas según sea necesario (si aún no lo has hecho)
nuevos_nombres = {
    'B1': 'Estado de salud en últimos 12 meses',
    'C1': 'Enfermedad crónica o de larga duración',
    'C2_1': 'Tensión alta',
    'C2_2': 'Infarto de miocardio, angina de pecho o enfermedad coronaria',
    'C2_3': 'Artrosis (excluyendo artritis)',
    'C2_4': 'Dolor de espalda crónico (cervical)',
    'C2_5': 'Dolor de espalda crónico (lumbar)',
    'C2_6': 'Alergia crónica',
    'C2_7': 'Asma',
    'C2_8': 'Bronquitis crónica, enfisema, EPOC',
    'C2_9': 'Diabetes',
    'C2_10': 'Úlcera de estómago o duodeno',
    'C2_11': 'Colesterol alto',
    'C2_12': 'Depresión',
    'C2_13': 'Ansiedad crónica',
    'C2_14': 'Migraña o dolor de cabeza frecuente',
    'F12_5': 'Número de veces que va al médico al año',
    'C2_15': 'Problemas de tiroides',
    'C2_16': 'Otra enfermedad crónica',
    'C2_16OS1': 'Otra enfermedad crónica especificada',
    'C3': 'Limitación en actividades por problema de salud',
    'C4': 'Uso de medicamentos en las últimas dos semanas',
    'C5_1A1': 'Uso de tranquilizantes o medicación para dormir (últimas 2 semanas)',
    'C5_1A2': 'Uso de tranquilizantes o medicación para dormir (último año)',
    'C5_1B': 'Receta de tranquilizantes o medicación para dormir',
    'C5_2A1': 'Uso de antidepresivos (últimas 2 semanas)',
    'C5_2A2': 'Uso de antidepresivos (último año)',
    'C5_2B': 'Receta de antidepresivos',
    'C5_3A1': 'Uso de medicamentos fuertes para el dolor (últimas 2 semanas)'
}

# Renombrar las columnas existentes según el diccionario
df = df.rename(columns=nuevos_nombres)


# Verificar el DataFrame con las columnas renombradas
print(df.columns)

# Crear intervalos de edad
bins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']
df['Rango de Edad'] = pd.cut(df['EDAD_C'], bins=bins, labels=labels, right=False)


# Obtener el conteo de personas por intervalo de edad
edad_counts = df['Rango de Edad'].value_counts().sort_index()


# Graficar distribución de edad con el número de personas por intervalo
plt.figure(figsize=(10, 6))
ax = sns.countplot(x='Rango de Edad', data=df, palette='viridis')
plt.title('Distribución de Edad')
plt.xlabel('Intervalo de Edad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)

# Mostrar el número de personas por encima de cada barra
for i, count in enumerate(edad_counts):
    ax.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=10)

plt.show()


# Asegurarse de que la columna 'SEXO' exista en el DataFrame
if 'SEXO' in df.columns:
    
    # Verificar la conversión (opcional)
    print(df['SEXO'].unique())

    # Obtener el conteo de personas por sexo
    sexo_counts = df['SEXO'].value_counts().sort_index()

    # Graficar la distribución de sexo
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(x='SEXO', data=df, palette='pastel')
    plt.title('Distribución de Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Frecuencia')

    # Mostrar el número de personas por encima de cada barra
    for i, count in enumerate(sexo_counts):
        ax.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=10)

    plt.show()
else:
    print("La columna 'SEXO' no existe en el DataFrame")


# Verificar la existencia de las columnas 'EDAD_INTERVALO' y 'SEXO' en el DataFrame
if 'Rango de Edad' in df.columns and 'SEXO' in df.columns:
   
    
    # Graficar distribución de sexo por intervalos de edad
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Rango de Edad', hue='SEXO', data=df, palette='pastel')
    plt.title('Distribución de Sexo por Intervalos de Edad')
    plt.xlabel('Intervalo de Edad')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.legend(title='Sexo')
    
    # Mostrar el número de personas por encima de cada barra
    for p in plt.gca().patches:
        plt.gca().annotate(f'\n{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                           ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), 
                           textcoords='offset points')

    plt.tight_layout()
    plt.show()
else:
    print("Las columnas 'Rango de Edad' y/o 'SEXO' no existen en el DataFrame")



# Verificar los valores únicos en la columna 'Depresión'
print(df['Depresión'].unique())

# Contar la frecuencia de cada valor en la columna 'Depresión'
print(df['Depresión'].value_counts())

# Graficar la distribución de la columna 'Depresión'
plt.figure(figsize=(10, 6))
ax = sns.countplot(x=df['Depresión'], palette='viridis')
plt.title('Distribución de Depresión en la Población')
plt.xlabel('Depresión (1 = Sí, 2 = No)')
plt.ylabel('Número de Personas')
plt.xticks([0, 1], ['Sí', 'No'])

# Agregar etiquetas encima de las barras
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()

# Calcular la frecuencia de cada valor en la columna 'Ansiedad'
print("Frecuencia de Ansiedad:")
print(df['Ansiedad crónica'].value_counts())

# Graficar la distribución de la columna 'Ansiedad'
plt.figure(figsize=(10, 6))
ax = sns.countplot(x=df['Ansiedad crónica'], palette='viridis')
plt.title('Distribución de Ansiedad en la Población')
plt.xlabel('Ansiedad (2 = Sí, 1 = No)')
plt.ylabel('Número de Personas')
plt.xticks([0, 1], ['No', 'Sí'])

# Agregar etiquetas encima de las barras
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()

# Calcular la frecuencia de cada valor en la columna 'Asma'
print("Frecuencia de Asma:")
print(df['Asma'].value_counts())

# Graficar la distribución de la columna 'Asma'
plt.figure(figsize=(10, 6))
ax = sns.countplot(x=df['Asma'], palette='viridis')
plt.title('Distribución de Asma en la Población')
plt.xlabel('Asma (1 = Sí, 2 = No)')
plt.ylabel('Número de Personas')
plt.xticks([0, 1], ['Sí', 'No'])

# Agregar etiquetas encima de las barras
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()



# Convertir a numérico y rellenar NaN con la media
df['Número de veces que va al médico al año'] = pd.to_numeric(df['Número de veces que va al médico al año'], errors='coerce')
mean_visitas_medicas = df['Número de veces que va al médico al año'].mean()
df['Número de veces que va al médico al año'].fillna(mean_visitas_medicas, inplace=True)

# Calcular estadísticas descriptivas después de limpiar
stats_visitas_medicas = df['Número de veces que va al médico al año'].describe()

# Calcular mediana después de limpiar
mediana_visitas_medicas = df['Número de veces que va al médico al año'].median()

# Mostrar resultados
print("Estadísticas de número de veces que va al médico al año después de limpiar:")
print(stats_visitas_medicas)
print("\nMediana de número de veces que va al médico al año después de limpiar:", mediana_visitas_medicas)