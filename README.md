# Tipo de cambio Sunat
Programa para extraer los tipos de cambio oficial del dólar publicados por Sunat.

Esta aplicación devuelve un arreglo con el tipo de cambio de compra y venta del dólar publicados en la página web de Sunat (URL: http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias), se usa Scrapy (versión mínima: 1.6.X) (https://scrapy.org/) para la extracción de datos, se requiere de Python (versión mínima: 3.7.X): https://www.python.org/downloads/.

Para ejecutar la aplicación se tiene que ejecutar el siguiente comando:

```
scrapy crawl tc_sunat_spider
```


En la última línea del archivo **sunat/spiders/tc_sunat_spider.py** encontrará el arreglo con la información de los tipos de cambio:
```python
pprint.pprint(self.tipos_cambio_arr)
```

Este es un ejemplo de la información que tendrá el arreglo:
```python
[
 {'compra': 3.308, 
  'fecha': datetime.datetime(2019, 8, 1, 0, 0), 
  'venta': 3.31},
 {'compra': 3.316,
  'fecha': datetime.datetime(2019, 8, 2, 0, 0),
  'venta': 3.319},
 {'compra': 3.343,
  'fecha': datetime.datetime(2019, 8, 3, 0, 0),
  'venta': 3.346},
 {'compra': 3.375,
  'fecha': datetime.datetime(2019, 8, 6, 0, 0),
  'venta': 3.385},
 {'compra': 3.38, 'fecha': datetime.datetime(2019, 8, 7, 0, 0), 'venta': 3.384},
 {'compra': 3.379,
  'fecha': datetime.datetime(2019, 8, 8, 0, 0),
  'venta': 3.382},
 {'compra': 3.379,
  'fecha': datetime.datetime(2019, 8, 9, 0, 0),
  'venta': 3.382},
 {'compra': 3.379,
  'fecha': datetime.datetime(2019, 8, 10, 0, 0),
  'venta': 3.383},
 {'compra': 3.386,
  'fecha': datetime.datetime(2019, 8, 13, 0, 0),
  'venta': 3.389},
 {'compra': 3.375,
  'fecha': datetime.datetime(2019, 8, 14, 0, 0),
  'venta': 3.377},
 {'compra': 3.389,
  'fecha': datetime.datetime(2019, 8, 15, 0, 0),
  'venta': 3.389},
 {'compra': 3.39,
  'fecha': datetime.datetime(2019, 8, 16, 0, 0),
  'venta': 3.394}
  ]
```
