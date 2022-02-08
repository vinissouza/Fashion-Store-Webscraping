# from data_collect import DataCollect
# from data_transform import DataTransform
# from data_insert import DataInsert
#
#
# if __name__ == '__main__':
#
#     # Data Collect from H&M
#     url = 'https://www2.hm.com/en_us/men/products/jeans.html'
#
#     data_collect = DataCollect(url)
#
#     page = data_collect.api_request()
#
#     soup = data_collect.beautifulsoup_object(page)
#
#     page_number = data_collect.number_of_products(soup)
#
#     data_showroom = data_collect.showroom_products(page_number)
#
#     data_color = data_collect.product_color(data_showroom)
#
#     data_attributes = data_collect.product_attributes(data_color)
#
#     data_collect = data_collect.join_data(data_showroom, data_color, data_attributes)
#
#     # print( data_showroom.shape )
#     # print( data_color.shape )
#     # print( data_attributes.shape )
#     # print( data_raw.shape )
#     # print( data_raw )
#     # print( data_raw.isna().sum() )
#     #
#     # data_showroom = pd.read_csv('../Datasets/data_showroom')
#     # data_color = pd.read_csv('../Datasets/data_color')
#     # data_attributes = pd.read_csv('../Datasets/data_attributes')
#
#     # Data Transform
#
#     # Data Showroom Transform
#     showroom_transform = DataTransform(data_showroom)
#
#     data_showroom_processed = showroom_transform.showroom_transform()
#
#     data_showroom_processed.to_csv(
#         '../Datasets/data_showroom_processed.csv', index=False
#     )
#
#     print( 'data_showroom_processed finished' )
#
#     # Data Color Transform
#     color_transform = DataTransform(data_color)
#
#     data_color_processed = color_transform.color_transform()
#
#     data_color_processed.to_csv(
#         '../Datasets/data_color_processed.csv', index=False
#     )
#
#     print( 'data_color_processed finished' )
#
#     # Data Composition Feature
#     composition_transform = DataTransform(data_attributes)
#
#     data_composition_feature = composition_transform.composition_feature()
#
#     data_composition_feature.to_csv(
#         '../Datasets/data_composition_feature.csv', index=False
#     )
#
#     print( 'data_composition_feature finished' )
#
#     # Data Material Feature
#     material_transform = DataTransform(data_composition_feature)
#
#     data_material_feature = material_transform.material_feature()
#
#     data_material_feature.to_csv(
#         '../Datasets/data_material_feature.csv', index=False
#     )
#
#     print( 'data_material_feature finished' )
#
#     # Data Attributes Transform
#     attributes_transform = DataTransform(data_material_feature)
#
#     data_attributes_processed = attributes_transform.attributes_transform()
#
#     data_attributes_processed.to_csv(
#         '../Datasets/data_attributes_processed.csv', index=False
#     )
#
#     print( 'data_attributes_processed finished' )
#
#     # DATA LOAD
#
#     # Data Showroom Insertion
#     # with DataInsert(data_showroom_processed,
#     #                 table_name='showroom_table') as showroom_insertion:
#     #     showroom_insertion.insert_data()
#
#     showroom_insertion = DataInsert(data_showroom_processed, table_name='showroom_table')
#
#     showroom_insertion.insert_data()
#
#     # Data Color Insertion
#     with DataInsert(data_color_processed,
#                     table_name='color_table') as color_insertion:
#         color_insertion.insert_data()
#
#     # color_insertion = DataInsert(data_color_processed, table_name='data_color')
#     # color_insertion.insert_data()
#
#     # Data Attributes Insertion
#     with DataInsert(data_attributes_processed,
#                     table_name='attributes_table') as attributes_insertion:
#         attributes_insertion.insert_data()
#
#     # attributes_insertion = DataInsert(data_attributes_processed, table_name='data_attributes')
#     # attributes_insertion.insert_data()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from Model.data_collect import DataCollect
from Model.data_transform import DataTransform
from Model.data_insert import DataInsert


def data_extraction(url):
    data_collect = DataCollect(url)

    #page = data_collect.api_request()

    #soup = data_collect.beautifulsoup_object(page)

    #page_number = data_collect.number_of_products(soup)

    data_showroom = data_collect.showroom_products()

    data_color = data_collect.product_color(data_showroom)

    data_attributes = data_collect.product_attributes(data_color)

    data_collect = data_collect.join_data(data_showroom, data_color, data_attributes)

    return data_showroom, data_color, data_attributes


def data_transform(data_showroom, data_color, data_attributes):
    # Data Showroom Transform
    showroom_transform = DataTransform(data_showroom)

    data_showroom_processed = showroom_transform.showroom_transform()

    data_showroom_processed.to_csv(
        '../Datasets/data_showroom_processed.csv', index=False
    )

    print('data_showroom_processed finished')

    # Data Color Transform
    color_transform = DataTransform(data_color)

    data_color_processed = color_transform.color_transform()

    data_color_processed.to_csv(
        '../Datasets/data_color_processed.csv', index=False
    )

    print('data_color_processed finished')

    # Data Composition Feature
    composition_transform = DataTransform(data_attributes)

    data_composition_feature = composition_transform.composition_feature()

    data_composition_feature.to_csv(
        '../Datasets/data_composition_feature.csv', index=False
    )

    print('data_composition_feature finished')

    ## data material feature
    material_transform = DataTransform(data_composition_feature)

    data_material_feature = material_transform.material_feature()

    data_material_feature.to_csv(
        '../Datasets/data_material_feature.csv', index=False
    )

    print('data_material_feature finished')

    ## data attributes transform
    attributes_transform = DataTransform(data_material_feature)

    data_attributes_processed = attributes_transform.attributes_transform()

    data_attributes_processed.to_csv(
        '../Datasets/data_attributes_processed.csv', index=False
    )

    print('data_attributes_processed finished')

    return data_showroom_processed, data_color_processed, data_attributes_processed


def data_insert(data, table_name):
    with DataInsert(data,
                    table_name=table_name) as data_insertion:
        data_insertion.insert_data()

    return None


if __name__ == '__main__':
    # extraction
    url = 'https://www2.hm.com/en_us/men/products/jeans.html'

    showroom_collect, color_collect, attributes_collect = data_extraction(url=url)

    # transform
    showroom_process, color_process, attributes_process = data_transform(showroom_collect, color_collect,
                                                                         attributes_collect)

    # load
    data_insert(showroom_process, table_name='showroom_table')

    data_insert(color_process, table_name='color_table')

    data_insert(attributes_process, table_name='attributes_table')
