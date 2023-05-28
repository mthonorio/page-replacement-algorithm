from in_out import open_file

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru_list = []

    def get(self, page):
        if page in self.cache:
            self.lru_list.remove(page)
            self.lru_list.append(page)
            return True
        else:
            return False

    def put(self, page):
        if len(self.lru_list) >= self.capacity:
            evicted_page = self.lru_list.pop(0)
            del self.cache[evicted_page]
        self.cache[page] = True
        self.lru_list.append(page)


def LRU(file):
    # Ler o arquivo, retornar a capacidade da memória e a lista de páginas
    page_capacity, pages = open_file(file)
    page_faults = 0  # Contador de faltas de página
    cache = LRUCache(page_capacity)

    for page in pages:
        if cache.get(page):
            continue
        else:
            cache.put(page)
            page_faults += 1

    print(f"LRU {page_faults}")
    return page_faults
