#
# A simple program to help produce the book. There is the requirement to include a source file. For example,
# the include files are very helpfull to have as an appendix. So that they look a bit nicer, there need
# to be C++ comment lines that are actually commands to the markdown formatter. We will have a simple
# processer of text lines that recognizes those special lines. 
# 
# A comment line starts with a special token is processed as described for the tokens defined below. Any 
# other line is just copied to the output text file.
#
# Yes, I know there is doxygen for generating documentation. However, it does support processing markdown,
# it does not generate markdown output. You would need yet another tool. Granted, it genrates a ton of 
# great stuff, but all that is not needed to just put the inlude file content into the book. It seems 
# easier to just process a file with a simple "token" markings line as described.
#
import re
import argparse

#
# The defined tokens. A "//!-" followed by zero or more "_" is considered a comment line not to appear
# in the output file. Just to make the include comment look nicer in the C-Code.
#
# A line that begines with "//! " is stripped of the token, the leading blank is removed and the line 
# found is added to the output file. If the line had just that token, a blank line is added.
#
# A line that begins with "//!include " will include the file found under the file path. This is a 
# recursive call to the line processing routine.
#
# The "//!block-begin-+" and "//!block-end-+" bracket a code block with the respective markdown tokens.
#
process_token       = "//!"
comment_token       = "//!-+"
include_token       = "//!include "
block_begin_token   = "//!block-begin-*"
block_end_token     = "//!block-end-*"

#
# Process the file
#
def process_file(input_file ):
    
    with open( input_file, 'r') as infile:

        print ( "processing infile: ", infile.name, "\n" )
        
        for line in infile:

            if re.search( comment_token, line ):
                continue
  
            elif re.search( block_begin_token, line ):
                outfile.write( "```cpp \n")   
            
            elif re.search( block_end_token, line ):
                outfile.write( "``` \n") 

            elif re.search( include_token, line ):
                tokens = re.split( r'\s+', line )
                process_file( tokens[ 1 ] )

            elif re.search( process_token, line ):

                if ( line.strip( ) == process_token ):
                    outfile.write( "\n" )
                else: 
                    outfile.write( line.strip( ' ' ).replace( process_token + " ", '' ))

            else:
                outfile.write(line)

#
# here we go ...
#
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Process a text file by removing lines with a special token.")
    parser.add_argument('input_file', type=str, help='The input file path')
    parser.add_argument('output_file', type=str, help='The output file path')
    
    args = parser.parse_args( )

    outfile = open(args.output_file, 'w')

    process_file(args.input_file )
