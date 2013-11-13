import os, pdb, glob

def unzip(filename):
    """
    Unzips filename into a folder with name given by the
    filename root and then moves the zipped file into
    another folder called already_unpacked.
    """
    ix = filename.rfind('.')
    if ix<0:
        pdb.set_trace()
    root = filename[:ix]
    extn = filename[ix:]
    finished_dir = 'already_unpacked'
    try:
        os.mkdir(root)
    except:
        pass
    os.system('tar -xzvf '+filename+' -C '+root)
    try:
        os.mkdir(finished_dir)
    except:
        pass
    os.system('mv '+filename+' '+finished_dir)
    return None
