# raml-to-umlet-diagram
Generate a new draft UMLet diagram from the GSIM RAML-schemas, or update an existing UMLet diagram when RAML-schemas are changed. For more infomation about Statistics Norways information model in RAML-format see https://github.com/statisticsnorway/gsim-raml-schema

_raml-to-umlet-diagram_ generates an Umlet XML diagram file (uxf-file) based on information in the RAML-schema files.

Veiw the generated diagram with UMLet. UMLet is a free, open-source UML tool with a simple user interface. See https://www.umlet.com/ and http://www.umletino.com/ for more information.

## Prerequisites
* `pip install PyYAML`  (see https://pypi.org/project/PyYAML/ )

## Usage
1. Set paths in ./Config.py
   * Path to RAML-files (source)
   * Path to Umlet diagram (target)
2. Set `__main__.umletFileName` in ./UmletDiagram.py  
   * _(The "umletFileName" must either be a new (empty) Umlet uxf-file, or an existing Umlet diagram (uxf-file) to be updated.)_
3. Run ./UmletDiagram.py
4. Open the generated/updated Umlet diagram i the Umlet application (or Umletino)
5. Fix the layout
   * add lines/arrows, colors, text, ..

# Generated Umlet diagram and documentation
* [Physical data model Umlet diagram file](https://github.com/statisticsnorway/raml-to-umlet-diagram/blob/master/umlet_diagram_files/GSIM_physical_model.uxf)
* [Physical data model documentation details](https://github.com/statisticsnorway/raml-to-umlet-diagram/blob/master/umlet_diagram_files/PhysicalDataModelDetails.md)
