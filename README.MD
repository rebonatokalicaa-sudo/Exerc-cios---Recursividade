# 🧠 Exercícios de Recursividade em Python

Este projeto contém cinco desafios sobre **funções e recursividade**, desenvolvidos para treinar lógica, uso de escopo, retorno de valores e comparação entre abordagens recursivas e iterativas.  
Os códigos foram feitos de forma simples e didática, para facilitar o entendimento dos conceitos.

---

## 📘 Desafio 1 – Função com múltiplos retornos e escopo

### 📝 Enunciado:
Crie uma função `analisar_numeros(lista)` que:
- Retorne três valores: quantidade de positivos, negativos e zeros.  
- Teste o comportamento ao usar uma **variável global** chamada `total_elementos` e mostre como o escopo interfere no resultado.  
- **Desafio extra:** reescreva sem variável global, usando apenas parâmetros e retornos.

### 💡 Solução:
Foi criada uma função que percorre a lista e conta quantos valores são positivos, negativos ou zeros.  
Na primeira versão, uma variável global controla o total de elementos.  
Na segunda, o total é retornado diretamente, evitando o uso de variáveis globais.

---

## 🔁 Desafio 2 – Soma Recursiva

### 📝 Enunciado:
Implemente uma função recursiva `soma_lista(lista)` que some todos os elementos de uma lista numérica.  
**Exemplo:** `soma_lista([1, 2, 3, 4]) → 10`

### 💡 Solução:
A função chama a si mesma retirando o primeiro elemento da lista a cada passo.  
Quando a lista fica vazia, retorna 0.  
Essa estrutura garante a soma de todos os valores de forma recursiva.

---

## 🔍 Desafio 3 – Recursão com Retorno Condicional

### 📝 Enunciado:
Crie uma função `buscar_maior(lista)` que:
- Retorne o **maior número** da lista usando recursão (sem usar `max()`).
- Mostre no `print` cada comparação feita.

### 💡 Solução:
A função compara o primeiro elemento da lista com o maior encontrado no restante (obtido recursivamente).  
Cada comparação é exibida no terminal, mostrando o processo passo a passo até encontrar o maior valor.

---

## 🧮 Desafio 4 – Sequência de Fibonacci (Recursiva e Iterativa)

### 📝 Enunciado:
Crie duas funções:
- `fibonacci_recursivo(n)`  
- `fibonacci_iterativo(n)`  
Mostre a diferença de performance entre as duas, exibindo o tempo total de execução.

### 💡 Solução:
O método recursivo chama a si mesmo para calcular `f(n-1)` e `f(n-2)`, o que é mais lento.  
O método iterativo usa um `for`, sendo muito mais rápido.  
Foi utilizado o módulo `time` para medir e exibir o tempo de execução.

---

## 📦 Desafio 5 – Controle de Estoque Recursivo

### 📝 Enunciado:
Desenvolva uma simulação para controle de estoque recursivo:  
Cada produto tem **nome** e **quantidade**.  
A função `verificar_estoque(lista, indice=0)` percorre recursivamente a lista e retorna a soma total das quantidades.  
Exibir mensagens como:  
