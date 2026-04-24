import schemdraw
import schemdraw.elements as elm

def generate_voltage_divider_bias():
    with schemdraw.Drawing(file='topics/02-transistor-bjt/assets/bjt-divisor-voltaje-circuito.png', show=False) as d:
        d.config(unit=2.5, fontsize=12)
        
        # --- COMPONENTES CENTRALES ---
        # Transistor NPN
        Q = d.add(elm.BjtNpn().anchor('base'))
        d.add(elm.Label().at(Q.center).label('Q1', loc='right', ofst=(0.6, 0)))
        
        # Nodo de base
        d.add(elm.Line().left().at(Q.base).length(1.0))
        B_node = d.add(elm.Dot())
        
        # --- ALINEACIÓN DE RESISTENCIAS ---
        vcc_level = 3.5  # Altura de la línea VCC
        gnd_level = -3.5 # Profundidad de la línea GND
        
        # Resistencias de arriba (R1 y RC)
        # R1 va desde el nodo de base hacia arriba hasta el nivel VCC
        R1 = d.add(elm.Resistor().up().at(B_node.center).toy(vcc_level).label('$R_1$'))
        # RC va desde el colector hacia arriba hasta el mismo nivel VCC
        RC = d.add(elm.Resistor().up().at(Q.collector).toy(vcc_level).label('$R_C$'))
        
        # Conexión VCC (Línea horizontal que une R1 y RC)
        d.add(elm.Line().at(R1.end).to(RC.end))
        d.add(elm.Vdd().at(RC.end).label('$V_{CC}$'))
        
        # Resistencias de abajo (R2 y RE)
        # R2 va desde el nodo de base hacia abajo hasta el nivel GND
        R2 = d.add(elm.Resistor().down().at(B_node.center).toy(gnd_level).label('$R_2$'))
        # RE va desde el emisor hacia abajo hasta el mismo nivel GND
        RE = d.add(elm.Resistor().down().at(Q.emitter).toy(gnd_level).label('$R_E$'))
        
        # Conexión GND (Línea horizontal que une R2 y RE)
        d.add(elm.Line().at(R2.end).to(RE.end))
        d.add(elm.Ground().at(RE.end))

if __name__ == "__main__":
    generate_voltage_divider_bias()
    print("Imagen de divisor de voltaje corregida y alineada.")
