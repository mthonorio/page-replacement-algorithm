# Algoritmo de Substituição de Página

Este projeto foi desenvolvido como trabalho final da disciplina de Sistemas Operacionais I no semestre 2022.1 ministrada pelo professor Fernando.

## Especificação do Projeto

Implementar uma simulação do funcionamento dos principais algoritmos de substituição de páginas estudados na disciplina.
Os algoritmos de substituição de páginas a serem implementados são os seguintes:

- FIFO (First In, First Out)
- OTM: Algoritmo Ótimo
- LRU: (Least Recently Used ou Menos Recentemente Utilizado)

O programa deverá ler de um arquivo um conjunto de número inteiros onde o primeiro número representa a quantidade de quadros de memória disponíveis na RAM e os demais representam a sequência de referências às páginas, sempre um número por linha.
Deverá imprimir na saída o número de faltas de páginas obtido com a utilização de cada um dos algoritmos.

### Descrição da entrada:

A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória RAM e, em seguida, a sequência de referências à memória.

### Descrição da saída:

A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a utilização de cada um deles

## Execução

Antes de executar o programa é necessário passar o argumento de localização no arquivo principal `main.py`:

Para alterar os parâmetros ou arquivos a serem executados basta alterar as constantes do início do arquivo main.py:
```
file_path = "tests/example1.txt"
```

Depois disso, basta executar no terminal:
```
python main.py
```