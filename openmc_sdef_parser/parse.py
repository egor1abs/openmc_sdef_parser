import numpy as np

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def parse_sdef(sdef_file, 
               keyword, initial_line = '', 
               ignore_first: bool = False, 
               data_type = float
               ) -> tuple:
    """
    Parse a SDEF file and extract values for a given keyword.

    Parameters
    ----------
    sdef_file : file object
        The SDEF file object to parse.
    keyword : str
        The keyword to search for in the file.
    initial_line : str, optional
        The initial line to start reading from. Defaults to an empty line.
    ignore_first : bool, optional
        Whether to ignore the first element of the extracted array. Defaults to False.
    data_type : type, optional
        The data type to convert the extracted values to. Defaults to float.

    Returns
    -------
    tuple
        A tuple containing the extracted array and the last read line.
    """

    # Initialize variables
    values = [] 
    line = initial_line

    # Search for the keyword in the file
    while keyword not in line:
        line = sdef_file.readline()
        if line == '' or line == 'C':
            print(f'Keyword {keyword} not found')
            break

    # If the keyword is found, set keyword_in_this_line to True
    # Set flag to True to continue reading the file
    else:
        keyword_in_this_line = True
        
        keywords_initial = ['POS', 'SDEF', 'RAD', 'ERG', 'EXT FRAD', 'WGT']
        
        # If the keyword is 'POS' or 'SDEF', replace '=' with a space for future split
        if keyword in keywords_initial:
            line = line.replace('=', ' ')

        # Continue reading the file until the end or the array is filled
        # Assuming that the array is full when not float value is found (flag = False)
        # Special treatment for line with keyword (keyword_in_this_line) because it has not only float values
        while True:
            if not keyword_in_this_line:
                line = sdef_file.readline()
                if line == '' or line.split()[0][0].isalpha():
                    break

            # Split the line and extract the values
            if keyword == 'SDEF' or keyword == 'RAD' or keyword == 'EXT FRAD' or keyword == 'WGT':
                elements = line.split()
            else:
                elements = [elem for elem in line.split() if isfloat(elem)]
            # If the keyword is 'DS', choose every second element because they correspond to the number of probabilty group
            if keyword.startswith('DS'):
                elements = elements[1::2]
            for elem in elements:
                values.append(elem)
                keyword_in_this_line = False
            if elements == []:
                keyword_in_this_line = False

    # If ignore_first is True, remove the first element of the array in SP card
    if ignore_first:
        values = values[1:]
        
    values = list(map(data_type, values))

    return values, line


def sdef_template(sdef_file: str) -> dict:
    """Reads a MCNP SDEF file and returns the origin, energy, r_bins, z_bins, r_prob, z_prob.

    Parameters
    ----------
    sdef_file : str
        The path to the MCNP SDEF file.

    Returns
    -------
    dict
        A dictionary containing the origin, energy, r_bins, z_bins, r_prob, z_prob.
    """
    
    _origin = []
    _sdef = []
    _energy = []

    _constraints = [] 
    
    _r_bins = []
    _r_prob = []

    _z_ind = []
    _z_bins = []
    _z_prob = []

    sdef_dict = {'CEL': None, 'ERG': None, 'WGT': None}
    dist_dict = {'RAD': None, 'EXT FRAD': None}
    
    with open(sdef_file, 'r') as file:
        
        _sdef, last_string = parse_sdef(file, 'SDEF', data_type=str)

        dist_flag = False
        
        for i, elem in enumerate(_sdef):
            if elem == 'CEL':    
                if _sdef[i+1][0].isalpha():
                        dist_flag = True
                        sdef_dict[elem] = _sdef[i+1][1:]
                else:
                    sdef_dict[elem] = _sdef[i+1]
            elif elem == 'ERG':
                sdef_dict[elem] = _sdef[i+1][1:]
            elif elem == 'WGT':
                sdef_dict[elem] = _sdef[i+1]
                
        _origin, _ = parse_sdef(file, 'POS', initial_line=last_string)
        
        _rad, last_string = parse_sdef(file, 'RAD', data_type=str)
        for i, elem in enumerate(_rad):
           if elem == 'RAD':
               dist_dict['RAD'] = _rad[i+1][1:]
               break
        
        _ext_frad, _ = parse_sdef(file, 'EXT FRAD', data_type=str, initial_line=last_string)
        for i, elem in enumerate(_ext_frad):
           if elem == 'EXT':
               dist_dict['EXT FRAD'] = _ext_frad[i+2][1:]
               break 
        
        if dist_flag:
            _constraints, last_string = parse_sdef(file, 'SP'+sdef_dict['CEL'], data_type=str)
        else:
            _constraints = [sdef_dict['CEL']]
            
        _energy, _ = parse_sdef(file, 'SP'+sdef_dict['ERG'], initial_line=last_string)
        
        _r_bins, last_string = parse_sdef(file, 'SI'+dist_dict['RAD'])
        _r_prob, _ = parse_sdef(file, 'SP'+dist_dict['RAD'], initial_line=last_string, ignore_first=True)

        _z_ind, last_string = parse_sdef(file, 'DS'+dist_dict['EXT FRAD'], data_type=int)

        for i, ind in enumerate(_z_ind):

            if len(_z_bins) == 0:
                _z_bins, last_string = parse_sdef(file, f'SI{ind}', initial_line=last_string)

            _z_prob.append([])
            _z_prob[i], last_string = parse_sdef(file, f'SP{ind}', initial_line=last_string, ignore_first=True)

        print('Read finished')
    
    origin = np.array(_origin) 
    
    energy = np.array(_energy)
    
    constraints = np.array(_constraints)
    
    if sdef_dict['WGT'] is None:
        wgt = 1.0
    else:
        wgt = float(sdef_dict['WGT'])

    r_bins = np.array(_r_bins) 
    r_prob = np.array(_r_prob) 

    z_bins = np.array(_z_bins) 
    z_prob = np.array(_z_prob)
    
    return {
        'origin': origin,
        'energy': energy,
        'r_bins': r_bins,
        'z_bins': z_bins,
        'r_prob': r_prob,
        'z_prob': z_prob,
        'wgt': wgt,
        'constraints': constraints
    }