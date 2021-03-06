from pyspark.sql.functions import *

#armazenando diretório do arquivo
path = "c://exemplo/exemplo.csv"


#criando data frame para leitura, com cabeçalho ativado e delimitador ";"
df_spark = (spark.read.format("csv")
           .option("header", "true")
           .option("delimiter", ";")
           .load(path)             )

#visualizar dados
display(df_spark)

#para renomear uma ou mais colunas, faça o seguinte
df_spark = (df_spark
                       .withColumnRenamed("nome_antigo", "nome_novo")
                       .withColumnRenamed("nome_antigo", "nome_novo")
            )



#alterando datatype 

#exibindo tipo de dados armazenados no dataframe
df_spark.printSchema

# no exemplo abaixo temos 2 colunas: order_date e ship_date, elas estão no formato "string" dd/mm/yyyy e precisamos converter
# para yyyy-mm-dd para armazenar no banco de dados

df_spark = (df_spark
                   .withColumn("order_date",    to_date("order_date", "dd/MM/yyyy"))
                   .withColumn("ship_date",     to_date("ship_date", "dd/MM/yyyy"))

)


#substituindo (replace) valores em uma coluna com regexp_replace
df_spark = (df_spark
                    .withColumn("coluna_x", regexp_replace("coluna_x", ",", ".") #troca "," por "." na coluna inteira
                    .withColumn("coluna_y", regexp_replace("coluna_y", "A", "B") #troca todos os caracteres "A" por "B" na coluna inteira
)

