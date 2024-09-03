def negative_to_binary(n, bit_width=8):
    if n >= 0:
        raise ValueError("Input should be a negative integer.")
    
    abs_bin = bin(abs(n))[2:]  
    
    abs_bin = abs_bin.zfill(bit_width)
    
    inverted_bin = ''.join('1' if bit == '0' else '0' for bit in abs_bin)
    
 
    inverted_int = int(inverted_bin, 2)
    twos_complement_int = inverted_int + 1
    
    twos_complement_bin = bin(twos_complement_int)[2:].zfill(bit_width)
    
    return twos_complement_bin


negative_number = int(input("what is the negative number u would like to translate"))
bit_width = 8  
binary_representation = negative_to_binary(negative_number, bit_width)
print(f"The binary representation of {negative_number} in {bit_width}-bit format is: {binary_representation}")
