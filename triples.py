list = ['25nt_oligo_Rep1.1.fastq','25nt_oligo_Rep2.1.fastq','25nt_oligo_Rep3.1.fastq','25nt_oligo_Rep4.1.fastq']
output = []
for file in list:
    input = open(file)
    RNA = 'AACTTCGTCGAGTACGCTCAA'
    RNA_RC = 'TTGAGCGTACTCGACGAAGTT'
    
    input.readline()
    line_seq = input.readline()
    
    triples_count = {}
    
    while line_seq:
        RNApos = line_seq.strip().find(RNA)
        if RNApos == -1:
            next
        else:
            first_nuc = line_seq.strip()[RNApos-4]
            second_nuc = line_seq.strip()[RNApos-3]
            third_nuc = line_seq.strip()[RNApos-2]
            triple = first_nuc + second_nuc + third_nuc
            if 'N' in triple:
                next
            else:
                if(triple) in triples_count:
                    triples_count[triple] += 1
                else:
                    triples_count[triple] = 1
        
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
    output.append(triples_count)


import csv
for i in range(len(output)):
    with open('triples'+str(i+1)+'.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in output[i].items():
            writer.writerow([key, value])