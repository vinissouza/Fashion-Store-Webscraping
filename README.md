# Fashion-Store-Webscraping
This repos contains all information about fashion store webscraping project.

## Business Problem
Brazilians entrepreneurs intend to open a fashion ecommerce store in the US and
determined that their entry product would be jeans for men.

To understand more about the American fashion market and guide their
product strategy, they hired a consulting to provide a study based on two 
competitors considered to be benchmarks for their desired business model, 
H&M and Macy's.

This consultancy should build a database to monitor these competitors and 
deliver a report capable of answering the following questions:
- What is the ideal selling price of jeans?
- What types and colors should be considered for the launch collection?
- What are the raw materials needed to produce the pants?

All the context about this project is completely fictitious, incluidng company, CEO and business issues.

This is a project provided by <i>Comunidade DS</i>.


## Business Assumptions
1. Company has not a cost limit to factory their products.
2. The company logistic can support production from all the world.


## Solution Strategy
This project follow the methodology from CRISP-DM. The main steps followed by this project
was descriptive bellow:
1. Built a database that contains price, color, type, material and others interests info from product.
2. Define the schema to table.
3. Define the design for ETL.
4. Schedule from update the database.
5. Calculate the median of price by product, type and color from last 30 days.
6. Create the visualization dashboard with Streamlit/Tableau.
7. Delivery the final product.

## Main Data Insights
mapa de métricas

metrics to be collect:
- preço
- tipo
- material
- origem
- custo
- quantidade de produtos e porcentagem
- posicao da vitrine
- qual a página
- avaliação do produto
- assortment

### rascunho
metrica de faturamento ( ticket médio, markup médio) , crescimento ou retenção de custo (custo de producao).

## ~~Machine Learning Model~~
## Scraping Model

### Extraction process
Step by step of scraping process

###Transform process
Step by step of cleaning and transform data

###Load process
Step by step of create and load database

## <del>Machine Learning Performance</del>

## Business Results

## Conclusions

## Lessons Learned
- Webscrapping: bs4
- SQL
- Design ETL
- Database Schema
- Regex
- Business model: ecommerce

## Next Steps
- Airflow to schedule and constantly update the database and hel in decision-make
