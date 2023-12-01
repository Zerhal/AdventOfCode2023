def read_file(file_name):
    # Ouvre le fichier et lit toutes les lignes
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_sum_part_one(lines):
    # Transforme chaque ligne en une liste de chiffres
    numbers = [[char for char in line if char.isdigit()] for line in lines]
    total_sum = 0

    for numbers_on_line in numbers:
        # Ignore les lignes sans chiffres
        if not numbers_on_line:
            continue
        elif len(numbers_on_line) == 1:
            # Si un seul chiffre, ajoute le double à la somme
            total_sum += int(numbers_on_line[0] * 2)
        else:
            # Sinon, ajoute le premier et le dernier chiffre à la somme
            total_sum += int(numbers_on_line[0] + numbers_on_line[-1])

    return total_sum

def calculate_sum_part_two(lines):
    def replace_if_exists(string):
        # Dictionnaire de correspondances entre les mots et les chiffres
        digit_strings = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        for string_num, int_num in digit_strings.items():
            # Recherche du mot dans la chaîne
            if string_num in string:
                return string_num, int_num
        return None

    def replace_string_number(line, backwards=False):
        partial_string = ""
        for char in line:
            # Si un chiffre est trouvé avant une lettre, retourne la ligne inchangée
            if char.isdigit():
                return line[::-1] if backwards else line

            # Ajoute les caractères un par un pour trouver le mot correspondant
            partial_string = char + partial_string if backwards else partial_string + char
            if (num := replace_if_exists(partial_string)) is not None:
                to_replace = num[0][::-1] if backwards else num[0]
                replaced = line.replace(to_replace, str(num[1]), 1)
                return replaced[::-1] if backwards else replaced

        return line[::-1] if backwards else line

    modified_lines = []
    for line in lines:
        # Remplace les mots par les chiffres dans la ligne
        line = replace_string_number(line)
        line = replace_string_number(line[::-1], backwards=True)
        modified_lines.append(line)

    # Calcule la somme avec les lignes modifiées
    return calculate_sum_part_one(modified_lines)

# Nom du fichier à lire
file_name = 'input.txt'
# Lecture du fichier
file_lines = read_file(file_name)

# Affichage des résultats des deux parties
print(calculate_sum_part_one(file_lines))
print(calculate_sum_part_two(file_lines))
