from ct_nerf.Module.cil_loader import CILLoader

def demo():
    txrm_file_path = '/home/chli/Dataset/ICT/usb/gruppe 4/gruppe 4_2014-03-20_1404_12/tomo-A/gruppe 4_tomo-A.txrm'

    cil_loader = CILLoader(txrm_file_path)
    cil_loader.showGeometry()
    return True
