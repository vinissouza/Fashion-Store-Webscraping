import numpy as np
import pandas as pd


class DataTransform:

    def __init__(self, data):
        self.data = data

    def columns_pattern(self):
        # get columns name from dataframe
        columns = list(self.data.columns)

        # remove spaces, specified characters and format to snake case
        columns = list(map( lambda x: x.strip().lower().replace(' ', '_').replace(':', '').replace('.', ''), columns))
        self.data.columns = columns

        # for col in columns:
        #     self.data[col] = self.data[col].apply(
        #         lambda x: x.strip().lower().replace(' ', '_').replace(':', '')
        #     )

        return self.data

    def price_format(self):
        # format price columns to float
        self.data['product_price'] = self.data['product_price'].apply(
            lambda x: float(x.replace('$', '').strip()) if pd.notnull(x) else x
        )

        return self.data

    def str_values_pattern(self):
        # select string subset of the dataframe
        #data_cat = self.data.select_dtypes(include='str')

        # get string columns name from dataframe
        columns = list(self.data.select_dtypes(include='object').columns)

        # remove spaces, specified characters and format to snake case
        for col in columns:
            self.data[col] = self.data[col].apply(
                lambda x: x.strip().lower().replace(' ', '_') if pd.notnull(x) else x
            )

        return self.data

    def model_code_feature(self):

        # feature unique model code without color info
        self.data['model_code'] = self.data['product_id'].apply(
            lambda x: str(x[:-3])
        )

        # feature color code from products
        self.data['color_code'] = self.data['product_id'].apply(
            lambda x: str(x[-3:])
        )

        return self.data

    def showroom_transform(self):
        # format columns name if necessary
        self.columns_pattern()

        # format price columns to float
        self.data = self.price_format()

        # format string to pattern
        self.str_values_pattern()

        # feature model and color code to assist in merge
        self.model_code_feature()

        # rearrange columns in dataframe
        self.data = self.data[['product_id', 'model_code', 'color_code', 'product_category',
                               'product_name', 'product_price', 'product_link']]

        return self.data

    def color_transform(self):
        # format columns name if necessary
        self.data = self.columns_pattern()

        # format string to snake case
        self.data = self.str_values_pattern()

        # feature model and color code to assist in merge
        self.data = self.model_code_feature()

        # rearrange columns in dataframe
        self.data = self.data[['product_id', 'model_code', 'color_code',
                               'color_name', 'product_link']]

        return self.data

    def composition_feature(self):
        # composition data feature
        data_composition = pd.DataFrame(
            self.data['Composition'].str.strip().str.split('\n', expand=True)
        ).fillna(np.nan)

        # empty list to fill with all compositions type
        compositions_type = []

        # iterable to find all compositions types
        for i in range(len(data_composition.columns)):
            compositions_type += data_composition[i].str.extract('(.+:)')[0].unique().tolist()

        # result from all unique compositions type find in dataset
        compositions_type = list(filter(pd.notna, list(set(compositions_type))))

        # empty dataframe to store all composition type data
        df_composition = pd.DataFrame(index=range(len(data_composition)))

        # iterable to go through all composition dataframe columns
        for i in range(len(data_composition.columns)):
            # empty list to fill with all boolean that contain certain compositions type
            all_comp_type = []

            # iterable to create all composition type columns in df_composition
            for comp_type in compositions_type:
                contain_comp_type = data_composition[i].str.contains(comp_type, na=True)

                all_comp_type.append(contain_comp_type)

                df_composition.loc[contain_comp_type, comp_type] = data_composition.loc[contain_comp_type, i]

            # create material columns from composition without type
            contain_all_types = pd.DataFrame(all_comp_type).sum().apply(lambda x: False if x == 0 else True)

            df_composition.loc[(~contain_all_types) &
                               (pd.notnull(data_composition[i])),
                               'material'] = data_composition.loc[(~contain_all_types) &
                                                                  (pd.notnull(data_composition[i])), i]

        # drop old composition column
        self.data = self.data.drop(columns=['Composition'])

        # join data with new composition features
        self.data = pd.concat([self.data, df_composition], axis=1)

        return self.data

    def material_feature(self):
        # create dataframe for each material
        data_material = pd.DataFrame(
            self.data['material'].str.strip().str.split(',', expand=True)
        ).fillna(np.nan)

        # empty list to fill with all material type
        material_type = []

        # iterable to find all materials types
        for i in range(len(data_material.columns)):
            material_type += data_material[i].astype(str).str.extract('([A-Z][a-z]+-?[A-Z]?).')[0].unique().tolist()

        # unique list with materials types
        material_type = list(filter(pd.notna, list(set(material_type))))

        # empty dataframe to store materials type
        df_materials = pd.DataFrame(
            index=range(len(data_material))
        )

        # iterable to go through all materials columns
        for i in range(len(data_material.columns)):

            # iterable to create all materials types columns
            for mat_type in material_type:
                contain_mat_type = data_material[i].str.contains(mat_type, na=False)

                df_materials.loc[contain_mat_type, mat_type] = data_material.loc[contain_mat_type, i]

        # join data with new materials features
        self.data = pd.concat([self.data, df_materials], axis=1)

        # drop material column
        self.data = self.data.drop(columns=['material'])

        return self.data

    def attributes_transform(self):
        # self.data = self.composition_feature()
        #
        # self.data = self.material_feature()

        # # composition data feature
        # data_composition = pd.DataFrame(
        #     self.data['Composition'].str.strip().str.split('\n', expand=True)
        # )
        #
        # # empty list to fill with all compositions type
        # compositions_type = []
        #
        # # iterable to find all compositions type
        # for i in range(len(data_composition.columns)):
        #     compositions_type += data_composition[i].str.extract('(.+:)')[0].unique().tolist()
        #
        # # result from all unique compositions type find in dataset
        # compositions_type = list(filter(pd.notna, list(set(compositions_type))))
        #
        # # empty dataframe to store all composition type data
        # df_composition = pd.DataFrame(index=range(len(data_composition)))
        #
        # # iterable to go through all composition dataframe columns
        # for i in range(len(data_composition.columns)):
        #     # empty list to fill with all boolean that contain certain compositions type
        #     all_comp_type = []
        #
        #     # iterable to create all composition type columns in df_composition
        #     for comp_type in compositions_type:
        #         contain_comp_type = data_composition[i].str.contains(comp_type, na=True)
        #
        #         all_comp_type.append(~contain_comp_type)
        #
        #         df_composition.loc[contain_comp_type, comp_type] = data_composition.loc[contain_comp_type, i]
        #
        #     contain_non_type = pd.DataFrame(all_comp_type).sum().apply(lambda x: False if x == 0 else True)
        #
        #     df_composition.loc[(~contain_non_type) &
        #                        (pd.notnull(data_composition[i])),
        #                        'composition'] = data_composition.loc[(~contain_non_type) &
        #                                                              (pd.notnull(data_composition[i])), i]
        #
        # # drop old composition column
        # self.data = self.data.drop(columns=['Composition'])
        # # join data with new composition features
        # self.data = pd.concat([self.data, df_composition], axis=1)

        # format columns name if necessary
        self.data = self.columns_pattern()

        # format price columns to float
        self.data = self.price_format()

        # format string to snake case
        self.data = self.str_values_pattern()

        # change article number to product_id as standard
        self.data = self.data.rename(columns={'art_no': 'product_id'})

        # feature  model and color code to assist in merge
        self.model_code_feature()

        return self.data













