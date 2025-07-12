from veb_tree import VanEmdeBoasTree

def process_commands(input_file, output_file):
    universe_size = 2**32  # universo de 32 bits
    tree = VanEmdeBoasTree(universe_size)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue  # pula linhas vazias

            parts = line.split()
            cmd = parts[0]

            if cmd == 'INC':
                x = int(parts[1])
                tree.insert(x)
                outfile.write(f"{line}\n")
            elif cmd == 'REM':
                x = int(parts[1])
                tree.delete(x)
                outfile.write(f"{line}\n")
            elif cmd == 'SUC':
                x = int(parts[1])
                result = tree.successor(x)
                outfile.write(f"{line}\n")
                if result is not None:
                    outfile.write(f"{result}\n")
            elif cmd == 'PRE':
                x = int(parts[1])
                result = tree.predecessor(x)
                outfile.write(f"{line}\n")
                if result is not None:
                    outfile.write(f"{result}\n")
            elif cmd == 'IMP':
                outfile.write(f"{line}\n")
                output = print_structure(tree)
                outfile.write(f"{output}\n")
            else:
                outfile.write(f"Comando inválido: {line}\n")


def print_structure(tree):
    if tree.min is None:
        return "Min: None"

    parts = [f"Min: {tree.min}"]
    for c in sorted(tree.clusters.keys()):
        cluster_values = collect_cluster_values(tree.clusters[c])
        if cluster_values:
            parts.append(f"C[{c}]: {', '.join(map(str, cluster_values))}")
    return ", ".join(parts)


def collect_cluster_values(cluster):
    # Coleta todos os valores da sub-árvore recursivamente
    values = []
    if cluster.min is not None:
        values.append(cluster.min)
    for sub_cluster in cluster.clusters.values():
        values.extend(collect_cluster_values(sub_cluster))
    return values


if __name__ == "__main__":
    # Exemplo de uso
    input_file = 'entrada.txt'
    output_file = 'saida.txt'
    process_commands(input_file, output_file)
