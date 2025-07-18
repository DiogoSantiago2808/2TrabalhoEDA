# 2º Trabalho de EDA - Van Emde Boas

## Como rodar?

Dentro do diterório, rode, no terminal:

`python test_veb_tree $(ARQUIVO_ENTRADA)`

Onde `$(ARQUIVO_ENTRADA)` é o arquivo-texto com as especificações da estrutura.
exemplo: python test_veb_tree.py entrada.txt

## Resumo do código

Os componentes do programa se encontram em dois arquivos Python distintos:

#### veb_tree.py

Este é o arquivo que define e implementa os métodos da estrutura da árvore Van Emde Boas, sendo o arquivo inteiro a classe da estrutura. Nela é implementada os métodos requisitados nas especificações do trabalho, sendo estes:

- Inclusão: `VanEmdeBoasTree.insert`
- Remoção: `VanEmdeBoasTree.delete`
- Sucessor: `VanEmdeBoasTree.successor`
- Predecessor: `VanEmdeBoasTree.predecessor`
- Imprimir: `VanEmdeBoasTree.print_structure`

Para além desses métodos, também existem métodos auxiliares para o desenvolvimento desses algoritmos, sendo estes:

- `VanEmdeBoasTree.high`: Para definir qual sub-árvore está um elemento X;
- `VanEmdeBoasTree.low`: Para definir o índice dentro da sub-árvore que X está que o representa;
- `VanEmdeBoasTree.index`: Para reconstruir X dados os valores de high e low;

#### test_veb_tree.py

Este é o arquivo que define as operações de leitura e escrita dos arquivos-texto, além de possuir métodos auxiliares para o funcionamento desse algoritmo, sendo eles:

- `process_commands`: Processa o arquivo-texto de entrada seguindo as especificações do trabalho;
- `print_structure`: Imprime a estrutura;
- `collect_cluster_values`: Retorna os valores presentes na árvore de forma ordenada.

Este arquivo também é o arquivo principal pelo o qual o usuário deve testar seus arquivos de entrada.
