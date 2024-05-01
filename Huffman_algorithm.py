import os

def clean_dictionary(dictionary): # Función para limpiar el diccionario
    del_keys = [] # Lista para almacenar las llaves a eliminar
    for key, value in dictionary.items(): #Estructura de control para recorrer el diccionario
        if value == 0: # Si el valor es 0
            del_keys.append(key) # Agrega la llave a la lista
    for key in del_keys: # Estructura de control para recorrer la lista de llaves a eliminar
        del dictionary[key] # Elimina la llave del diccionario
    
    dictionary = sorted(dictionary.items(), key=lambda x:x[1]) # Ordena el diccionario por los valores de menor a mayor 
    return dictionary # Regresa el diccionario

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None
        self.code = None

    def __str__(self): # Método para imprimir el nodo
        return f"Character: {self.char}, Frequency: {self.freq}"

    def huffman_tree(dictionary): # Método para crear el árbol de Huffman
        nodes = [TreeNode(key, value) for key, value in dictionary.items()]
        #print(nodes)
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq) # Ordena los nodos por frecuencia
            left = nodes.pop(0) # Elimina el primer nodo
            right = nodes.pop(0) # Elimina el segundo nodo
            new_node = TreeNode(None, left.freq + right.freq) # Crea un nuevo nodo con la suma de las frecuencias de los nodos eliminados
            new_node.left = left # Asigna el nodo izquierdo
            new_node.right = right # Asigna el nodo derecho
            nodes.append(new_node) # Agrega el nuevo nodo a la lista de nodos
            # Print nodes at each iteration
        return nodes
    
    def code_maker(node, code_dict, code=""): # Método para asignar códigos a los nodos
        if node is None: # Si el nodo es nulo,
            return # Regresa
        if node.char is not None: # Si el nodo tiene un caracter
            node.code = code # Asigna el código al nodo
            code_dict[node.char] = code # Diccionario para almacenar los códigos
        TreeNode.code_maker(node.left, code_dict, code + "0") # Recorre el nodo izquierdo
        TreeNode.code_maker(node.right, code_dict, code + "1") # Recorre el nodo derecho
        return code_dict # Regresa el diccionario


    def encoded_text(text, dictionary): # Método para codificar el texto
        encoded_text = "" # Variable para almacenar el texto codificado
        for line in text:
            for char in line:
                char = char.lower()
                if char in dictionary.keys():
                    encoded_text += dictionary[char] # Agrega el código del caracter al texto codificado
        return encoded_text
    
    def pad_encoded_text(encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
            
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text
    
    def get_byte_array(padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
            return b
        
    def compress(path, encoded_text):
        filename, file_extension = os.path.splitext(path)
        output_path = filename + ".bin"
        with open(path, 'r+') as file, open(output_path, 'wb') as output:
            padded_encoded_text = TreeNode.pad_encoded_text(encoded_text)
            b = TreeNode.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        print("Compressed")
        return output_path
    

def print_nodes(node, prefix=""): # Método para imprimir los nodos
    if node is None:
        return
    if node.char is not None: # Si el nodo tiene un caracter
        print(f"Character: {node.char}, Frequency: {node.freq}, Code: {node.code}") # Imprime el caracter, la frecuencia y el código
    print_nodes(node.left)  # Recorre el nodo izquierdo
    print_nodes(node.right) # Recorre el nodo derecho


# dict = {'0': 43, '1': 117, '2': 29, '3': 28, '4': 37, '5': 32, '6': 26, '7': 41, '8': 14, '9': 18, 'a': 36606, 'b': 7484, 'c': 12819, 'd': 20421, 'e': 60476, 'f': 11525, 'g': 8921, 'h': 28554, 'i': 32552, 'j': 689, 'k': 2739, 'l': 17169, 'm': 13653, 'n': 32151, 'o': 37112, 'p': 8754, 'q': 521, 'r': 28962, 's': 29227, 't': 43903, 'u': 13764, 'v': 5162, 'w': 10628, 'x': 860, 'y': 9496, 'z': 150, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, '!': 13, '"': 0, '#': 1, '$': 2, '%': 1, '&': 1, "'": 4, '(': 151, ')': 151, '*': 12, '+': 0, ',': 10122, '-': 354, '.': 3063, '/': 6, ':': 315, ';': 1567, '<': 0, '=': 0, '>': 0, '?': 57, '@': 0, '[': 17, '\\': 0, ']': 17, '^': 0, '_': 816, '`': 0, '{': 0, '|': 0, '}': 0, '~': 0, ' ': 99429, '\t': 0, '\n': 9921, '\r': 0, '\x0b': 0, '\x0c': 0}
# print(clean_dictionary(dict))
# print("\n")

# nodos = TreeNode.huffman_tree(dict)
# root_node =nodos[0]  # The Huffman tree's root node is the first (and only) element in the list
# code_dict = TreeNode.code_maker(root_node, {})
# print_nodes(root_node)
# print("\n")
# print(code_dict)
# print("\n")
# print(TreeNode.encoded_text("Hello, World!", code_dict))