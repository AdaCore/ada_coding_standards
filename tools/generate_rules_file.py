import argparse
import os

RULE   = "---"
HEADER = "==="

global_file = None

def write ( text ):
    global global_file
    global_file.write ( text + '\n' )

def list_text ( items ):
    retval = ""
    for item in items:
        if len(retval) > 0:
            retval = retval + ", "
        retval = retval + item
    return retval

def find_value ( lines, key ):
    for line in lines:
        if key in line:
            return line[line.rindex(' '):].replace('*','').strip()
    return ''

def find_values ( lines, key ):
    start_looking = False
    retval = ''

    for line in lines:
        if key in line:
            start_looking = True
        elif start_looking:
            l = line.strip()
            if len(l) <= 1:
                break
            first = l.find(':')
            last = l.find(':', first+1)
            if first >= 0 and last > first:
                if len(retval) > 0:
                    retval = retval + ', '
                retval = retval + l[first+1:last]
    return retval

def process_rule ( lines, full ):
    id_start = lines[1].index('(')
    id = f = lines[1][id_start+1:lines[1].index(')')]
    name = lines[1][:id_start].strip().replace(' ','_')
    rule = find_value ( lines[2:], 'GNATcheck Rule' )
    write ( '+R:' + id + '_' + name + ':' + rule )
    if full:
        level = find_value ( lines, "*Level*" )
        if len(level) > 0:
            write ( '--  Level: ' + level )
        category = find_values ( lines, '*Category*' )
        if len(category) > 0:
            write ( '--  Category: ' + category )
        goal = find_values ( lines, '*Goal*' )
        if len(category) > 0:
            write ( '--  Goal: ' + goal )
        write('')
            

def process_one_file ( in_filename, full ):

    with open ( in_filename ) as f:
        lines = f.read().splitlines()

    start_of_rule = -1

    for i in range(1,len(lines)-1):
        line = lines[i].strip()
        if line.startswith ( HEADER ):
            line = lines[i+1].strip()
            if len(line) > 3 and "(" in line:
                write ( '' )
                write ( '' )
                sep = '-'.ljust(len(lines[i+1]),'-')
                write ( "---" + sep + "---" )
                write ( "-- " + lines[i+1] + " --" )
                write ( "---" + sep + "---" )
                write ( '' )
        elif line.startswith ( RULE ):
            if start_of_rule < 0:
                start_of_rule = i
            elif i - start_of_rule > 3:
                process_rule ( lines[start_of_rule:i], full )
                start_of_rule = i

def process_directory ( source, output, full ):
    global global_file

    global_file = open ( args.output, 'w' )

    for root, dirs, files in os.walk ( args.source ):
        for file in files:
            if file.lower().endswith ( ".rst" ):
                process_one_file ( os.path.join ( root, file ), full )


if __name__== "__main__":

    parser = argparse.ArgumentParser(
        description='Use coding standards to generate a rules file for using with "gnatcheck"')

    parser.add_argument('--source',
                        help='Directory containing source files for guidelines (will be searched recursively)',
                        required=True)

    parser.add_argument('--output',
                        help='Filename for rules file',
                        required=True)

    parser.add_argument('--full',
                        help='Include "level", "category", and "goal" in comments section',
                        action='store_true')
                        
    args = parser.parse_args()

    process_directory ( args.source, args.output, args.full )
