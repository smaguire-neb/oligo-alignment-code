list = ['25nt_oligo_Rep1.1.fastq']

for file in list:
    input = open(file)
    RNA = 'AACTTCGTCGAGTACGCTCAA'
    RNA_RC = 'TTGAGCGTACTCGACGAAGTT'
    
    input.readline()
    line_seq = input.readline()
    
    count_contain = 0
    
    while line_seq:
        
        if line_seq.strip().find(RNA_RC) != -1:
            count_contain +=1
            
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
        
    input.close()
    
    
print count_contain