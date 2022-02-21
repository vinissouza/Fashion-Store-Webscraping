# Fashion-Store-Webscraping
This repos contains all information about fashion store webscraping project.

<a href="https://fashion-store-analytics.herokuapp.com/">
  <img alt="Made by vinissouza" src="https://img.shields.io/badge/Acess%20Dashboard%20-Streamlit-%2304D361">
</a>


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
3. Compositions designated as _Shell_ will be considered as product composition, without a special class like _Lining_ and _Pocket Lining_.
4. Compositions designated as _Lining_ and _Pocket Lining_ are considered as a separate class of the main product composition.
5. A precificação não considera o markup do produto, sendo referencia o preçço de mercado sem considerar
6. o custo total de produção


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

Based on the CRISP-DS methodology, the topics below describe the tasks performed in each project cycle to speed up the
delivery of results according to the business need.

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

Further development cycles will be carried out until the business demands are satisfied.

## Main Data Insights
Through exploratory data analysis done on data collected in a single day, the main insights can be seen below:

#### Insight 01: The composition with 98% cotton and 2% spandex is the most common, with a 33% presence in all products.


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-01.png?raw=true" alt="etl_collect_model" width="700px" class="center"/>
<figcaption><b>Fig.1 - Material Composition Features</b></figcaption>


- Product made with 98% cotton and 2% spandex has a **mean price** of **$22.82** and **median price** of **$20.99**.
- Product made with 98% cotton and 2% spandex has a **maximum price** of **$39.99** and **minimum price** of **$7.99**.
- Product made with 99% cotton and 1% spandex is the **second most common**, with 30% presence.


#### Insight 02: On average, each model has 6 different colors and the most common colors are denim blue,light denim blue, black, dark denim blue, dark gray, and dark blue.


<img  align = "center" src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-02.png?raw=true" alt="etl_collect_model" width="500px" class="center"/>
<figcaption><b>Fig.2 - Product Color Features</b></figcaption>


- _Denim Blue_ is the most common color with **19%** of presence, followed by _Light Denim Blue_ with **18%** and _Black_ with _13%_.
- _Denim Blue_ has a **mean price** of **$26.18** and a **median price** of **$24.99**.
- _Light Denim Blue_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Black_ has a **mean price** of **$28.74** and a **median price** of **$29.99**.


#### Insight 03: _Skinny Fit_ is the most common fit with a 37% presence in all products.


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-03.png?raw=true" alt="etl_collect_model" width="600px" class="center"/>
<figcaption><b>Fig.3 - Product Fit Features</b></figcaption>

- _Slim Fit_ is the second most common fit with 29% of presence, followed by _Regular Fit_ with 21%.
- _Skinny Fit_  has a **maximum price** of **$39.99** and **minimum price** of **$7.99**.
- _Skinny Fit_ has a **mean price** of **$24.12** and a **median price** of **$19.99**.
- _Slim Fit_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Regular Fit_ has a **mean price** of **$25.99** and a **median price** of **$21.99**.


#### Insight 04: The most popular product category is _Men Jeans Slim_ with a 29% of presence in all products.


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/data-insight-04.png?raw=true" alt="etl_collect_model" width="600px" class="center"/>
<figcaption><b>Fig.4 - Product Category Features</b></figcaption>


- _Mean Jeans Skinny_ is the second most common category with **20%**, followed by _Men Jeans Regular_ with **19%** and _Men Jeans Ripped_ with **17%**.
- _Men Jeans Slim_ has a **mean price** of **$27.13** and a **median price** of **$22.99**.
- _Men Jeans Slim_  has a **maximum price** of **$49.99** and **minimum price** of **$7.99**.



## Scraping Model

The project's main pillar was the data extraction process that allowed the analysis of competitors and pricing of the
initial product. The following topics explore the ETL architecture developed and detail the metrics resulting from the 
process.

All files are available in the <a href="https://github.com/vinissouza/Fashion-Store-Webscraping/tree/main/Model">Model 
</a> </li> folder in this directory.

### Extraction process

The main Python libraries used for data extraction were Beautiful Soup and Requests, resulting in the creation of three
dataframes, the first related to the products displayed on the main page (showrrom), the second related to the 
information of the available colors of each model and the third related to the attributes found for all the available 
products, dealing with each color of the models separately.


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_collect_model.png?raw=true" width="700px" class="center"/>
<figcaption><b>Fig.5 - Scraping Process - 1st Cycle</b></figcaption>


###Transform process

The transformation process focuses on standardizing column names, string column values in snake_case format, removing 
special characters, and especially on decomposing all the composition types and their materials flexibly to absorb any
composition other than the current ones.

Diagrams of data cleaning and transformation for each dataframe are given below:

- **Showroom Transform:**


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_showroom_model.png?raw=true" width="550px" class="center"/>
<figcaption><b>Fig.6 - Showroom Data Transform Process - 1st Cycle</b></figcaption>

- **Color Transform:**


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_color_model.png?raw=true" width="500px" class="center"/>
<figcaption><b>Fig.7 - Color Data Transform Process - 1st Cycle</b></figcaption>


- **Attributes Transform:**


<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/etl_transform_attributes_model.png?raw=true" width="700px" class="center"/>
<figcaption><b>Fig.8 - Attributes Data Transform Process - 1st Cycle</b></figcaption>

### Load process

The load process in the database deals mainly with the following functions, checking for the existence of tables, verify 
the available columns and if it is necessary to adjust the structure of the table columns and construct queries in SQL 
for creating and querying tables.

For better organization and understanding, the data is divided into multiple datasets, demonstrated by the following 
data schema:

<img src="https://github.com/vinissouza/Fashion-Store-Webscraping/blob/main/Images/database_schema.png?raw=true" width="500px" class="center"/>
<figcaption><b>Fig.9 - Data Schema - 1st Cycle</b></figcaption>

### Datasets Metrics Description

<details> 
<summary> <strong> Showroom dataset </strong> </summary>

**product_id:** unique code that represents the model and color of the product.

**model_code:** code that represents the product model.

**color_code:** code that represents the color of the products.

**product_category:** product model category.

**product_name:** product model name.

**product_price:** price of the product.

**product_link:** url of the product page.

**scrapy_datetime:** date and time of the data extraction.

</details>

<details>

<summary> <strong> Color dataset </strong> </summary>

**product_id:** unique code that represents the model and color of the product.

**model_code:** code that represents the product model.

**color_code:** code that represents the color of the products.

**color_name:** color name of the products.

**product_link:** url of the product page.

**scrapy_datetime:** date and time of the data extraction.

</details>

<details>

<summary> <strong> Attributes dataset </strong> </summary>

**product_id:** unique code that represents the model and color of the product.

**model_code:** code that represents the product model.

**color_code:** code that represents the color of the products.

**product_name:** product model name.

**product_price:** price of the product.

**fit:** modeling of each model.

**art_no:** unique product code.

**size:** size for reference of the models in the photos on the product page.

**more_sustainable_materials:** percentage of the composition of sustainable materials present in the product.

**product_safety:** safety instructions for using the product, especially for children.

**material_elasterell_p:** percentage of elasterell-p in the main composition in the product.

**material_cotton:** percentage of cotton in the main composition in the product.

**material_spandex:** percentage of spandex in the main composition in the product.

**material_modal:** percentage of modal in the main composition in the product.

**material_polyester:** percentage of polyester in the main composition in the product.

**lining_cotton:** percentage of cotton in the composition of the lining in the product.

**lining_polyester:** percentage of polyester in the composition of the lining in the product.

**shell_elasterell_p:** percentage of elasterell-p in the main composition in the product.

**shell_cotton:** percentage of cotton in the main composition in the product.

**shell_spandex:** percentage of spandex in the main composition in the product.

**shell_polyester:** percentage of polyester in the main composition in the product.

**pocket_cotton:** percentage of cotton in the pocket composition in the product.

**pocket_lining_cotton:** percentage of cotton in the pocket composition in the product.

**pocket_lining_polyester:** percentage of polyester in the pocket composition in the product.

**scrapy_datetime:** date and time of the data extraction.

</details>


## Results


Given the time needed to accumulate a lot of relevant data for a more in-depth study and to enable faster delivery,
an initial study was conducted with a single day's collection, which practically represents a panorama of the 
products currently on display at the competitor's site.

A more conservative strategy was adopted at this first moment and a single product was chosen, to better understand 
the market in practice and avoid excessive costs with a large number of products that have a greater potential to
generate losses depending on the acceptance of the public.

This type of strategy allows the company to make a greater number of changes to the initial product in order to better
adapt it to consumer preferences. Further characteristics of this entry-level product are discussed bellow in the 
answers to the business questions.


- **What is the ideal selling price of jeans?**

Subsequently, a market entry strategy could be adopted to gain a larger market share, with reduced prices or larger
discounts to attract customers and retain them with the quality of the product, but such strategy requires high 
investment and due to the minimum price presented by competitors reach around $10 make this type of strategy unfeasible.

Thus, we adopted the median price of the competitor's jeans of $22.99 to have a truer impression of the real market
scenario with a competitive price.


- **What types and colors should be considered for the launch collection?**

For working with only one model, the most common type was chosen in the dataset because it is a product that covers
a larger audience, being tbe most popular category the _Slim Jeans_.

The study shows that each model has 6 colors in the median, it is decided to work with the 3 most popular colors and
the 3 colors with lower presence, about 2%, to reach some possible gap in the market, to have less competition and 
a more unique identity. The most popular colors are Denim Blue, Light Denim Blue and Black, the less popular colors 
chosen are Light Blue, Washed Out and Pale Denim Blue. 


What are the raw materials needed to produce the pants?

The most commonly used composition will be adopted, and it will probably be easier to produce without requiring a more
innovative production process and higher costs, making it easier to find suppliers as well. The composition will be 
separated into three types below:
- Composition: 98% of cotton and 2% of spandex.
- Lining composition: 100% polyester.
- Pocket composition: 35% of cotton and 65% of polyester.


## Conclusions

Through the initial study of one of the competitors with a single day sample and by adopting a more conservative
strategy for entering the U.S. market, the results for pricing are shown below:

- Product price: $22.99 based in median price of all products.
- Only one type of jeans with 6 different colors:
  - Denim Blue.
  - Light Denim Blue.
  - Black.
  - Light Blue.
  - Washed Out.
  - Pale Denim Blue.
- Category: Slim Jeans.
- Composition: 98% of cotton and 2% of spandex.
- Lining composition: 100% polyester.
- Pocket composition: 35% of cotton and 65% of polyester.

## Lessons Learned
First development cycle:
- Libraries: Request and Beautiful Soup.
- Language SQL.
- Design ETL.
- Database Schemas.
- Extract of substrings with Regex.
- POO fundamentals.

## Next Steps

The next steps of the project are listed below in priority order and will be approached by the next development cycles.
The goal of the next steps is to collect more different data to assist in pricing, hence to improve the market
research.

- Selenium to collect more data available only with javascript interactive
- Data collect in the Macy's website. 
- User-friendly data visualization software for business teams: Tableau.
- Airflow to schedule and constantly update the database and hel in decision-make.



