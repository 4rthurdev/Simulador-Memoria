# Memory Manager

## Descrição

Este projeto implementa um **Gerenciador de Memória** que simula a alocação e liberação de blocos de memória de acordo com diferentes estratégias de alocação: **First Fit**, **Next Fit** e **Best Fit**. O sistema gerencia blocos de memória dinâmica de maneira eficiente e permite visualizar o estado da memória utilizando a biblioteca `tabulate` para melhor apresentação.

## Funcionalidades

- **Alocação de Memória:** Possibilidade de alocar blocos de memória utilizando diferentes algoritmos.
- **Liberação de Memória:** Libera blocos de memória especificados, consolidando espaços livres adjacentes.
- **Visualização do Estado da Memória:** Exibe a representação da memória em formato de tabela utilizando `tabulate`.
- **Gerenciamento Otimizado:** Implementa técnicas de divisão e fusão de blocos para maximizar o uso da memória.

## Algoritmos de Alocação

1. **First Fit:** Encontra o primeiro bloco livre que tenha tamanho suficiente e o aloca.
2. **Next Fit:** Continua a busca de onde parou na última alocação, melhorando a performance em algumas situações.
3. **Best Fit:** Encontra o menor bloco disponível que seja suficiente para a alocação, minimizando desperdício de memória.

## Estrutura do Código

### Classe `MemoryBlock`

Representa um bloco de memória na lista encadeada. Cada bloco possui:
- `size`: tamanho do bloco.
- `free`: booleano que indica se o bloco está livre.
- `next`: referência para o próximo bloco.

### Classe `MemoryManager`

Gerencia a memória e implementa os algoritmos de alocação:
- `allocate(size, strategy)`: Aloca um bloco de memória usando a estratégia escolhida.
- `free_memory(size)`: Libera blocos ocupados de um determinado tamanho.
- `display_memory()`: Exibe o estado atual da memória em formato de tabela usando `tabulate`.
- `_split(block, size)`: Divide um bloco caso sobre espaço extra.
- `_merge()`: Junta blocos livres adjacentes.

## Exemplo de Uso

```python
from tabulate import tabulate

memory = MemoryManager()
print(memory.allocate(20, 'first_fit'))
print(memory.allocate(10, 'first_fit'))
print(memory.allocate(20, 'next_fit'))
print(memory.allocate(10, 'next_fit'))
print(memory.allocate(10, 'best_fit'))
print(memory.allocate(10, 'best_fit'))
print(memory.display_memory())
print(memory.free_memory(10))
print(memory.display_memory())
```

Saída esperada:
```text
Alocado 20 KB (First Fit)
Alocado 10 KB (First Fit)
Alocado 20 KB (Next Fit)
Alocado 10 KB (Next Fit)
Alocado 10 KB (Best Fit)
Alocado 10 KB (Best Fit)
+---------+----------+
| Estado  | Tamanho  |
+---------+----------+
| Ocupado | 20 KB    |
| Ocupado | 10 KB    |
| Ocupado | 20 KB    |
| Ocupado | 10 KB    |
| Ocupado | 10 KB    |
| Ocupado | 10 KB    |
| Livre   | 48 KB    |
+---------+----------+
Liberados 3 bloco(s) de 10 KB
+---------+----------+
| Estado  | Tamanho  |
+---------+----------+
| Ocupado | 20 KB    |
| Livre   | 10 KB    |
| Ocupado | 20 KB    |
| Livre   | 10 KB    |
| Livre   | 10 KB    |
| Livre   | 10 KB    |
| Livre   | 48 KB    |
+---------+----------+
```

# Lembre-se de ler os comentários no código se tiver dúvidas.
