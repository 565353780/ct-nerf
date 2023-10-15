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
        self.trans_data = None

        if txrm_file_path is not None:
            assert self.loadTXRMFile(txrm_file_path)
        return

    def reset(self):
        self.txrm_file_path = None
        self.data = None
        self.trans_data = None
        return True

    def loadTXRMFile(self, txrm_file_path):
        if not os.path.exists(txrm_file_path):
            print('[ERROR][CILLoader::loadTXRMFile]')
            print('\t txrm file not exist!')
            print('\t txrm_file_path:', txrm_file_path)
            return False

        self.txrm_file_path = txrm_file_path
        self.data = ZEISSDataReader(file_name=self.txrm_file_path).read()
        self.data = TransmissionAbsorptionConverter()(self.data)
        return True

    def getShape(self):
        if self.data is None:
            print('[WARN][CILLoader::getShape]')
            print('\t data is None! please load data first')
            return [0, 0, 0]

        return self.data.shape

    def getSliceNum(self):
        return self.getShape()[0]

    def showGeometry(self):
        if self.data is None:
            print('[ERROR][CILLoader::showGeometry]')
            print('\t data is None! please load data first')
            return False

        show_geometry(self.data.geometry)
        return True

    def showData2D(self, slice_idx):
        slice_num = self.getSliceNum()

        if slice_idx < 0:
            slice_idx += slice_num

        if slice_idx < 0 or slice_idx >= slice_num:
            print('[ERROR][CILLoader::showData2D]')
            print('\t slice_idx out of range! valid range: [0, ' + \
                str(slice_num - 1) + ']')
            print('\t slice_idx:', slice_idx)
            return False

        show2D(self.data, slice_list=('angle', slice_idx))
        return True

    def test(self):
        self.getShape()
        self.showGeometry()
        self.showData2D(0)
        self.showData2D(-1)
        return True
