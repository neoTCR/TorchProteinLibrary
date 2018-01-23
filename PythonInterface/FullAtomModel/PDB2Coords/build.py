import os
import torch
import glob
from torch.utils.ffi import create_extension

this_file = os.path.dirname(__file__)


here = os.path.normpath(os.path.dirname(__file__))
lib_dir = os.path.abspath(os.path.join(here, '../../../'))
sources = [ os.path.join(lib_dir,'Layers/FullAtomModel/PDB2Coords/pdb2coords_interface.cpp'),
            ]
headers = [	os.path.join(lib_dir,'Layers/FullAtomModel/PDB2Coords/pdb2coords_interface.h'),
			]

include_dirs = [
	os.path.join(lib_dir, 'Layers/FullAtomModel'),
	os.path.join(lib_dir, 'Math'),
]
library_dirs=[	os.path.join(lib_dir, 'build/Layers/FullAtomModel'),
				os.path.join(lib_dir, 'build/Math')]

defines = []
with_cuda = False

ffi = create_extension(
	'Exposed.cppPDB2Coords',
	headers=headers,
	sources=sources,
	define_macros=defines,
	relative_to=__file__,
	with_cuda=with_cuda,
	include_dirs = include_dirs,
	extra_compile_args=["-fopenmp"],
	extra_link_args = [],
	libraries = ["FULL_ATOM_MODEL", "TH_MATH"],
    library_dirs = library_dirs
)

if __name__ == '__main__':
	ffi.build()
	from Exposed import cppPDB2Coords
	print cppPDB2Coords.__dict__.keys()
