import numpy as np
import os
import matplotlib.pyplot as plt

from cil.io import ZEISSDataReader, TIFFWriter
from cil.processors import TransmissionAbsorptionConverter, CentreOfRotationCorrector, Slicer
from cil.framework import AcquisitionData
from cil.plugins.astra import FBP
from cil.utilities.display import show2D, show1D, show_geometry
from cil.utilities.jupyter import islicer, link_islicer

class CILLoader(object):
    def __init__(self, txrm_file_path=None) -> None:
        self.txrm_file_path = None
        self.data = None

        if txrm_file_path is not None:
            assert self.loadTXRMFile(txrm_file_path)
        return

    def reset(self):
        self.txrm_file_path = None
        self.data = None

    def loadTXRMFile(self, txrm_file_path):
        if not os.path.exists(txrm_file_path):
            print('[ERROR][CILLoader::loadTXRMFile]')
            print('\t txrm file not exist!')
            print('\t txrm_file_path:', txrm_file_path)
            return False

        self.txrm_file_path = txrm_file_path
        self.data = ZEISSDataReader(file_name=self.txrm_file_path).read()
        return True

    def showGeometry(self):
        show_geometry(self.data.geometry)
        return True
