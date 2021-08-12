# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(\none)
import uos, machine
#uos.dupterm(\none, 1) # disable \rEPL on UA\rT(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
