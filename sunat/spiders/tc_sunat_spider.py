import datetime
import json
import locale
import scrapy
import pprint

from scrapy import signals
from scrapy import Spider

class TcSunatSpider(scrapy.Spider):
    name = 'tc_sunat_spider'
    start_urls = ['https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias']
    tipos_cambio_arr = []


    def parse(self, response):
        fecha_data = response.xpath("//h3/text()").extract()
        mes = ""
        anho = ""

        locale.setlocale(locale.LC_ALL, 'es_PE')

        if len(fecha_data) > 0:
            fecha_arr = fecha_data[0].split("-")

            mes = fecha_arr[0].strip()
            anho = fecha_arr[1].strip()

        cabecera_exonerada = False


        for sel_tr in response.xpath("//table[@class='class=\"form-table\"']//tr"):
            if cabecera_exonerada == False:
                cabecera_exonerada = True
                continue

            contador_columnas = 0
            tc_fecha = ""
            tc_compra = 0.0
            tc_venta = 0.0

            for sel_td in sel_tr.xpath("td"):
                contador_columnas = contador_columnas + 1

                if contador_columnas > 3:
                    contador_columnas = 1

                td_dia_mes = sel_td.xpath("strong")

                if len(td_dia_mes) > 0:
                    texto_arr = td_dia_mes.xpath("text()").extract()
                else:
                    texto_arr = sel_td.xpath("text()").extract()

                if contador_columnas == 1:
                    dia_str = texto_arr[0].strip()

                    tc_fecha = datetime.datetime.strptime(anho + "-" + mes + "-" + dia_str, '%Y-%B-%d')

                if contador_columnas == 2:
                    tc_compra = float(texto_arr[0].strip())

                if contador_columnas == 3:
                    tc_venta = float(texto_arr[0].strip())

                    self.tipos_cambio_arr.append({ 'fecha': tc_fecha, 'compra': tc_compra, 'venta': tc_venta })

        pprint.pprint(self.tipos_cambio_arr)