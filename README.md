# CT NeRF

## Install

first set libmamba as conda solver
```bash
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

then install requirements

```bash
conda create --name cil -c conda-forge -c intel -c ccpi cil=23.1.0 astra-toolbox tigre ccpi-regulariser tomophantom "ipywidgets<8"
conda activate cil
./setup.sh
```

## Run

```bash
python demo.py
```

## Enjoy it~
