import os, pdb, glob

def unpack_dir():
    """
    Unpacks all the archives in the current directory.
    Can add file extensions as required, eg. tar.gz.
    """
    extns = ['tgz', 'tar']
    archives = []
    for i in range(len(extns)):
        extn = extns[i]
        archives = archives+glob.glob('*.'+extn)
    n_archives = len(archives)
    print 'Now unpacking %i archives:' % n_archives
    for i in range(len(archives)):
        current = i+1
        print '\n   currently unpacking %i of %i...\n' % (current,n_archives)
        unzip(archives[i])
    print 'Finished.\n'
    return None

