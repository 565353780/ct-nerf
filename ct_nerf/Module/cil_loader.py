import os
import numpy as np
from copy import deepcopy

from cil.utilities.display import show2D, show_geometry

class CILLoader(object):
    def __init__(self, txrm_file_path=None) -> None:
        self.txrm_file_path = None
        self.data = None
        self.slice_direction_list = []

        if txrm_file_path is not None:
            assert self.loadTXRMFile(txrm_file_path)
        return

    def reset(self):
        self.txrm_file_path = None
        self.data = None
        self.slice_direction_list = []
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
        self.slice_direction_list = list(self.data.dimension_labels)
        return True

    def isSliceDirectionValid(self, slice_direction):
        if slice_direction in self.slice_direction_list:
            return True

        print('[WARN][CILLoader::isSliceDirectionValid]')
        valid_directions_str = '[' + self.slice_direction_list[0]
        for i in range(1, len(self.slice_direction_list)):
            valid_directions_str += ', ' + self.slice_direction_list[i]
        valid_directions_str += ']'
        print('\t slice_direction not found! valid directions: ' + \
            valid_directions_str)
        print('\t slice_direction:', slice_direction)
        return False

    def getShape(self):
        if self.data is None:
            print('[WARN][CILLoader::getShape]')
            print('\t data is None! please load data first')
            return [0, 0, 0]

        return self.data.shape

    def getSliceNum(self):
        return self.getShape()[0]

    def getSliceImage(self, slice_idx):
        if self.data is None:
            print('[ERROR][CILLoader::getSliceImage]')
            print('\t data is None! please load data first')
            return None

        data_array = self.data.as_array()

        data_2d = deepcopy(data_array[slice_idx])

        range_min = data_array.min()
        range_max = data_array.max()

        slice_image = (255.0 * (data_2d - range_min) /
            (range_max - range_min)).astype(np.uint8)
        return slice_image

    def showData2D(self, slice_direction, slice_idx):
        if not self.isSliceDirectionValid(slice_direction):
            print('[ERROR][CILLoader::showData2D]')
            print('\t isSliceDirectionValid failed!')
            return False

        slice_num = self.getSliceNum()

        if slice_idx < 0:
            slice_idx += slice_num

        if slice_idx < 0 or slice_idx >= slice_num:
            print('[ERROR][CILLoader::showData2D]')
            print('\t slice_idx out of range! valid range: [0, ' + \
                str(slice_num - 1) + ']')
            print('\t slice_idx:', slice_idx)
            return False

        show2D(self.data, slice_list=(slice_direction, slice_idx))
        return True

    def showGeometry(self):
        if self.data is None:
            print('[ERROR][CILLoader::showGeometry]')
            print('\t data is None! please load data first')
            return False

        show_geometry(self.data.geometry)
        return True
