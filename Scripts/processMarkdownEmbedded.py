#
# A simple program to help produce the book. There is the requirment to include a source file. For example,
# the include files are very helpfull to have as an appendix. So that they look a bit nicer, there need
# to be C++ comment lines that are actually commands to the markdown formatter. We will have a simple
# processer of text lines that recognizes those special lines. 
# 
# A comment line starts with ( "//!--" ) and is a line that is not added to the text output file.
#
# An include line starts with ( "//!include " ) and is a line that has a file path of a text file that
# should be processed recursively. The content is added to the text output file.
#
# A markdown line starts with ( "//! " ) and is just added to the text output file.
#
# Any other line is also just added to the text output file.
# 
#
# Yes, I know there is doxygen for generating documentation. However, it does support processing markdown,
# it does not generate markdown output. You would need yet another tool. Granted, it genrates a ton of 
# great stuff, but all that is not needed to just put the inlude file content into the book. It seems 
# easier to just process a file with a simple "token" markings line as described.
#
import re
import argparse

# the defined tokens
comment_token   = "//!--"
include_token   = "//!include "
process_token   = "//! "

# process the file
def process_file(input_file ):
    
    with open(input_file, 'r') as infile:

        print ( "processing infile\n ")
        
        for line in infile:

            if comment_token in line:
                continue

            elif include_token in line:
                tokens = re.split( r'\s+', line )
                process_file( tokens[ 1 ] )

            elif process_token in line:
                outfile.write( "\n" )
                outfile.write( line.replace( process_token, '' ))
                outfile.write( "\n" )
            
            else:
                outfile.write(line)

# here we go ...
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Process a text file by removing lines with a special token.")
    parser.add_argument('input_file', type=str, help='The input file path')
    parser.add_argument('output_file', type=str, help='The output file path')
    
    args = parser.parse_args( )

    outfile = open(args.output_file, 'w')

    process_file(args.input_file )
