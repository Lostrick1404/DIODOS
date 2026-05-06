import schemdraw
import schemdraw.elements as elm

def generate_voltage_divider_currents():
    with schemdraw.Drawing(file='topics/02-transistor-bjt/assets/bjt-divisor-voltaje-corrientes.png', show=False) as d:
        d.config(unit=2.5, fontsize=12)
        
        # --- COMPONENTES ---
        Q = d.add(elm.BjtNpn().anchor('base'))
        d.add(elm.Label().at(Q.center).label('Q1', loc='right', ofst=(0.6, 0)))
        
        # Nodo de base y línea
        L_base_conn = d.add(elm.Line().left().at(Q.base).length(1.2))
        B_node = d.add(elm.Dot())
        
        vcc_level = 3.5
        gnd_level = -3.5
        
        R1 = d.add(elm.Resistor().up().at(B_node.center).toy(vcc_level).label('$R_1$'))
        RC = d.add(elm.Resistor().up().at(Q.collector).toy(vcc_level).label('$R_C$'))
        d.add(elm.Line().at(R1.end).to(RC.end))
        d.add(elm.Vdd().at(RC.end).label('$V_{CC}$'))
        
        R2 = d.add(elm.Resistor().down().at(B_node.center).toy(gnd_level).label('$R_2$'))
        RE = d.add(elm.Resistor().down().at(Q.emitter).toy(gnd_level).label('$R_E$'))
        d.add(elm.Line().at(R2.end).to(RE.end))
        d.add(elm.Ground().at(RE.end))

        # Coordenadas manuales basadas en el layout
        bx, by = B_node.center
        cx, cy = Q.collector
        ex, ey = Q.emitter

        # --- SEÑALIZACIÓN DE CORRIENTES CON LÍNEAS DE REFERENCIA ---
        
        # I1: Entrando al divisor
        l1 = d.add(elm.Line().at((bx, vcc_level-0.5)).length(0.6).theta(180).color('gray').linewidth(1))
        d.add(elm.Label().at(l1.end).label('$I_1$', loc='left').color('purple'))
        d.add(elm.Arrow(headwidth=0.2).at((bx-0.3, vcc_level-0.1)).down().length(0.4).color('purple'))

        # I2: Bajando por R2
        l2 = d.add(elm.Line().at((bx, gnd_level+0.5)).length(0.6).theta(180).color('gray').linewidth(1))
        d.add(elm.Label().at(l2.end).label('$I_2$', loc='left').color('orange'))
        d.add(elm.Arrow(headwidth=0.2).at((bx-0.3, gnd_level+0.9)).down().length(0.4).color('orange'))

        # IB: Entrando a la base
        l3 = d.add(elm.Line().at((bx+0.6, 0)).length(0.6).theta(90).color('gray').linewidth(1))
        d.add(elm.Label().at(l3.end).label('$I_B$', loc='top').color('red'))
        d.add(elm.Arrow(headwidth=0.2).at((bx+0.4, 0.3)).right().length(0.4).color('red'))

        # IC: Bajando por el colector
        l4 = d.add(elm.Line().at((cx, vcc_level-0.5)).length(0.6).theta(0).color('gray').linewidth(1))
        d.add(elm.Label().at(l4.end).label('$I_C$', loc='right').color('blue'))
        d.add(elm.Arrow(headwidth=0.2).at((cx+0.3, vcc_level-0.1)).down().length(0.4).color('blue'))

        # IE: Saliendo por el emisor
        l5 = d.add(elm.Line().at((ex, gnd_level+0.5)).length(0.6).theta(0).color('gray').linewidth(1))
        d.add(elm.Label().at(l5.end).label('$I_E$', loc='right').color('darkgreen'))
        d.add(elm.Arrow(headwidth=0.2).at((ex+0.3, gnd_level+0.9)).down().length(0.4).color('darkgreen'))

if __name__ == "__main__":
    generate_voltage_divider_currents()
    print("Imagen de corrientes perfeccionada con líneas de referencia.")
