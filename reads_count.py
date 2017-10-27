list = ['25nt_oligo_Rep1.1.fastq']

for file in list:
    input = open(file)
    
    input.readline()
    line_seq = input.readline()
    
    count = 0
    
    while line_seq:
        count += 1
        
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
    
    input.close()
    
print count