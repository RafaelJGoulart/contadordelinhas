# Contador de linhas

## Descrição

O Contador de Linhas é uma ferramenta para contar o número de linhas não em branco em arquivos de código-fonte dentro de um diretório e suas subpastas. O programa classifica esses arquivos por extensão e exibe o número total de linhas não em branco para cada tipo de arquivo. É útil para desenvolvedores que desejam analisar a quantidade de código por linguagem em um projeto.

  

## Funcionalidades

Contagem de Linhas: Conta o número de linhas não em branco em arquivos de código-fonte.

Classificação por Extensão: Classifica os arquivos por extensão e exibe o número total de linhas não em branco para cada extensão.

Atualização Periódica: Atualiza a classificação a cada intervalo de tempo definido.

Configuração de Extensões: Permite definir quais extensões de arquivos devem ser consideradas para a contagem através de um arquivo de configuração.

## Como Usar

1. Executar o Programa

Execute o arquivo Contador_de_Linhas.exe criado. A janela principal do programa será aberta.

  

2. Configuração de Extensões

O programa lê as extensões de arquivos a serem contados a partir de um arquivo de configuração JSON chamado config.json.

  

3. Editar o Arquivo de Configuração

Abra o arquivo config.json no seu editor de texto favorito e edite a lista de extensões permitidas. O arquivo JSON deve ter o seguinte formato:

  


`{
    "allowed_extensions": [".js", ".css", ".html"]
}`

Adicione ou remova extensões conforme necessário. Certifique-se de incluir o ponto antes da extensão (por exemplo, .js, .css, .html).

  

4. Definir o Diretório

Digite o caminho para o diretório que você deseja analisar no campo de entrada de diretório e clique no botão "Start" para iniciar a contagem de linhas.

  

5. Visualizar Resultados

O programa exibirá uma lista com as extensões de arquivos e o número total de linhas não em branco para cada extensão. A classificação será atualizada a cada 30 segundos (ou o intervalo definido).

  

## Dependências

O programa usa as seguintes bibliotecas Python:

  

customtkinter para a interface gráfica.

PIL (Python Imaging Library) para manipulação de fontes.

Você pode instalar essas dependências com o seguinte comando:

  


Licença

Este projeto está licenciado sob a MIT License.

  

Exemplo de config.json

Se você quiser que o arquivo de configuração comece com algumas extensões comuns, pode criar um arquivo config.json com o seguinte conteúdo:

  

json

Copiar código

{

    "allowed_extensions": [
	    ".js",
	    ".css", 
	    ".html",
	    ".py", 
	    ".java", 
	    ".cpp", 
	    ".c"
      ]

}

Observações

O programa não possui um menu para abrir o arquivo de configuração a partir da interface gráfica, então você deve editar o config.json manualmente.

Certifique-se de que o config.json esteja no mesmo diretório do executável ou especifique o caminho correto para ele no código.