import platform
import os
from pathlib import Path
import sys
import subprocess

def install_package( package_name ):
    print( f"Installing {package_name}..." )
    if platform.system() == "Windows":
        python_path = str( Path(os.__file__).parents[1] / 'python.exe' )
    else:
        raise Exception( f'Unsupported platform {platform.system()}' )

    try:
        import pip
    except:
        get_pip_filepath = os.path.join(
            os.path.dirname( __file__ ), 'get-pip.py'
        )
        print(get_pip_filepath)
        subprocess.check_call( [ python_path, get_pip_filepath ] )

    subprocess.check_call(
        [ python_path, '-m', 'pip', 'install', package_name ]
    )

try:
    import urdf2webots
except ModuleNotFoundError:
    install_package( 'urdf2webots' )
    import urdf2webots