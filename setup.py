import cx_Freeze

executables = [cx_Freeze.Executable("Shadow of war.py")]

cx_Freeze.setup(
    name="Shadow of war ",
    options={"build_exe": {"packages":["pygame"], "include_files": ["menu_sound.wav","critical_sound.wav","direct_sound.wav","explostion_sound.wav","gun_sound.wav","mods.py", "mods.py", "assets.py"]}},
    version = "1.20.1",
    description = "This is a buggy game made just for fun,in the latest version a few bugs have been worked out some cool new things added but the game is not done yet.",

    executables = executables
    
    )
