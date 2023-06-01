from in_out import open_file


def optimal(file):
    # Ler o arquivo, retornar a capacidade da memória e a lista de páginas
    page_capacity, pages = open_file(file)

    # Initialize variables
    page_faults = 0  # Contador de faltas de página
    frame = []  # Lista para armazenar as páginas na memória

    for page in pages:
        distances = []
        if page not in frame:
            page_faults += 1
            if len(frame) == page_capacity:
                # Encontra a página mais distante no futuro para substituir
                future_pages = pages[pages.index(page):]
                index_of_farthest_page = max(future_pages, key=future_pages.index) - 1
                farthest_page = future_pages[index_of_farthest_page]
                if farthest_page not in frame:
                    for f in frame:
                        distance_of_f = (f, future_pages.index(f))
                        distances.append(distance_of_f)
                    max_distance = max(distances, key=lambda distance: distance[1])
                    frame[frame.index(max_distance[0])] = farthest_page
            else:
                frame.append(page)

    print(f"OTM {page_faults}")
    return page_faults
