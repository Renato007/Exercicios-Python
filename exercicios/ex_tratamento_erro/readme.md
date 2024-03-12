# Tratamento de Erro

## Resolução de erros com if
Podemos ter um código que checa se ocorreu se o resultado da função é um erro ou não.
Demostrado no exercicio [calcul_tratamento_de_erro_if](./calcul_tratamento_de_erro_if.py)

Observação: em alguns casos não é possível utilizá-lo ou seu uso tornaria código mais complicado de ser desenvolvido.

## Estrutura de exceção e de tratamento de erros
São usadas para tratar erros inesperados que podem aparecer durante o código. Elas possuem a seguinte estrutura:

> try: CODIGO except CODIGO

Demostrado no exercicio: [calcul_tratamento_de_erro_estrut_excecao](./ex_tratamento_de_erro_estrut_excecao.py)

observação:

Caso você tenha o interesse de averiguar o erro, é possível mostrar na tela adicionando o texto except Exception as e: ao invés de apenas except:. Assim, uma variável é criada com o erro que foi executado.
 

Vale destacar que a forma como o erro é mostrado é diferente de quando o código é executado sem o try exception. Mesmo mostrando o erro, o código não para de rodar, ele apenas mostra a mensagem.

### nota

Essas estruturas preparam o código para executarem ações caso erros predeterminados ocorram. Assim, evitam que o erro interrompa a execução  do programa.