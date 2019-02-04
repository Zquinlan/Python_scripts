## Written by Taylor O'Connell for Zach Quinlan Jan 2019
## Editted by Zach Quinlan Feb 2019

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ID_file', help='IDs of interest; text file with one ID per line')
parser.add_argument('infile', help='File to parse')
args = parser.parse_args()

#Read file of ids
IDs = []
with open(args.ID_file, 'r') as fin:
    for line in fin:
         IDs.append(line.strip())        


#Read through the input file
with open(args.infile, 'r') as fin:
    
    #Boolean variable to keep track of 
    keep = False
    
    for line in fin:
        
        #When we hit a FEATURE_ID line,check the feature ID to see if
        #it's a feature we want to keep
        if line.startswith('FEATURE_ID'):
            ID = line.strip().split('=')[1]
            if ID in IDs:
                sys.stdout.write('BEGIN IONS\n' + line)
                keep = True
                
        #Lines other than FEATURE_ID lines
        else:
            
            #Write every line until the "END IONS" line 
            if keep:
                #Lines other than end line
                if not line.startswith("END IONS"):
                    sys.stdout.write(line)
                
                #Here we have reached the end line
                else:
                    #Write the end line plus an extra space
                    sys.stdout.write(line + '\n')
                    #Reset the keep boolean variable to False
                    #until we hit another keeper ID
                    keep = False
               
                
            
            
            
        
        
        
## What to run in terminal to get the script to work
## python parse_by_feature_ID.py Feature_ID.txt Moorea_sirius.txt > outfile.txt
