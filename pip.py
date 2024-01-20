


# Poleschuk Fedor
# Contact-poleschuk.fa@gmail.com
# Description-Install python libraries
import platform
import os
from pathlib import Path
import sys
import subprocess


import adsk.core, traceback # pylint: disable=import-error
import os
import platform


import xml.etree.ElementTree as etree

this_addin_name = 'PipToFusion360'
this_addin_version = '2.5.0'
this_addin_author = 'Poleschuk Fedor'
this_addin_contact = 'poleschuk.fa@gmail.com'

this_addin_name += ' - v' + this_addin_version

debug_mode = False


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



def run(context):

    ui = None

    try:

        app = adsk.core.Application.get()
        ui = app.userInterface

        if not debug_mode:
            # Ask the user to enter the URL of the git repo to import in Fusion 360
            (lib_url, cancelled) = ui.inputBox('Enter the name of python library to import in Fusion 360', this_addin_name)
            if cancelled:
                ui.messageBox('Process aborted', this_addin_name, adsk.core.MessageBoxButtonTypes.OKButtonType, adsk.core.MessageBoxIconTypes.CriticalIconType)
                return
        
        install_package( lib_url )
        if ui:
            ui.messageBox('install success')
 
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))







