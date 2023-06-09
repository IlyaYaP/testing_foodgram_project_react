
class DataRecipeCreateBreakfast():
    RECIPE_NAME = 'Ленивые хачапури с сыром на сковороде на кефире'
    MEAL =  'Завтрак'
    INGREDIENTS = {
                   'мука': '50',
                   'кефир': ' 100',
                   'яйца': '1',
                   'масло':'100',
                   'сыр': '120'
                   }
    COOKING_TIME = '60'
    RECIPE_DESCRIPTION = 'Для приготовления ленивых хачапури подойдет любой сыр, \
                          который можно натереть на терке, я взяла сулугуни. \
                          Он достаточно соленый, поэтому соль в тесто класть не надо.\
                          Если у вас не оказалось кефира, возьмите сметану,\
                          творог или простоквашу - подойдет все, что заскучало в вашем холодильнике.\
                          Если вы взяли творог, то надо будет добавить немного молока.\
                          Можно положить рубленую зелень сразу в тесто или сделать что-то типа начинки.\
                          Для этого после того, как вы перевернете лепешку,\
                          посыпьте ее зеленью и сложите пополам, затем жарьте с двух сторон.'
    
    IMAGE_NAME = 'lenivye-xachapuri.jpg'
    
    RECIP_DATA_BREAKFAST= [RECIPE_NAME, 
                            COOKING_TIME, 
                            RECIPE_DESCRIPTION, 
                            MEAL, 
                            INGREDIENTS, 
                            IMAGE_NAME]


class DataRecipeCreateLunch():
    RECIPE_NAME = 'Говядина с болгарским перцем'
    MEAL =  'Обед'
    INGREDIENTS = {
                   'говядина': '800',

                   'помидоры': '100',
                   'вода':'100',
                   'перец': '200',
                   'лук': '200',
                   }
    COOKING_TIME= '80'
    RECIPE_DESCRIPTION = 'Невероятно аппетитная и нежная, покорит с первого раза!\
                                Говядину с болгарским перцем можно подать как\
                                самостоятельное блюдо или в дополнение в любым гарниром.\
                                Идеальное угощение на праздничный стол:\
                                мягкое тушеное сочное мясо с ароматной подливкой\
                                и овощами никого не оставит равнодушным.'
    
    IMAGE_NAME = 'govyadina-s-bolgarskim-percem.jpg'

    RECIP_DATA_LUNCH = [RECIPE_NAME,
                         COOKING_TIME,
                         RECIPE_DESCRIPTION,
                         MEAL,
                         INGREDIENTS,
                         IMAGE_NAME]


class DataRecipeCreateDinner():
    RECIPE_NAME = 'Сало в соевом соусе вареное'
    MEAL =  'Ужин'
    INGREDIENTS= {
                   'сало': '250',
                   'вода': ' 200',
                   'соевый': '250',
                   'чеснок': '15',

                   }
    COOKING_TIME = '60'
    RECIPE_DESCRIPTION = 'Потрясающе ароматное и мягкое,\
                                 никто не сможет устоять!\
                                 Сало в соевом соусе вареное делается очень легко и просто!\
                                 Его можно предложить гостям на праздничный стол\
                                 в виде закуски или подать на семейный ужин.\
                                 Оно прекрасно сочетается со свежими овощами\
                                 или салатами. Обязательно пробуем!'
    
    IMAGE_NAME = 'salo-v-soevom-souse-varenoe.jpg'


    RECIP_DATA_DINNER = [RECIPE_NAME,
                          COOKING_TIME,
                          RECIPE_DESCRIPTION,
                          MEAL,
                          INGREDIENTS,
                          IMAGE_NAME]

