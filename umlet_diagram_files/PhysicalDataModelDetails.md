# Physical data model documentation details

#### About  
_Information about the model_  
  * model_version  
      * Mandatory: True  
      * Type: string  
      * Label: Current model version  
      * Description: This version adds shortName to all objects and dataType to InstanceVariable  

#### AdministrativeRegister  
_A source of administrative information which is obtained from an external organisation (or sometimes from another department of the same organisation)_  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ExchangeChannel** 
  * supplierIdentifier  
      * Mandatory: True  
      * Type: string  
      * Label: Supplier identifier  
      * Description: An identifier for the supplier of the Administrative Register  

#### Agent  
_An actor that performs a role in relation to the statistical Business Process._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * agentType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['INDIVIDUAL', 'ORGANIZATION', 'SYSTEM']  
      * Label: Agent type  
      * Description: The type of agent.  
  * parentAgents?  
      * Mandatory: False  
      * Link to: *_Agent_*  
      * Label: Parent agents  
  * isExternal  
      * Mandatory: True  
      * Type: boolean  
      * Label: Is external  
      * Description: Is this an external agent?  
  * agentDetails?  
      * Mandatory: False  
      * Type: AgentDetails.AgentDetails[]  
      * Label: Agent details  
      * Description: Agent details (e.g. contackt adress, email, phone, mobile ...).  

#### AgentInRole  
_Reflects an agent acting in a specific role._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * role  
      * Mandatory: True  
      * Link to: *_Role_*  
      * Label: Role  
  * agents  
      * Mandatory: True  
      * Link to: *_Agent_*  
      * Label: Agents  

#### Assessment  
_The result of the analysis of the quality and effectiveness of any activity undertaken by a statistical organization and recommendations on how these can be improved._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * datesAssessed  
      * Mandatory: True  
      * Type: datetime[]  
      * Label: Dates assessed  
      * Description: Date assessed  
  * issues?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Issues  
      * Description: Issues  
  * recommendations?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Recommendations  
      * Description: Recommendations  
  * results?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Results  
      * Description: Results  
  * statisticalNeeds?  
      * Mandatory: False  
      * Link to: *_EnvironmentChange, InformationRequest_*  
      * Label: Statistical needs  

#### BusinessCase  
_A proposal for a body of work that will deliver outputs designed to achieve outcomes. A Business Case will provide the reasoning for undertaking a Statistical Support Program to initiate a new Statistical Program Design for an existing Statistical Program, or an entirely new Statistical Program, as well as the details of the change proposed._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * dateInitiated?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date initiated  
      * Description: Date initiated  
  * dateApproved?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date approved  
      * Description: Date approved  
  * dateImplementationCommenced?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date implementation commenced  
      * Description: Date implementation commenced  
  * businessCaseType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['NEW', 'PERMANENT', 'TEMPORARY', 'CEASE']  
      * Label: Business case type  
      * Description: Business case type.  
  * objective  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Objective  
      * Description: The objective of the business case  
  * deliverable  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Deliverable  
      * Description: The deliverable of the business case  
  * assessments?  
      * Mandatory: False  
      * Link to: *_Assessment_*  
      * Label: Assessments  
  * statisticalPrograms?  
      * Mandatory: False  
      * Link to: *_StatisticalProgram_*  
      * Label: Statistical programs  
  * statisticalSupportPrograms?  
      * Mandatory: False  
      * Link to: *_StatisticalSupportProgram_*  
      * Label: Statistical support programs  
  * statisticalNeeds?  
      * Mandatory: False  
      * Link to: *_EnvironmentChange, InformationRequest_*  
      * Label: Statistical needs  
  * changeDefinitions?  
      * Mandatory: False  
      * Link to: *_ChangeDefinition_*  
      * Label: Change definitions  

#### BusinessFunction  
_Something an enterprise does, or needs to do, in order to achieve its objectives._  
  * Inherit: 
    * **IdentifiableArtefact** 

#### BusinessProcess  
_The set of Process Steps to perform one of more Business Functions to deliver a Statistical Program Cycle or Statistical Support Program._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * isPlaceholderProcess  
      * Mandatory: True  
      * Type: boolean  
      * Label: Is placeholder process  
      * Description: If true this is a placeholder-process (only a grouping of other businessprocesses in a hierarchical manner), but without link(s) to any ProcessSteps.  
  * processSteps?  
      * Mandatory: False  
      * Link to: *_ProcessStep_*  
      * Label: Process steps  
  * businessFunctions?  
      * Mandatory: False  
      * Link to: *_BusinessFunction_*  
      * Label: Business functions  
  * businessServices?  
      * Mandatory: False  
      * Link to: *_BusinessService_*  
      * Label: Business services  
  * previousBusinessProcess?  
      * Mandatory: False  
      * Link to: *_BusinessProcess_*  
      * Label: Previous Business Process  
  * parentBusinessProcess?  
      * Mandatory: False  
      * Link to: *_BusinessProcess_*  
      * Label: Parent Business Process  

#### BusinessService  
_A means of performing a Business Function (an ability that an organization possesses, typically expressed in general and high level terms and requiring a combination of organization, people, processes and technology to achieve)._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * location?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Location  
      * Description: Specifies where the service can be accessed.  
  * serviceInterface?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Service interface  
      * Description: Specifies how to communicate with the service.  

#### ChangeDefinition  
_A structured, well-defined specification for a proposed change._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * populations?  
      * Mandatory: False  
      * Link to: *_Population_*  
      * Label: Populations  

#### DataHarvesting  
_A concrete and usable tool to gather information from the Internet._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ExchangeChannel** 
  * dataHarvestingType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['API', 'WEBSCRAPING']  
      * Label: Data harvester type  
      * Description: Method for harvesting data  

#### DataResource  
_An organized collection of stored information made of one or more Data Sets._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **InformationResource** 
  * dataResourceType?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['STATISTICAL_REGISTER_PERSONS', 'ETABLISHMENT_ENTERPRISE_REGISTER']  
      * Label: Data resource type  
  * dataSets?  
      * Mandatory: False  
      * Link to: *_UnitDataSet, DimensionalDataSet_*  
      * Label: Data Sets  

#### DescribedValueDomain  
_A Value Domain defined by an expression._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ValueDomain** 
  * minValue?  
      * Mandatory: False  
      * Type: number  
      * Label: Min value  
      * Description: A Value Domain defined by an expression.  
  * maxValue?  
      * Mandatory: False  
      * Type: number  
      * Label: Max value  
      * Description: A Value Domain defined by an expression.  
  * minLength?  
      * Mandatory: False  
      * Type: number  
      * Label: Min length  
      * Description: A Value Domain defined by an expression.  
  * maxLength?  
      * Mandatory: False  
      * Type: number  
      * Label: Max length  
      * Description: A Value Domain defined by an expression.  
  * minDecimals?  
      * Mandatory: False  
      * Type: number  
      * Label: Min decimals  
      * Description: A Value Domain defined by an expression.  
  * maxDecimals?  
      * Mandatory: False  
      * Type: number  
      * Label: Max decimals  
      * Description: A Value Domain defined by an expression.  

#### DimensionalDataSet  
_A collection of dimensional data that conforms to a known structure._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **DataSet** 
  * dimensionalDataStructure  
      * Mandatory: True  
      * Link to: *_DimensionalDataStructure_*  
      * Label: Dimensional data structure  

#### DimensionalDataStructure  
_Describes the structure of a Dimensional Data Set._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **DataStructure** 
  * instanceVariables  
      * Mandatory: True  
      * Link to: *_InstanceVariable_*  
      * Label: Instance variables  

#### EnumeratedValueDomain  
_A Value Domain expressed as a list of Categories and associated Codes._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ValueDomain** 
  * klassUrl  
      * Mandatory: True  
      * Type: string  
      * Label: Klass url  
      * Description: The url to KLASS codelist.  

#### EnvironmentChange  
_A requirement for change  that originates from a change in the operating environment of the statistical organization._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **StatisticalNeed** 
  * environmentChangeType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['INTERNAL', 'EXTERNAL']  
      * Label: Environment change type  
      * Description: Environment change type.  
  * changeOrigin  
      * Mandatory: True  
      * Type: string  
      * Label: Change origin  
      * Description: Change origin  
  * legalChange?  
      * Mandatory: False  
      * Type: string  
      * Label: Legal change  
      * Description: Legal change  
  * methodChange?  
      * Mandatory: False  
      * Type: string  
      * Label: Method change  
      * Description: Method change  
  * softwareChange?  
      * Mandatory: False  
      * Type: string  
      * Label: Software change  
      * Description: Software change  
  * otherChange?  
      * Mandatory: False  
      * Type: string  
      * Label: Other change  
      * Description: Other change  

#### InformationRequest  
_An outline of a need for new information required for a particular purpose._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **StatisticalNeed** 
  * coverageOfInformationRequired  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Information requester  
      * Description: Coverage of information required  
  * dateInformationRequired?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date information required  
      * Description: Date Information Required  
  * subjectFields?  
      * Mandatory: False  
      * Link to: *_SubjectField_*  
      * Label: Subject fields  

#### InstanceVariable  
_The use of a Represented Variable within a Data Set. It may include information about the source of the data._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * representedVariable  
      * Mandatory: True  
      * Link to: *_RepresentedVariable_*  
      * Label: Represented variable  
  * population  
      * Mandatory: True  
      * Link to: *_Population_*  
      * Label: Population  
  * dataStructureComponentType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['IDENTIFIER', 'MEASURE', 'ATTRIBUTE']  
      * Label: Data Structure Component Type  
      * Description: The data structure component type (identifier, measure or attribute) of the instance variable.  
  * sentinelValueDomain?  
      * Mandatory: False  
      * Link to: *_EnumeratedValueDomain, DescribedValueDomain_*  
      * Label: Sentinel value domain  
  * formatMask?  
      * Mandatory: False  
      * Type: string  
      * Label: Format  
      * Description: This attribute describes the data-format of the instance variable. For example a date-format-mask.  
  * identifierComponentIsUnique?  
      * Mandatory: False  
      * Type: boolean  
      * Label: Identifier component is unique  
      * Description: For INDENTIFIER-components. Indicates if the key is unique.  
  * identifierComponentIsComposite?  
      * Mandatory: False  
      * Type: boolean  
      * Label: Identifier component is composite  
      * Description: For INDENTIFIER-components. Indicates if the key is composite, e.g. person-identifier and date/time.  
  * dataStructureComponentRole?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['ENTITY', 'IDENTITY', 'COUNT', 'TIME', 'GEO']  
      * Label: Data structure component role  
      * Description: For INDENTIFIER-components or MEASURE-components. Specifies the type of role --> "entity", "count", "time", "geography" or "identity" (only INDENTIFIER-components).  
  * geoType?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['POINT', 'POLYGON', 'LINE']  
      * Label: Geo type  
      * Description: If the component is a geolocation (dataStructureComponentRole is GEO) then there are different types  
  * mandatory?  
      * Mandatory: False  
      * Type: boolean  
      * Label: Mandatory  
      * Description: Is the variable mandatory or not  
  * physicalDataType?  
      * Mandatory: False  
      * Type: string  
      * Label: Data type  
      * Description: Data type of instance variable  

#### InstanceVariableRelationship  
_This reflects that there could be a structure within the Logical Record and Data Structure, for example several fields can together represent a structured field (e.g. an address), or the record can be structured as in the case of an XML file conformant to a schema. Another example is the relationship between attributes (source, quality, ..) and measures._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * relationType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['PARENT', 'CHILD', 'SIBLING', 'UNKNOWN']  
      * Label: Relation type  
      * Description: The type of relation  
  * sourceComponents  
      * Mandatory: True  
      * Link to: *_InstanceVariable_*  
      * Label: Source components  
      * Description: The relation source instance variables (components), e.g. "street", "zipCode" and "city".  
  * targetComponents  
      * Mandatory: True  
      * Link to: *_InstanceVariable_*  
      * Label: Target components  
      * Description: The relation target instance variables (components), e.g. "address"  

#### LogicalRecord  
_Describes a type of Unit Data Record for one Unit Type within a Unit Data Set._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * unitType  
      * Mandatory: True  
      * Link to: *_UnitType_*  
      * Label: Unit type  
  * parentLogicalRecord?  
      * Mandatory: False  
      * Link to: *_LogicalRecord_*  
      * Label: Parent logical record  
  * parentChildMultiplicity?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['ZERO_ONE', 'ONE_ONE', 'ZERO_MANY', 'ONE_MANY']  
      * Label: Parent child multiplicity  
      * Description: Describes the multiplicity of this LogicalRecord when a link to parentLogicalRecord exists.  
  * isPlaceholderRecord  
      * Mandatory: True  
      * Type: boolean  
      * Label: Is placeholder record  
      * Description: If true this is a placeholder-record (only a grouping of other records in a hierarchical UnitDataSet), but without link(s) to any InstanceVariables.  
  * instanceVariables?  
      * Mandatory: False  
      * Link to: *_InstanceVariable_*  
      * Label: Instance variables  

#### MappingRawDataToInputData  
_Mapping elements from external Raw Data Object Store to Input Data (InstanceVariable)._  
  * id  
      * Mandatory: True  
      * Type: string  
      * Label: Id  
      * Description: Global unique identifier (GUID).  
  * sourceName  
      * Mandatory: True  
      * Type: string  
      * Label: Raw data element name (or id)  
      * Description: The name of the raw data source-element/field/variable (e.g. streetName or streetNumber)  
  * sourcePath  
      * Mandatory: True  
      * Type: string  
      * Label: Raw data source path  
      * Description: Path to the raw data source-element/field/variable (e.g. Xpath /person/address/)  
  * targetInstanceVariable  
      * Mandatory: True  
      * Link to: *_InstanceVariable_*  
      * Label: Target input data InstanceVariable (id)  
  * validFrom?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Valid from  
      * Description: The date on which the mapping is effective or valid. Set this date only once (constant).  
  * validUntil?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Valid until  
      * Description: The date on which the mapping is no longer effective or valid.  
  * lastUpdatedDate?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Last updated dat  
      * Description: The date on which the object was created or updated.  
  * lastUpdatedBy?  
      * Mandatory: False  
      * Type: string  
      * Label: Last updated by  
      * Description: Created or updated by.  

#### MeasurementType  
_The Measurement Type defines the type of a measure e.g. mass or currency. The Measurement Type groups all Measurement Units, which can be converted into each other. A Measurement Type can have a standard Measurement Unit, which can be used for conversion between different Measurement Units._  
  * Inherit: 
    * **IdentifiableArtefact** 

#### MeasurementUnit  
_A Measurement Unit is the metric for a measurement in terms of an official unit of measurement._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * measurementType?  
      * Mandatory: False  
      * Link to: *_MeasurementType_*  
      * Label: Measurement type  
  * conversionRule?  
      * Mandatory: False  
      * Type: string  
      * Label: Conversion rule  
      * Description: Rule for conversion to the standard Measurement Unit, if this exists.  
  * abbreviation?  
      * Mandatory: False  
      * Type: string  
      * Label: Abbreviation  
      * Description: Abbreviation for the Measurement Unit e.g. kg for kilograms  

#### OutputSpecification  
_Defines how Information Sets consumed by a Product are presented to Information Consumers._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * products?  
      * Mandatory: False  
      * Link to: *_Product_*  
      * Label: Products  
  * presentations?  
      * Mandatory: False  
      * Link to: *_Presentation_*  
      * Label: Presentations  

#### ParameterInput  
_Inputs used to specify which configuration should be used for a specific Process Step which has been designed to be configurable._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessInput** 
  * parameterDataType  
      * Mandatory: True  
      * Type: string  
      * Label: Parameter data type  
      * Description: The datatype of the parameter input  
  * parameterRole?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['WEIGHT', 'UPPER_THRESHOLD', 'AGREEMENT_LEVEL']  
      * Label: Parameter role  
      * Description: Used to convey the role of this parameter.  
  * parameterValue  
      * Mandatory: True  
      * Type: string  
      * Label: Parameter value  
      * Description: The content of the parameter  

#### Population  
_The total membership of a defined class of people, objects or events._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **Concept** 
  * populationType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['TARGET', 'SURVEY']  
      * Label: Population type  
      * Description: The type og pupulation.  
  * referencePeriodStartDate  
      * Mandatory: True  
      * Type: datetime  
      * Label: Reference period start date  
      * Description: The time period to which the population is associated.  
  * referencePeriodEndDate  
      * Mandatory: True  
      * Type: datetime  
      * Label: Reference period end date  
      * Description: The time period to which the population is associated.  
  * geography?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['CONTINENT', 'COUNTRY', 'REGION', 'COUNTY', 'MUNICIPALITY', 'ADRESS', 'CADASTRE', 'GEOLOCATION']  
      * Label: Geography  
      * Description: The geographical area to which the population is associated.  
  * universes  
      * Mandatory: True  
      * Link to: *_Universe_*  
      * Label: Universes  
  * parentPopulations?  
      * Mandatory: False  
      * Link to: *_Population_*  
      * Label: Parent populations  

#### Presentation  
_The way data and referential metadata are presented in a Product._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * presentationType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['TABLE', 'FILE', 'GRAPH', 'CLASSIFICATION', 'PDF', 'WEBPAGE']  
      * Label: Presentation type  
      * Description: Type of presentation  
  * presentationFormat  
      * Mandatory: True  
      * Type: string  
      * Label: Presentation format  
      * Description: Format of the presentation type  
  * informationSetsToPresent  
      * Mandatory: True  
      * Link to: *_DimensionalDataSet, UnitDataSet_*  
      * Label: Informationsets to present  

#### ProcessControl  
_A set of decision points which determine the flow between the Process Steps used to perform a Business Process._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * startEvent?  
      * Mandatory: False  
      * Type: string  
      * Label: Start event  
      * Description: The event which triggered the control.  
  * processControlStatus?  
      * Mandatory: False  
      * Type: string  
      * Label: Process control status  
      * Description: Success or error, typically using a coded value.  

#### ProcessControlDesign  
_The specification of the decision points required during the execution of a Business Process._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * rules?  
      * Mandatory: False  
      * Link to: *_Rule_*  
      * Label: Rules  
  * processControl  
      * Mandatory: True  
      * Link to: *_ProcessControl_*  
      * Label: Process control  

#### ProcessDesign  
_The specification of how a Process Step will be performed. This includes specifying the types of Process Inputs required and the type of Process Outputs that will be produced._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * processSteps?  
      * Mandatory: False  
      * Link to: *_ProcessStep_*  
      * Label: Process steps  
  * processInputSpecifications  
      * Mandatory: True  
      * Link to: *_ProcessInputSpecification_*  
      * Label: Process input specifications  
  * processOutputSpecifications  
      * Mandatory: True  
      * Link to: *_ProcessOutputSpecification_*  
      * Label: Process output specifications  
  * processControlDesign  
      * Mandatory: True  
      * Link to: *_ProcessControlDesign_*  
      * Label: Process control design  
  * processMethods?  
      * Mandatory: False  
      * Link to: *_ProcessMethod_*  
      * Label: Process methods  
  * businessServices?  
      * Mandatory: False  
      * Link to: *_BusinessService_*  
      * Label: Business services  
  * businessFunctions?  
      * Mandatory: False  
      * Link to: *_BusinessFunction_*  
      * Label: Business functions  
  * processPatterns?  
      * Mandatory: False  
      * Link to: *_ProcessPattern_*  
      * Label: Process patterns  

#### ProcessExecutionLog  
_The Process Execution Log captures the output of a Process Step which is not directly related to the Transformed Output it produced. It may include data that was recorded during the real time execution of the Process Step._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessOutput** 
  * processId?  
      * Mandatory: False  
      * Type: string  
      * Label: Process id  
      * Description: Carries a reference to the instance, so that the log entry can be related to the process. Can be useful for both manual resolution or by the process control.  
  * startTime?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Start time  
      * Description: The time the Process Step started  
  * endTime?  
      * Mandatory: False  
      * Type: datetime  
      * Label: End time  
      * Description: The time the Process Step ended  
  * logType?  
      * Mandatory: False  
      * Type: string  
      * Label: Log type  
      * Description: The type of event that occurred during process execution (for example, an error)  
  * logCode?  
      * Mandatory: False  
      * Type: string  
      * Label: Log code  
      * Description: The code for the event that occurred during the process execution.  
  * logMessage?  
      * Mandatory: False  
      * Type: string  
      * Label: Log message  
      * Description: The human readable message for the event that occurred during the process execution.  
  * logSeverity?  
      * Mandatory: False  
      * Type: string  
      * Label: Log severity  
      * Description: The severity for the event that occurred during the process execution.  

#### ProcessInputSpecification  
_A record of the types of inputs required for a Process Design._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * prosessInputType  
      * Mandatory: True  
      * Type: string  
      * Label: Prosess input type  
      * Description: This denotes the type of object which can be used as an input.  

#### ProcessMethod  
_A specification of the technique which will be used to perform the unit of work._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * rules?  
      * Mandatory: False  
      * Link to: *_Rule_*  
      * Label: Rules  

#### ProcessMetric  
_A Process Output whose purpose is to measure and report some aspect of how the Process Step performed during execution._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessOutput** 

#### ProcessOutputSpecification  
_A record of the types of outputs required for a Process Design._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * processOutputType  
      * Mandatory: True  
      * Type: string  
      * Label: Process output type  
      * Description: This denotes the type of object which can be used as an output.  

#### ProcessPattern  
_A nominated set of Process  Designs, and associated Process Control Designs (flow), which have been highlighted for possible reuse._  
  * Inherit: 
    * **IdentifiableArtefact** 

#### ProcessStep  
_A Process Step is a work package that performs a Business Process. A Process Step implements the Process Step Design specified in order to produce the outputs for which the Process Step was designed._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * isComprehensive  
      * Mandatory: True  
      * Type: boolean  
      * Label: Is comprehensive  
      * Description: Used to indicate whether this ProcessStep has sub-ProcessSteps.  
  * codeBlocks?  
      * Mandatory: False  
      * Type: ProcessStepCodeBlockDetails.ProcessStepCodeBlockDetails[]  
      * Label: Code block details  
      * Description: Code blocks  
  * technicalPackageID?  
      * Mandatory: False  
      * Type: string  
      * Label: Techical ID  
      * Description: ID or URI of technical implementation  
  * parentProcessStep?  
      * Mandatory: False  
      * Link to: *_ProcessStep_*  
      * Label: Parent process step  
  * processControl?  
      * Mandatory: False  
      * Link to: *_ProcessControl_*  
      * Label: Process control  
  * previousProcessStep?  
      * Mandatory: False  
      * Link to: *_ProcessStep_*  
      * Label: Previous process step  

#### ProcessStepInstance  
_An executed step in a Business Process. A Process Step Instance specifies the actual inputs to and outputs from for an occurrence of a Process Step._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * processExecutionCode  
      * Mandatory: True  
      * Type: string  
      * Label: Process execution code  
      * Description: The action that took place as executable code  
  * parameterInputs?  
      * Mandatory: False  
      * Link to: *_ParameterInput_*  
      * Label: Parameter inputs  
  * transformableInputs?  
      * Mandatory: False  
      * Link to: *_TransformableInput_*  
      * Label: Transformable inputs  
  * processSupportInputs?  
      * Mandatory: False  
      * Link to: *_ProcessSupportInput_*  
      * Label: Process support inputs  
  * transformedOutputs?  
      * Mandatory: False  
      * Link to: *_TransformedOutput_*  
      * Label: Transformed outputs  
  * processMetrics?  
      * Mandatory: False  
      * Link to: *_ProcessMetric_*  
      * Label: Process metrics  
  * processExecutionLog  
      * Mandatory: True  
      * Link to: *_ProcessExecutionLog_*  
      * Label: Process execution log  

#### ProcessSupportInput  
_A form of Process Input that influences the work performed by the Process Step, and therefore influences its outcome._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessInput** 
  * processSupportDataType?  
      * Mandatory: False  
      * Type: string  
      * Label: Process support data type  
      * Description: The datatype of the ProcessSupportInput  
  * processSupportRoles?  
      * Mandatory: False  
      * Link to: *_Role_*  
      * Label: Process support roles  
      * Description: Used to convey the role of this input.  
  * processSupportValue?  
      * Mandatory: False  
      * Type: string  
      * Label: Process support value  
      * Description: The content of the ProcessSupportInput  

#### Product  
_A package of content that can be disseminated as a whole._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ExchangeChannel** 
  * presentations  
      * Mandatory: True  
      * Link to: *_Presentation_*  
      * Label: Presentations  

#### Protocol  
_The mechanism for exchanging information through an Exchange Channel._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * protocolType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['API', 'FTP', 'SFTP', 'HTTP', 'HTTPS', 'EMAIL', 'OPTICAL_DEVICE', 'DATABASE']  
      * Label: Protocol type  
      * Description: Type of protocol.  

#### ProvisionAgreement  
_The legal or other basis by which two parties agree to exchange data._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * regulation  
      * Mandatory: True  
      * Type: string  
      * Enum: ['VOLUNTARY', 'MANDATORY', 'ADMINISTRATIVE_REGISTER']  
      * Label: Regulation  
      * Description: Legal or lawful basis to collect data  
  * provisionAgreementStatus  
      * Mandatory: True  
      * Type: string  
      * Enum: ['DRAFT', 'INTERNAL', 'OPEN', 'DEPRECATED']  
      * Label: Provision Agreement Status  
      * Description: Provision agreement status  
  * changeManagement?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Change management  
      * Description: Change management  
  * informationSource  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Information source  
      * Description: External source  
  * frequency  
      * Mandatory: True  
      * Type: string  
      * Enum: ['ONGOING', 'DAILY', 'WEEKLY', 'MONTHLY', 'ANNUAL']  
      * Label: Frequency  
      * Description: The time frequency at which data is collected at regular intervals.  
  * exchangeChannels?  
      * Mandatory: False  
      * Link to: *_Product, AdministrativeRegister, Questionnaire, DataHarvesting_*  
      * Label: Exchange channels  
  * informationProviders?  
      * Mandatory: False  
      * Link to: *_AgentInRole_*  
      * Label: Information providers  
  * informationConsumers?  
      * Mandatory: False  
      * Link to: *_AgentInRole_*  
      * Label: Information consumers  
  * agreedDataStructures?  
      * Mandatory: False  
      * Link to: *_UnitDataStructure, DimensionalDataStructure_*  
      * Label: Agreed Data Structures  

#### Questionnaire  
_A concrete and usable tool to elicit information from observation units._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ExchangeChannel** 

#### RepresentedVariable  
_A combination of a characteristic of a population to be measured and how that measure will be represented._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * variable  
      * Mandatory: True  
      * Link to: *_Variable_*  
      * Label: Variable  
  * universe  
      * Mandatory: True  
      * Link to: *_Universe_*  
      * Label: Universe  
  * substantiveValueDomain?  
      * Mandatory: False  
      * Link to: *_EnumeratedValueDomain, DescribedValueDomain_*  
      * Label: Substantive value domain  

#### Role  
_The responsible function involved in the statistical Business Process._  
  * Inherit: 
    * **IdentifiableArtefact** 

#### Rule  
_A specific mathematical or logical expression which can be evaluated to determine specific behavior._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * algorithm?  
      * Mandatory: False  
      * Type: string  
      * Label: Algorithm  
      * Description: The rule expressed as an algorithm.  
  * commandCode?  
      * Mandatory: False  
      * Type: string  
      * Label: Command code  
      * Description: Structured information used by a system to process the instruction.  
  * ruleType?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['INPUT', 'COMPARISON', 'IMPUTATION', 'EDIT', 'DERIVATION', 'RECODE']  
      * Label: Rule type  
      * Description: A type taken from a controlled vocabulary.  
  * expression?  
      * Mandatory: False  
      * Type: string  
      * Label: Expression  
      * Description: The expression of the rule that is evaluated.  
  * isSystemExecutable?  
      * Mandatory: False  
      * Type: boolean  
      * Label: Is system executable  
      * Description: Whether the rule is formatted to be executed by a system, or is only documentary.  

#### StatisticalProgram  
_A set of activities, which may be repeated, to investigate characteristics of a given Population. It describes the purpose and context of a set of Business Process within the context of the relevant Statistical Program Cycles._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * parentStatisticalPrograms?  
      * Mandatory: False  
      * Link to: *_StatisticalProgram_*  
      * Label: Parent statistical programs  
  * statisticalProgramDesign?  
      * Mandatory: False  
      * Link to: *_StatisticalProgramDesign_*  
      * Label: Statistical program design  
  * statisticalProgramCycles?  
      * Mandatory: False  
      * Link to: *_StatisticalProgramCycle_*  
      * Label: Statistical program cycles  
  * dateInitiated?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date initiated  
      * Description: First date of validity  
  * dateEnded?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date ended  
      * Description: Last date of validity  
  * statisticalProgramStatus  
      * Mandatory: True  
      * Type: string  
      * Enum: ['NEW', 'UNDER_DEVELOPMENT', 'CURRENT', 'COMPLETED', 'CANCELLED', 'TRANSFERRED']  
      * Label: Statistical program status  
      * Description: The current condition of the program  
  * history  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: History  
      * Description: A description of the precursors of the program within the organisation  
  * subjectMatterDomains  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Subject matter domains  
      * Description: A description of the subject matters  
  * sourceOfFunding?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Source of funding  
      * Description: A description of the source of funding  
  * budget?  
      * Mandatory: False  
      * Type: number  
      * Label: Budget  
      * Description: Budget  
  * legislativeReferences?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Legislative references  
      * Description: Any legislative materials, eg parliamentary tabling documents  
  * legalFrameworks?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Legal frameworks  
      * Description: Description of the legal framework  

#### StatisticalProgramCycle  
_A set of activities to investigate characteristics of a given Population for a particular reference period._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * businessProcesses?  
      * Mandatory: False  
      * Link to: *_BusinessProcess_*  
      * Label: Business processes  
  * referencePeriodStart  
      * Mandatory: True  
      * Type: datetime  
      * Label: Reference period start  
      * Description: First date of validity  
  * referencePeriodEnd  
      * Mandatory: True  
      * Type: datetime  
      * Label: Reference period end  
      * Description: Last date of validity  

#### StatisticalProgramDesign  
_The specification of the resources required, processes used and description of relevant methodological information about the set of activities undertaken to investigate characteristics of a given Population._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * businessCases?  
      * Mandatory: False  
      * Link to: *_BusinessCase_*  
      * Label: Business cases  
  * processDesigns?  
      * Mandatory: False  
      * Link to: *_ProcessDesign_*  
      * Label: Process designs  
  * processPatterns?  
      * Mandatory: False  
      * Link to: *_ProcessPattern_*  
      * Label: Process patterns  
  * businessFunctions?  
      * Mandatory: False  
      * Link to: *_BusinessFunction_*  
      * Label: Business functions  
  * dateInitiated?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date initiated  
      * Description: First date of validity  
  * dateEnded?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date ended  
      * Description: Last date of validity  
  * statisticalProgramDesignStatus  
      * Mandatory: True  
      * Type: string  
      * Enum: ['NEW', 'UNDER_DEVELOPMENT', 'CURRENT', 'COMPLETED', 'CANCELLED', 'TRANSFERRED']  
      * Label: Statistical program design status  
      * Description: The current condition of the program design  
  * conceptualFrameworks?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Conceptual frameworks  
      * Description: Description of the conceptual framework  

#### StatisticalSupportProgram  
_A program which is not related to the post-design cyclic production of statistical products, but is necessary to support cyclical production._  
  * Inherit: 
    * **IdentifiableArtefact** 
  * statisticalProgramDesign?  
      * Mandatory: False  
      * Link to: *_StatisticalProgramDesign_*  
      * Label: Statistical program design  
  * statisticalNeeds?  
      * Mandatory: False  
      * Link to: *_EnvironmentChange, InformationRequest_*  
      * Label: Statistical needs  
  * changeDefinitions?  
      * Mandatory: False  
      * Link to: *_ChangeDefinition_*  
      * Label: Change definitions  
  * businessProcesses?  
      * Mandatory: False  
      * Link to: *_BusinessProcess_*  
      * Label: Business processes  
  * dateInitiated?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date initiated  
      * Description: Initiated date  
  * dateEnded?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date ended  
      * Description: Last date of validity  
  * statisticalSupportProgramStatus  
      * Mandatory: True  
      * Type: string  
      * Enum: ['NEW', 'UNDER_DEVELOPMENT', 'CURRENT', 'COMPLETED', 'CANCELLED', 'TRANSFERRED']  
      * Label: Statistical support program status  
      * Description: The current condition of the program  
  * history?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: History  
      * Description: A description of the precursors of the program within the organisation  
  * subjectMatterDomain?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Subject matter domain  
      * Description: A description of the subject matters  
  * significantEvents?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Significant events  
      * Description: A description of the real-world events which lead to the creation of the program  

#### SubjectField  
_One or more Concept Systems used for the grouping of Concepts and Categories for the production of statistics._  
  * Inherit: 
    * **IdentifiableArtefact** 

#### TransformableInput  
_A type of Process Input whose content goes into a Process Step and is changed in some way by the execution of that Process Step. Some or all of the content will be represented in the Transformed Output._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessInput** 
  * inputId  
      * Mandatory: True  
      * Link to: *_UnitDataSet, DimensionalDataSet_*  
      * Label: Input id  
  * inputAlias?  
      * Mandatory: False  
      * Type: string  
      * Label: Resource alias  
      * Description: Alias used in code when referring to the resource  

#### TransformedOutput  
_A Process Output (a result) which provides the reason for existence for the Process Step._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **ProcessOutput** 
  * outputId  
      * Mandatory: True  
      * Link to: *_UnitDataSet, DimensionalDataSet_*  
      * Label: Output id  

#### UnitDataSet  
_A collection of data that conforms to a known structure and describes aspects of one or more Units._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **DataSet** 
  * unitDataStructure  
      * Mandatory: True  
      * Link to: *_UnitDataStructure_*  
      * Label: Unit data structure  

#### UnitDataStructure  
_Describes the structure of a Unit Data Set._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **DataStructure** 
  * logicalRecords  
      * Mandatory: True  
      * Link to: *_LogicalRecord_*  
      * Label: Logical records  

#### UnitType  
_A Unit Type is a class of objects of interest_  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **Concept** 
  * typeOfStatisticalUnit  
      * Mandatory: True  
      * Type: string  
      * Enum: ['ENTERPRISE', 'ESTABLISHMENT', 'PERSON', 'FAMILY', 'HOUSEHOLD', 'SHAREHOLDER', 'MUNICIPALITY', 'NOT_APPLICABLE']  
      * Label: Type of statistical unit  
      * Description: Type of unit.  
  * parentUnitTypes?  
      * Mandatory: False  
      * Link to: *_UnitType_*  
      * Label: Parent unit types  

#### Universe  
_A defined class of people, entities, events, or objects, with no specification of time and geography, contextualizing a Unit Type._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **Concept** 
  * unitTypes  
      * Mandatory: True  
      * Link to: *_UnitType_*  
      * Label: Unit types  

#### Variable  
_The use of a Concept as a characteristic of a Population intended to be measured._  
  * Inherit: 
    * **IdentifiableArtefact** 
    * **Concept** 
  * unitType  
      * Mandatory: True  
      * Link to: *_UnitType_*  
      * Label: Unit type  

#### AdministrativeDetails  
_A generic and expandable key-value-store for adding present and future AdministrativeDetails-attributes to any information object._  
  * Inherit: 
    * **object** 
  * administrativeDetailType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['DEFAULTLANGUAGE', 'ANNOTATION', 'ALIAS', 'URL', 'DOCUMENTATION', 'LOCALID', 'ORIGIN']  
      * Label: Administrative detail type  
      * Description: The type (key) of the AdministrativeDetails-attribute.  
  * values  
      * Mandatory: True  
      * Type: string[]  
      * Label: Values  
      * Description: One or more values (a list) for this administrativeDetailType.  

#### AgentDetails  
_A generic and expandable key-value-store for adding present and future AgentDetails-attributes to the Agent-object._  
  * Inherit: 
    * **object** 
  * agentDetailType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['CONTACT_EMAIL', 'CONTACT_MOBILE', 'CONTACT_PHONE', 'CONTACT_ADDRESS']  
      * Label: Agent detail type  
      * Description: The type (key) of the AgentDetails-attribute.  
  * values  
      * Mandatory: True  
      * Type: string[]  
      * Label: Values  
      * Description: One or more values (a list) for this agentDetailType.  

#### Concept  
_Unit of thought differentiated by characteristics._  
  * subjectFields?  
      * Mandatory: False  
      * Link to: *_SubjectField_*  
      * Label: Subject fields  
  * nationalConceptsCatalogURI?  
      * Mandatory: False  
      * Type: string  
      * Label: National concepts catalog  
      * Description: Link to national concepts catalog  

#### DataSet  
_An organized collection of data._  
  * dataSetState  
      * Mandatory: True  
      * Type: string  
      * Enum: ['RAW_DATA', 'INPUT_DATA', 'PROCESSED_DATA', 'OUTPUT_DATA', 'DATA_PRODUCT', 'OTHER_DATA']  
      * Label: Data set state  
      * Description: The type of "steady state" for the dataset.  
  * temporalityType?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['EVENT', 'STATUS', 'ACCUMULATED', 'FIXED']  
      * Label: Temporality type  
      * Description: Dataset temporality  
  * valuation?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['SENSITIVE', 'SHIELDED', 'INTERNAL', 'OPEN']  
      * Label: Valuation  
      * Description: Classification of the value or damage potential of a dataset  
  * dataExistsFromDate?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Data exists from date  
      * Description: The date on which data is effective or valid.  
  * dataExistsUntilDate?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Data exists until date  
      * Description: The date on which data is no longer effective or valid.  
  * dataSourcePath?  
      * Mandatory: False  
      * Type: string  
      * Label: Data source path  
      * Description: The path (API endpoint, URI, catalog, ..) to the raw dataset.  
  * metadataSourcePath?  
      * Mandatory: False  
      * Type: string  
      * Label: Metadata source path  
      * Description: The path (API endpoint, URI, catalog, ..) to the metadata describing the raw dataset.  

#### DataStructure  
_Defines the structure of an organized collection of data (Data Set)._  

#### ExchangeChannel  
_A means of exchanging data._  
  * direction  
      * Mandatory: True  
      * Type: string  
      * Enum: ['COLLECT', 'DISSEMINATE']  
      * Label: Direction  
      * Description: Direction of the exchange channel  
  * protocol  
      * Mandatory: True  
      * Link to: *_Protocol_*  
      * Label: Protocol  
  * consumesInformationSets?  
      * Mandatory: False  
      * Link to: *_UnitDataSet, DimensionalDataSet_*  
      * Label: Consumes Data Sets  
  * producesInformationSets?  
      * Mandatory: False  
      * Link to: *_UnitDataSet, DimensionalDataSet_*  
      * Label: Produces Data Sets  

#### IdentifiableArtefact  
_IdentifiableArtefact is reusable abstract object (type). All identifiable objects inherits all attributes from this object (type)._  
  * id  
      * Mandatory: True  
      * Type: string  
      * Label: Id  
      * Description: The global unique identifier (GUID) of the information object assigned by the owner agency.  
  * name  
      * Mandatory: True  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Name  
      * Description: A term which designates a concept, in this case an information object. The identifying name will be the preferred designation. There will be many terms to designate the same information object, such as synonyms and terms in other languages.  
  * description?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Description  
      * Description: The description of the information object  
  * shortName?  
      * Mandatory: False  
      * Type: string  
      * Label: Short name  
      * Description: A short technical name. (Avoid special characters not supported as variable names in common programming languages).  
  * administrativeStatus?  
      * Mandatory: False  
      * Type: string  
      * Enum: ['DRAFT', 'INTERNAL', 'OPEN', 'DEPRECATED']  
      * Label: Administrative status  
      * Description: Indicator for access to an item.  
  * createdDate  
      * Mandatory: True  
      * Type: datetime  
      * Label: Created date  
      * Description: The date on which the information object was created  
  * createdBy  
      * Mandatory: True  
      * Type: string  
      * Label: Created by  
      * Description: Information object created by.  
  * version?  
      * Mandatory: False  
      * Type: string  
      * Label: Version  
      * Description: Formal versioning of the information object. The version designator of the information object assigned by the owner agency. "major.minor.patch", e.g. "1.12.5".  
  * versionValidFrom  
      * Mandatory: True  
      * Type: datetime  
      * Label: Version valid from  
      * Description: The date on which the current version of the infomation object is effective or valid.  
  * versionRationale?  
      * Mandatory: False  
      * Type: MultilingualText.MultilingualText[]  
      * Label: Version rationale  
      * Description: The reason for making this version of the information object.  
  * lastUpdatedDate?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Last updated date  
      * Description: The date on which the object was last updated.  
  * lastUpdatedBy?  
      * Mandatory: False  
      * Type: string  
      * Label: Last updated by  
      * Description: Last updated by.  
  * validFrom  
      * Mandatory: True  
      * Type: datetime  
      * Label: Valid from  
      * Description: The date on which the information object is effective or valid. Set this date only once (constant). The same date for all versions of this information object.  
  * validUntil?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Valid until  
      * Description: The date on which the information object is no longer effective or valid.  
  * administrativeDetails?  
      * Mandatory: False  
      * Type: AdministrativeDetails.AdministrativeDetails[]  
      * Label: Administrative details  
      * Description: Administrative details (e.g. default language, documentation, localID, ...).  
  * agentInRoles?  
      * Mandatory: False  
      * Link to: *_AgentInRole_*  
      * Label: Agent in roles  
      * Description: Agent(s) acting in the Role(s) for this information object.  

#### InformationResource  
_An abstract notion that is any organized collection of information._  
  * parentResource?  
      * Mandatory: False  
      * Link to: *_DataResource_*  
      * Label: Parent resource  
  * owner  
      * Mandatory: True  
      * Link to: *_ProvisionAgreement, StatisticalProgram_*  
      * Label: Owner  

#### InformationSet  
_Organized collections of statistical content._  

#### MultilingualText  
_A reusable type for supporting multilingual texts._  
  * Inherit: 
    * **object** 
  * languageCode  
      * Mandatory: True  
      * Type: string  
      * Enum: ['nb', 'nn', 'en']  
      * Label: Language code  
      * Description: The language code. Use only ISO 639-1 codes.  
  * languageText  
      * Mandatory: True  
      * Type: string  
      * Label: Language text  
      * Description: The text (e.g. label, title, description)  

#### ProcessInput  
_Any instance of an information object which is supplied to a Process Step Instance at the time its execution is initiated._  

#### ProcessOutput  
_Any instance of an information object which is produced by a Process Step as a result of its execution._  

#### ProcessStepCodeBlockDetails  
_A key-value-store for adding a complex array of code block attributes to the ProcessStep-object._  
  * Inherit: 
    * **object** 
  * codeBlockType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['DOCUMENTATION', 'CODE']  
      * Label: Type of code block  
      * Description: The type of code block  
  * codeBlockTitle  
      * Mandatory: True  
      * Type: string  
      * Label: Code block title  
      * Description: Title of code block  
  * codeBlockValue  
      * Mandatory: True  
      * Type: string  
      * Label: Value  
      * Description: The actual code or text  
  * codeBlockIndex  
      * Mandatory: True  
      * Type: number  
      * Label: Index  
      * Description: Index of the code block  
  * processStepInstance?  
      * Mandatory: False  
      * Link to: *_ProcessStepInstance_*  
      * Label: Process step instance  

#### StatisticalNeed  
_A requirement, request or other notification that will be considered by an organization. A Statistical Need does not necessarily have structure or format - it is a 'raw' need as received by the organization. A Statistical Need may be of a variety of types including Environmental Change or Information Request._  
  * dateCreated?  
      * Mandatory: False  
      * Type: datetime  
      * Label: Date created  
      * Description: Date created  
  * statisticalNeedStatus  
      * Mandatory: True  
      * Type: boolean  
      * Label: Statistical need status  
      * Description: Statistical need status  

#### ValueDomain  
_The permitted range of values for a characteristic of a variable_  
  * dataType  
      * Mandatory: True  
      * Type: string  
      * Enum: ['STRING', 'INTEGER', 'FLOAT', 'DATETIME', 'BOOLEAN']  
      * Label: Data type  
      * Description: The data type for a value domain  
  * measurementUnit?  
      * Mandatory: False  
      * Link to: *_MeasurementUnit_*  
      * Label: Measurement unit  
