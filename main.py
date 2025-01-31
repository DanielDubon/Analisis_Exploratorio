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

