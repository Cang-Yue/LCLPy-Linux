# LCLPy-Linux: A CLI Launcher For LunarClient In Linux

## Fork From https://github.com/Aetopia/LCLPy
## Update In 2022/04/07

## How To Use
```
usage: lcl [-v | --version ] <version>
           [-s | --server ] <version> <server>
           [-d | --debug ]
           [-c | --config ]
```

`--version` Select your game version

`--server` Launch LC and auto join in a server

`--debug` Open debug mode

`--config` Edit lcl Config (need install nano)

## How To Build
install `python3`
```
sudo apt install python3
```
install `pyinstaller`
```
pip install pyinstaller
```
run build.sh
```
./build.sh
```
You can find 'lcl' file in `./dist/` and put into $PATH dir
LCL config file in `$HOME/.lcl/Opinion.ini`
