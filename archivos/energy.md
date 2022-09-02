# $$\text{Reporte para el csv: energyco2}$$




## Tabla Hecho
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|Año|Año del dato|Indexado| Texto(TEXT)|2022|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Combustible|Tipo de combustible.|Indexado| Texto(TEXT)|Geothermal|
|Continente|Contiente al que pertenece el país.|Indexado| Texto(TEXT)|Africa|
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Clave Primaria| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Clave Primaria| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|Id_Combustible|Código obtenido mediante funcion hash aplicada a la fuente de emisión del CO2.|Indexado| Texto(TEXT)|57a34c10edc9db4cc4fbfc06367285f8|
|Id_Continente|Código obtenido mediante funcion hash aplicada al continente emisor del CO2.|Indexado| Texto(TEXT)|f5cd262901883dff68d06b215fb0f28e|

#
#

## sub_energ
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Código|Código corto alfabético que representar a los países.|Indexado| Texto(TEXT)|AFG|
|Año|Año del dato|Indexado| Texto(TEXT)|2022|esta tb como BIGINT
|Combustibles Fósiles (% Energía Primaria Equivalente)|Porcentaje que representan los  combustibles fósiles en la demanda de energía primaria.|Indexado|DOUBLE |"93|88"|
|Renovables (% Energía Primaria Equivalente)|Porcentaje que representan los  combustibles de fuente renovable en la demanda de energía primaria.|Indexado|DOUBLE |"6|12"|
|Nuclear (% Energía Primaria Equivalente)|Porcentaje que representan los  combustibles de fuente nucler en la demanda de energía primaria.|Indexado|DOUBLE |"12|36"|
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Clave Primaria| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Indexado| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_País|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al país de la emisión.|Clave Foránea | Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_gases_normalizados_Id_Año|Código proveniente de  tabla_hecho_gases_normalizados obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#


## historical_emission
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Fuente De Datos|Fuente de obtención de la información|Indexado| Texto(TEXT)|CAIT|
|Sector|Fuente a la que pertenecen las emisiones.|Indexado| Texto(TEXT)|Total including LUCF|
|Gas|Tipo de gas de las emisiones.|Indexado| Texto(TEXT)|All GHG|
|Unidad |Unidad de medición en megatoneladas de CO2 equivalente (MtCO2eq)|Indexado| Texto(TEXT)|MtCO₂e|
1990 al 2020|Columnas una por cada año.|Indexado|DOUBLE|1990|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Indexado| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#

## primary_sub
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Código|Código corto alfabético que representar a los países.|Indexado| Texto(TEXT)|AFG|
|Año|Año del dato|Indexado| Texto(TEXT)|2022|
|Consumo Eólico - Twh|Consumo proveniente de fuentes de energía eólica en TWh (Teravatio/hora)|Indexado|DOUBLE |"323|50"|
|Consumo Hidroeléctrico - Twh|Consumo proveniente de fuentes de energía hidroeléctrica en TWh (Teravatio/hora)|Indexado|DOUBLE |"145|50"|
|Consumo Solar - Twh|Consumo proveniente de fuentes de energía solar en TWh (Teravatio/hora)|Indexado|DOUBLE |"223|50"|
|Consumo Nuclear - Twh|Consumo proveniente de fuentes de energía nuclear en TWh (Teravatio/hora)|Indexado|DOUBLE |"65|50"|
|Consumo De Biocombustibles - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"53|50"|
|Geo Biomasa Otros - Twh|Consumo proveniente proveniente de biomasa en TWh (Teravatio/hora)|Indexado|DOUBLE |"93|50"|
|Consumo De Carbón - Twh|Consumo proveniente de fuentes de carbón en TWh (Teravatio/hora)|Indexado|DOUBLE |"323|50"|
|Consumo De Aceite - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"83|50"|
|Consumo De Gas - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"113|50"|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Clave Primaria| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Clave Primaria| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_País|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al país de la emisión.|Clave Foránea | Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_gases_normalizados_Id_Año|Código proveniente de  tabla_hecho_gases_normalizados obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#

## energyco2
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Combustible|Tipo de combustible|Indexado| Texto(TEXT)|Coal|
|Año|Año del dato|Indexado| Texto(TEXT)|2022|
|Consumo De Energía|Consumo total de energía en el país en TWh (Teravatio/hora)|Indexado|DOUBLE |"292|88"|
|Producción de Energía|Producción total de energía en el país en TWh (Teravatio/hora)|Indexado|DOUBLE |"521|88"|
|PiB|Producto interno bruto es el valor total de la corriente de bienes y servicios finales.|Indexado|DOUBLE |"27770|91"|
|Población|Cantidad de habitantes de un territorio.|Indexado|DOUBLE |"4298127000000|00"|
|Intensidad_Energética_per_cápita|Es el cociente entre el consumo energético y los habitantes.|Indexado|DOUBLE |"68|50"|
|Intensidad_Energética_per_PiB|Es el cociente entre el consumo energético y el PiB.|Indexado|DOUBLE |"10541|50"|
|Emisión de CO2|Emisión total de CO2 del país.|Indexado|DOUBLE |"323|50"|
|Consumo De Energía - Twh|Consumo total  de energía del país en Teravatio/hora.|Indexado|DOUBLE |"323|50"|
|Produción De Energía - Twh|Producción total  de energía del país en Teravatio/hora.|Indexado|DOUBLE |323|
|Intensidad_Energética_per_Cápita TWh|"Es el cociente entre el consumo energético y los habitantes| medido en Teravatio/hora"|Indexado|DOUBLE |"11|59"|
|Intensidad_Energética_per_PiB TWh|"Es el cociente entre el consumo energético y el PiB| medido en Teravatio/hora"|Indexado|DOUBLE |"11|59"|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Clave Primaria| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Indexado| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|Id_Combustible|Código obtenido mediante funcion hash aplicada al tipo de combustible empleado.||Indexado| Texto(TEXT)|cc8cc099b05d2c44e441a5443da94571|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_País|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al país de la emisión.|Clave Foránea | Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_gases_normalizados_Id_Año|Código proveniente de  tabla_hecho_gases_normalizados obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#


## partic_global_energía
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Clave Primaria| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|AFG|arreglar como CODIGO
|País Largo|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|arreglar como País
|Combustible|Tipo de combustible|Indexado| Texto(TEXT)|Hydro|
cant|Cantidad total.|Indexado|BIGINT|1|
|Percentage|Porcentaje del total de energía global.|Indexado| Texto(TEXT)|0.143266|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_País|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al país de la emisión.|Clave Foránea | Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_gases_normalizados_Id_Año|Código proveniente de  tabla_hecho_gases_normalizados obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#

## primary_energy
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Clave Primaria| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|Id_País|Código obtenido mediante funcion hash aplicada al país de la emisión.|Indexado| Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|País|Nombre del País en inglés|Indexado| Texto(TEXT)|Afghanistan|
|Código|Código corto alfabético que representar a los países.|Indexado| Texto(TEXT)|AFG|
|Año|Año del dato|Indexado|BIGINT|2022|el año en otros esta como texto
|Consumo Eólico - Twh|Consumo proveniente de fuentes de energía eólica en TWh (Teravatio/hora)|Indexado|DOUBLE |"323|50"|
|Consumo Hidroeléctrico - Twh|Consumo proveniente de fuentes de energía hidroeléctrica en TWh (Teravatio/hora)|Indexado|DOUBLE |"145|50"|
|Consumo Solar - Twh|Consumo proveniente de fuentes de energía solar en TWh (Teravatio/hora)|Indexado|DOUBLE |"223|50"|
|Consumo Nuclear - Twh|Consumo proveniente de fuentes de energía nuclear en TWh (Teravatio/hora)|Indexado|DOUBLE |"65|50"|
|Consumo De Biocombustibles - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"53|50"|
|Geo Biomasa Otros - Twh|Consumo proveniente proveniente de biomasa en TWh (Teravatio/hora)|Indexado|DOUBLE |"93|50"|
|Consumo De Carbón - Twh|Consumo proveniente de fuentes de carbón en TWh (Teravatio/hora)|Indexado|DOUBLE |"323|50"|
|Consumo De Aceite - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"83|50"|
|Consumo De Gas - Twh|Consumo proveniente de fuentes de biocombustibles en TWh (Teravatio/hora)|Indexado|DOUBLE |"113|50"|
|tabla_hecho_Id_Año|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
|tabla_hecho_Id_País|Código proveniente de  tabla_hecho  obtenido mediante funcion hash aplicada al país de la emisión.|Clave Foránea | Texto(TEXT)|f5a7924e621e84c9280a9a27e1bcb7f6|
|tabla_hecho_gases_normalizados_Id_Año|Código proveniente de  tabla_hecho_gases_normalizados obtenido mediante funcion hash aplicada al año de la emisión.|Clave Foránea | Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|

#
#


## gases
|Atributo|Descripción|Obligación /Condición|Tipo de dato|Ejemplo|
|:-------------------:|---|---|---|---|
|Año|Año del dato|Indexado|BIGINT|2022|ver el año que en algunos esta como texto
|Media N2O|Producción media anual de  óxido nitroso por pais en ppb (partes por billón).|Indexado|DOUBLE|"293|56"|
|Unc N2O||Indexado|DOUBLE||los borraria
|Media Sf6|Producción media anual de  Hexafluoruro de azufre por año en ppb (partes por billón).|Indexado|DOUBLE|"9|64"|
|Unc Sf6||Indexado|DOUBLE||los borraria
|Media CO2|Producción media anual de  dióxido de carbono por año en ppm (partes por millón).|Indexado|DOUBLE|"334|31"|
|Unc CO2||Indexado|DOUBLE||los borraria
|Id_Año|Código obtenido mediante funcion hash aplicada al año de la emisión.|Clave Primaria| Texto(TEXT)|e4dd5528f7596dcdf871aa55cfccc53c|
