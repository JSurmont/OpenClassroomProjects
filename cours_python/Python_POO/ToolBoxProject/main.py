from ToolBoxProject.src.Nail import Nail
from ToolBoxProject.src.Srew import Screw
from ToolBoxProject.src.ToolBox import ToolBox
from ToolBoxProject.src.Screwdriver import ScrewDriver
from ToolBoxProject.src.Hammer import Hammer

if __name__ == '__main__':

    # Instanciez une boîte à outils, un tournevis, et un marteau.
    toolBox = ToolBox()
    screwdriver = ScrewDriver(3)
    hammer = Hammer("pink")

    # Placez le marteau et le tournevis dans la boîte à outils.
    toolBox.add_tool(screwdriver)
    toolBox.add_tool(hammer)

    # Instanciez une vis, et serrez-la avec le tournevis.
    # Affichez la vis avant après avoir été serrée.
    screw = Screw()

    print(screw.__str__())

    screwdriver.tighten(screw)

    print(screw.__str__())

    # Instanciez un clou, puis enfoncez-le avec le marteau.
    # Affichez le clou avant et après avoir été enfoncé.
    nail = Nail()

    print(nail.__str__())

    hammer.hammer_in(nail)

    print(nail.__str__())

    # --------------------------------------------------------------
    # Que pouvez-vous faire d’autre avec ces classes et ces objets ?

    # enlever un outil
    print("outils dans la boîte:", toolBox.tools)
    toolBox.remove_tool(hammer)
    print("on a enlevé le marteau")
    print("outils dans la boîte:", toolBox.tools)

    # désserrer la vis
    screwdriver.loosen(screw)
    print(screw)

    # enlever le clou
    hammer.remove(nail)
    print(nail)

    # repeindre le marteau
    hammer.paint("yellow")
    print(hammer)
