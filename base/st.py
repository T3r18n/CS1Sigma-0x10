import common  as com
import architecture as arch
import arrbuf as ab

#-------------------------------------------------------------------------
# Stages
#-------------------------------------------------------------------------

StageAsm = Symbol ("Asm")   # .asm.   assembly language source
StageObj = Symbol ("Obj")   # .obj.   object code
StageOmd = Symbol ("Omd")   # .omd.   metadata for obj
StageLnk = Symbol ("Lnk")   # .lnk.   link command
StageExe = Symbol ("Exe")   #.xmd.    metadata for exe
StageXmd = Symbol ("Xmd")   #.xmd.    metadata for exe

def getStageSym (xs) :
    if(xs == "asm"):
        return StageAsm
    if(xs == "obj"):
        return StageObj
    if(xs == "omd"):
        return StageOmd
    if(xs == "lnk"):
        return StageLnk
    if(xs == "exe"):
        return StageExe
    if(xs == "xmd"):
        return StageXmd
    return None

#-------------------------------------------------------------------------
# Representation of system state
#-------------------------------------------------------------------------

# The system state contains a map from a base name foo to an
# S16Module object, as well as the emulator state.

class SystemState :
    def __init__ (this) :
        this.modules = {}
        this.selectedModule = None
        this.anonymousCount = 0
        this.emulatorState = None
        this.linkerState = None

    def showSelectedModuleName (this):
        if(this.selectedModule):
            return this.selectedModule
        return "No module selected"

    def clearModules (this) :
        this.modules = {}
        this.anonymousCount = 0
        this.selectedModule = None

    def mkSelectModule (this,mname):
        com.mode.devlog (f"mkSelectModule {mname}")
        if (mname & this.modules.has(mname)):
            this.selectedModule = mname
        elif (mname):
            this.selectedModule = mname
            this.modules.set (mname, S16Module (mname))
        } else {
            this.anonymousCount+=1
            const xs = f"anonymous{this.anonymousCount}"
            this.modules.set (xs, new S16Module (xs))
            this.selectedModule = xs
        }
        m = this.modules.get(this.selectedModule)
        return m
    }
    closeModule (this,mname) {
        this.modules.delete (mname)
    }
    getSelectedModule (this) {
        com.mode.devlog ("getSelectedModule")
        if (env.modules.size == 0) { # no modules
#            this.anonymousCount++
#            const xs = `anonymous${this.anonymousCount}`
#            this.modules.set (xs, new S16Module (xs))
#            this.selectedModule = xs
            this.selectedModule = None
        } else if (!this.selectedModule) { # nothing selected
            com.mode.devlog ("getSelectedModule, in nothing selected")
            this.selectedModule = [...this.modules.keys()][0].baseName
        } else if (this.modules.get(this.selectedModule)) { # it exists
            com.mode.devlog ("getSelectedModule, found it")
        } else  { # it doesn't exist
            com.mode.devlog ("getSelectedModule, doesn't exist, making it")
            return this.mkModule (this.selectedModule)
        }
        return this.modules.get (this.selectedModule)
    }
}
