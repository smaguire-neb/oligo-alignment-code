list = ['25nt_oligo_Rep1.2.fastq']

for file in list:
    input = open(file)
    RNA = 'AACTTCGTCGAGTACGCTCAA'
    RNA_RC = 'TTGAGCGTACTCGACGAAGTT'
    
    input.readline()
    line_seq = input.readline()
    
    count_A = 0
    count_G = 0
    count_C = 0
    count_T = 0
    
    while line_seq:
        
        RNApos = line_seq.strip().find(RNA_RC)
        if RNApos == -1:
            next
        else:
            if line_seq.strip()[RNApos+len(RNA_RC)-1+4] == 'T':
                count_A += 1
            if line_seq.strip()[RNApos+len(RNA_RC)-1+4] == 'C':
                count_G += 1
            if line_seq.strip()[RNApos+len(RNA_RC)-1+4] == 'G':
                count_C += 1
            if line_seq.strip()[RNApos+len(RNA_RC)-1+4] == 'A':
                count_T += 1
        
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
        
    input.close()
    
print 'reads with first A', count_A   
print 'reads with first G', count_G
print 'reads with first C', count_C 
print 'reads with first T', count_T