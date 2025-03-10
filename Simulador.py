from tabulate import tabulate


class MemoryBlock:
    def __init__(self, size, free=True):
        self.size = size  # Tamanho do bloco
        self.free = free  # Se está livre ou ocupado
        self.next = None  # Próximo bloco na lista
        # current é usado como um apontador para os blocos que vão ser utilizados nos métodos FF, NF e BF
        # self, é quase um this do java, parametro que representa a instância da classe, usa para acessar os atributos
        # freed, conta quantos blocos iguais foram liberados, antes so liberava 1, agora libera vários iguais


class MemoryManager:
    def __init__(self):
        self.head = MemoryBlock(128)  # Memória inicial, 128 KB
        self.last_alloc = self.head  # Para Next Fit

    def _split(self, block, size):
        """Divide o bloco se houver espaço extra."""
        if block.size > size:
            new_block = MemoryBlock(block.size - size)
            new_block.next = block.next
            block.next = new_block
            block.size = size

    def _merge(self):
        """Combina blocos livres que estão próximos."""
        current = self.head
        while current and current.next:
            if current.free and current.next.free:
                current.size += current.next.size
                current.next = current.next.next
            else:
                current = current.next

    def allocate(self, size, strategy):
        """Escolhe o algoritmo de alocação."""
        if strategy == 'first_fit':
            return self.first_fit(size)
        elif strategy == 'next_fit':
            return self.next_fit(size)
        elif strategy == 'best_fit':
            return self.best_fit(size)
        return "Erro: Estratégia inválida"

    def first_fit(self, size):
        """Aloca no primeiro bloco disponível."""
        current = self.head
        while current:
            if current.free and current.size >= size:
                self._split(current, size)
                current.free = False
                return f"Alocado {size} KB (First Fit)"
            current = current.next
        return "Erro: Memória insuficiente"

    def next_fit(self, size):
        """Continua a busca de onde parou, a ultima alocação."""
        current = self.last_alloc
        while current:
            if current.free and current.size >= size:
                self._split(current, size)
                current.free = False
                self.last_alloc = current
                return f"Alocado {size} KB (Next Fit)"
            current = current.next or self.head
        return "Erro: Memória insuficiente"

    def best_fit(self, size):
        """Aloca no menor bloco que sirva, vai somando até achar o tamanho certo."""
        best = None
        current = self.head
        while current:
            if current.free and current.size >= size and (not best or current.size < best.size):
                best = current
            current = current.next
        if best:
            self._split(best, size)
            best.free = False
            return f"Alocado {size} KB (Best Fit)"
        return "Erro: Memória insuficiente"

    def free_memory(self, size):
        """Libera todos os blocos ocupados do tamanho especificado."""
        current = self.head
        freed = 0  # Contador de blocos livres, inicia em 0
        while current:
            if not current.free and current.size == size:
                current.free = True  # Marca o bloco como livre
                freed += 1  # Incrementa o contador
            current = current.next
        self._merge()  # Junta blocos livres adjacentes
        return f"Liberados {freed} bloco(s) de {size} KB" if freed > 0 else \
            "Erro: Nenhum bloco desse tamanho encontrado"

    def display_memory(self):
        """Exibe o estado da memória em formato de tabela."""
        current = self.head
        table = []
        while current:
            table.append(["Livre" if current.free else "Ocupado", f"{current.size} KB"])
            current = current.next
        return tabulate(table, headers=["Estado", "Tamanho"], tablefmt="grid")

# Exemplo de uso
# O merge só une blocos livres se estiverem juntos, se tiver ex: 20-10-20-10-10, e pedir para liberar 10KB,
# ele so libera os ultimos 10KB


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
