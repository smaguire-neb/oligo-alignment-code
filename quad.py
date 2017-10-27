file_list = ['25nt_oligo_Rep1.1.fastq','25nt_oligo_Rep2.1.fastq','25nt_oligo_Rep3.1.fastq','25nt_oligo_Rep4.1.fastq']
output = []
for file in file_list:
    print(file)
    input = open(file)
    RNA = 'AACTTCGTCGAGTACGCTCAA'
    RNA_RC = 'TTGAGCGTACTCGACGAAGTT'
    
    input.readline()
    line_seq = input.readline()
    
    quad_count = {}
    
    while line_seq:
        RNApos = line_seq.strip().find(RNA)
        if RNApos == -1:
            next
        else:
            first_nuc = line_seq.strip()[RNApos-4]
            second_nuc = line_seq.strip()[RNApos-3]
            third_nuc = line_seq.strip()[RNApos-2]
            fourth_nuc = line_seq.strip()[RNApos-1]
            quad = first_nuc + second_nuc + third_nuc + fourth_nuc
            
            if 'N' in quad:
                next
            else:
                if(quad) in quad_count:
                    quad_count[quad] += 1
                else:
                    quad_count[quad] = 1
        
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
    output.append(quad_count)

import csv
for i in range(len(output)):
    with open('quad'+str(i+1)+'.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in output[i].items():
            writer.writerow([key, value])