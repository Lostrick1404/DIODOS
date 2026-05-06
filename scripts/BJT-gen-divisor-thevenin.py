import schemdraw
import schemdraw.elements as elm

def generate_thevenin_equivalent():
    with schemdraw.Drawing(file='topics/02-transistor-bjt/assets/bjt-divisor-thevenin-equivalente.png', show=False) as d:
        d.config(unit=2.5, fontsize=12)
        
        # --- CIRCUITO EQUIVALENTE DE THÉVENIN ---
        # Definir punto de inicio para la fuente
        start_pt = (0, 0)
        
        # Fuente de voltaje Thévenin (conectada a tierra en la base)
        d.add(elm.Ground().at(start_pt))
        Vth = d.add(elm.SourceV().up().at(start_pt).label('$V_{TH}$'))
        
        # Resistencia de Thévenin (conectada al tope de Vth)
        Rth = d.add(elm.Resistor().right().at(Vth.end).label('$R_{TH}$'))
        
        # Transistor NPN (conectado a Rth)
        Q = d.add(elm.BjtNpn().anchor('base').at(Rth.end))
        d.add(elm.Label().at(Q.center).label('Q1', loc='right', ofst=(0.6, 0)))
        
        # Colector
        RC = d.add(elm.Resistor().up().at(Q.collector).label('$R_C$'))
        d.add(elm.Vdd().label('$V_{CC}$'))
        
        # Emisor
        RE = d.add(elm.Resistor().down().at(Q.emitter).label('$R_E$'))
        d.add(elm.Ground())

        # --- BLOQUE DE FÓRMULAS (Alejado a la derecha) ---
        # Coordenadas calculadas para estar lejos del transistor
        formula_x = 6.0
        formula_y = 1.0
        
        # Dibujar un recuadro para las fórmulas
        d.add(elm.Rect(at=(formula_x-0.5, formula_y-0.5), w=4.5, h=3.0).color('black'))
        
        formula_text = (
            r'$\mathbf{Valores\ de\ Th\acute{e}venin:}$' + '\n\n'
            r'$R_{TH} = \frac{R_1 \cdot R_2}{R_1 + R_2}$' + '\n\n'
            r'$V_{TH} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right)$'
        )
        d.add(elm.Label().at((formula_x, formula_y + 1.2)).label(formula_text))

if __name__ == "__main__":
    generate_thevenin_equivalent()
    print("Imagen de equivalente de Thévenin corregida y fórmulas desplazadas.")
