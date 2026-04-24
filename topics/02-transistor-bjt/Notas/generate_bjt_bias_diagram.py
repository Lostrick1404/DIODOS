import schemdraw
import schemdraw.elements as elm

# Create a new drawing
d = schemdraw.Drawing(unit=2.5)

# VCC line
d += elm.SourceV().up().label('V_CC', loc='top')
d.push() # Save VCC top for RC branch
d.push() # Save VCC top for RB branch

# RC and Collector branch
d += elm.Resistor().right().label('R_C')
# Place NPN transistor with its collector at the end of R_C
Q1 = elm.NPN(d='down').at(d.here).anchor('collector')
d += Q1
Q1.add_label('C', loc='top', ofst=(0.2, 0.2)) # Label Collector

# RB and Base branch
d.pop() # Return to VCC top for RB
d += elm.Resistor().right().label('R_B')
d += elm.Line().right().length(d.unit/2) # Short line to extend for base connection
d += elm.Line().down().to(Q1.base) # Connect to transistor base
Q1.add_label('B', loc='top', ofst=(0.2, 0.2)) # Label Base

# Emitter to Ground
d += elm.Ground().at(Q1.emitter)
Q1.add_label('E', loc='bottom', ofst=(0.2, -0.2)) # Label Emitter

# Save the drawing
output_path = '/workspaces/DIODOS-Y-TRANSISTORES/assets/bjt-emisor-comun-polarizacion-fija.png'
d.save(output_path)

print(f"Diagrama guardado en: {output_path}")