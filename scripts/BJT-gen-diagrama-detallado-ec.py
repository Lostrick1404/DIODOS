import schemdraw
import schemdraw.elements as elm

def generate_detailed_ce_diagram():
    with schemdraw.Drawing(file='topics/02-transistor-bjt/assets/bjt-detalles-corrientes-voltajes-ec.png', show=False) as d:
        d.config(unit=2.5, fontsize=11)
        
        # --- CIRCUITO ---
        Q = d.add(elm.BjtNpn().anchor('base'))
        d.add(elm.Label().at(Q.center).label('Q1', loc='right', ofst=(0.5, 0)))
        
        # Base
        L_base = d.add(elm.Line().left().at(Q.base).length(1.2))
        d.add(elm.CurrentLabel(length=0.7, ofst=0.6).at(L_base.end).label('$I_B$').color('red').reverse())
        d.add(elm.Line().left().length(0.3))
        d.add(elm.Resistor().up().label('$R_B$', loc='bottom'))
        d.add(elm.Vdd().label('$V_{CC}$'))
        
        # Colector
        d.add(elm.Resistor().up().at(Q.collector).label('$R_C$', loc='bottom'))
        d.add(elm.Vdd().label('$V_{CC}$'))
        
        # Emisor
        d.add(elm.Resistor().down().at(Q.emitter).label('$R_E$', loc='top'))
        d.add(elm.Ground())

        # --- CORRIENTES ---
        d.add(elm.CurrentLabel(length=0.7, ofst=1.0).at(Q.collector).label('$I_C$').color('blue'))
        d.add(elm.CurrentLabel(length=0.7, ofst=1.0).at(Q.emitter).label('$I_E$').color('darkgreen'))

        # --- VOLTAJES DE NODO ---
        d.add(elm.Dot().at(Q.base).color('black'))
        L_vb = d.add(elm.Line().at(Q.base).length(0.5).theta(135).color('gray').linewidth(1))
        d.add(elm.Label().at(L_vb.end).label('$V_B$', loc='left'))
        
        d.add(elm.Dot().at(Q.collector).color('black'))
        L_vc = d.add(elm.Line().at(Q.collector).length(0.5).theta(45).color('gray').linewidth(1))
        d.add(elm.Label().at(L_vc.end).label('$V_C$', loc='right'))
        
        d.add(elm.Dot().at(Q.emitter).color('black'))
        L_ve = d.add(elm.Line().at(Q.emitter).length(0.5).theta(-45).color('gray').linewidth(1))
        d.add(elm.Label().at(L_ve.end).label('$V_E$', loc='right'))

        # --- DIFERENCIAS DE POTENCIAL ---
        d.add(elm.Label().at(Q.base).label('+', ofst=(0.0, -0.5)).color('gray'))
        d.add(elm.Label().at(Q.emitter).label('-', ofst=(-0.5, 0.0)).color('gray'))
        d.add(elm.Label().at(Q.base).label('$V_{BE}$', ofst=(0.8, -1.0)))

        d.add(elm.Label().at(Q.collector).label('+', ofst=(0.5, -0.2)).color('gray'))
        d.add(elm.Label().at(Q.emitter).label('-', ofst=(0.5, 0.2)).color('gray'))
        d.add(elm.Label().at(Q.collector).label('$V_{CE}$', ofst=(1.2, -1.8)))

        # --- CUADRO DE FÓRMULAS COLORIZADO ---
        rect_x, rect_y = 4.5, -0.5
        d.add(elm.Rect(at=(rect_x, rect_y), w=5.2, h=5.5).color('black'))
        
        start_y = rect_y + 5.0
        d.add(elm.Label().at((rect_x + 0.3, start_y)).label(r'$\mathbf{Relaciones\ del\ Circuito:}$'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 0.6)).label(r'$I_E = I_B + I_C$', color='darkgreen'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 1.2)).label(r'$I_C = \beta I_B$', color='blue'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 1.8)).label(r'$I_E = (1 + \beta) I_B$ (Ec. 1)', color='darkgreen'))
        
        d.add(elm.Label().at((rect_x + 0.3, start_y - 2.8)).label(r'$\mathbf{Voltajes:}$'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 3.4)).label(r'$V_E = I_E R_E$'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 4.0)).label(r'$V_C = V_{CC} - I_C R_C$'))
        d.add(elm.Label().at((rect_x + 0.3, start_y - 4.6)).label(r'$V_{CE} = V_C - V_E$'))

if __name__ == "__main__":
    generate_detailed_ce_diagram()
