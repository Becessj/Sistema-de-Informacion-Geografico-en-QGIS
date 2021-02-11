<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" labelsEnabled="0" simplifyLocal="1" simplifyDrawingHints="0" maxScale="0" simplifyAlgorithm="0" readOnly="0" version="3.12.0-București" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" enableorderby="0" forceraster="0" symbollevels="0">
    <symbols>
      <symbol clip_to_extent="1" type="marker" alpha="1" name="0" force_rhr="0">
        <layer locked="0" pass="0" class="SvgMarker" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="114,155,111,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="metro.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="6"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory labelPlacementMethod="XHeight" opacity="1" rotationOffset="270" penWidth="0" direction="0" penAlpha="255" minScaleDenominator="0" enabled="0" scaleBasedVisibility="0" sizeScale="3x:0,0,0,0,0,0" spacing="5" diagramOrientation="Up" height="15" lineSizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" maxScaleDenominator="1e+08" width="15" minimumSize="0" backgroundAlpha="255" barWidth="5" spacingUnit="MM" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" sizeType="MM" showAxis="1" lineSizeType="MM" penColor="#000000">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" field="" label=""/>
      <axisSymbol>
        <symbol clip_to_extent="1" type="line" alpha="1" name="" force_rhr="0">
          <layer locked="0" pass="0" class="SimpleLine" enabled="1">
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" linePlacementFlags="18" priority="0" showAll="1" zIndex="0" obstacle="0" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="V_ID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="G_LOTE">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PREDIO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CONTRIBUYENTE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="NOMBRE_COMPLETO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DIRECCION_FISCAL">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PERIODO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MEDIDOR">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CONEXION">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="METRO_3">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="V_ID" name=""/>
    <alias index="1" field="G_LOTE" name=""/>
    <alias index="2" field="PREDIO" name=""/>
    <alias index="3" field="CONTRIBUYENTE" name=""/>
    <alias index="4" field="NOMBRE_COMPLETO" name=""/>
    <alias index="5" field="DIRECCION_FISCAL" name=""/>
    <alias index="6" field="PERIODO" name=""/>
    <alias index="7" field="MEDIDOR" name=""/>
    <alias index="8" field="CONEXION" name=""/>
    <alias index="9" field="METRO_3" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="V_ID"/>
    <default expression="" applyOnUpdate="0" field="G_LOTE"/>
    <default expression="" applyOnUpdate="0" field="PREDIO"/>
    <default expression="" applyOnUpdate="0" field="CONTRIBUYENTE"/>
    <default expression="" applyOnUpdate="0" field="NOMBRE_COMPLETO"/>
    <default expression="" applyOnUpdate="0" field="DIRECCION_FISCAL"/>
    <default expression="" applyOnUpdate="0" field="PERIODO"/>
    <default expression="" applyOnUpdate="0" field="MEDIDOR"/>
    <default expression="" applyOnUpdate="0" field="CONEXION"/>
    <default expression="" applyOnUpdate="0" field="METRO_3"/>
  </defaults>
  <constraints>
    <constraint field="V_ID" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="G_LOTE" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="PREDIO" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="CONTRIBUYENTE" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="NOMBRE_COMPLETO" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="DIRECCION_FISCAL" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="PERIODO" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="MEDIDOR" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="CONEXION" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="METRO_3" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="V_ID" exp="" desc=""/>
    <constraint field="G_LOTE" exp="" desc=""/>
    <constraint field="PREDIO" exp="" desc=""/>
    <constraint field="CONTRIBUYENTE" exp="" desc=""/>
    <constraint field="NOMBRE_COMPLETO" exp="" desc=""/>
    <constraint field="DIRECCION_FISCAL" exp="" desc=""/>
    <constraint field="PERIODO" exp="" desc=""/>
    <constraint field="MEDIDOR" exp="" desc=""/>
    <constraint field="CONEXION" exp="" desc=""/>
    <constraint field="METRO_3" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="V_ID" hidden="0" width="-1"/>
      <column type="field" name="G_LOTE" hidden="0" width="-1"/>
      <column type="field" name="PREDIO" hidden="0" width="-1"/>
      <column type="field" name="CONTRIBUYENTE" hidden="0" width="-1"/>
      <column type="field" name="NOMBRE_COMPLETO" hidden="0" width="-1"/>
      <column type="field" name="DIRECCION_FISCAL" hidden="0" width="-1"/>
      <column type="field" name="PERIODO" hidden="0" width="-1"/>
      <column type="field" name="MEDIDOR" hidden="0" width="-1"/>
      <column type="field" name="CONEXION" hidden="0" width="-1"/>
      <column type="field" name="METRO_3" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- codificación: utf-8 -*-
"""
Los formularios de QGIS pueden tener una función de Python que
es llamada cuando se abre el formulario.

Use esta función para añadir lógica extra a sus formularios.

Introduzca el nombre de la función en el campo
"Python Init function".
Sigue un ejemplo:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="CONEXION"/>
    <field editable="1" name="CONTRIBUYENTE"/>
    <field editable="1" name="DIRECCION_FISCAL"/>
    <field editable="1" name="G_LOTE"/>
    <field editable="1" name="MEDIDOR"/>
    <field editable="1" name="METRO_3"/>
    <field editable="1" name="NOMBRE_COMPLETO"/>
    <field editable="1" name="PERIODO"/>
    <field editable="1" name="PREDIO"/>
    <field editable="1" name="V_ID"/>
  </editable>
  <labelOnTop>
    <field name="CONEXION" labelOnTop="0"/>
    <field name="CONTRIBUYENTE" labelOnTop="0"/>
    <field name="DIRECCION_FISCAL" labelOnTop="0"/>
    <field name="G_LOTE" labelOnTop="0"/>
    <field name="MEDIDOR" labelOnTop="0"/>
    <field name="METRO_3" labelOnTop="0"/>
    <field name="NOMBRE_COMPLETO" labelOnTop="0"/>
    <field name="PERIODO" labelOnTop="0"/>
    <field name="PREDIO" labelOnTop="0"/>
    <field name="V_ID" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>NOMBRE_COMPLETO</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
