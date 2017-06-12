from __future__ import print_function
#from unzip import unzip
import os, pdb, glob

def unpack_dir( extns=[ 'tgz', 'tar' ] ):
    """
    Unpacks all the archives in the current directory with
    the extensions listed in the keyword argument list.
    This is routine currently fairly experimental and I tend
    to use it on an ad hoc basis.
    """
    
    archives = []
    for i in range( len( extns ) ):
        extn = extns[i]
        archives = archives+glob.glob('*.'+extn)
    n_archives = len(archives)
    print( 'Now unpacking %i archives:' % n_archives )
    finished_dir = 'already_unpacked'
    try:
        os.mkdir( finished_dir )
    except:
        pass
    for i in range(len(archives)):
        current = i+1
        print( '\n   currently unpacking %i of %i...\n' % (current,n_archives) )
        ix = archives[i].rfind( '.' )
        extn_i = archives[i][ix+1:]
        if ( extn_i=='tgz' )+( extn_i=='tar' ):
            os.system( 'tar -xzvf {0}'.format( archives[i] ) )
        elif ( extn_i=='gz' )+( extn_i=='Z' ):
            uncompressed = archives[i][:ix]
            os.system( 'gunzip {0} -c > {1}'.format( archives[i], uncompressed ) )
            os.system( 'mv {0} {1}'.format( archives[i], finished_dir ) )
        else:
            print( 'file extension {0} not recognised'.format( extn_i ) )
            pdb.set_trace()
        #unzip(archives[i])
    print( 'Finished.\n' )
    return None

