list = ['25nt_oligo_Rep1.1.fastq','25nt_oligo_Rep2.1.fastq','25nt_oligo_Rep3.1.fastq','25nt_oligo_Rep4.1.fastq']
output = []
for file in list:
    print file
    input = open(file)
    RNA = 'AACTTCGTCGAGTACGCTCAA'
    RNA_RC = 'TTGAGCGTACTCGACGAAGTT'
    
    input.readline()
    line_seq = input.readline()
    
    doubles_count = {}
    
    while line_seq:
        RNApos = line_seq.strip().find(RNA)
        if RNApos == -1:
            next
        else:
            first_nuc = line_seq.strip()[RNApos-4]
            second_nuc = line_seq.strip()[RNApos-3]
            double = first_nuc + second_nuc
            if 'N' in double:
                next
            else:
                if(double) in doubles_count:
                    doubles_count[double] += 1
                else:
                    doubles_count[double] = 1
        
        input.readline()
        input.readline()
        input.readline()
        
        line_seq = input.readline()
        
    input.close()
    output.append(doubles_count)

    
import csv
for i in range(len(output)):
    with open('doubles'+str(i+1)+'.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in output[i].items():
            writer.writerow([key, value])