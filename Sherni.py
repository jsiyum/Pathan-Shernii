import platform
bit=platform.architecture()[0]
if bit=='64bit':
    import aarch
    aarch.reg()
elif bit=='32bit':
    import arm
    arm.reg()
