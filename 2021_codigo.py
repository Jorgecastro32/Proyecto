import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el archivo CSV
df = pd.read_excel(r'C:\Users\lucia\downloads\encuesta_salud_madrid_2021.xlsx')

# Renombrar las variables de salud si es necesario
renombrar_salud = {
    'C1_1': 'Tensión_alta',
    'C1_2': 'Infarto_angina_coronaria',
    'C1_3': 'Artrosis',
    'C1_4': 'Dolor_espalda_cervical',
    'C1_5': 'Dolor_espalda_lumbar',
    'C1_6': 'Alergia_cronica',
    'C1_7': 'Asma',
    'C1_8': 'Diabetes',
    'C1_9': 'Colesterol_alto',
    'C1_10': 'Depresion',
    'C1_11': 'Ansiedad_cronica',
    'C1_12': 'Migraña',
    'C1_13': 'Problemas_tiroides',
    'C1_14': 'Varices',
    'C1_15': 'Cataratas',
    'C1_16': 'Problemas_piel',
    'C1_17': 'Sindrome_post_COVID',
    'C1A_V1': 'Salud_bucodental',
    'C6_V1': 'Asistencia_medica_lista_espera',
    'C7_V1': 'Asistencia_medica_colapso_sistema',
    'C8_V1': 'Posposicion_asistencia_medica_por_covid',
    'C9_V1_1': 'No_pudo_pagar_atencion_medica',
    'C9_V1_2': 'No_pudo_pagar_fisioterapia',
    'C9_V1_3': 'No_pudo_pagar_atencion_dental',
    'C9_V1_4': 'No_pudo_pagar_atencion_auditiva',
    'C9_V1_5': 'No_pudo_pagar_atencion_optica',
    'C9_V1_6': 'No_pudo_pagar_medicamento_recetado',
    'C9_V1_7': 'No_pudo_pagar_atencion_salud_mental',
    'C10_V1': 'Opinion_sanidad_publica_municipio',
    'C11_V1': 'Aseguramiento_sanitario',
    'C12_V1_1': 'Motivo_seguro_salud_privado_mal_funcionamiento_sanidad_publica',
    'C12_V1_2': 'Motivo_seguro_salud_privado_comodidad_confort',
    'C12_V1_3': 'Motivo_seguro_salud_privado_rapidez_en_atencion',
    'C12_V1_4': 'Motivo_seguro_salud_privado_contratado_por_empresa',
    'C12_V1_5': 'Motivo_seguro_salud_privado_confianza_en_atencion_privada',
    'C12_V1_6': 'Motivo_seguro_salud_privado_otro',
    'C12_V1_9': 'Motivo_seguro_salud_privado_NS_NC',
    'C13_V1': 'Uso_mas_frecuente_sistema_sanitario',
    'C14_V1_1': 'Uso_seguro_privado_atencion_primaria',
    'C14_V1_2': 'Uso_seguro_privado_consultas_especialistas',
    'C14_V1_3': 'Uso_seguro_privado_hospitales',
    'C14_V1_4': 'Uso_seguro_privado_servicios_urgencia_hospitalaria',
    'C14_V1_5': 'Uso_seguro_privado_servicios_urgencia_extrahospitalaria',
    'C14_V1_6': 'Uso_seguro_privado_ninguno',
    'C14_V1_999': 'Uso_seguro_privado_no_contesta',
    'C15_V1_1': 'Donde_busca_informacion_salud_acude_profesional_salud',
    'C15_V1_2': 'Donde_busca_informacion_salud_internet',
    'E9_V1': 'Veces_que_va_al_médico_al_año',
    'C15_V1_3': 'Donde_busca_informacion_salud_medios_comunicacion',
    'C15_V1_4': 'Donde_busca_informacion_salud_consulta_familiares_amigos',
    'C15_V1_5': 'Donde_busca_informacion_salud_no_busca_informacion',
    'C15_V1_999': 'Donde_busca_informacion_salud_NS_NC',
    'C6A_1_V2': 'Tomado_tranquilizantes_ansioliticos',
    'C6B_1_V2': 'Recetado_tranquilizantes_ansioliticos',
    'C6A_2_V2': 'Tomado_antidepresivos',
    'C6B_2_V2': 'Recetado_antidepresivos',
    'C6A_3_V2': 'Tomado_medicamentos_fuertes_dolor',
    'C6B_3_V2': 'Recetado_medicamentos_fuertes_dolor',
    'C15_V2': 'Importancia_vacunas_salud_publica',

}

# Renombrar las columnas del DataFrame
df.rename(columns=renombrar_salud, inplace=True)

# Verificar el DataFrame con las columnas renombradas
print(df.columns)

# Crear intervalos de edad
bins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']
df['EDAD_INTERVALO'] = pd.cut(df['EDAD_NUM'], bins=bins, labels=labels, right=False)

# Obtener el conteo de personas por intervalo de edad
edad_counts = df['EDAD_INTERVALO'].value_counts().sort_index()

# Graficar distribución de edad con el número de personas por intervalo
plt.figure(figsize=(10, 6))
ax = sns.countplot(x='EDAD_INTERVALO', data=df, palette='viridis')
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
    # Convertir los valores de 'SEXO' a etiquetas más legibles
    df['SEXO'] = df['SEXO'].map({1: 'Hombre', 2: 'Mujer'})
    
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
if 'EDAD_INTERVALO' in df.columns and 'SEXO' in df.columns:
    # Convertir los valores de 'SEXO' a etiquetas más legibles si es necesario
    if set(df['SEXO'].unique()) == {1, 2}:  # Asegura que 'SEXO' esté en formato numérico antes de mapear
        df['SEXO'] = df['SEXO'].map({1: 'Hombre', 2: 'Mujer'})
    
    # Graficar distribución de sexo por intervalos de edad
    plt.figure(figsize=(12, 6))
    sns.countplot(x='EDAD_INTERVALO', hue='SEXO', data=df, palette='pastel')
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
    print("Las columnas 'EDAD_INTERVALO' y/o 'SEXO' no existen en el DataFrame")

# Crear una nueva columna booleana para personas con depresión
df['Tiene_Depresion'] = df['Depresion'].apply(lambda x: 'Sí' if x == 1 else 'No')

# Crear intervalos de edad
bins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']
df['EDAD_INTERVALO'] = pd.cut(df['EDAD_NUM'], bins=bins, labels=labels, right=False)

# Graficar la distribución de personas con y sin depresión por intervalo de edad
plt.figure(figsize=(14, 8))
sns.countplot(x='EDAD_INTERVALO', hue='Tiene_Depresion', data=df, palette='Set2')
plt.title('Distribución de Personas con y sin Depresión por Intervalo de Edad')
plt.xlabel('Intervalo de Edad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.legend(title='Tiene Depresión')

# Mostrar el número de personas por encima de cada barra
for p in plt.gca().patches:
    plt.gca().annotate(f'\n{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), 
                       textcoords='offset points')

plt.tight_layout()
plt.show()



# Crear una nueva columna booleana para personas con ansiedad
df['Tiene_Ansiedad'] = df['Ansiedad_cronica'].apply(lambda x: 'Sí' if x == 1 else 'No')

# Crear intervalos de edad
bins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']
df['EDAD_INTERVALO'] = pd.cut(df['EDAD_NUM'], bins=bins, labels=labels, right=False)

# Graficar la distribución de personas con y sin ansiedad por intervalo de edad
plt.figure(figsize=(14, 8))
sns.countplot(x='EDAD_INTERVALO', hue='Tiene_Ansiedad', data=df, palette='Set2')
plt.title('Distribución de Personas con y sin Ansiedad por Intervalo de Edad')
plt.xlabel('Intervalo de Edad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.legend(title='Tiene Ansiedad')

# Mostrar el número de personas por encima de cada barra
for p in plt.gca().patches:
    plt.gca().annotate(f'\n{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), 
                       textcoords='offset points')

plt.tight_layout()
plt.show()



# Crear una nueva columna booleana para personas con asma
df['Tiene_Asma'] = df['Asma'].apply(lambda x: 'Sí' if x == 1 else 'No')

# Crear intervalos de edad
bins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 100]
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']
df['EDAD_INTERVALO'] = pd.cut(df['EDAD_NUM'], bins=bins, labels=labels, right=False)

# Graficar la distribución de personas con y sin asma por intervalo de edad
plt.figure(figsize=(14, 8))
sns.countplot(x='EDAD_INTERVALO', hue='Tiene_Asma', data=df, palette='Set2')
plt.title('Distribución de Personas con y sin Asma por Intervalo de Edad')
plt.xlabel('Intervalo de Edad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.legend(title='Tiene Asma')


# Mostrar el número de personas por encima de cada barra
for p in plt.gca().patches:
    plt.gca().annotate(f'\n{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', fontsize=10, color='black', xytext=(0, 10), 
                       textcoords='offset points')

plt.tight_layout()
plt.show()


# Calcular varios estadísticos para la columna específica
estadisticos_antes = df['Veces_que_va_al_médico_al_año'].describe()
print("\nEstadísticos antes de llenar NaN:")
print(estadisticos_antes)

# Calcular la media de la columna y rellenar NaN con la media correspondiente
media_visitas_medicas = df['Veces_que_va_al_médico_al_año'].mean()
df['Veces_que_va_al_médico_al_año'] = df['Veces_que_va_al_médico_al_año'].fillna(media_visitas_medicas)

# Verificar que no haya más NaN
print("\nNúmero de NaN después de llenar con la media:")
print(df['Veces_que_va_al_médico_al_año'].isnull().sum())

# Verificar nuevamente los estadísticos después de llenar los valores faltantes
estadisticos_despues = df['Veces_que_va_al_médico_al_año'].describe()
print("\nEstadísticos después de llenar NaN con la media:")
print(estadisticos_despues)


def calcular_media(datos, veces_que_va_al_médico_al_año):
    try:
        # Eliminar NaN de la columna y calcular la media manualmente
        valores = datos[veces_que_va_al_médico_al_año].dropna().tolist()
        suma = sum(valores)
        cantidad = len(valores)
        if cantidad!=0:
            return suma/cantidad
        else:
            return np.nan
    except:
        print("La columna no existe o algo impide calcular la media")
        return 0
        
# Calcular varios estadísticos para la columna específica
estadisticos_antes = df['Veces_que_va_al_médico_al_año'].describe()
print("\nEstadísticos antes de llenar NaN:")
print(estadisticos_antes)

# Calcular la media de la columna y rellenar NaN con la media correspondiente
media_visitas_medicas = df['Veces_que_va_al_médico_al_año'].mean()
df['Veces_que_va_al_médico_al_año'] = df['Veces_que_va_al_médico_al_año'].fillna(media_visitas_medicas)

# Verificar que no haya más NaN
print("\nNúmero de NaN después de llenar con la media:")
print(df['Veces_que_va_al_médico_al_año'].isnull().sum())

# Verificar nuevamente los estadísticos después de llenar los valores faltantes
estadisticos_despues = df['Veces_que_va_al_médico_al_año'].describe()
print("\nEstadísticos después de llenar NaN con la media:")
print(estadisticos_despues)





# Asignar nombres de distritos
distritos = {
    1: 'Centro',
    2: 'Arganzuela',
    3: 'Retiro',
    4: 'Salamanca',
    5: 'Chamartín',
    6: 'Tetuán',
    7: 'Chamberí',
    8: 'Fuencarral-El Pardo',
    9: 'Moncloa-Aravaca',
    10: 'Latina',
    11: 'Carabanchel',
    12: 'Usera',
    13: 'Puente de Vallecas',
    14: 'Moratalaz',
    15: 'Ciudad Lineal',
    16: 'Hortaleza',
    17: 'Villaverde',
    18: 'Villa de Vallecas',
    19: 'Vicálvaro',
    20: 'San Blas',
    21: 'Barajas'
}

df['DISTRITOS'] = df['DISTRITO'].map(distritos)

# Verificar los nombres de las columnas
print(df.columns)

# Asegúrate de que el nombre de la columna es correcto
columna_visitas = 'Veces_que_va_al_médico_al_año'

# Verificar si la columna existe en el DataFrame
if columna_visitas in df.columns:
    # Calcular la media de veces que van al médico por distrito
    media_visitas_por_distrito = df.groupby('DISTRITOS')[columna_visitas].mean()

    # Verificar la media calculada
    print(media_visitas_por_distrito)

    # Graficar la media de veces que van al médico por distrito
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(x=media_visitas_por_distrito.index, y=media_visitas_por_distrito.values, palette='viridis')
    plt.title('Media de Veces que Van al Médico por Distrito')
    plt.xlabel('Distrito')
    plt.ylabel('Media de Veces que Van al Médico')
    plt.xticks(rotation=45)

    # Mostrar la media por encima de cada barra
    for i, media in enumerate(media_visitas_por_distrito.values):
        ax.text(i, media + 0.1, f'{media:.2f}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()
else:
    print(f"La columna '{columna_visitas}' no existe en el DataFrame")

# Seleccionar las columnas de enfermedades
enfermedades = [
    'Tensión_alta', 'Infarto_angina_coronaria', 'Artrosis',
    'Dolor_espalda_cervical', 'Dolor_espalda_lumbar', 'Alergia_cronica',
    'Asma', 'Diabetes', 'Colesterol_alto', 'Depresion', 'Ansiedad_cronica',
    'Migraña', 'Problemas_tiroides', 'Varices', 'Cataratas', 'Problemas_piel',
    'Sindrome_post_COVID'
]

# Calcular estadísticas descriptivas para cada enfermedad
for enfermedad in enfermedades:
    print(f"Estadísticas para: {enfermedad}")
    print(df[enfermedad].describe())
    print()

    # Renombrar las respuestas de B2 según la descripción proporcionada
renombrar_b2 = {
    1: 'Mejor',
    2: 'Igual',
    3: 'Peor',
    8: 'No sabe',
    9: 'No contesta'
}

# Renombrar la columna B2 con los nuevos nombres
df['Estado_salud_hoy_después_covid'] = df['B2'].map(renombrar_b2)

# Calcular la tabla de frecuencias
tabla_frecuencias = pd.crosstab(index=df['Estado_salud_hoy_depués_covid'], columns='count', normalize=True) * 100

# Mostrar la tabla de frecuencias con porcentajes
print("\nTabla de frecuencias del estado de salud hoy comparado con marzo 2020:")
print(tabla_frecuencias)
