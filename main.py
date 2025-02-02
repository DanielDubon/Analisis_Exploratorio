import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


movies = pd.read_csv('movies.csv', encoding='ISO-8859-1')


#-----------
#Ejercicio 1 resumen estadistico:
"""
summary_statistics = movies.describe()
data_info = movies.info()
print(summary_statistics)
print(data_info)
"""
#-----------

#-----------
#Ejercicio 3 Investigacion de la distribucion Normal y tablas de frecuencias de las variables cualitativas:
"""
movies['castWomenAmount'] = pd.to_numeric(movies['castWomenAmount'], errors='coerce')
movies['castMenAmount'] = pd.to_numeric(movies['castMenAmount'], errors='coerce')

quantitative_vars = ['id', 'budget', 'revenue', 'runtime', 'popularity', 'voteAvg', 'voteCount', 
                     'genresAmount', 'productionCoAmount', 'productionCountriesAmount', 
                     'actorsAmount', 'castWomenAmount', 'castMenAmount']

# Verificar la normalidad de las variables cuantitativas usando la prueba de Anderson-Darling
normality_results = {}
for var in quantitative_vars:
    ad_stat, critical_values, significance_level = stats.anderson(movies[var].dropna(), dist='norm')
    normality_results[var] = (ad_stat, critical_values)

print("Resultados de la prueba de normalidad (Estadístico de Anderson-Darling):")
for var, (ad_stat, critical_values) in normality_results.items():
    print(f"{var}: Estadístico = {ad_stat:.4f}, Valores críticos = {critical_values}")
    if ad_stat < critical_values[2]:  # Usando el nivel de significancia del 5%
        print(f" - {'Normal'}")
    else:
        print(f" - {'No Normal'}")


qualitative_vars = ['genres', 'homePage', 'productionCompany', 'productionCompanyCountry', 
                    'productionCountry', 'video', 'director', 'actors', 'originalTitle', 
                    'title', 'originalLanguage', 'releaseDate']

frequency_tables = {}
for var in qualitative_vars:
    frequency_tables[var] = movies[var].value_counts()

print("\nTablas de frecuencias para variables cualitativas:")
for var, freq in frequency_tables.items():
    print(f"\nFrecuencias de {var}:")
    print(freq)


for var in quantitative_vars:
    plt.figure(figsize=(10, 6))
    sns.histplot(movies[var].dropna(), kde=True, bins=30)
    plt.title(f'Distribución de {var}')
    plt.xlabel(var)
    plt.ylabel('Frecuencia')
    plt.xlim(0, movies[var].max())
    
    plt.savefig(f'distribucion_{var}.png')
    plt.close()
"""
#-----------

#------PREGUNTAS EJERCICIO 4-----
#Ejercicio A ¿Cuáles son las 10 películas que contaron con más presupuesto? 
"""
top_budget_movies = movies.nlargest(10, 'budget')
print(top_budget_movies[['originalTitle', 'budget']])

plt.figure(figsize=(12, 6))
plt.bar(top_budget_movies['originalTitle'], top_budget_movies['budget'], color='blue', alpha=0.7)

plt.title('Presupuesto de las 10 Películas con Más Presupuesto')
plt.xlabel('Título de la Película')
plt.ylabel('Presupuesto (en millones)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig('Pregunta_A_presupuesto_top_peliculas.png')  
plt.close() 
"""
#-----------



#-----------
#Ejercicio B ¿Cuáles son las 10 películas que más ingresos tuvieron?
"""
top_revenue_movies = movies.nlargest(10, 'revenue')
print(top_revenue_movies[['originalTitle', 'revenue']])

plt.figure(figsize=(12, 6))
plt.bar(top_revenue_movies['originalTitle'], top_revenue_movies['revenue'], color='green', alpha=0.7)

plt.title('Ingresos de las 10 Películas con Más Ingresos')
plt.xlabel('Título de la Película')
plt.ylabel('Ingresos (en millones)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig('Pregunta_B_ingresos_top_peliculas.png')
plt.close() 
"""
#-----------

#Ejercicio C ¿Cuál es la película que más votos tuvo?
"""
top_5_movies = movies.nlargest(5, 'voteCount')
print("Las 5 películas con más votos son:")
for index, row in top_5_movies.iterrows():
    print(f"{row['originalTitle']} con {row['voteCount']} votos.")

# Gráfico de las 5 películas con más votos
plt.figure(figsize=(10, 6))
plt.bar(top_5_movies['originalTitle'], top_5_movies['voteCount'], color='blue', alpha=0.7)
plt.title('Top 5 Películas con Más Votos')
plt.xlabel('Título de la Película')
plt.ylabel('Número de Votos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('top_5_peliculas_mas_votos.png')
plt.close()
"""
#-----------

#-----------
#Ejercicio D ¿Cuál es la peor película de acuerdo a los votos de todos los usuarios?
"""
worst_movie = movies.loc[movies['voteCount'].idxmin()]
print(f"La peor película de acuerdo a los votos es: {worst_movie['originalTitle']} con {worst_movie['voteCount']} votos.")
"""
#-----------

#-----------
#Ejercicio E ¿Cuántas películas se hicieron en cada año? ¿En qué año se hicieron más películas?
"""
# Asegurarse de que la columna 'releaseDate' esté en formato de fecha
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'], errors='coerce')

# Extraer el año de la fecha de lanzamiento
movies['releaseYear'] = movies['releaseDate'].dt.year

# Contar el número de películas por año
movies_per_year = movies['releaseYear'].value_counts().sort_index()

# Imprimir el año con más películas
most_movies_year = movies_per_year.idxmax()
most_movies_count = movies_per_year.max()
print(f"El año con más películas es {most_movies_year} con {most_movies_count} películas.")

# Gráfico de barras de películas por año
plt.figure(figsize=(12, 6))
movies_per_year.plot(kind='bar', color='teal', alpha=0.7)
plt.title('Número de Películas por Año')
plt.xlabel('Año')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('peliculas_por_año.png')
plt.close()
"""
#-----------


#-----------
#Ejercicio F ¿Cuál es el género principal de las 20 películas más recientes? 
# ¿Cuál es el género principal que predomina en el conjunto de datos? 
# ¿A qué género principal pertenecen las películas más largas?
"""
# Asegurarse de que la columna 'releaseDate' esté en formato de fecha
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'], errors='coerce')

# Obtener las 20 películas más recientes
recent_movies = movies.nlargest(20, 'releaseDate')

# Crear un DataFrame con las 20 películas más recientes y su género
recent_movies_genres = recent_movies[['originalTitle', 'genres']].copy()
recent_movies_genres['genres'] = recent_movies_genres['genres'].str.split(',').explode().str.strip()

# Contar la cantidad de películas por género en las 20 más recientes
genre_counts_recent = recent_movies_genres['genres'].value_counts().reset_index()
genre_counts_recent.columns = ['Género', 'Cantidad']

print("Géneros de las 20 películas más recientes:")
print(genre_counts_recent)

# Determinar el género principal que predomina en el conjunto de datos
all_genres = movies['genres'].str.split(',').explode().str.strip()
main_genre_all = all_genres.value_counts().idxmax()
print(f"El género principal que predomina en el conjunto de datos es: {main_genre_all}")

# Gráfico de géneros de las 20 películas más recientes
plt.figure(figsize=(12, 6))
genre_counts_recent.plot(kind='bar', x='Género', y='Cantidad', color='orange', alpha=0.7)
plt.title('Géneros de las 20 Películas Más Recientes')
plt.xlabel('Género')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('generos_20_peliculas_recientes.png')
plt.close()

# Determinar los 5 géneros principales en el conjunto de datos
top_5_genres = all_genres.value_counts().nlargest(5).reset_index()
top_5_genres.columns = ['Género', 'Cantidad']

# Gráfico de los 5 géneros principales en el conjunto de datos
plt.figure(figsize=(12, 6))
top_5_genres.plot(kind='bar', x='Género', y='Cantidad', color='blue', alpha=0.7)
plt.title('Top 5 Géneros Principales en el Conjunto de Datos')
plt.xlabel('Género')
plt.ylabel('Número de Películas')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('top_5_generos_principales.png')
plt.close()

# Determinar el género de las películas más largas
longest_movies = movies.nlargest(5, 'runtime')
longest_genres = longest_movies['genres'].str.split(',').explode().str.strip()
main_genre_longest = longest_genres.value_counts().idxmax()
print(f"El género principal de las películas más largas es: {main_genre_longest}")

"""
#-----------

#-----------
#Ejercicio G ¿Las películas de qué género principal obtuvieron mayores ganancias?
"""
# Asegurarse de que la columna 'revenue' esté en formato numérico
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')

# Explode de géneros para contar las ganancias por género
all_genres = movies['genres'].str.split(',').explode().str.strip()

# Crear un DataFrame con los géneros y sus ingresos
genre_revenue = movies[['genres', 'revenue']].copy()
genre_revenue['genres'] = genre_revenue['genres'].str.split(',')
genre_revenue = genre_revenue.explode('genres')
genre_revenue['genres'] = genre_revenue['genres'].str.strip()

# Sumar las ganancias por género
revenue_by_genre = genre_revenue.groupby('genres')['revenue'].sum().reset_index()

# Determinar el género con mayores ganancias
max_revenue_genre = revenue_by_genre.loc[revenue_by_genre['revenue'].idxmax()]
print(f"El género principal que obtuvo mayores ganancias es: {max_revenue_genre['genres']} con ganancias de {max_revenue_genre['revenue']:.2f}.")

# Obtener los 5 géneros con mayores ganancias para el gráfico
top_5_revenue = revenue_by_genre.nlargest(5, 'revenue')

# Gráfico de ganancias por los 5 géneros principales
plt.figure(figsize=(12, 6))
top_5_revenue.plot(kind='bar', x='genres', y='revenue', color='green', alpha=0.7)
plt.title('Top 5 Ganancias por Género de Películas')
plt.xlabel('Género')
plt.ylabel('Ganancias (en millones)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('top_5_ganancias_por_genero.png')
plt.close()
"""
#-----------

#-----------
#Ejercicio H ¿La cantidad de actores influye en los ingresos de las películas? 
# ¿Se han hecho películas con más actores en los últimos años?
"""
# Asegurarse de que la columna 'revenue' y 'actorsAmount' estén en formato numérico
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['actorsAmount'] = pd.to_numeric(movies['actorsAmount'], errors='coerce')

# Análisis de la relación entre la cantidad de actores y los ingresos
plt.figure(figsize=(10, 6))
plt.scatter(movies['actorsAmount'], movies['revenue'], alpha=0.5)
plt.title('Relación entre la Cantidad de Actores y los Ingresos de las Películas')
plt.xlabel('Cantidad de Actores')
plt.ylabel('Ingresos (en millones)')
plt.xlim(0, movies['actorsAmount'].max())
plt.ylim(0, movies['revenue'].max())
plt.tight_layout()

# Añadir línea de regresión
sns.regplot(x='actorsAmount', y='revenue', data=movies, scatter=False, color='red')
plt.savefig('relacion_actores_ingresos.png')
plt.close()

# Imprimir la correlación
correlation = movies['actorsAmount'].corr(movies['revenue'])
print(f"La correlación entre la cantidad de actores y los ingresos es: {correlation:.2f}")

# Análisis de la cantidad de actores en los últimos años
# Asegurarse de que la columna 'releaseDate' esté en formato de fecha
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'], errors='coerce')

# Extraer el año de la fecha de lanzamiento
movies['releaseYear'] = movies['releaseDate'].dt.year

# Contar la cantidad de actores por año
actors_per_year = movies.groupby('releaseYear')['actorsAmount'].mean().reset_index()

# Gráfico de la cantidad promedio de actores por año
plt.figure(figsize=(12, 6))
plt.plot(actors_per_year['releaseYear'], actors_per_year['actorsAmount'], marker='o', color='purple')
plt.title('Cantidad Promedio de Actores por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad Promedio de Actores')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('cantidad_promedio_actores_por_año.png')
plt.close()
"""
#-----------


#-----------
#Ejercicio I ¿Es posible que la cantidad de hombres y mujeres en el reparto influya en la popularidad y los ingresos de las películas?
"""

# Asegurarse de que las columnas 'popularity', 'revenue', 'castWomenAmount' y 'castMenAmount' estén en formato numérico
movies['popularity'] = pd.to_numeric(movies['popularity'], errors='coerce')
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['castWomenAmount'] = pd.to_numeric(movies['castWomenAmount'], errors='coerce')
movies['castMenAmount'] = pd.to_numeric(movies['castMenAmount'], errors='coerce')

# Obtener las 10 películas más populares
top_popular_movies = movies.nlargest(10, 'popularity')
print("Las 10 películas más populares:")
print(top_popular_movies[['originalTitle', 'popularity', 'castWomenAmount', 'castMenAmount']])

# Obtener las 10 películas con mayores ingresos
top_revenue_movies = movies.nlargest(10, 'revenue')
print("\nLas 10 películas con mayores ingresos:")
print(top_revenue_movies[['originalTitle', 'revenue', 'castWomenAmount', 'castMenAmount']])

# Análisis de la relación entre la cantidad de hombres y mujeres en el reparto y la popularidad
plt.figure(figsize=(10, 6))
plt.scatter(top_popular_movies['castWomenAmount'], top_popular_movies['popularity'], alpha=0.5, label='Mujeres')
plt.scatter(top_popular_movies['castMenAmount'], top_popular_movies['popularity'], alpha=0.5, label='Hombres')
plt.title('Relación entre la Cantidad de Hombres y Mujeres en el Reparto y la Popularidad')
plt.xlabel('Cantidad de Actores')
plt.ylabel('Popularidad')
plt.xlim(0, max(top_popular_movies['castWomenAmount'].max(), top_popular_movies['castMenAmount'].max()))
plt.ylim(0, top_popular_movies['popularity'].max())
plt.legend()
plt.tight_layout()

# Añadir líneas de regresión
sns.regplot(x='castWomenAmount', y='popularity', data=top_popular_movies, scatter=False, color='blue')
sns.regplot(x='castMenAmount', y='popularity', data=top_popular_movies, scatter=False, color='orange')
plt.savefig('relacion_genero_popularidad_top.png')
plt.close()

# Análisis de la relación entre la cantidad de hombres y mujeres en el reparto y los ingresos
plt.figure(figsize=(10, 6))
plt.scatter(top_revenue_movies['castWomenAmount'], top_revenue_movies['revenue'], alpha=0.5, label='Mujeres')
plt.scatter(top_revenue_movies['castMenAmount'], top_revenue_movies['revenue'], alpha=0.5, label='Hombres')
plt.title('Relación entre la Cantidad de Hombres y Mujeres en el Reparto y los Ingresos')
plt.xlabel('Cantidad de Actores')
plt.ylabel('Ingresos (en millones)')
plt.xlim(0, max(top_revenue_movies['castWomenAmount'].max(), top_revenue_movies['castMenAmount'].max()))
plt.ylim(0, top_revenue_movies['revenue'].max())
plt.legend()
plt.tight_layout()

# Añadir líneas de regresión
sns.regplot(x='castWomenAmount', y='revenue', data=top_revenue_movies, scatter=False, color='blue')
sns.regplot(x='castMenAmount', y='revenue', data=top_revenue_movies, scatter=False, color='orange')
plt.savefig('relacion_genero_ingresos_top.png')
plt.close()
"""
#-----------

#-----------
# Ejercicio J ¿Quiénes son los directores que hicieron las 20 películas mejor calificadas?
"""
# Asegurarse de que la columna 'voteAvg' esté en formato numérico
movies['voteAvg'] = pd.to_numeric(movies['voteAvg'], errors='coerce')

# Obtener las 20 películas mejor calificadas
top_rated_movies = movies.nlargest(20, 'voteAvg')
print("Los directores de las 20 películas mejor calificadas:")
print(top_rated_movies[['originalTitle', 'voteAvg', 'director']])
"""
#-----------

#-----------
#Ejercicio K ¿Cómo se correlacionan los presupuestos con los ingresos? ¿Los altos presupuestos significan altos ingresos?
"""

movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
movies_filtered = movies[(movies['budget'] > 0) & (movies['revenue'] > 0)].copy()

# Top 5 películas con mayor presupuesto
print("\nTop 5 películas con mayor presupuesto:")
top_budget = movies_filtered.nlargest(5, 'budget')[['originalTitle', 'budget', 'revenue']]
print(top_budget)

# Gráfico de las 5 películas con mayor presupuesto
plt.figure(figsize=(12, 6))
plt.bar(top_budget['originalTitle'], top_budget['budget'], color='blue', alpha=0.7)
plt.title('Top 5 Películas con Mayor Presupuesto')
plt.xlabel('Título de la Película')
plt.ylabel('Presupuesto')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_K_top_5_presupuesto.png')
plt.close()

# Top 5 películas con mayores ganancias
print("\nTop 5 películas con mayores ganancias:")
top_revenue = movies_filtered.nlargest(5, 'revenue')[['originalTitle', 'budget', 'revenue']]
print(top_revenue)

# Gráfico de las 5 películas con mayores ganancias
plt.figure(figsize=(12, 6))
plt.bar(top_revenue['originalTitle'], top_revenue['revenue'], color='green', alpha=0.7)
plt.title('Top 5 Películas con Mayores Ganancias')
plt.xlabel('Título de la Película')
plt.ylabel('Ganancias')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_K_top_5_ganancias.png')
plt.close()

# Análisis de la relación entre presupuesto e ingresos
plt.figure(figsize=(12, 8))
plt.scatter(movies_filtered['budget'], movies_filtered['revenue'], alpha=0.5)
plt.title('Correlación entre Presupuesto e Ingresos')
plt.xlabel('Presupuesto')
plt.ylabel('Ingresos')
plt.tight_layout()

# Añadir línea de regresión
sns.regplot(x='budget', y='revenue', data=movies_filtered, scatter=False, color='red')

# Añadir texto con la correlación
correlation = movies_filtered['budget'].corr(movies_filtered['revenue'])
plt.text(0.05, 0.95, f'Correlación: {correlation:.2f}', 
         transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.savefig('Pregunta_K_correlacion_presupuesto_ingresos.png')
plt.close()

# Calcular ROI solo para películas con presupuesto > 0
movies_filtered['ROI'] = (movies_filtered['revenue'] - movies_filtered['budget']) / movies_filtered['budget']

# Remover valores extremos del ROI para mejor visualización
roi_q1 = movies_filtered['ROI'].quantile(0.05)
roi_q3 = movies_filtered['ROI'].quantile(0.95)
movies_filtered_roi = movies_filtered[
    (movies_filtered['ROI'] >= roi_q1) & 
    (movies_filtered['ROI'] <= roi_q3)
]

# Gráfico de ROI vs Presupuesto
plt.figure(figsize=(12, 8))
plt.scatter(movies_filtered_roi['budget'], movies_filtered_roi['ROI'], alpha=0.5)
plt.title('ROI vs Presupuesto (sin valores extremos)')
plt.xlabel('Presupuesto')
plt.ylabel('ROI (Return on Investment)')
plt.tight_layout()

plt.savefig('Pregunta_K_roi_vs_presupuesto.png')
plt.close()

# Imprimir estadísticas relevantes
print(f"\nLa correlación entre presupuesto e ingresos es: {correlation:.2f}")
print("\nTop 5 películas con mayor ROI (excluyendo valores extremos):")
top_roi = movies_filtered_roi.nlargest(5, 'ROI')[['originalTitle', 'budget', 'revenue', 'ROI']]
print(top_roi)
"""
#-----------

#-----------
#Ejercicio L, M ¿Se asocian ciertos meses de lanzamiento con mejores ingresos? 
"""

movies['releaseDate'] = pd.to_datetime(movies['releaseDate'], errors='coerce')
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['releaseMonth'] = movies['releaseDate'].dt.month

# Calcular ingresos promedio por mes
monthly_revenue = movies.groupby('releaseMonth')['revenue'].agg(['mean', 'count']).reset_index()
monthly_revenue.columns = ['Mes', 'Ingreso_Promedio', 'Cantidad_Peliculas']


meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
         7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
monthly_revenue['Nombre_Mes'] = monthly_revenue['Mes'].map(meses)

# Gráfico de ingresos promedio por mes
plt.figure(figsize=(12, 6))
plt.bar(monthly_revenue['Nombre_Mes'], monthly_revenue['Ingreso_Promedio'], color='blue', alpha=0.7)
plt.title('Ingresos Promedio por Mes de Lanzamiento')
plt.xlabel('Mes')
plt.ylabel('Ingreso Promedio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_LM_ingresos_promedio_por_mes.png')
plt.close()

# Gráfico de cantidad de películas por mes
plt.figure(figsize=(12, 6))
plt.bar(monthly_revenue['Nombre_Mes'], monthly_revenue['Cantidad_Peliculas'], color='green', alpha=0.7)
plt.title('Cantidad de Películas Lanzadas por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Películas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_L_cantidad_peliculas_por_mes.png')
plt.close()

# Top 5 meses con mejores ingresos promedio
print("\nTop 5 meses con mejores ingresos promedio:")
top_months = monthly_revenue.nlargest(5, 'Ingreso_Promedio')[['Nombre_Mes', 'Ingreso_Promedio', 'Cantidad_Peliculas']]
print(top_months)


# la película más exitosa de cada mes
top_movies_per_month = []
for mes in range(1, 13):
    top_movie = movies[movies['releaseMonth'] == mes].nlargest(1, 'revenue')
    if not top_movie.empty:
        top_movies_per_month.append({
            'Mes': meses[mes],
            'Película': top_movie['originalTitle'].iloc[0],
            'Ingresos': top_movie['revenue'].iloc[0]
        })

top_movies_df = pd.DataFrame(top_movies_per_month)
print("\nPelícula más exitosa de cada mes:")
print(top_movies_df)

# Boxplot de ingresos por mes para ver la distribución
plt.figure(figsize=(15, 8))
sns.boxplot(x='releaseMonth', y='revenue', data=movies)
plt.title('Distribución de Ingresos por Mes')
plt.xlabel('Mes')
plt.ylabel('Ingresos')
plt.xticks(range(12), [meses[i] for i in range(1, 13)], rotation=45)
plt.tight_layout()
plt.savefig('Pregunta_L_distribucion_ingresos_por_mes.png')
plt.close()
"""
#-----------

#-----------
#Ejercicio N ¿Cómo se correlacionan las calificaciones con el éxito comercial?
"""

movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['voteAvg'] = pd.to_numeric(movies['voteAvg'], errors='coerce')
movies['voteCount'] = pd.to_numeric(movies['voteCount'], errors='coerce')

movies_filtered = movies[
    (movies['revenue'] > 0) & 
    (movies['voteAvg'] > 0) & 
    (movies['voteCount'] > 0)
].copy()

# Top 10 películas mejor calificadas
top_rated = movies_filtered.nlargest(10, 'voteAvg')
plt.figure(figsize=(12, 6))
plt.bar(range(len(top_rated)), top_rated['voteAvg'], color='blue', alpha=0.7)
plt.title('Top 10 Películas Mejor Calificadas')
plt.xlabel('Películas')
plt.ylabel('Calificación Promedio')
plt.xticks(range(len(top_rated)), top_rated['originalTitle'], rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Preguta_N_top_10_mejores_calificaciones.png')
plt.close()

# Top 10 películas con mayores ingresos
top_revenue = movies_filtered.nlargest(10, 'revenue')
plt.figure(figsize=(12, 6))
plt.bar(range(len(top_revenue)), top_revenue['revenue'], color='green', alpha=0.7)
plt.title('Top 10 Películas con Mayores Ingresos')
plt.xlabel('Películas')
plt.ylabel('Ingresos')
plt.xticks(range(len(top_revenue)), top_revenue['originalTitle'], rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_N_top_10_mayores_ingresos.png')
plt.close()

# Gráfico de correlación entre calificaciones e ingresos
plt.figure(figsize=(10, 6))
plt.scatter(movies_filtered['voteAvg'], movies_filtered['revenue'], alpha=0.5)
plt.title('Correlación entre Calificaciones e Ingresos')
plt.xlabel('Calificación Promedio')
plt.ylabel('Ingresos')

sns.regplot(x='voteAvg', y='revenue', data=movies_filtered, scatter=False, color='red')

correlation = movies_filtered['voteAvg'].corr(movies_filtered['revenue'])
plt.text(0.05, 0.95, f'Correlación: {correlation:.2f}', 
         transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('Pregunta_N_correlacion_calificaciones_ingresos.png')
plt.close()

print("\nTop 10 películas mejor calificadas:")
print(top_rated[['originalTitle', 'voteAvg', 'revenue']].to_string())

print("\nTop 10 películas con mayores ingresos:")
print(top_revenue[['originalTitle', 'voteAvg', 'revenue']].to_string())

print(f"\nCorrelación entre calificaciones e ingresos: {correlation:.2f}")
"""
#-----------

#-----------
#Ejercicio O ¿Qué estrategias de marketing, como videos promocionales o páginas oficiales, generan mejores resultados?
"""
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['video'] = movies['video'].astype(bool)
movies['homePage'] = movies['homePage'].notna()  # True si tiene página oficial

# Crear grupos para el análisis
movies['marketing_strategy'] = 'Sin estrategia'
movies.loc[movies['video'], 'marketing_strategy'] = 'Solo Video'
movies.loc[movies['homePage'], 'marketing_strategy'] = 'Solo Página Web'
movies.loc[(movies['video']) & (movies['homePage']), 'marketing_strategy'] = 'Ambas estrategias'

# Calcular estadísticas por estrategia de marketing
marketing_stats = movies.groupby('marketing_strategy').agg({
    'revenue': ['mean', 'count'],
    'voteAvg': 'mean'
}).round(2)

print("\nEstadísticas por estrategia de marketing:")
print(marketing_stats)

# Gráfico de ingresos promedio por estrategia
plt.figure(figsize=(12, 6))
avg_revenue = movies.groupby('marketing_strategy')['revenue'].mean()
plt.bar(avg_revenue.index, avg_revenue.values, color='blue', alpha=0.7)
plt.title('Ingresos Promedio por Estrategia de Marketing')
plt.xlabel('Estrategia de Marketing')
plt.ylabel('Ingresos Promedio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_O_ingresos_por_estrategia.png')
plt.close()

# Gráfico de cantidad de películas por estrategia
plt.figure(figsize=(12, 6))
movies_count = movies['marketing_strategy'].value_counts()
plt.bar(movies_count.index, movies_count.values, color='green', alpha=0.7)
plt.title('Cantidad de Películas por Estrategia de Marketing')
plt.xlabel('Estrategia de Marketing')
plt.ylabel('Cantidad de Películas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_O_cantidad_por_estrategia.png')
plt.close()

# Análisis de calificaciones promedio por estrategia
plt.figure(figsize=(12, 6))
avg_rating = movies.groupby('marketing_strategy')['voteAvg'].mean()
plt.bar(avg_rating.index, avg_rating.values, color='purple', alpha=0.7)
plt.title('Calificación Promedio por Estrategia de Marketing')
plt.xlabel('Estrategia de Marketing')
plt.ylabel('Calificación Promedio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Pregunta_O_calificacion_por_estrategia.png')
plt.close()

# Top 5 películas más exitosas por cada estrategia
print("\nTop 5 películas más exitosas por estrategia:")
for strategy in movies['marketing_strategy'].unique():
    print(f"\n{strategy}:")
    top_5 = movies[movies['marketing_strategy'] == strategy].nlargest(5, 'revenue')
    print(top_5[['originalTitle', 'revenue', 'voteAvg']].to_string())

"""
#-----------


#-----------
# Pregunta P ¿La popularidad del elenco está directamente correlacionada con el éxito de taquilla?
"""
# Asegurarse de que las columnas 'revenue' y 'actorsPopularity' estén en formato numérico
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['actorsPopularity'] = pd.to_numeric(movies['actorsPopularity'], errors='coerce')

# Calcular la correlación entre la popularidad del elenco y los ingresos
correlation = movies['actorsPopularity'].corr(movies['revenue'])
print(f"La correlación entre la popularidad del elenco y el éxito de taquilla es: {correlation:.2f}")

# Visualizar la relación
plt.figure(figsize=(10, 6))
plt.scatter(movies['actorsPopularity'], movies['revenue'], alpha=0.5)
plt.title('Relación entre la Popularidad del Elenco y el Éxito de Taquilla')
plt.xlabel('Popularidad del Elenco')
plt.ylabel('Ingresos (en millones)')
plt.xlim(0, movies['actorsPopularity'].max())
plt.ylim(0, movies['revenue'].max())
plt.tight_layout()

# Añadir línea de regresión
sns.regplot(x='actorsPopularity', y='revenue', data=movies, scatter=False, color='blue')
plt.savefig('relacion_popularidad_elenco_ingresos.png')
plt.close()
"""
#-----------

#-----------
# Pregunta q: ¿Cuál es la duración promedio de las películas en el conjunto de datos?
"""
# Asegurarse de que la columna 'runtime' esté en formato numérico
movies['runtime'] = pd.to_numeric(movies['runtime'], errors='coerce')

# Calcular la duración promedio
average_runtime = movies['runtime'].mean()
print(f"La duración promedio de las películas es: {average_runtime:.2f} minutos")

# Visualizar la distribución de la duración
plt.figure(figsize=(10, 6))
plt.hist(movies['runtime'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Distribución de la Duración de las Películas')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('distribucion_duracion_peliculas.png')
plt.close()
"""
#-----------

#-----------
# Pregunta r: ¿Qué actores tienen más películas?
"""
# Asegurarse de que la columna 'actors' esté en formato de lista
# Suponiendo que 'actors' es una cadena de texto con los nombres de los actores separados por comas o '|'
movies['actors'] = movies['actors'].str.replace('|', ',')  # Reemplazar '|' por ',' para unificar el separador
movies['actors'] = movies['actors'].str.split(',')  # Convertir la cadena en una lista

# Explotar la columna 'actors' para tener un registro por actor
actors_exploded = movies.explode('actors')

# Limpiar espacios en blanco
actors_exploded['actors'] = actors_exploded['actors'].str.strip()

# Verificar los valores únicos en la columna 'actors'
print("Valores únicos en la columna 'actors':")
print(actors_exploded['actors'].unique())

# Filtrar actores no válidos (por ejemplo, eliminar 'FALSE', 'NaN', y cadenas vacías)
actors_exploded = actors_exploded[~actors_exploded['actors'].isin(['FALSE', 'NaN', ''])]

# Asegurarse de que no haya valores nulos
actors_exploded = actors_exploded[actors_exploded['actors'].notnull()]

# Contar la cantidad de películas por actor
actor_counts = actors_exploded['actors'].value_counts()

# Obtener los 10 actores con más películas
top_actors = actor_counts.head(10)
print("Los 10 actores con más películas:")
print(top_actors)

# Visualizar la cantidad de películas por actor
plt.figure(figsize=(10, 6))
top_actors.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Los 10 Actores con Más Películas')
plt.xlabel('Actores')
plt.ylabel('Cantidad de Películas')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas y alinearlas a la derecha
plt.tight_layout()  # Ajustar el layout
plt.savefig('top_actores_peliculas.png')
plt.close()
"""
#-----------

#-----------
# Pregunta s: ¿Cuál es la relación entre el presupuesto y la calificación de las películas?
"""
# Asegurarse de que las columnas 'budget' y 'voteAvg' estén en formato numérico
movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
movies['voteAvg'] = pd.to_numeric(movies['voteAvg'], errors='coerce')

# Calcular la correlación entre el presupuesto y la calificación
correlation = movies['budget'].corr(movies['voteAvg'])
print(f"La correlación entre el presupuesto y la calificación de las películas es: {correlation:.2f}")

# Visualizar la relación
plt.figure(figsize=(10, 6))
plt.scatter(movies['budget'], movies['voteAvg'], alpha=0.5)
plt.title('Relación entre el Presupuesto y la Calificación de las Películas')
plt.xlabel('Presupuesto (en millones)')
plt.ylabel('Calificación Promedio')
plt.xlim(0, movies['budget'].max())
plt.ylim(0, 10)  # Asumiendo que la calificación está en una escala de 0 a 10
plt.tight_layout()

# Añadir línea de regresión
sns.regplot(x='budget', y='voteAvg', data=movies, scatter=False, color='blue')
plt.savefig('relacion_presupuesto_calificacion.png')
plt.close()
"""
#-----------

