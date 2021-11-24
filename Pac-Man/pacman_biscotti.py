#numero matricola 331968
board = ["#############################",
         "#                           #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# +### -#### -# -#### -### +#",
         "# -    -     -  -     -    -#",
         "# --------------------------#",
         "# -### -# -####### -# -### -#",
         "# -    -# -   #    -# -    -#",
         "# ------# ----# ----# ------#",
         "###### -####  #  #### -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "       -   #######    -      ",
         "       -   #######    -      ",
         "###### -#  #######  # -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "#      -      #       -     #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# -  # -     -  -     -#   -#",
         "# +--# -------  -------# --+#",
         "### -# -# -####### -# -# -###",
         "#   -  -# -   #    -# -  -  #",
         "# ------# ----# ----# ------#",
         "# -######### -# -######### -#",
         "# -          -  -          -#",
         "# --------------------------#",
         "#############################"]
#creazione corrdinate per i biscotti
def cookis ()-> list:
    coordinates_cookis = []

    for riga1 in range(32):
        line = board[riga1]
        for colonna1 in range(29):
            if "-" in line[colonna1]:
                coordinate = (riga1, colonna1) 
                coordinates_cookis.append(coordinate)
        colonna1+=0

    return coordinates_cookis

#creazione coordinate per i power up
def big_cookis () -> list:
    coordinates_cookis = []

    for riga1 in range(32):
        line = board[riga1]
        for colonna1 in range(29):
            if "+" == line[colonna1]:
                coordinate = (riga1, colonna1) 
                coordinates_cookis.append(coordinate)
        colonna1+=0

    return coordinates_cookis
