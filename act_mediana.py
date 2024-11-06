# -*- coding: utf-8 -*-
"""Act-MEDIANA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Ir6qXQ2-PHDPOEDg-LQMYwj1BrXfgZi
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Act-MEDIANA").getOrCreate()

spark

csv_file_path = "/content/Libro 1(Sheet1).csv"
variable = spark.read.csv(csv_file_path, header = True, inferSchema=True)

"""
Contexto:
Encuentra la mediana del salario de los empleados
"""

variable.show()

var_mediana =variable.approxQuantile("Salario",[0.5],0.0)

print("La mediana es: ", var_mediana)