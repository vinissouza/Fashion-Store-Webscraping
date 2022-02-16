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
3. Material raw don't include pocket lining, shell and etc. (unconsidered in product composition)
4. A colunas de lining e shell são consideradas materiais da calça jeans


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
<li> Schedule ETL. </li>
<li> Data analysis. </li>
<li> Create hypothesis and main insights. </li>
<li> Built a dashboard report. </li>
<li> Deploy model. </li>
</ol>
</details>


## Main Data Insights
Through exploratory data analysis done on data collected in a single day, the main insights can be seen below:

#### Insight 01: The composition with 98% cotton and 2% spandex is the most common, with a 33% presence in all products.

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-01.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

- Product made with 98% cotton and 2% spandex has a **mean price** of **$22.82** and **median price** of **$20.99**.
- Product made with 98% cotton and 2% spandex has a **maximum price** of **$39.99** and **minimum price** of **$7.99**.
- Product made with 99% cotton and 1% spandex is the **second most common**, with 30% presence.
- 


#### Insight 02: On average, each model has 6 different colors and the most common colors are denim blue,light denim blue, black, dark denim blue, dark gray, and dark blue.

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-02.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

- _Denim Blue_ is the most common color with **19%** of presence, followed by _Light Denim Blue_ with **18%** and _Black_ with _13%_.
- _Denim Blue_ has a **mean price** of **$26.18** and a **median price** of **$24.99**.
- _Light Denim Blue_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Black_ has a **mean price** of **$28.74** and a **median price** of **$29.99**.

#### Insight 03: _Skinny Fit_ is the most common fit with a 37% presence in all products.

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-03.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

- _Slim Fit_ is the second most common fit with 29% of presence, followed by _Regular Fit_ with 21%.
- _Skinny Fit_  has a **maximum price** of **$39.99** and **minimum price** of **$7.99**.
- _Skinny Fit_ has a **mean price** of **$24.12** and a **median price** of **$19.99**.
- _Slim Fit_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Regular Fit_ has a **mean price** of **$25.99** and a **median price** of **$21.99**.

#### Insight 04: The most popular product category is _Men Jeans Slim_ with a 29% of presence in all products.

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-04.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

- _Mean Jeans Skinny_ is the second most common category with **20%**, followed by _Men Jeans Regular_ with **19%** and _Men Jeans Ripped_ with **17%**.
- _Men Jeans Slim_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Men Jeans Slim_  has a **maximum price** of **$49.99** and **minimum price** of **$7.99**.



### rascunho
considerar colocar após o modelo de scrapy
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
metrica de faturamento ( ticket médio, markup médio) , crescimento ou retenção de custo (custo de producao).

## ~~Machine Learning Model~~
## Scraping Model


### Extraction process
Step by step of scraping process

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_collect_model.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

###Transform process
Step by step of cleaning and transform data

#### Showroom Transform

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_showroom_model.png?raw=true" alt="etl_collect_model" width="250px" class="center"/>

#### Color Transform

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_color_model.png?raw=true" alt="etl_collect_model" width="200px" class="center"/>

#### Attributes Transform

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_attributes_model.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

###Load process
Step by step of create and load database

colocar nessa seção a explicação de cada metrica

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/database_schema.png?raw=true" alt="etl_collect_model" width="300px" class="center"/>

## <del>Machine Learning Performance</del>

## Business Results
Talvez adicionar aqui os resultados obtidos mais detalhadamente (mudar o nome da seção)

## Conclusions
Adicionar aquis os resultados obtidos

## Lessons Learned
First development cycle:
- Webscrapping: bs4
- SQL
- Design ETL
- Database Schema
- Regex
- Business model: ecommerce
- POO fundaments

## Next Steps
- Airflow to schedule and constantly update the database and hel in decision-make
- Business friendly data visualization data software: Tableau
- Selenium to collect more data available only with javascript interactive
- Add Macy's web scraping

Todos os ciclos de desenvolvimento atenderam as necessidades do projeto até o momento.

Refazer analises com um grande periodo de coleta para treinar pyshark and hadoop alem de 
ter uma analise EDA melhor.

Através do Selenium, descobrir quantas cores por modelo ficam ativas na pagina do produto

Através do Selenium, inspecionar site da Macys para ter a metrica de interesse: numero de vendas

Através do Selenium, inspecionar site da HM para ter metrica de reviews e pais de fabricação.