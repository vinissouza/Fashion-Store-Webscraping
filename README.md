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

All the context about this project is completely fictitious, including company, CEO and business issues.

This is a project provided by <i>Comunidade DS</i>.


## Business Assumptions
1. Company has not a cost limit to factory their products.
2. The company logistic can support production from all the world.


## Solution Strategy
This project was developed based on the CRISP-DS (Cross-Industry Standard Process - 
Data Science, a.k.a. CRISP-DM) project management method, adapted to the project at
hand by following these steps:

- **Business Understanding:** Determine business objectives, key assumptions, constrains,
data mining goals and project plan.
- **Data Understanding:** Collect initial data from competitors, checking its quality and enunciate
the description of the data set.
- **Data Preparation:** Create a database schema, select, clean, transform, format and integrate
into the database.
- **Modeling:** Explore: Explore the data to generate a list of hypotheses and insights to assist in 
building the dashboard with the report on competitors.
- **Evaluation:** Review project and determine business results and next steps.
- **Deployment:** Deploy a dashboard with analysis and finding in a cloud environment and produce
final documentation.


<details>
<summary> <strong> First development cycle - 31-01 - 04-02-2022: </strong> </summary>
<ol>
<li> Analysis of competitors website: <a href="https://www2.hm.com/en_us/men/products/jeans.html">H&M jeans for men </a> </li> 
<li> Define which metrics will be collect and database schema. </li>
<li> Define scraping process. </li> 
<li> Collect initial data. </li>
<li> Data preparing, cleaning and transform. </li>
<li> Integrate in database. </li>
<li> Data analysis. </li>
<li> Create hypothesis and main insights. </li>
<li> Built a dashboard report. </li>
<li> Deploy model. </li>
</ol>
</details>


## Main Data Insights
mapa de métricas explorados nesse projeto

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
- Business friendly data visualization data software: Tableau
- Selenium to collect more data available only with javascript interactive