# Portfolio

**Creditas**, esse é uma análise completa referente a dados fictícios utilizados dentro de um processo seletivo para trabalhar na empresa. Vale lembrar que eu **NÃO** participei de nenhum processo seletivo na empresa. A obtenção desse conjunto de dados foi por meio de um ex- colega que participou e posteriormente me solicitou ajuda na modelagem dos dados. 
Aqui consta desde os dados analisados, a criação do modelo, o arquivo Peakle contendo os resultados do modelo, e o arquivo da aplicação web. 

-------------------------------------------------------------------------------------------------------------------------------

**KaysCash** esse sim é um arquivo proveniente de um processo seletivo para Cientista de Dados Junior. Na pasta do arquivo, contém a análise, os dados utilizados, os arquivos peakle do modelo, e mais dois arquivos de aplicações web que ainda não foram finalizadas. 

-------------------------------------------------------------------------------------------------------------------------------

**PostgreeSQL**, esse é um arquivo que fiz, para praticar consultas do Python, diretamente nos bancos de dados. Foi utilizado dados do arquivo **DVD RENTAL**, contido no seguinte [link](https://www.postgresqltutorial.com/postgresql-sample-database/).

-------------------------------------------------------------------------------------------------------------------------------

**Simulação de Monte Carlo**, é um arquivo contendo uma simulação de Receita, Despesas e Lucros, com base num arquivo **FICTÍCIO** de receitas mensais. O período é de 12 meses. Em decorrência da pouca quantidade de série histórica para a elaboração de um modelo de série temporal tradicional, a simulação de monte carlo é utilizada justamente para simular diferentes cenários com a pouca quantidade de dados existentes. 

-------------------------------------------------------------------------------------------------------------------------------

**Churn: Análise e Modelo de Machine Learning** é um arquivo de uma competição do Kaggle, aonde deseja prever quais serão os possíveis clientes que pretendem cancelar o serviço de telecomunicação. Primeiramente, foi feito uma análise exploratória dos dados, para buscar entender os dados 
e as suas relações e correlações. Após realizada a analise de exploração dos dados, buscamos construir o nosso modelo. 
O modelo apresentou um score de **0.96444**. 

-------------------------------------------------------------------------------------------------------------------------------

**Heart Atack** é um arquivo referente a classificação de pessoas que podem ou não ter um ataque cardíaco / infarto. Os dados utilizados foram obtidos no site do Kaggle. Buscou-se fazer uma análise exploratória primeiramente, e posteriormente a construção do modelo. O modelo apresentou uma acurácia de **0.8132**.

-------------------------------------------------------------------------------------------------------------------------------

**Vagas.com** é um arquivo referente a classificação de pessoas que foram aprovados ou não em uma determinada vaga de emprego. Os dados utilizados foram obtidos diretamente no [link](https://github.com/VAGAScom/desafio-cientista-de-dados).Primeiramente foi feito um modelo no Pycaret (machine automatizado). Posteriormente foi feita a melhoria no modelo, começando pelo AutoMLSearch, depois foi testado os melhores modelos e aperfeiçoando eles. Primeiramente, foram utilizadas técnicas de normalização nos dados. Os dados se encontravam muito desbalanceados, por isso foi utilizado também o método **Near()** para que fosse balanceados. Após isso o resultado do modelo de machine learning apresentou um **score do Random Forest de 83.90%**. A melhor configuração é:

**Nova precisão: 0.8965
Novo recall: 0.7671
Novo F1 Score: 0.8268
ROC: 0.9092**

Por fim, foi feito uma rede neural para classificar. Os resultados da Rede Neural se assemelham ao do modelo de machine learning. Segue abaixo a pontuação:

**Nova Acuracia: 0.8262
Nova precisão: 0.8341
Nova recall: 0.8140
Nova F1 Score: 0.8239**

Os resultados do arquivo de submissão apresentou os seguintes resultados:
**Machine Learning: 25055 aprovados e 1079 não aprovados
Rede Neural: 24335 aprovados e 1799 não aprovados.** 

-------------------------------------------------------------------------------------------------------------------------------

**Porto Seguro** é um arquivo referente uma competição no site do [Kaggle](https://www.kaggle.com). Foi feito, vários modelos, utilizamos **Pycaret** e pacotes do próprio **Sklearn**. O pycaret foi utilizado para termos uma base de quais modelos perfomariam melhor. E após isso, tratamos de melhorar o modelo de forma mais "personalizada" na biblioteca do Sklearn. Foram tentadas algumas abordagens, como por exemplo, usar **PCA** para diminuirmos a quantidade de variáveis, sem muito sucesso. 
Após isso, algumas variáveis foram excluídas. Após isso, obtivemos as seguintes pontuações:

**Nova precisão: 0.6420
Novo recall: 0.6583
Novo F1 Score: 0.6501
ROC: 0.8733**

Sem a utilização do Pycaret, conseguimos melhorar o nosso modelo final. Saimos de 0.38943 para 0.60690, o que nos colocaria entre os 138° na competição.

No link abaixo, minha submissão feita diretamente no site no **Kaggle**, aonde minha pontução com **Private Score** foi de **0.63696** e o **Public Score de 0.64212**.

Link da resolução no site do Kaggle: https://www.kaggle.com/felipesembay/modelo-gradientboosting

--------------------------------------------------------------------------------------------------------------------------------
**Bolsa de Valores**: Nesta pasta, possui 2 arquivos, um que trata da **Análise Fundamentalista** e o outro que trata do **Calculo de Valuation**. 

O primeiro arquivo trata, desde coletar dados do site [Fundamentus](https://www.fundamentus.com.br/resultado.php), para extração de informações referentes sobretudo a Analise Fundamentalista. Após isso é feito um ranking com algumas informações consideradas importantes. 
Após isso, buscamos os dados das cotações das empresas **Porto Seguro - PSSA3.SA** e da **Marfrig - MRFG3.SA** e comparamos com o **IBOV**. 
Nesse primeiro arquivo é testado também um método de **Otimização** utilizado para calcular quais seriam as melhores retornos de acordo com o problema proposto. Ainda nesse primeiro arquivo, é abordado também, a utilização de médias móveis em gráficos de ações e como elas podem indicar e ajudar na tomada de decisão. 

No segundo arquivo, é trabalhado em cima de variáveis e fórmulas para calcular o **Valuation** de uma determinada empresa, com base no seu **fluxo de caixa presente**. 

--------------------------------------------------------------------------------------------------------------------------------

**Fundos Imobiliários** é um arquivo, que coleta a analisa as informações dos principais fundos imobiliários. Essas análises tem o intuito de ajudar a localizar quais são as melhores oportunidades de investimento em **Fundos Imobiliários no país**. 


--------------------------------------------------------------------------------------------------------------------------------
**PROJEÇÃO INDICADORES ECONOMICAS - JUROS**, neste arquivo, é utilizado as bibliotecas **Quandl e pycaret-ts-alpha** para buscar e gerar modelos de série temporal referente a indicadores macroeconômicos. O arquivo, traz as projeções futuras desde o mês 12/2021 até o mês 12/2023. Segue abaixo resultado final das projeções feitas. 

2021-12     8.4760
2022-01     9.4377
2022-02    10.3553
2022-03    10.9080
2022-04    11.4699
2022-05    11.9859
2022-06    12.4154
2022-07    12.7405
2022-08    12.9434
2022-09    13.0627
2022-10    13.0005
2022-11    12.8475
2022-12    12.6674
2023-01    12.3839
2023-02    12.0607
2023-03    11.7124
2023-04    11.2990
2023-05    10.8544
2023-06    10.3951
2023-07     9.9282
2023-08     9.4646
2023-09     9.0144
2023-10     8.5876
2023-11     8.1758
2023-12     7.7861

Se as projeções se concretizarem, os juros só tenderam a cair com mais força no 2° semestre de 2023. 







