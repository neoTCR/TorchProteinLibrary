from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(name='TorchProteinLayers',
	  ext_modules=[
		  	CppExtension('TorchProteinLayers', 
				sources = [
				'Math/cMatrix33.cpp',
				'Math/cMatrix44.cpp',
				'Math/cVector3.cpp',
				'Layers/FullAtomModel/cConformation.cpp',
				'Layers/FullAtomModel/cConformationAA.cpp',
				'Layers/FullAtomModel/cGeometry.cpp',
				'Layers/FullAtomModel/cRigidGroup.cpp',
				'Layers/FullAtomModel/nUtil.cpp',
				'Layers/FullAtomModel/Angles2Coords/angles2coords_interface.cpp'],
				include_dirs = ['Layers/FullAtomModel',
				'Math'])
		  	],
	  cmdclass={'build_ext': BuildExtension})