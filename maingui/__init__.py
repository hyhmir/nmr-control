# handle imports and exports

print('importing the main gui')

import maingui.main
import maingui.func
import maingui.frames

__all__ = [
    'main',
    'func',
    'frames'
]