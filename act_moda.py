# -*- coding: utf-8 -*-
"""Act-MODA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bvf2ONLi3Nq5ezQuLPCPF1ulZ-FbuPnS
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Act-MODA").getOrCreate()

spark

csv_file_path = "/content/Libro 2(Sheet1).csv"
variable = spark.read.csv(csv_file_path, header = True, inferSchema=True)

"""
Contexto:

Se desea saber que dias se ha tenido mas ventas, para ello es necesario la moda.

"""

variable.show()

var_moda = variable.groupBy("Ventas").count().orderBy(col("count").desc()).first()

print("La moda es: ", var_moda["Ventas"])