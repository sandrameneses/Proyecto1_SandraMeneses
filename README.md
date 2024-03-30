# **Proyecto MLOps**

## **Recomendaciones a usuarios sobre Videojuegos**

## **Objetivo**

En este proyecto asumi el rol de ingeniero MLOps, teniendo responsabilidades de ingeniero de datos y científico de datos, para la plataforma multinacional de videojuegos Steam. El objetivo es desarrollar un Producto Mínimo Viable (MVP) que incluya una API y la aplicación Machine Learning. Estos modelos se abordan con el análisis de sentimientos sobre los comentarios de los usuarios sobre juegos, las recomendaciones de juegos basadas en la información del usuario y la similitud entre juegos por género.

## **Data Utilizada**

1. australian_user_reviews.json: Contiene comentarios de usuarios sobre juegos, información de recomendaciones, emoticonos y estadísticas. También incluye la ID de usuario, la URL del perfil y la ID del juego.

2. australian_users_items.json: proporciona información sobre los juegos jugados por los usuarios y el tiempo acumulado jugado por cada usuario en un juego específico.

3. output_steam_games.json: Contiene datos relacionados con los juegos, como título, desarrollador, precios y características técnicas.

## **Creacion de API**

 - PlayTimeGenre: Toma el género ingresado devuelve el año con más horas jugadas por los usuarios.
 - UserForGenre: Para el género ingresado devuelve el usuario que acumula mas horas jugadas y una lista de horas acumuladas por año. 
 - Users_recommend: Para el año ingresado, devuelve el top 3 de juegos más recomendados.
 - UsersNotRecommend: Para el año ingresado, devuelve el top 3 de juegos menos recomendados.
 - Sentiment_analysis: Para el año ingresado, devuelve una lista con la cantidad de reseñas de los usuarios. Categorizadas con análisis de sentimiento.
