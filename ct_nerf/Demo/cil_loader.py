from ct_nerf.Module.cil_loader import CILLoader

def demo():
    txrm_file_path = '/home/chli/Dataset/ICT/usb/gruppe 4/gruppe 4_2014-03-20_1404_12/tomo-A/gruppe 4_tomo-A.txrm'
    save_dataset_folder_path = '/home/chli/Dataset/NeRF/usb/input/'
    print_progress = True

    cil_loader = CILLoader(txrm_file_path)
    cil_loader.generateDataset(save_dataset_folder_path, print_progress)
    return True
