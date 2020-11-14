import pandas as pd
import numpy as np


def getAnalysisData():
    df = pd.read_csv(r'..\DS\DataSet\Nutrients\archive\nutrients_csvfile.csv')

    dfNutrient = pd.DataFrame(df.values,
                              columns=['Food', 'Measure', 'Grams', 'Calories', 'Protein', 'Fat', 'SatFat', 'Fiber'
                                  , 'Carbs', 'Category'])
    # print(dfNutrient)

    dfdata = pd.read_csv(r'..\DS\DataSet\Nutrients\archive\Recipe.csv')
    dfRecipe = pd.DataFrame(dfdata.values, columns=['Food', 'Grams'])
    # print(dfRecipe)
    print('=======recipe=====')
    columnlist = ['Food', 'Measure', 'Grams', 'Calories', 'Protein', 'Fat', 'SatFat', 'Fiber', 'Carbs', 'Category'];
    dfAnalysis = pd.DataFrame(columns=columnlist)

    print('=======Analysis=============')
    analysisFinalData = [];
    for ingredient in dfRecipe.index:
        print(dfRecipe['Food'][ingredient].lower())
        for nutrient in dfNutrient.index:
            analysisData = [];
            if dfRecipe['Food'][ingredient].lower() in dfNutrient['Food'][nutrient].lower():
                analysisData.append(dfNutrient['Food'][ingredient]);
                analysisData.append(dfNutrient['Measure'][ingredient]);
                analysisData.append(int(dfNutrient['Grams'][ingredient]));
                analysisData.append(int(dfNutrient['Calories'][ingredient]));  # tablespoonToGrams
                analysisData.append(int(dfNutrient['Protein'][nutrient]));
                analysisData.append(int(dfNutrient['Fat'][nutrient]));
                analysisData.append(int(dfNutrient['SatFat'][nutrient]));
                analysisData.append(float(dfNutrient['Fiber'][nutrient]));
                analysisData.append(int(dfNutrient['Carbs'][nutrient]));
                analysisData.append(dfNutrient['Category'][nutrient]);
                analysisFinalData.append(analysisData)
                break

    dfAnalysis = pd.DataFrame(analysisFinalData, columns=columnlist)
    return dfAnalysis;


def getTotal(dfAnalysis):
    print('======Summerize Value=====')
    sum_column = dfAnalysis.sum(axis=1)
    return sum_column;
