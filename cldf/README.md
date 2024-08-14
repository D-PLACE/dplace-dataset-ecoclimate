<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset D-PLACE dataset derived from Lima-Ribeiro et al. 2015 'ecoClimate'

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

Dataset Baseline Historical (1900-1949), CCSM ecoClimate model

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Lima-Ribeiro MS; Varela S; González-Hernández J; Oliveira G; Diniz-Filho JAF; Terribile LC. 2015. ecoClimate: a database of climate data from multiple models for past, present, and future for Macroecologists and Biogeographers Biodiversity Informatics 10, 1-21. DOI: 10.17161/bi.v10i0.4955

Lima-Ribeiro MS; Varela S; González-Hernández J; Oliveira G; Diniz-Filho JAF; Peterson AT; Terribile LC. The ecoClimate Database, http://ecoclimate.org
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://www.ecoclimate.org/
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by-nc-sa/4.0/
[dc:references](http://purl.org/dc/terms/references) | <ol><li>dplace-dataset-ea</li><li>dplace-dataset-binford</li><li>dplace-dataset-sccs</li><li>dplace-dataset-wnai</li></ol>
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/D-PLACE/dplace-dataset-ecoclimate
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/D-PLACE/dplace-dataset-ecoclimate/tree/v3.0">D-PLACE/dplace-dataset-ecoclimate v3.0</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.0">Glottolog v5.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.10.12</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | dplace-dataset-ecoclimate
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-datacsv"></a>Table [data.csv](./data.csv)

Values are coded datapoints, i.e. measurements of a variable for a society.

**Note:** Missing data is signaled by an empty Value column.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 19880


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Soc_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | 
[Var_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [variables.csv::ID](#table-variablescsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | Values for categorical and ordinal variables reference the corresponding code via the Code_ID column. Values for continuous variables have the measured number in the Value column and an empty Code_ID.
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | 
`sub_case` | `string` | More specific description of the population the data refer to in terms of society or area.
`year` | `string`<br>Regex: `-?[0-9]{1,4}(-[0-9]{4})?` | Focal year, i.e. the time period to which the data refer.
`source_coded_data` | `string` | The source of the coded data, which was aggregated in this dataset.
`admin_comment` | `string` | 

## <a name="table-variablescsv"></a>Table [variables.csv](./variables.csv)

Variables are cultural features or practices, or environmental descriptors.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 10


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[A-Za-z.0-9_]+([0-9]+)?` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | 
`category` | list of `string` (separated by `, `) | 
`type` | `string`<br>Valid choices:<br> `Continuous` `Categorical` `Ordinal` | Variables may be categorical (and then must be accompanied by a list of possible ‘codes’, i.e. rows in Codetable. Variables can also be continuous (e.g. Population size) or ordinal. Ordinal variables are accompanied by a list of codes (like categorical variables). The order of codes is encoded as `ord` column in CodeTable.
`unit` | `string` | The unit of measurement
`source_comment` | `string` | A note about the source of this variable.
`changes` | `string` | Notes about how a variable may have been derived from the source.
[comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 

