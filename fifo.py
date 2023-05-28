from in_out import open_file


def fifo(file):
    # Ler o arquivo, retornar a capacidade da memória e a lista de páginas
    page_capacity, pages = open_file(file)

    # Initialize variables
    page_faults = 0  # Contador de faltas de página
    frame = []  # Lista para armazenar as páginas na memória

    for page in pages:
        if page not in frame:
            page_faults += 1
            if len(frame) == page_capacity:
                frame.pop(0)
            frame.append(page)
        else:
            continue
    
    print(f"FIFO {page_faults}")
    return page_faults
